[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20202095.svg)](https://doi.org/10.5281/zenodo.20202095)
# Hydrogen Research Infrastructure Ontology (HYDLAB)

A domain specific layered OWL ontology for the semantic modeling of hydrogen research infrastructure or a smart laboratory 

## Namespace

```
Prefix:  hydlab:
Base IRI: https://purl.org/hydlab/ns#
```

## Hierarchy at a glance

```
TBox (Schema Level — Classes and Properties)

owl:Thing
└── Entity
      ├── Organization                              (schema:Organization)
      │     └── Research Organization               (schema:ResearchOrganization)
      │
      └── Technological Infrastructure              (hydlab:TechnologicalInfrastructure)
            └── Hydrogen Power Plant                (oeo:HydrogenPowerPlant)
                  └── Main Process Unit             (hydlab:MainProcessUnit)
                        └── Electrochemical Device  (emmo:Device)
                              └── Electrolyzer
                                    └── PEM Electrolyzer
                                          └── Sensor          (sosa:Sensor)

 ABox (Instance Level — Named Individuals)

Individuals of type: Research Organization
└── hydlab:AreaSciencePark
      └── rdfs:label → "Area Science Park"

Individuals of type: Technological Infrastructure
└── hydlab:H2INFRA
      └── dcterms:isPartOf → hydlab:AreaSciencePark

Individuals of type: Hydrogen Power Plant
└── hydlab:APSU
      └── dcterms:isPartOf → hydlab:H2INFRA

Individuals of type: Main Process Unit
└── hydlab:H2SmartLab
      └── dcterms:isPartOf → hydlab:APSU

Individuals of type: Electrolyzer
└── hydlab:Electrolyzer
      └── dcterms:isPartOf → hydlab:H2SmartLab

Individuals of type: PEM Electrolyzer
└── hydlab:PEMElectrolyzer
      └── dcterms:isPartOf → hydlab:H2SmartLab

Individuals of type: Sensor
└── hydlab:EIT
      ├── rdfs:label → "Electrical Impedance Tomography"
      ├── dcterms:isPartOf → hydlab:PEMElectrolyzer
      ├── sosa:observes → hydlab:ElectricalPotentialDifference
      ├── sosa:madeSampling → hydlab:madeSampling
      ├── hydlab:hasSamplingFrequency → "1"^^xsd:float
      ├── hydlab:hasID → "EIT-001"^^xsd:string
      └── om:hasUnit → om:volt

Individuals of type: Observable Property
└── hydlab:PotentialDifference
      └── rdf:type → qudt:ElectricPotentialDifference

Individuals of type: Measurement
└── hydlab:madeSampling
      └── rdf:type → ssn-system:Frequency         → V
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
| `scripts/pylode_debug.py`        | Debug script: runs pyLODE and shows the full error if HTML generation fails |
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
