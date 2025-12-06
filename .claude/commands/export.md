---
description: Esporta dati da Neo4j a YAML (backup)
allowed-tools:
  - Bash
  - Read
argument-hint: ""
---

Esegui lo script di export per salvare i dati Neo4j su file YAML.

## Comando

```bash
python3 migration/export_neo4j.py
```

## Output

Lo script esporta in `db/`:
- `db/persons.yaml` - Tutte le persone con affiliazioni
- `db/organizations.yaml` - Tutte le organizzazioni con stakeholders
- `db/families.yaml` - Tutte le famiglie con membri
- `db/events.yaml` - Tutti gli eventi

## Verifica

Dopo l'export, mostra:
1. Conteggio entita' esportate
2. Data ultimo export (timestamp file)
3. Eventuali errori

## Uso

Esegui `/export` periodicamente per:
- Backup dei dati
- Versioning con Git
- Sincronizzazione offline
