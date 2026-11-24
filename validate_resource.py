#!/usr/bin/env python3
"""Validate an SE-KG RDF graph using SHACL and SPARQL."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph
from pyshacl import validate


def run_validation(graph, shapes_path):
    shapes = Graph()
    shapes.parse(shapes_path, format="turtle")

    conforms, report_graph, _ = validate(
        graph,
        shacl_graph=shapes,
        inference="none",
        abort_on_first=False,
        allow_infos=False,
        allow_warnings=False,
        advanced=True,
    )

    return {
        "conforms": bool(conforms),
        "report_triples": len(report_graph),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Validate the SE-KG RDF resource."
    )

    parser.add_argument(
        "--graph",
        required=True,
        help="Path to the RDF graph."
    )

    parser.add_argument(
        "--output",
        default="validation_results.json",
        help="Output JSON report path."
    )

    args = parser.parse_args()

    repository = Path(__file__).resolve().parent
    graph_path = Path(args.graph).resolve()

    if not graph_path.is_file():
        raise FileNotFoundError(graph_path)

    graph = Graph()
    graph.parse(graph_path)

    results = {
        "resource": "SE-KG",
        "timestamp_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "graph_triples": len(graph),
        "shacl": {},
        "sparql": {},
    }

    shape_files = {
        "structural": (
            repository
            / "sekg_shapes.ttl"
        ),
        "advanced": (
            repository
            / "sekg_evidence_provenance_shapes.ttl"
        ),
    }

    for name, path in shape_files.items():
        results["shacl"][name] = run_validation(
            graph, path
        )

    query_directory = (
        repository
    )

    queries = sorted(
        query_directory.glob("CQ*.rq")
    )

    if len(queries) != 8:
        raise RuntimeError(
            f"Expected 8 competency queries, found {len(queries)}"
        )

    for query_path in queries:
        query = query_path.read_text(
            encoding="utf-8"
        )

        result = graph.query(query)

        results["sparql"][query_path.stem] = {
            "result_type": result.type,
            "rows": (
                len(result)
                if result.type == "SELECT"
                else None
            ),
        }

    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path.write_text(
        json.dumps(
            results,
            indent=2
        ),
        encoding="utf-8"
    )

    print("SE-KG validation completed.")
    print("Graph triples:", len(graph))

    for name, result in results["shacl"].items():
        print(
            f"SHACL {name}:",
            "PASS" if result["conforms"] else "FAIL"
        )

    print("SPARQL queries executed:", len(results["sparql"]))
    print("Report:", output_path)


if __name__ == "__main__":
    main()
