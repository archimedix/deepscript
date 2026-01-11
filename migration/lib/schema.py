"""
DeepScript Schema Loader

Single source of truth reader for db/schema.yaml.
Used by all migration scripts and tools.

Usage:
    from lib.schema import get_type_to_sublabel, get_docs_path

    sublabel = get_type_to_sublabel()["forum"]  # -> "Forum"
    path = get_docs_path("Forum", "bilderberg")  # -> "docs/forum/bilderberg.md"
"""

import os
import yaml
from functools import lru_cache
from typing import Dict, List, Optional, Any

# Path to schema.yaml (relative to this file)
SCHEMA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "db",
    "schema.yaml"
)


@lru_cache(maxsize=1)
def get_schema() -> Dict[str, Any]:
    """
    Load and cache the schema from db/schema.yaml.

    Returns the complete schema dictionary.
    Cached after first load for performance.
    """
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_type_to_sublabel() -> Dict[str, str]:
    """
    Get the type -> Neo4j sublabel mapping.

    Example:
        mapping = get_type_to_sublabel()
        mapping["forum"]  # -> "Forum"
        mapping["defense"]  # -> "Defense"
    """
    return get_schema().get("type_mapping", {})


def get_sublabels() -> List[str]:
    """
    Get list of valid Organization sublabels.

    Returns:
        ["Forum", "Company", "Bank", "CentralBank", ...]
    """
    return get_schema().get("org_sublabels", [])


def get_node_types() -> List[str]:
    """
    Get list of node types.

    Returns:
        ["Person", "Organization", "Family", "Event"]
    """
    return get_schema().get("node_types", [])


def get_relationship_types() -> Dict[str, Dict]:
    """
    Get relationship type definitions.

    Returns:
        {
            "AFFILIATED_WITH": {"from": "Person", "to": "Organization", "properties": [...]},
            ...
        }
    """
    return get_schema().get("relationship_types", {})


def get_docs_path_mapping() -> Dict[str, str]:
    """
    Get label -> docs folder mapping.

    Returns:
        {"Person": "persons", "Forum": "forum", "Defense": "defense", ...}
    """
    return get_schema().get("docs_path_mapping", {})


def get_docs_path(label: str, entity_id: str, base_dir: str = "docs") -> str:
    """
    Calculate the docs path for an entity.

    Args:
        label: Neo4j label (e.g., "Person", "Forum", "Defense")
        entity_id: Entity ID (e.g., "mario-draghi", "bilderberg")
        base_dir: Base directory (default "docs")

    Returns:
        Path like "docs/persons/mario-draghi.md"
    """
    mapping = get_docs_path_mapping()
    folder = mapping.get(label, label.lower())
    return os.path.join(base_dir, folder, f"{entity_id}.md")


def get_affiliation_roles() -> List[str]:
    """Get valid affiliation roles (Person -> Organization)."""
    return get_schema().get("enums", {}).get("affiliation_roles", [])


def get_stake_roles() -> List[str]:
    """Get valid stake roles (Organization -> Organization)."""
    return get_schema().get("enums", {}).get("stake_roles", [])


def get_family_roles() -> List[str]:
    """Get valid family roles (Person -> Family)."""
    return get_schema().get("enums", {}).get("family_roles", [])


def get_event_types() -> List[str]:
    """Get valid event types."""
    return get_schema().get("enums", {}).get("event_types", [])


def get_person_relation_types() -> List[str]:
    """Get valid person-to-person relation types."""
    return get_schema().get("enums", {}).get("person_relation_types", [])


def get_sectors() -> List[str]:
    """Get valid company sectors."""
    return get_schema().get("enums", {}).get("sectors", [])


def get_org_status() -> List[str]:
    """Get valid organization status values."""
    return get_schema().get("enums", {}).get("org_status", [])


def get_role_mapping() -> Dict[str, Any]:
    """
    Get legacy role -> standard role mapping.

    Note: Some values are lists (compound roles).

    Returns:
        {"ceo": "executive", "ceo-fondatore": ["founder", "executive"], ...}
    """
    return get_schema().get("role_mapping", {})


def get_field_mapping() -> Dict[str, str]:
    """
    Get Italian -> English field mapping.

    Returns:
        {"nato": "born", "sede": "headquarters", ...}
    """
    return get_schema().get("field_mapping", {})


def validate_type(org_type: str) -> Optional[str]:
    """
    Validate and normalize an organization type.

    Args:
        org_type: Type string (e.g., "forum", "Forum", "FORUM")

    Returns:
        Neo4j sublabel if valid, None otherwise
    """
    mapping = get_type_to_sublabel()
    # Try exact match first
    if org_type in mapping:
        return mapping[org_type]
    # Try lowercase
    lower = org_type.lower()
    if lower in mapping:
        return mapping[lower]
    # Check if it's already a valid sublabel
    sublabels = get_sublabels()
    if org_type in sublabels:
        return org_type
    return None


def validate_role(role: str, context: str = "affiliation") -> bool:
    """
    Validate a role against the schema.

    Args:
        role: Role string to validate
        context: One of "affiliation", "stake", "family", "event_person", "event_org"

    Returns:
        True if valid, False otherwise
    """
    role_getters = {
        "affiliation": get_affiliation_roles,
        "stake": get_stake_roles,
        "family": get_family_roles,
        "event_person": lambda: get_schema().get("enums", {}).get("event_participation_roles", []),
        "event_org": lambda: get_schema().get("enums", {}).get("event_involvement_roles", []),
    }

    getter = role_getters.get(context)
    if not getter:
        return False

    valid_roles = getter()
    return role in valid_roles


def normalize_role(role: str) -> Any:
    """
    Normalize a role using the role_mapping.

    Args:
        role: Role string (possibly legacy Italian)

    Returns:
        Normalized role (string or list for compound roles)
    """
    mapping = get_role_mapping()
    return mapping.get(role, role)


def normalize_field(field: str) -> str:
    """
    Normalize a field name using the field_mapping.

    Args:
        field: Field name (possibly Italian)

    Returns:
        Normalized English field name
    """
    mapping = get_field_mapping()
    return mapping.get(field, field)


# Convenience function for getting sublabel from type with default
def type_to_sublabel(org_type: str, default: str = "Company") -> str:
    """
    Convert type to Neo4j sublabel with fallback.

    Args:
        org_type: Type string
        default: Default sublabel if type not found

    Returns:
        Neo4j sublabel
    """
    result = validate_type(org_type)
    return result if result else default
