"""
pylode_debug.py

To be run from the repo root:
    python ontology/pylode_debug.py

This script imports pyLODE's OntDoc and calls make_html, printing a full
traceback if an exception occurs so it can be diagnosed why pyLODE fell back
to the minimal HTML output.
"""

import sys
import traceback
from pathlib import Path

TTL_FILE = Path("ontology/hydlab.ttl")


def main():
    try:
        from pylode import OntDoc
        print("Imported pylode.OntDoc")
        od = OntDoc(ontology=str(TTL_FILE))
        print("Created OntDoc")
        raw_html = od.make_html()
        print(f"make_html completed, output length: {len(raw_html)}")
    except Exception as e:
        print("Exception during pyLODE run:", repr(e))
        traceback.print_exc()
        sys.exit(2)


if __name__ == "__main__":
    main()
