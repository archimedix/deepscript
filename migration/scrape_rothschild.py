#!/usr/bin/env python3
"""
Scrape Rothschild family member profiles from family.rothschildarchive.org
and produce DeepScript-compatible YAML + Markdown schede.

Usage:
    python migration/scrape_rothschild.py                # full run
    python migration/scrape_rothschild.py --list-only    # scrape list only
    python migration/scrape_rothschild.py --resume       # resume from saved list
    python migration/scrape_rothschild.py --no-docs      # skip markdown generation
"""

import argparse
import os
import re
import time
import unicodedata
import warnings
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

BASE_URL = "https://family.rothschildarchive.org"
PEOPLE_URL = f"{BASE_URL}/people"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "docs" / "persons"
OUTPUT_PERSONS = PROJECT_ROOT / "migration" / "rothschild_scraped.yaml"
OUTPUT_RELATIONS = PROJECT_ROOT / "migration" / "rothschild_relations.yaml"
LINKS_CACHE = PROJECT_ROOT / "migration" / "rothschild_links.yaml"

SESSION = requests.Session()
SESSION.verify = False
SESSION.headers.update({"User-Agent": "DeepScript-Research/1.0"})

# ---------------------------------------------------------------------------
# ID generation
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    """Convert a name to a DeepScript-compatible id slug."""
    # Remove accents
    nfkd = unicodedata.normalize("NFKD", name)
    ascii_name = nfkd.encode("ascii", "ignore").decode("ascii")
    # Remove parenthetical nicknames like "(Willy Carl or Willy)"
    ascii_name = re.sub(r"\(.*?\)", "", ascii_name)
    # Lowercase, replace non-alphanum with dash, collapse dashes
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug


def infer_nationality(name: str) -> str:
    """Infer nationality from name prefix (von -> DEU/AUT, de -> FRA, else GBR)."""
    lower = name.lower()
    if " von " in lower:
        return "DEU"
    if " de " in lower:
        return "FRA"
    return "GBR"


# ---------------------------------------------------------------------------
# Step 1: Scrape people list
# ---------------------------------------------------------------------------

