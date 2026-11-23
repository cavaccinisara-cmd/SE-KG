# SE-KG: Semantic Evidence Knowledge Graph

**A provenance-aware RDF/OWL resource for biomedical topic grounding**

> **Release status:** Pre-publication repository candidate.
> The complete RDF knowledge graph is not included in this
> repository snapshot pending final metadata, privacy, and
> redistribution-rights review.

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

- `data/`: Approved RDF distribution (pending).
- `ontology/`: Ontology schema (pending packaging).
- `validation/shacl/`: Structural and advanced SHACL shapes.
- `validation/sparql/`: Eight competency queries.
- `validation/reports/`: Validation and regression reports.
- `provenance/`: Provenance documentation (pending).
- `scripts/`: Reproducibility scripts (pending).
- `docs/`: Technical documentation (pending).
- `examples/`: Usage examples (pending).
- `ARTIFACT_MANIFEST.json`: SHA-256 checksums.

Some directories are intentionally empty during
pre-publication preparation.

## Validation

### SHACL

The sanitized RDF candidate was checked against:

- Structural SHACL constraints.
- Advanced evidence and provenance constraints.

Both validation runs reported conformance without violations
for the tested candidate graph.

Validation shapes and reports are available under
`validation/shacl/` and `validation/reports/`.

### SPARQL Competency Queries

Eight competency queries are provided in
`validation/sparql/`.

They cover topic inventory, association summaries,
terminology grounding, evidence tracing, human evaluation,
candidate review, hierarchical positioning, and ratings.

An initial regression comparison identified a difference
in CQ07 caused by an underspecified ordering at a tied
ranking boundary.

A deterministic secondary ordering was subsequently added.
The corrected CQ07 produced matching results across the
original and sanitized RDF graphs.

Both the initial regression report and the correction
record are preserved for transparency.

## Provenance and Review Status

SE-KG models analytical provenance and records ontology
review candidates without treating them as automatically
human-approved ontology additions.

The verified snapshot contains 114 ontology review
candidates pending human review.

The presence of a candidate in the graph does not imply
expert acceptance.

## Data Availability

The complete RDF graph is currently withheld from this
repository snapshot.

A sanitized candidate has been prepared and subjected to
structural and query-regression checks.

Final review of metadata, source-data redistribution
conditions, and publication permissions remains pending.

No public dataset release, persistent identifier, or
redistribution license is claimed at this stage.

## Reproducibility

The repository currently provides:

- SHACL validation shapes.
- SPARQL competency queries.
- Validation reports.
- SHA-256 artifact manifest.

Executable instructions and the final approved resource
distribution will be added before public release.

## Citation

Citation metadata will be provided once the associated
publication and repository release details are finalized.

## License

**License pending.**

No license is granted for underlying biomedical source
records or terminology data by the presence of this
pre-publication repository snapshot.

Redistribution conditions must be verified before release.
