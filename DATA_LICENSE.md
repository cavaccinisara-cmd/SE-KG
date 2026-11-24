# SE-KG: Data provenance, licensing and attribution

## Scope

This document describes third-party data sources represented in SE-KG and their applicable conditions. It does not grant rights over third-party material beyond those provided by the respective rights holders.

The repository distributes a derived RDF knowledge graph, ontology and validation artifacts. The source clinical reports and images are not intentionally redistributed as original documents. Article-level provenance identifiers and terminology mappings may remain in the graph.

## MultiCaRe

**Source:** MultiCaRe: An open-source clinical case dataset for medical image classification and multimodal AI applications, by Mauro Nievas Offidani and contributors.

**Reference record:** https://zenodo.org/records/20416562 (version 3.0.1; DOI: 10.5281/zenodo.20416562).

**Dataset-level license:** Creative Commons Attribution–NonCommercial–ShareAlike 4.0 International (CC BY-NC-SA 4.0): https://creativecommons.org/licenses/by-nc-sa/4.0/

The dataset record states that individual components can carry different, sometimes less restrictive, licenses. Users must respect the license applicable to any underlying content they reuse. The version of the precise corpus snapshot used in the experiments should be checked against the frozen experimental manifests before being represented as definitively identical to Zenodo v3.0.1.

Where material from MultiCaRe is adapted in the released RDF graph, that adapted material is offered subject to CC BY-NC-SA 4.0, including attribution, non-commercial use and ShareAlike requirements. This statement does not purport to relicense independent original software or third-party content under other terms.

## MeSH 2026

**Source:** Medical Subject Headings (MeSH), 2026 release, U.S. National Library of Medicine (NLM).

**Terms:** https://www.nlm.nih.gov/databases/download/terms_and_conditions_mesh.html

NLM freely provides MeSH data, subject to its terms. SE-KG acknowledges NLM as the source of MeSH identifiers, descriptors and hierarchical information. SE-KG is not endorsed by NLM. The graph uses the **2026 release** and may not reflect the most current MeSH data.

## Original project materials

Original code, ontology design, SHACL constraints, SPARQL queries, documentation and reports may have separate rights and license terms. Do not assume the MultiCaRe dataset license automatically applies to all such artifacts. A repository-wide LICENSE file should be chosen only after confirming rights and agreement among contributors.

## Release limitations

SE-KG is a research resource, not a clinical decision-support system. Statistical associations and ontology review candidates do not establish clinical validity or human approval. No redistribution rights are claimed over original articles or images beyond the rights provided by their respective holders.

## Suggested attribution

SE-KG contributors. *SE-KG: provenance-aware biomedical semantic evidence knowledge graph*. Repository: https://github.com/cavaccinisara-cmd/SE-KG (access date and version/commit recommended).

Nievas Offidani, M. *MultiCaRe: An open-source clinical case dataset for medical image classification and multimodal AI applications*, Zenodo record 20416562, version 3.0.1. https://doi.org/10.5281/zenodo.20416562.

U.S. National Library of Medicine. *Medical Subject Headings (MeSH), 2026 release*. https://www.nlm.nih.gov/mesh/.
