# SE-KG v1.0.1 — Release checklist

- [x] Migrate RDF, OWL, SHACL and SPARQL local namespace.
- [x] Parse RDF and Turtle; run SPARQL queries (see MIGRATION_VALIDATION.json).
- [ ] Correct the duplicate `.htaccess` file in w3id PR #7281 and confirm useful redirects.
- [ ] Wait for w3id PR merge; test URI resolution.
- [ ] Run SHACL validation with `pip install -r requirements.txt` then `python validate_resource.py --graph SE-KG_PUBLIC_CANDIDATE.nt --output validation_results_v1.0.1.json`.
- [ ] Run HermiT in Protege on the migrated ontology; record version, consistency result, and unsatisfiable classes check.
- [ ] Confirm data and ontology licenses/rights with authors; review DATA_LICENSE.md.
- [ ] Publish GitHub v1.0.1 only after all checks; let Zenodo mint a new version DOI.
- [ ] Update ESWC paper to cite the actual published version and DOI.

**Important:** PRE_MIGRATION_* files are historical, not evidence for this candidate.
