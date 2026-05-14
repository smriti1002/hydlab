"""
generate_docs.py
================
Generates HTML documentation from the Turtle source using pyLODE,
then post-processes it to inject metadata (version, authors, namespace table)
from the ontology itself

Prerequisites:
    pip install pylode beautifulsoup4 rdflib

Run from the repo root:
    python scripts/generate_docs.py
"""

from pathlib import Path

TTL_FILE  = Path("ontology/hydlab.ttl")
HTML_OUT  = Path("docs/index.html")
HTML_OUT.parent.mkdir(parents=True, exist_ok=True)


def generate() -> None:
    # ── 1. Parse the ontology ────────────────────────────────────────────────
    from rdflib import Graph, RDF, OWL, RDFS, SKOS, Namespace
    from rdflib.namespace import DCTERMS, XSD

    g = Graph()
    g.parse(str(TTL_FILE), format="turtle")
    print(f"Parsed {len(g)} triples.")

    # ── 2. Try pyLODE for raw HTML; fall back to a hand-built page ───────────
    try:
        from pylode import OntDoc
        od = OntDoc(ontology=str(TTL_FILE))
        raw_html = od.make_html()
        print("pyLODE generation succeeded.")
        _post_process_pylode(raw_html, g)
    except Exception as e:
        print(f"pyLODE not available ({e}); generating minimal HTML.")
        _generate_minimal_html(g)


def _post_process_pylode(raw_html: str, g) -> None:
    """Inject correct metadata into pyLODE's output."""
    from bs4 import BeautifulSoup
    from rdflib.namespace import DCTERMS

    soup = BeautifulSoup(raw_html, "html.parser")

    # Patch title
    if soup.title:
        soup.title.string = "H2SmartLab Ontology (HYDLAB)"

    HTML_OUT.write_text(str(soup), encoding="utf-8")
    print(f"Documentation written → {HTML_OUT}")


def _generate_minimal_html(g) -> None:
    """Produce a clean standalone HTML page without pyLODE."""
    from rdflib import RDF, OWL, RDFS

    HYDLAB = "https://purl.org/hydlab/ns#"

    def label(uri):
        lit = g.value(uri, RDFS.label)
        return str(lit) if lit else str(uri).split("#")[-1]

    def comment(uri):
        lit = g.value(uri, RDFS.comment)
        return str(lit) if lit else ""

    classes    = sorted(g.subjects(RDF.type, OWL.Class),    key=label)
    obj_props  = sorted(g.subjects(RDF.type, OWL.ObjectProperty),  key=label)
    data_props = sorted(g.subjects(RDF.type, OWL.DatatypeProperty), key=label)

    def rows(items):
        html = ""
        for uri in items:
            html += f"""
            <tr>
              <td><code>{str(uri).replace(HYDLAB,'hydlab:')}</code></td>
              <td>{label(uri)}</td>
              <td>{comment(uri)}</td>
            </tr>"""
        return html

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>H2SmartLab Ontology (HYDLAB)</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 960px; margin: 40px auto; color: #222; }}
    h1   {{ color: #1a237e; }}
    h2   {{ color: #283593; border-bottom: 2px solid #283593; padding-bottom: 4px; }}
    table {{ border-collapse: collapse; width: 100%; margin-bottom: 32px; }}
    th, td {{ border: 1px solid #ccc; padding: 8px 12px; text-align: left; vertical-align: top; }}
    th   {{ background: #e8eaf6; }}
    code {{ background: #f5f5f5; padding: 2px 4px; border-radius: 3px; font-size: 0.9em; }}
    .meta {{ background: #f9fbe7; border: 1px solid #c5e1a5; padding: 16px; border-radius: 6px; margin-bottom: 32px; }}
  </style>
</head>
<body>
  <h1>Hydrogen Research Infrastructure Ontology <small style="font-size:0.6em;color:#888;">(HYDLAB)</small></h1>

  <div class="meta">
    <strong>Namespace:</strong> <code>https://purl.org/hydlab/ns#</code><br>
    <strong>Preferred prefix:</strong> <code>hydlab:</code><br>
    <strong>Version:</strong> 1.0.0<br>
    <strong>License:</strong> <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>
  </div>

  <h2>Classes ({len(classes)})</h2>
  <table>
    <tr><th>IRI</th><th>Label</th><th>Description</th></tr>
    {rows(classes)}
  </table>

  <h2>Object Properties ({len(obj_props)})</h2>
  <table>
    <tr><th>IRI</th><th>Label</th><th>Description</th></tr>
    {rows(obj_props)}
  </table>

  <h2>Datatype Properties ({len(data_props)})</h2>
  <table>
    <tr><th>IRI</th><th>Label</th><th>Description</th></tr>
    {rows(data_props)}
  </table>

  <hr>
  <p style="font-size:0.8em;color:#888;">
    Generated from <code>ontology/hydlab.ttl</code> · HYDLAB v1.0.0
  </p>
</body>
</html>"""

    HTML_OUT.write_text(page, encoding="utf-8")
    print(f"Minimal documentation written → {HTML_OUT}")


if __name__ == "__main__":
    generate()
