#!/usr/bin/env python3
"""
Export Neo4j data to YAML files in db/ folder.

Exports:
- db/persons.yaml - All Person nodes with affiliations
- db/organizations.yaml - All Organization nodes with stakeholders
- db/families.yaml - All Family nodes with members
- db/events.yaml - All Event nodes

Usage:
    python migration/export_neo4j.py
    python migration/export_neo4j.py --dry-run  # Preview only
"""

import os
import yaml
from neo4j import GraphDatabase
from collections import OrderedDict

# Neo4j connection
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "deepscript2025"

# Output directory
BASE_DIR = "/Users/archimedix/app/deepscript"
OUTPUT_DIR = os.path.join(BASE_DIR, "db")

# Custom YAML representer for OrderedDict
def represent_ordereddict(dumper, data):
    return dumper.represent_mapping('tag:yaml.org,2002:map', data.items())

yaml.add_representer(OrderedDict, represent_ordereddict)

# Custom representer to avoid YAML anchors/aliases
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def get_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def clean_dict(d):
    """Remove None values and empty strings from dict"""
    return {k: v for k, v in d.items() if v is not None and v != ""}

def export_persons(driver):
    """Export all Person nodes with their affiliations"""
    print("Exporting persons...")

    persons = OrderedDict()

    with driver.session() as session:
        # Get all persons
        result = session.run("""
            MATCH (p:Person)
            OPTIONAL MATCH (p)-[r:AFFILIATED_WITH]->(o:Organization)
            WITH p, collect({
                org: o.id,
                role: r.role,
                from: r.from,
                to: r.to,
                note: r.note
            }) as affiliations
            RETURN p.id as id, p.born as born, p.died as died,
                   p.nationality as nationality, p.family as family,
                   p.file as file, p.note as note, affiliations
            ORDER BY p.id
        """)

        for record in result:
            person_id = record["id"]
            person = OrderedDict()

            # Add basic fields
            if record["file"]:
                person["file"] = record["file"]
            if record["born"]:
                person["born"] = record["born"]
            if record["died"]:
                person["died"] = record["died"]
            if record["nationality"]:
                person["nationality"] = record["nationality"]
            if record["family"]:
                person["family"] = record["family"]
            if record["note"]:
                person["note"] = record["note"]

            # Add affiliations
            affs = []
            for aff in record["affiliations"]:
                if aff["org"]:  # Skip if no org
                    aff_entry = OrderedDict()
                    aff_entry["org"] = aff["org"]
                    if aff["role"]:
                        aff_entry["role"] = aff["role"]
                    if aff["from"]:
                        aff_entry["from"] = aff["from"]
                    if aff["to"]:
                        aff_entry["to"] = aff["to"]
                    if aff["note"]:
                        aff_entry["note"] = aff["note"]
                    affs.append(dict(aff_entry))

            if affs:
                person["affiliations"] = affs

            persons[person_id] = dict(person)

        # Second pass: add RELATED_TO relationships
        result = session.run("""
            MATCH (p1:Person)-[r:RELATED_TO]->(p2:Person)
            RETURN p1.id as from_id, p2.id as to_id, r.type as type, r.note as note
            ORDER BY p1.id, p2.id
        """)

        for record in result:
            from_id = record["from_id"]
            if from_id in persons:
                if "relations" not in persons[from_id]:
                    persons[from_id]["relations"] = []
                rel_entry = OrderedDict()
                rel_entry["person"] = record["to_id"]
                if record["type"]:
                    rel_entry["type"] = record["type"]
                if record["note"]:
                    rel_entry["note"] = record["note"]
                persons[from_id]["relations"].append(dict(rel_entry))

    print(f"  Found {len(persons)} persons")
    return {"persons": dict(persons)}

def export_organizations(driver):
    """Export all Organization nodes with their stakeholders"""
    print("Exporting organizations...")

    orgs = OrderedDict()

    with driver.session() as session:
        # Get all organizations with their sub-labels
        result = session.run("""
            MATCH (o:Organization)
            OPTIONAL MATCH (p:Person)-[r:AFFILIATED_WITH]->(o)
            WITH o, collect({
                person: p.id,
                role: r.role,
                from: r.from,
                to: r.to,
                note: r.note
            }) as person_stakes
            OPTIONAL MATCH (other:Organization)-[s:STAKE_IN]->(o)
            WITH o, person_stakes, collect({
                org: other.id,
                role: s.role,
                share: s.share,
                from: s.from,
                to: s.to,
                note: s.note
            }) as org_stakes
            RETURN o.id as id, o.name as name, labels(o) as labels,
                   o.founded as founded, o.headquarters as headquarters,
                   o.status as status, o.sector as sector, o.aum as aum,
                   o.file as file, o.note as note,
                   person_stakes, org_stakes
            ORDER BY o.id
        """)

        for record in result:
            org_id = record["id"]
            org = OrderedDict()

            # Get type from labels (sub-label that's not "Organization")
            labels = record["labels"]
            org_type = None
            for label in labels:
                if label != "Organization":
                    org_type = label.lower()
                    break

            # Add basic fields
            if record["file"]:
                org["file"] = record["file"]
            if record["name"]:
                org["name"] = record["name"]
            if org_type:
                org["type"] = org_type
            if record["founded"]:
                org["founded"] = record["founded"]
            if record["headquarters"]:
                org["headquarters"] = record["headquarters"]
            if record["status"]:
                org["status"] = record["status"]
            if record["sector"]:
                org["sector"] = record["sector"]
            if record["aum"]:
                org["aum"] = record["aum"]
            if record["note"]:
                org["note"] = record["note"]

            # Add stakeholders (persons)
            stakeholders = []
            for stake in record["person_stakes"]:
                if stake["person"]:
                    entry = OrderedDict()
                    entry["person"] = stake["person"]
                    if stake["role"]:
                        entry["role"] = stake["role"]
                    if stake["from"]:
                        entry["from"] = stake["from"]
                    if stake["to"]:
                        entry["to"] = stake["to"]
                    if stake["note"]:
                        entry["note"] = stake["note"]
                    stakeholders.append(dict(entry))

            # Add stakeholders (orgs)
            for stake in record["org_stakes"]:
                if stake["org"]:
                    entry = OrderedDict()
                    entry["org"] = stake["org"]
                    if stake["role"]:
                        entry["role"] = stake["role"]
                    if stake["share"]:
                        # Handle both numeric and string shares (e.g., "81%")
                        share_val = stake["share"]
                        if isinstance(share_val, (int, float)):
                            entry["share"] = round(share_val, 4)
                        else:
                            entry["share"] = share_val
                    if stake["from"]:
                        entry["from"] = stake["from"]
                    if stake["to"]:
                        entry["to"] = stake["to"]
                    if stake["note"]:
                        entry["note"] = stake["note"]
                    stakeholders.append(dict(entry))

            if stakeholders:
                org["stakeholders"] = stakeholders

            orgs[org_id] = dict(org)

    print(f"  Found {len(orgs)} organizations")
    return {"organizations": dict(orgs)}

