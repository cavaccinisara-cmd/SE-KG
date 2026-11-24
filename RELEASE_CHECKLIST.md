# SE-KG v1.0.1 — Release checklist (updated 24 November 2026)

- [x] Migrate RDF, OWL, SHACL and SPARQL namespace to `https://w3id.org/sekg/`.
- [x] Run local validation: 68,543 triples, structural SHACL PASS, advanced SHACL PASS, eight SPARQL queries executed. Evidence: `validation_results_v1.0.1.json`.
- [x] Run HermiT in Protégé on `sekg_ontology.ttl`: consistency confirmed by user; no classes observed below `owl:Nothing`.
- [ ] Record Protégé/HermiT versions and settings (and ideally save a reproducible reasoner log).
- [ ] Confirm redistribution rights and all licenses with contributors; check `DATA_LICENSE.md` and source snapshot attribution.
- [ ] Verify `CITATION.cff` authors and release metadata.
- [ ] Fix duplicate `.htaccess` and configure meaningful dereferencing in w3id PR #7281; confirm HTTP resolution after merge. This does not block GitHub access or DOI archiving.
- [ ] Publish the GitHub v1.0.1 release after licensing review; confirm Zenodo archive and obtain its actual new version DOI.
- [ ] Update ESWC paper with released resource URL, DOI, validation scope and license details.

**Scope:** SHACL validates stated constraints, SPARQL queries were executed (not fully manually adjudicated), and HermiT checks the schema loaded in Protégé. `PRE_MIGRATION_*` reports are historical.
