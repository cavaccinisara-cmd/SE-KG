# SE-KG: Semantic Evidence Knowledge Graph

**A provenance-aware RDF/OWL resource for biomedical topic grounding**

> **Release status:** v1.0.1 candidate, validated locally on 24 November 2026; GitHub release and Zenodo DOI for v1.0.1 not yet issued.
> Namespace adopted in the files: `https://w3id.org/sekg/`. Web resolution depends on completion of the w3id registration. Redistribution rights must be reviewed before release.

## Overview

SE-KG is a semantic resource designed to represent and query
evidence associated with biomedical topic grounding.

It connects topic-model outputs, terminology-grounding results,
hierarchical semantic similarity measurements, human evaluation
records, and provenance information within an RDF/OWL framework.

SE-KG is presented as a knowledge resource rather than as
a new topic-modeling or clustering algorithm.

## Research Context

The resource was developed using a cardiovascular subset of
the MultiCaRe 2026 corpus and terminology grounding against
the Medical Subject Headings (MeSH).

The experimental workflow included:

1. Biomedical text segmentation and representation.
2. Topic modeling and topic-level analysis.
3. Statistical topic-MeSH association testing.
4. Terminology grounding and hierarchical comparison.
5. Blinded human evaluation.
6. RDF/OWL representation and provenance modeling.
7. SHACL and SPARQL-based verification.

## Resource Characteristics

The verified research snapshot contains:

| Component | Quantity |
|---|---:|
| Cardiovascular cases | 1,105 |
| Source articles | 924 |
| Segmented sentences | 24,039 |
| Topics | 19 |
| Significant topic-MeSH associations | 114 |
| Hierarchical term pairs | 773 |
| Semantic similarity measurements | 6,184 |
| Human ratings | 36 |
| Ontology classes | 31 |
| Object properties | 35 |
| Datatype properties | 75 |
| Total RDF triples | 68,543 |
| Competency queries | 8 |
| SHACL node shapes | 11 |

These figures describe the verified research snapshot.
They do not imply that every underlying source record is
redistributable.

## Repository Structure

The current repository places the distributable artifacts in its root directory:

- `SE-KG_PUBLIC_CANDIDATE.nt`: RDF graph (68,543 triples).
- `sekg_ontology.ttl`: OWL ontology schema.
- `sekg_shapes.ttl` and `sekg_evidence_provenance_shapes.ttl`: SHACL constraints.
- `CQ01_*.rq` through `CQ08_*.rq`: SPARQL competency queries.
- `validate_resource.py` and `requirements.txt`: local validation tooling.
- `validation_results_v1.0.1.json`: validation execution report (24 November 2026).
- `MIGRATION_VALIDATION.json` and `PRE_MIGRATION_*`: migration and historical reports.
- `DATA_LICENSE.md`, `REPRODUCIBILITY.md`, `RELEASE_CHECKLIST.md`: documentation.

## Validation (v1.0.1 candidate)

On 24 November 2026, the locally executed `validate_resource.py` script
reported **68,543 RDF triples**, **SHACL structural conformance** and
**SHACL advanced conformance**. All eight SPARQL competency queries executed
successfully. Their SELECT result-row counts were, respectively,
**19, 1, 2, 6, 12, 1, 15, and 36**. The machine-readable execution
report is `validation_results_v1.0.1.json`.

HermiT was run in Protégé on `sekg_ontology.ttl`; the user observed
**logical consistency** and **no named classes under `owl:Nothing`** in
the inferred class hierarchy. This is a manually reported check, not an
automatically archived reasoner log. The version of Protégé/HermiT and
reasoner settings should be recorded for publication-grade reproducibility.

SHACL conformance checks the implemented constraints; successful SPARQL
execution does not by itself verify the correctness of every returned value.

CQ07 includes a deterministic tie-breaking correction. Historical
pre-migration reports must not be confused with v1.0.1 validation evidence.

## Provenance and Review Status

SE-KG models analytical provenance and records ontology
review candidates without treating them as automatically
human-approved ontology additions.

The verified snapshot contains 114 ontology review
candidates pending human review.

The presence of a candidate in the graph does not imply
expert acceptance.

## Data Availability

The RDF graph `SE-KG_PUBLIC_CANDIDATE.nt` is included in the repository
snapshot and can be downloaded with the ontology, shapes and queries.
The existing **v1.0.0** Zenodo version DOI is `10.5281/zenodo.24498384`.
Do **not** cite that DOI as a DOI for v1.0.1: a new version DOI is expected
only after the v1.0.1 release is archived.

The SE-KG namespace in these artifacts is `https://w3id.org/sekg/`.
Its public HTTP resolution is not yet verified; w3id registration is
tracked in upstream PR #7281. This does not prevent access to the files
through GitHub or the existing Zenodo archive.

## Reproducibility

Install dependencies and run validation from the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 validate_resource.py --graph SE-KG_PUBLIC_CANDIDATE.nt --output validation_results_v1.0.1.json
```

See `REPRODUCIBILITY.md` for interpretation and validation scope.

## Citation

Use `CITATION.cff` for resource metadata. Cite the specific published
release DOI once the v1.0.1 archive is available.

## License

**Check DATA_LICENSE.md for dataset-specific terms.**

No license is granted for underlying biomedical source
records or terminology data by the presence of this
pre-publication repository snapshot.

Redistribution conditions must be verified before release.


## Namespace migration candidate (v1.0.1)

The local SE-KG namespace was changed from `https://example.org/sekg/` to
`https://w3id.org/sekg/` across RDF, OWL, SHACL and competency queries.
The persistent namespace is **not active until w3id PR #7281 is merged**.
Pre-migration validation reports are retained with `PRE_MIGRATION_` filenames;
`validation_results_v1.0.1.json` records the new candidate validation.
See `MIGRATION_VALIDATION.json` and `RELEASE_CHECKLIST.md`.
