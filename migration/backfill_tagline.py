#!/usr/bin/env python3
"""
Backfill tagline property on Neo4j nodes from docs/*.md files.

Reads the blockquote on line 3 of each markdown file (pattern: "> text")
and sets it as the `tagline` property on the matching Neo4j node.

Usage:
    python migration/backfill_tagline.py              # full run
    python migration/backfill_tagline.py --dry-run     # preview only
    python migration/backfill_tagline.py --limit 10    # limit to N files
"""

import os
import re
import argparse
from neo4j import GraphDatabase

# Reuse schema loader
import sys
sys.path.insert(0, os.path.dirname(__file__))
from lib.schema import get_docs_path_mapping

# Neo4j connection
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "deepscript2025"

BASE_DIR = "/Users/archimedix/app/deepscript"
DOCS_DIR = os.path.join(BASE_DIR, "docs")


def extract_tagline(filepath):
    """Extract tagline from line 3 of a markdown file (pattern: > text)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) >= 3:
            line = lines[2].strip()
            # Match blockquote: > text (with optional quotes inside)
            m = re.match(r'^>\s*"?(.+?)"?\s*$', line)
            if m:
                return m.group(1).strip()
    except Exception:
        pass
    return None


def build_folder_to_label():
    """Invert docs_path_mapping: folder -> label."""
    mapping = get_docs_path_mapping()
    return {folder: label for label, folder in mapping.items()}


def main():
    parser = argparse.ArgumentParser(description="Backfill tagline from docs to Neo4j")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--limit", type=int, default=0, help="Limit to N files")
    args = parser.parse_args()

    folder_to_label = build_folder_to_label()
    updated = 0
    no_tagline = 0
    no_node = 0
    processed = 0

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        with driver.session() as session:
            for folder in sorted(os.listdir(DOCS_DIR)):
                folder_path = os.path.join(DOCS_DIR, folder)
                if not os.path.isdir(folder_path):
                    continue

                label = folder_to_label.get(folder)
                if not label:
                    continue

                for filename in sorted(os.listdir(folder_path)):
                    if not filename.endswith(".md"):
                        continue

                    if args.limit and processed >= args.limit:
                        break

                    entity_id = filename[:-3]  # strip .md
                    filepath = os.path.join(folder_path, filename)
                    tagline = extract_tagline(filepath)

                    if not tagline:
                        no_tagline += 1
                        continue

                    processed += 1

                    if args.dry_run:
                        print(f"  [{label}] {entity_id}: {tagline[:80]}")
                        updated += 1
                    else:
                        result = session.run(
                            "MATCH (n {id: $id}) SET n.tagline = $tagline RETURN n.id",
                            id=entity_id, tagline=tagline
                        )
                        if result.single():
                            updated += 1
                        else:
                            no_node += 1
                            print(f"  WARN: no node for {entity_id} ({label})")

                if args.limit and processed >= args.limit:
                    break

    finally:
        driver.close()

    print(f"\n=== Backfill tagline {'(DRY RUN) ' if args.dry_run else ''}===")
    print(f"  Updated:      {updated}")
    print(f"  No tagline:   {no_tagline}")
    print(f"  No node:      {no_node}")


if __name__ == "__main__":
    main()
