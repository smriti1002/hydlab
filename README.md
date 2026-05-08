# Hydrogen Research Infrastructure Ontology (HYDLAB)

A domain specific layered OWL ontology for the semantic modeling of hydrogen research infrastructure or a smart laboratory 

## Namespace

```
Prefix:  hydlab:
Base IRI: https://purl.org/hydlab/ns#
```

## Hierarchy at a glance

```
Organization
  └── Research Organization          (schema:ResearchOrganization)
  └── Area Science Park              (hydlab:AreaSciencePark)
        └── Technological Infrastructure  (hydlab:TechnologicalInfrastructure)
        │     └── Hydrogen Power Plant    (oeo:HydrogenPowerPlant)
        │           └── Main Process Unit
        └── H2INFRA
              └── APSU
                    └── Main Process Unit
                          └── Electrolyzer          (emmo:Device)
                          │     └── PEM Electrolyzer
                          └── Electrochemical Device (emmo:Device)
                                └── EIT  (owl:Thing)
                                      ├── sosa:observes       → Potential Difference
                                      ├── sosa:madeSampling   → Sensor
                                      ├── skos:concept        → Sensor
                                      ├── hydlab:hasSamplingFrequency → 1 Hz
                                      ├── hydlab:hasID        → Sensor ID
                                      └── om:hasUnit          → V
```

## Files

| Path | Purpose |
|------|---------|
| `ontology/hydlab.ttl`    | **Canonical source** — only this to be edited for future versions |
| `ontology/hydlab.owl`    | OWL/RDF XML — auto-generated with python script, not to be hand-edited |
| `ontology/hydlab.jsonld` | JSON-LD — auto-generated with python script, not to be hand-edited |
| `scripts/convert.py`     | Regenerates `.owl` and `.jsonld` from `.ttl` |
| `scripts/generate_docs.py` | Generates `docs/index.html` documentation page |
| `docs/index.html`        | Human-readable HTML documentation |
| `.github/workflows/ontology_ci.yml` | CI: validates and converts on every push |

## Quick start

```bash
pip install rdflib

# For Regenerating OWL/RDF and JSON-LD from the Turtle source
python scripts/convert.py

# To generate HTML documentation
pip install pylode beautifulsoup4   # optional but gives richer output
python scripts/generate_docs.py
```

## External ontology alignments

| Prefix | Ontology | Used for |
|--------|----------|---------|
| `schema:` | schema.org | Organization, ResearchOrganization |
| `sosa:` | W3C SOSA | Sensor, observes, madeSampling |
| `ssn-system:` | W3C SSN Systems | Frequency |
| `emmo:` | EMMO | Device (Electrolyzer, ElectrochemicalDevice) |
| `oeo:` | Open Energy Ontology | HydrogenPowerPlant |
| `qudt:` | QUDT | ElectricPotentialDifference |
| `om:` | Ontology of Units of Measure | hasUnit |
| `dcterms:` | Dublin Core | isPartOf |
| `skos:` | SKOS | broadMatch, concept |

## Versioning

Ontology releases are tagged `v1.0.0` (semantic versioning).
The version is declared in `hydlab.ttl` via `owl:versionInfo`.


## License

**Ontology files** (`ontology/` directory) are licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) —
one is free to share and adapt as long as attribution is given 
and distribute derivatives under the same license.

**Software** (scripts, pipeline code) is licensed under the
[MIT License](LICENSE) — Copyright (c) 2026 Smritirekha.