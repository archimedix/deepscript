---
description: Aggiungi persona, istituzione, evento, famiglia o media a DeepScript
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - WebSearch
  - WebFetch
argument-hint: "<tipo> <nome>"
---

Argomento: $ARGUMENTS

Formato: `<tipo> <nome-entita>`
- tipo: persona | famiglia | istituzione | evento | media
- nome: identificativo (es. "mario-draghi", "rockefeller", "bilderberg")

Se manca tipo o nome, chiedi all'utente.

## Workflow

### 1. Leggi template e database

Template: `templates/<tipo>.md` (famiglia usa `templates/famiglia.md`)
Database: `<tipo>.yaml` (famiglia usa `famiglie.yaml`)

Verifica se l'entita' esiste. Se stub (senza `file:`), procedi a creare scheda.

### 2. Cerca informazioni

WebSearch per:
- Fonti ufficiali, Wikipedia, SEC
- Ruoli e affiliazioni
- Connessioni con entita' del progetto

Focus su:
- Forum (Bilderberg, Trilaterale, WEF, CFR, Aspen)
- Revolving door pubblico-privato
- Connessioni italiane

### 3. Crea scheda markdown

Percorsi:
- persona → `persone/<nome>.md`
- famiglia → `family/<nome>.md`
- istituzione → `istituzioni/<nome>.md`
- evento → `eventi/<nome>.md`
- media → `media/<nome>.md`

Stile: dati verificabili, fonti citate, no speculazioni.

### 4. Aggiorna database YAML

IMPORTANTE: Leggi `index.yaml` per enum validi, cerca sempre un significato equivalente prima di inventare un nuovo tag. Se ti sembra che sia necessario, allora crealo.

Persona:
```yaml
nome:
  file: persone/nome.md
  nato: ANNO
  naz: COD
  affiliazioni:
    - {org: x, ruolo: RUOLO, dal: ANNO}
```

Istituzione:
```yaml
nome:
  file: istituzioni/nome.md
  tipo: TIPO
  fondato: ANNO
  stakeholders:
    - {persona: x, ruolo: RUOLO}
```

### 5. Crosslink

Per ogni entita' referenziata:
1. Se non esiste → crea stub nel YAML
2. Se ha scheda → aggiorna sezione Connessioni nel .md
3. Bidirezionale: affiliazioni ↔ stakeholders

### 6. Report

- File creato
- Entry YAML aggiunta
- Stub creati
- Crosslink aggiornati
