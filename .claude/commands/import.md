---
description: Importa dati da YAML a Neo4j (restore/bulk)
allowed-tools:
  - Bash
  - Read
argument-hint: "[--clear]"
---

Esegui lo script di import per caricare i dati YAML in Neo4j.

## Comando

```bash
# Import normale (merge con dati esistenti)
python3 migration/import_yaml.py

# Preview senza modifiche
python3 migration/import_yaml.py --dry-run

# Reset completo (cancella tutto e reimporta)
python3 migration/import_yaml.py --clear
```

## Input

Lo script legge da `db/`:
- `db/persons.yaml` - Persone con affiliazioni
- `db/organizations.yaml` - Organizzazioni con stakeholders
- `db/families.yaml` - Famiglie con membri
- `db/events.yaml` - Eventi

## Comportamento

- **Default**: MERGE (aggiorna se esiste, crea se non esiste)
- **--clear**: Cancella TUTTI i dati Neo4j prima di importare (chiede conferma)
- **--dry-run**: Mostra cosa farebbe senza modificare Neo4j

## Uso

Esegui `/import` per:
- Restore da backup
- Bulk import dopo modifiche ai YAML
- Sync da altro ambiente
- Reset completo del database

## Argomento

$ARGUMENTS

Se l'utente passa `--clear`, usa l'opzione clear.
Se l'utente passa `--dry-run`, usa l'opzione dry-run.
