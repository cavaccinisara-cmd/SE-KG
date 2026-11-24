# SE-KG Reproducibility Guide — v1.0.1 candidate

## Available artifacts

The repository root includes `SE-KG_PUBLIC_CANDIDATE.nt` (68,543 triples),
`sekg_ontology.ttl`, `sekg_shapes.ttl`, `sekg_evidence_provenance_shapes.ttl`,
eight `CQ*.rq` competency queries, and `validate_resource.py`.

## Requirements

Python 3.10+; pinned dependencies in `requirements.txt`.

## Installation and validation

Run from the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 validate_resource.py --graph SE-KG_PUBLIC_CANDIDATE.nt --output validation_results_v1.0.1.json
```

The script loads the N-Triples graph, performs structural and advanced
SHACL validation, executes eight SPARQL SELECT queries, and saves a JSON report.

## Observed validation on 24 November 2026

The user executed the commands locally on macOS. The archived report
`validation_results_v1.0.1.json` records:

| Check | Result |
|---|---|
| RDF graph | 68,543 triples |
| Structural SHACL | `conforms: true` |
| Advanced SHACL | `conforms: true` |
| CQ01–CQ08 | all executed; 19, 1, 2, 6, 12, 1, 15, 36 result rows |

The user also loaded `sekg_ontology.ttl` into Protégé, ran HermiT,
and confirmed consistency and no inferred named subclasses of `owl:Nothing`.
These reasoner observations are not recorded in the JSON script report.

## Interpretation and limitations

- SHACL conformance applies to the tested graph and the supplied shapes.
- Query execution does not prove that every returned binding is correct.
- HermiT consistency applies to the ontology loaded in Protégé, not necessarily
  to the complete RDF instance graph.
- CQ07 has a deterministic tie-breaking correction; pre-migration
  reports are preserved for historical comparison.
- The graph is publicly distributed as a research resource, not a clinical
  decision-support system. Reuse is subject to `DATA_LICENSE.md`.
- The namespace `https://w3id.org/sekg/` is used in the files; its HTTP
  dereferencing must be checked after the w3id PR is merged.