def scrape_people_list() -> list[dict]:
    """Fetch the list of 188 people from the index page."""
    print("Fetching people list...")
    r = SESSION.get(PEOPLE_URL, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.select('a[href*="/people/"]')
    people = []
    for a in links:
        href = a.get("href", "")
        if not re.match(r"/people/\d+-", href):
            continue
        full_text = a.get_text(separator=" ", strip=True)
        # Name is before the year range
        name_part = re.split(r"\d{4}", full_text)[0].strip()
        people.append({"href": href, "name": name_part, "slug": slugify(name_part)})
    print(f"  Found {len(people)} profiles")
    return people


def save_links(people: list[dict]):
    with open(LINKS_CACHE, "w") as f:
        yaml.dump(people, f, allow_unicode=True)
    print(f"  Saved links to {LINKS_CACHE}")


def load_links() -> list[dict]:
    with open(LINKS_CACHE) as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# Step 2: Scrape individual profiles
# ---------------------------------------------------------------------------

def scrape_profile(href: str) -> dict | None:
    """Fetch and parse a single profile page."""
    url = f"{BASE_URL}{href}"
    try:
        r = SESSION.get(url, timeout=30)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"    ERROR fetching {url}: {e}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    # Name and dates from <h1>
    h1 = soup.find("h1")
    if not h1:
        return None
    h1_text = h1.get_text(strip=True)

    # Extract years from parentheses: "(1843-1922)" or "(1980-)"
    years = re.search(r"\((\d{4})\s*-\s*(\d{4})?\)", h1_text)
    born = int(years.group(1)) if years else None
    died = int(years.group(2)) if years and years.group(2) else None
    # Clean name (remove year part)
    name = re.sub(r"\s*\(\d{4}.*?\)\s*$", "", h1_text).strip()

    # Biography from div.biography
    bio_div = soup.find("div", class_="biography")
    bio_text = bio_div.get_text(separator="\n", strip=True) if bio_div else ""
    # The bio often starts with the person's name repeated — strip it
    if bio_text:
        lines = bio_text.split("\n")
        # Remove leading lines that are just the name (or part of it)
        while lines and lines[0].strip() and not lines[0].strip().endswith("."):
            first_line = lines[0].strip().lower()
            name_lower = name.lower()
            # If the line is just the name or a fragment of it
            if first_line in name_lower or name_lower.startswith(first_line):
                lines.pop(0)
            else:
                break
        bio_text = " ".join(l.strip() for l in lines if l.strip())

    # Genealogy link
    gen_link = None
    for a in soup.find_all("a", href=True):
        if "genealogy" in a["href"]:
            gen_link = a["href"]
            break

    return {
        "name": name,
        "born": born,
        "died": died,
        "bio": bio_text,
        "genealogy_url": gen_link,
        "source_url": f"{BASE_URL}{href}",
    }


# ---------------------------------------------------------------------------
# Step 3: Extract relations from biography text
# ---------------------------------------------------------------------------

RELATION_PATTERNS = [
    # Father / mother
    (r"(?:son|daughter) of ([A-Z][a-zà-ü]+(?: (?:von|de|d'))?[A-Z][a-zà-ü]+(?: \(\d{4}-\d{4}\))?)", "family", "father/mother"),
    # Married / spouse
    (r"married (?:her |his )?(?:cousin )?([A-Z][a-zà-ü]+(?: (?:von|de|d'))?[A-Z][a-zà-ü]+)", "spouse", "married"),
    (r"(?:wife|husband) of ([A-Z][a-zà-ü]+(?: (?:von|de|d'))?[A-Z][a-zà-ü]+)", "spouse", "spouse"),
]

def extract_relations_from_bio(bio: str) -> list[dict]:
    """Extract family relations from biography text using regex patterns."""
    relations = []
    seen = set()

    # Name pattern: optional title + capitalized words with particles
    NAME = r"(?:(?:Baron(?:ess)?|Sir|Lady|Lord|Prince(?:ss)?|Count(?:ess)?)\s+)?[A-ZÀ-Ü][a-zà-ü]+(?:\s+(?:von|de|d'|van|el-|di))?(?:\s+[A-ZÀ-Ü][a-zà-ü]+)+"

    # Pattern: "son/daughter of X (YYYY-YYYY)"
    for m in re.finditer(
        rf"(?:son|daughter|child) of ({NAME})(?:\s*\((\d{{4}})-(\d{{4}})?\))?",
        bio,
    ):
        name = m.group(1).strip()
        # Strip titles for the slug
        clean = re.sub(r"^(?:Baron(?:ess)?|Sir|Lady|Lord|Prince(?:ss)?|Count(?:ess)?)\s+", "", name)
        slug = slugify(clean)
        if slug not in seen:
            relations.append({"person": slug, "type": "family", "note": "parent", "name_raw": clean})
            seen.add(slug)

    # Pattern: "married X" or "married her/his cousin X"
    for m in re.finditer(
        rf"married (?:her |his )?(?:cousin )?({NAME})",
        bio,
    ):
        name = m.group(1).strip()
        clean = re.sub(r"^(?:Baron(?:ess)?|Sir|Lady|Lord|Prince(?:ss)?|Count(?:ess)?)\s+", "", name)
        slug = slugify(clean)
        if slug not in seen:
            relations.append({"person": slug, "type": "spouse", "note": "married", "name_raw": clean})
            seen.add(slug)

    # Pattern: "wife/husband of X"
    for m in re.finditer(
        rf"(?:wife|husband) of ({NAME})",
        bio,
    ):
        name = m.group(1).strip()
        clean = re.sub(r"^(?:Baron(?:ess)?|Sir|Lady|Lord|Prince(?:ss)?|Count(?:ess)?)\s+", "", name)
        slug = slugify(clean)
        if slug not in seen:
            relations.append({"person": slug, "type": "spouse", "note": "spouse", "name_raw": clean})
            seen.add(slug)

    # Pattern: "gave birth to X" or "had a son/daughter X"
    for m in re.finditer(
        rf"(?:gave birth to|bore|had (?:a |one )?(?:son|daughter|child)[, ]+)({NAME})",
        bio,
    ):
        name = m.group(1).strip()
        clean = re.sub(r"^(?:Baron(?:ess)?|Sir|Lady|Lord|Prince(?:ss)?|Count(?:ess)?)\s+", "", name)
        slug = slugify(clean)
        if slug not in seen:
            relations.append({"person": slug, "type": "family", "note": "child", "name_raw": clean})
            seen.add(slug)

    return relations


# ---------------------------------------------------------------------------
# Step 5: Output YAML
# ---------------------------------------------------------------------------

def build_output(people_data: list[dict]) -> tuple[dict, dict]:
    """Build persons YAML and relations YAML from scraped data."""
    persons = {}
    all_relations = {}

    for p in people_data:
        if not p.get("profile"):
            continue
        prof = p["profile"]
        pid = slugify(prof["name"])

        entry = {}
        if prof["born"]:
            entry["born"] = prof["born"]
        if prof["died"]:
            entry["died"] = prof["died"]

        nat = infer_nationality(prof["name"])
        entry["nationality"] = nat
        entry["family"] = "rothschild"

        # First sentence as note (truncated), prepend name if bio starts lowercase
        if prof["bio"]:
            first_sent = prof["bio"].split(".")[0].strip()
            if first_sent and first_sent[0].islower():
                first_sent = prof["name"] + " " + first_sent
            if len(first_sent) > 200:
                first_sent = first_sent[:197] + "..."
            entry["note"] = first_sent + "."

        entry["source"] = prof["source_url"]

        persons[pid] = entry

        # Relations
        rels = extract_relations_from_bio(prof["bio"])
        if rels:
            # Strip name_raw for output
            clean_rels = []
            for r in rels:
                clean_rels.append({
                    "person": r["person"],
                    "type": r["type"],
                    "note": r["note"],
                })
            all_relations[pid] = clean_rels

    return {"persons": persons}, {"relations": all_relations}


def save_yaml(data: dict, path: Path):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=True, width=120)
    print(f"  Saved {path}")


