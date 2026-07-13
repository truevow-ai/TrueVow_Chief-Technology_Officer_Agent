# run-sync-and-index
## Function: Infrastructure
## Trigger: After significant session work or new files added to vault
## Who: Orchestrator

Run `knowledge-sync` + `knowledge-indexer` to refresh the vault. Delete `.vector-index.json` to force reindex.