def export_families(driver):
    """Export all Family nodes"""
    print("Exporting families...")

    families = OrderedDict()

    with driver.session() as session:
        result = session.run("""
            MATCH (f:Family)
            OPTIONAL MATCH (p:Person)-[r:MEMBER_OF]->(f)
            WITH f, collect({
                person: p.id,
                generation: r.generation,
                role: r.role
            }) as members
            RETURN f.id as id, f.origin as origin, f.founder as founder,
                   f.sector as sector, f.generations as generations,
                   f.status as status, f.file as file, f.note as note,
                   members
            ORDER BY f.id
        """)

        for record in result:
            family_id = record["id"]
            family = OrderedDict()

            if record["file"]:
                family["file"] = record["file"]
            if record["origin"]:
                family["origin"] = record["origin"]
            if record["founder"]:
                family["founder"] = record["founder"]
            if record["sector"]:
                family["sector"] = record["sector"]
            if record["generations"]:
                family["generations"] = record["generations"]
            if record["status"]:
                family["status"] = record["status"]
            if record["note"]:
                family["note"] = record["note"]

            # Add members
            members = []
            for m in record["members"]:
                if m["person"]:
                    entry = OrderedDict()
                    entry["person"] = m["person"]
                    if m["generation"]:
                        entry["generation"] = m["generation"]
                    if m["role"]:
                        entry["role"] = m["role"]
                    members.append(dict(entry))

            if members:
                family["members"] = members

            families[family_id] = dict(family)

    print(f"  Found {len(families)} families")
    return {"families": dict(families)}

def export_events(driver):
    """Export all Event nodes"""
    print("Exporting events...")

    events = OrderedDict()

    with driver.session() as session:
        result = session.run("""
            MATCH (e:Event)
            RETURN e.id as id, e.year as year, e.month as month,
                   e.type as type, e.location as location,
                   e.outcome as outcome, e.file as file, e.note as note
            ORDER BY e.year, e.id
        """)

        for record in result:
            event_id = record["id"]
            event = OrderedDict()

            if record["file"]:
                event["file"] = record["file"]
            if record["year"]:
                event["year"] = record["year"]
            if record["month"]:
                event["month"] = record["month"]
            if record["type"]:
                event["type"] = record["type"]
            if record["location"]:
                event["location"] = record["location"]
            if record["outcome"]:
                event["outcome"] = record["outcome"]
            if record["note"]:
                event["note"] = record["note"]

            events[event_id] = dict(event)

    print(f"  Found {len(events)} events")
    return {"events": dict(events)}

def write_yaml(data, filename):
    """Write data to YAML file"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(data, f,
                  default_flow_style=False,
                  allow_unicode=True,
                  sort_keys=False,
                  Dumper=NoAliasDumper,
                  width=120)
    print(f"  Written to {filepath}")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Export Neo4j to YAML")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't write files")
    args = parser.parse_args()

    print("=== Exporting Neo4j to YAML ===\n")

    driver = get_driver()

    try:
        # Export all data
        persons_data = export_persons(driver)
        orgs_data = export_organizations(driver)
        families_data = export_families(driver)
        events_data = export_events(driver)

        if args.dry_run:
            print("\n=== DRY RUN - No files written ===")
            print(f"Would write {len(persons_data['persons'])} persons to db/persons.yaml")
            print(f"Would write {len(orgs_data['organizations'])} organizations to db/organizations.yaml")
            print(f"Would write {len(families_data['families'])} families to db/families.yaml")
            print(f"Would write {len(events_data['events'])} events to db/events.yaml")
        else:
            print("\n=== Writing YAML files ===")
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            write_yaml(persons_data, "persons.yaml")
            write_yaml(orgs_data, "organizations.yaml")
            write_yaml(families_data, "families.yaml")
            write_yaml(events_data, "events.yaml")
            print("\n=== Export complete ===")

    finally:
        driver.close()

if __name__ == "__main__":
    main()