# ---------------------------------------------------------------------------
# Step 6: Generate Markdown schede
# ---------------------------------------------------------------------------

def generate_markdown(pid: str, prof: dict, relations: list[dict]) -> str:
    """Generate a markdown scheda for a person."""
    name = prof["name"]
    born = prof["born"] or "?"
    died = prof["died"]
    year_range = f"{born} - {died}" if died else f"{born} -"
    bio = prof.get("bio", "")

    # Tagline: first sentence, prepend name if starts lowercase
    if bio:
        tagline = bio.split(".")[0].strip()
        if tagline and tagline[0].islower():
            tagline = name + " " + tagline
        tagline += "."
    else:
        tagline = "Membro della famiglia Rothschild."

    # Extract parent/spouse/children from relations
    parents = [r for r in relations if r["note"] == "parent"]
    spouses = [r for r in relations if r["type"] == "spouse"]
    children = [r for r in relations if r["note"] == "child"]

    # Nationality label
    nat = infer_nationality(name)
    branch_map = {"DEU": "Francoforte/Vienna", "FRA": "Parigi", "GBR": "Londra"}
    branch = branch_map.get(nat, "")

    lines = []
    lines.append(f"# {name} ({year_range})")
    lines.append("")
    lines.append(f"> {tagline}")
    lines.append("")
    lines.append("## Dati Essenziali")
    lines.append("")
    lines.append("| Aspetto | Dettaglio |")
    lines.append("|---------|-----------|")
    if prof["born"]:
        lines.append(f"| **Nascita** | {prof['born']} |")
    if prof["died"]:
        lines.append(f"| **Morte** | {prof['died']} |")
    lines.append(f"| **Famiglia** | Rothschild, ramo {branch} |")
    if parents:
        for p in parents:
            lines.append(f"| **Genitore** | [{p.get('name_raw', p['person'])}]({p['person']}.md) |")
    if spouses:
        for s in spouses:
            lines.append(f"| **Coniuge** | [{s.get('name_raw', s['person'])}]({s['person']}.md) |")
    if children:
        child_names = ", ".join(
            f"[{c.get('name_raw', c['person'])}]({c['person']}.md)" for c in children
        )
        lines.append(f"| **Figli** | {child_names} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Biography section (brief, no copyright issues)
    if bio:
        lines.append("## Biografia")
        lines.append("")
        # Summarize key facts only - not reproducing full text
        sentences = [s.strip() for s in bio.split(".") if s.strip()]
        # Take first 2-3 sentences max as overview
        summary = ". ".join(sentences[:3]) + "." if sentences else ""
        if len(summary) > 400:
            summary = ". ".join(sentences[:2]) + "."
        # Prepend name if starts lowercase
        if summary and summary[0].islower():
            summary = name + " " + summary
        lines.append(summary)
        lines.append("")
        lines.append("---")
        lines.append("")

    # Connessioni PowerLink
    lines.append("## Connessioni PowerLink")
    lines.append("")
    if relations:
        lines.append("### Persone")
        lines.append("")
        lines.append("| Persona | Relazione |")
        lines.append("|---------|-----------|")
        for r in relations:
            label = r.get("name_raw", r["person"])
            note = r["note"]
            lines.append(f"| [{label}]({r['person']}.md) | {note} |")
        lines.append("")

    lines.append("### Famiglia")
    lines.append("")
    lines.append("| Famiglia | Ruolo |")
    lines.append("|----------|-------|")
    lines.append(f"| [Rothschild](../family/rothschild.md) | Ramo {branch} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Fonti")
    lines.append("")
    lines.append("### Biografie")
    lines.append(f"- [Rothschild Archive]({prof['source_url']})")
    if prof.get("genealogy_url"):
        lines.append(f"- [Genealogia Rothschild]({prof['genealogy_url']})")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Ultimo aggiornamento: Febbraio 2026*")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Scrape Rothschild Archive profiles")
    parser.add_argument("--list-only", action="store_true", help="Only scrape the people list")
    parser.add_argument("--resume", action="store_true", help="Resume from saved links")
    parser.add_argument("--no-docs", action="store_true", help="Skip markdown generation")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of profiles to scrape (0=all)")
    args = parser.parse_args()

    # Step 1: Get people list
    if args.resume and LINKS_CACHE.exists():
        people = load_links()
        print(f"Resumed {len(people)} links from cache")
    else:
        people = scrape_people_list()
        save_links(people)

    if args.list_only:
        return

    # Step 2: Scrape profiles
    total = len(people)
    if args.limit:
        total = min(args.limit, total)

    print(f"\nScraping {total} profiles...")
    for i, p in enumerate(people[:total]):
        slug = slugify(p["name"])
        print(f"  [{i+1}/{total}] {slug}", flush=True)
        profile = scrape_profile(p["href"])
        p["profile"] = profile
        # Polite delay
        if i < total - 1:
            time.sleep(1.5)

    # Count successes
    ok = sum(1 for p in people[:total] if p.get("profile"))
    print(f"\nScraped {ok}/{total} profiles successfully")

    # Step 3-4: Build output with relations
    persons_yaml, relations_yaml = build_output(people[:total])
    print(f"Generated {len(persons_yaml.get('persons', {}))} person entries")
    print(f"Extracted relations for {len(relations_yaml.get('relations', {}))} persons")

    # Step 5: Save YAML
    save_yaml(persons_yaml, OUTPUT_PERSONS)
    save_yaml(relations_yaml, OUTPUT_RELATIONS)

    # Step 6: Generate markdown
    if not args.no_docs:
        DOCS_DIR.mkdir(parents=True, exist_ok=True)
        created = 0
        skipped = 0
        for p in people[:total]:
            if not p.get("profile"):
                continue
            prof = p["profile"]
            pid = slugify(prof["name"])
            md_path = DOCS_DIR / f"{pid}.md"
            if md_path.exists():
                skipped += 1
                continue
            rels = extract_relations_from_bio(prof["bio"])
            md = generate_markdown(pid, prof, rels)
            md_path.write_text(md, encoding="utf-8")
            created += 1
        print(f"\nMarkdown: {created} created, {skipped} skipped (already exist)")

    print("\nDone! Review output files:")
    print(f"  {OUTPUT_PERSONS}")
    print(f"  {OUTPUT_RELATIONS}")
    if not args.no_docs:
        print(f"  {DOCS_DIR}/")


if __name__ == "__main__":
    main()
