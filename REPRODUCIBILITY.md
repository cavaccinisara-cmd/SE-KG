# SE-KG Reproducibility Guide

## Overview

This repository provides the SE-KG ontology schema,
SHACL validation shapes, SPARQL competency queries,
and a validation script.

The full RDF data graph is not included in the
pre-release repository while redistribution and
privacy checks remain pending.

## Requirements

- Python 3.10 or newer
- Dependencies listed in `requirements.txt`
- An RDF graph compatible with the SE-KG ontology

## Installation

From the repository root:

    python -m pip install -r requirements.txt

## Running validation

Execute:

    python scripts/validate_resource.py \
        --graph /path/to/SEKG_GRAPH.nt \
        --output validation_results.json

The graph path must point to a locally available
RDF file. The example path is a placeholder.

## Validation procedure

The script:

1. Loads the supplied RDF graph.
2. Executes structural SHACL validation.
3. Executes advanced SHACL validation.
4. Runs eight SPARQL competency queries.
5. Saves a JSON execution report.

## Verified pre-release test

The validation script was executed against a
sanitized SE-KG candidate containing 68,543 triples.

Observed results:

- Structural SHACL: conformant.
- Advanced SHACL: conformant.
- SPARQL competency queries: 8 executed successfully.

These results apply to the tested candidate graph
and do not establish that arbitrary RDF inputs
will conform.

## Interpretation

SHACL conformance verifies satisfaction of the
implemented constraints. It does not establish
complete biomedical correctness.

Successful SPARQL execution demonstrates that the
queries run without errors. It does not, by itself,
establish equivalence with reference query results.

## Deterministic query ordering

CQ07 uses an explicit secondary ordering key to
resolve ties at the LIMIT boundary.

The repository retains documentation of the
original ordering discrepancy and its correction.

## Resource availability

The ontology schema, SHACL shapes, SPARQL queries,
and validation script can be inspected independently
of the full RDF data graph.

Publication of the data graph remains subject to
final provenance, privacy, and redistribution review.
