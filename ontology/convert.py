"""
convert.py
==========
Converts the canonical Turtle source (hydlab.ttl) into:
  - ontology/hydlab.owl   (OWL/RDF XML)
  - ontology/hydlab.jsonld (JSON-LD)

Run from the repo root:
    python scripts/convert.py

All three files should be committed together. Never hand-edit the .owl or
.jsonld files — edit hydlab.ttl and re-run this script.
"""

from pathlib import Path
from rdflib import Graph

ONTOLOGY_DIR = Path(__file__).parent.parent / "ontology"
TTL_FILE     = ONTOLOGY_DIR / "hydlab.ttl"
OWL_FILE     = ONTOLOGY_DIR / "hydlab.owl"
JSONLD_FILE  = ONTOLOGY_DIR / "hydlab.jsonld"


def convert() -> None:
    print(f"Loading {TTL_FILE} ...")
    g = Graph()
    g.parse(str(TTL_FILE), format="turtle")
    print(f"  Parsed {len(g)} triples.")

    # ── OWL / RDF XML ────────────────────────────────────────────────────────
    g.serialize(destination=str(OWL_FILE), format="xml")
    print(f"  Written → {OWL_FILE}")

    # ── JSON-LD ──────────────────────────────────────────────────────────────
    g.serialize(destination=str(JSONLD_FILE), format="json-ld", indent=2)
    print(f"  Written → {JSONLD_FILE}")

    print("Done.")


if __name__ == "__main__":
    convert()
