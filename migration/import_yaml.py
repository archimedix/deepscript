#!/usr/bin/env python3
"""
Import YAML files from db/ folder into Neo4j.

Imports:
- db/persons.yaml - Person nodes with affiliations
- db/organizations.yaml - Organization nodes with stakeholders
- db/families.yaml - Family nodes with members
- db/events.yaml - Event nodes

Usage:
    python migration/import_yaml.py
    python migration/import_yaml.py --dry-run   # Preview only
    python migration/import_yaml.py --clear     # Clear Neo4j before import
"""

import os
import sys
import yaml
from neo4j import GraphDatabase

# Import schema loader (single source of truth)
from lib.schema import get_type_to_sublabel, type_to_sublabel

# Neo4j connection
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "deepscript2025"

# Input directory
BASE_DIR = "/Users/archimedix/app/deepscript"
INPUT_DIR = os.path.join(BASE_DIR, "db")


def load_yaml(filename):
    """Load YAML file from db/ folder."""
    filepath = os.path.join(INPUT_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  File not found: {filepath}")
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def clear_database(driver, dry_run=False):
    """Clear all nodes and relationships from Neo4j."""
    if dry_run:
        print("[DRY-RUN] Would clear all nodes and relationships")
        return

    with driver.session() as session:
        result = session.run("MATCH (n) DETACH DELETE n RETURN count(n) as deleted")
        count = result.single()["deleted"]
        print(f"Cleared {count} nodes from Neo4j")


def import_persons(driver, dry_run=False):
    """Import persons from db/persons.yaml."""
    print("\nImporting persons...")
    data = load_yaml("persons.yaml")
    persons = data.get("persons", {})

    count = 0
    affiliations = 0

    for person_id, props in persons.items():
        # Extract affiliations separately
        affs = props.pop("affiliations", [])
        # Remove file property (deterministic path now)
        props.pop("file", None)

        if dry_run:
            print(f"  [DRY-RUN] MERGE Person {person_id}: {props}")
        else:
            with driver.session() as session:
                # Create person node
                session.run(
                    """
                    MERGE (p:Person {id: $id})
                    SET p += $props
                    """,
                    id=person_id,
                    props=props
                )

                # Create affiliations
                for aff in affs:
                    org_id = aff.get("org")
                    if not org_id:
                        continue
                    rel_props = {k: v for k, v in aff.items() if k != "org"}
                    session.run(
                        """
                        MATCH (p:Person {id: $person_id})
                        MERGE (o:Organization {id: $org_id})
                        MERGE (p)-[r:AFFILIATED_WITH]->(o)
                        SET r += $props
                        """,
                        person_id=person_id,
                        org_id=org_id,
                        props=rel_props
                    )
                    affiliations += 1

        count += 1

    print(f"  Imported {count} persons, {affiliations} affiliations")
    return count, affiliations


def import_organizations(driver, dry_run=False):
    """Import organizations from db/organizations.yaml."""
    print("\nImporting organizations...")
    data = load_yaml("organizations.yaml")
    orgs = data.get("organizations", {})

    count = 0
    stakeholders = 0

    for org_id, props in orgs.items():
        # Extract stakeholders separately
        shs = props.pop("stakeholders", [])
        # Remove file property
        props.pop("file", None)
        # Get type for sub-label (using schema.yaml as source of truth)
        org_type = props.pop("type", None)
        sublabel = type_to_sublabel(org_type) if org_type else None

        if dry_run:
            print(f"  [DRY-RUN] MERGE Organization:{sublabel} {org_id}: {props}")
        else:
            with driver.session() as session:
                # Create organization node with sub-label
                if sublabel:
                    session.run(
                        f"""
                        MERGE (o:Organization {{id: $id}})
                        SET o:{sublabel}, o += $props
                        """,
                        id=org_id,
                        props=props
                    )
                else:
                    session.run(
                        """
                        MERGE (o:Organization {id: $id})
                        SET o += $props
                        """,
                        id=org_id,
                        props=props
                    )

                # Create stakeholder relationships
                for sh in shs:
                    rel_props = {k: v for k, v in sh.items() if k not in ("person", "org")}

                    if "person" in sh:
                        # Person stakeholder -> AFFILIATED_WITH (reverse)
                        session.run(
                            """
                            MERGE (p:Person {id: $person_id})
                            MATCH (o:Organization {id: $org_id})
                            MERGE (p)-[r:AFFILIATED_WITH]->(o)
                            SET r += $props
                            """,
                            person_id=sh["person"],
                            org_id=org_id,
                            props=rel_props
                        )
                    elif "org" in sh:
                        # Org stakeholder -> STAKE_IN
                        session.run(
                            """
                            MERGE (o1:Organization {id: $stakeholder_id})
                            MATCH (o2:Organization {id: $org_id})
                            MERGE (o1)-[r:STAKE_IN]->(o2)
                            SET r += $props
                            """,
                            stakeholder_id=sh["org"],
                            org_id=org_id,
                            props=rel_props
                        )
                    stakeholders += 1

        count += 1

    print(f"  Imported {count} organizations, {stakeholders} stakeholder relations")
    return count, stakeholders


def import_families(driver, dry_run=False):
    """Import families from db/families.yaml."""
    print("\nImporting families...")
    data = load_yaml("families.yaml")
    families = data.get("families", {})

    count = 0
    members = 0

    for family_id, props in families.items():
        # Extract members separately
        mems = props.pop("members", [])
        # Remove file property
        props.pop("file", None)

        if dry_run:
            print(f"  [DRY-RUN] MERGE Family {family_id}: {props}")
        else:
            with driver.session() as session:
                # Create family node
                session.run(
                    """
                    MERGE (f:Family {id: $id})
                    SET f += $props
                    """,
                    id=family_id,
                    props=props
                )

                # Create member relationships
                for mem in mems:
                    person_id = mem.get("person")
                    if not person_id:
                        continue
                    rel_props = {k: v for k, v in mem.items() if k != "person"}
                    session.run(
                        """
                        MERGE (p:Person {id: $person_id})
                        MATCH (f:Family {id: $family_id})
                        MERGE (p)-[r:MEMBER_OF]->(f)
                        SET r += $props
                        """,
                        person_id=person_id,
                        family_id=family_id,
                        props=rel_props
                    )
                    members += 1

        count += 1

    print(f"  Imported {count} families, {members} member relations")
    return count, members


def import_events(driver, dry_run=False):
    """Import events from db/events.yaml."""
    print("\nImporting events...")
    data = load_yaml("events.yaml")
    events = data.get("events", {})

    count = 0

    for event_id, props in events.items():
        # Remove file property
        props.pop("file", None)

        if dry_run:
            print(f"  [DRY-RUN] MERGE Event {event_id}: {props}")
        else:
            with driver.session() as session:
                session.run(
                    """
                    MERGE (e:Event {id: $id})
                    SET e += $props
                    """,
                    id=event_id,
                    props=props
                )

        count += 1

    print(f"  Imported {count} events")
    return count


def main():
    dry_run = "--dry-run" in sys.argv
    clear = "--clear" in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    print(f"Importing from: {INPUT_DIR}")
    print(f"Neo4j: {NEO4J_URI}")

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        # Verify connection
        driver.verify_connectivity()
        print("Connected to Neo4j\n")

        # Clear if requested
        if clear:
            if not dry_run:
                confirm = input("WARNING: This will delete ALL data in Neo4j. Continue? (yes/no): ")
                if confirm.lower() != "yes":
                    print("Aborted.")
                    return
            clear_database(driver, dry_run)

        # Import all data
        p_count, p_affs = import_persons(driver, dry_run)
        o_count, o_shs = import_organizations(driver, dry_run)
        f_count, f_mems = import_families(driver, dry_run)
        e_count = import_events(driver, dry_run)

        # Summary
        print("\n" + "=" * 50)
        print("IMPORT COMPLETE")
        print("=" * 50)
        print(f"Persons:       {p_count} nodes, {p_affs} affiliations")
        print(f"Organizations: {o_count} nodes, {o_shs} stakeholders")
        print(f"Families:      {f_count} nodes, {f_mems} members")
        print(f"Events:        {e_count} nodes")

        if dry_run:
            print("\n[DRY-RUN] No changes made to Neo4j")

    finally:
        driver.close()


if __name__ == "__main__":
    main()
