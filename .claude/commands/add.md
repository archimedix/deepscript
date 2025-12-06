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
  - mcp__neo4j-cypher__read-cypher
  - mcp__neo4j-cypher__write-cypher
argument-hint: "<tipo> <nome>"
---

Argomento: $ARGUMENTS

Formato: `<tipo> <nome-entita>`
- tipo: person | org | family | event
- nome: identificativo (es. "mario-draghi", "rockefeller", "bilderberg")

Se manca tipo o nome, chiedi all'utente.

## Workflow

### 1. Verifica se esiste in Neo4j

```cypher
// Per persona
MATCH (p:Person {id: 'nome-id'}) RETURN p

// Per organizzazione
MATCH (o:Organization {id: 'nome-id'}) RETURN o, labels(o)
```

Controlla se esiste gia' la scheda in `docs/`.
- Se nodo esiste E scheda esiste → gia' documentata.
- Se nodo esiste MA scheda non esiste → stub, procedi a documentare.
- Se nodo non esiste → nuova entita'.

### 2. Cerca informazioni

WebSearch per:
- Fonti ufficiali, Wikipedia, SEC
- Ruoli e affiliazioni
- Connessioni con entita' del progetto

Focus su:
- Forum (Bilderberg, Trilaterale, WEF, CFR, Aspen)
- Revolving door pubblico-privato
- Connessioni italiane

### 3. Aggiungi a Neo4j

**Person:**
```cypher
MERGE (p:Person {id: 'nome-id'})
SET p.born = 1970,
    p.nationality = 'ITA'
```

**Organization (con sub-label):**
```cypher
MERGE (o:Organization {id: 'nome-id'})
SET o:Forum,  // o Bank, Company, ThinkTank, etc.
    o.founded = 1970,
    o.headquarters = 'City, Country',
    o.status = 'active'
```

**Affiliazione (Person → Organization):**
```cypher
MATCH (p:Person {id: 'person-id'})
MATCH (o:Organization {id: 'org-id'})
MERGE (p)-[r:AFFILIATED_WITH]->(o)
SET r.role = 'executive',
    r.from = 2020,
    r.to = 2023,
    r.note = 'CEO'
```

**Family:**
```cypher
MERGE (f:Family {id: 'nome-id'})
SET f.origin = 'USA',
    f.founder = 'person-id',
    f.sector = 'finance',
    f.status = 'active'
```

### 4. Crea scheda markdown

Path deterministico: `docs/{cartella}/{id}.md`

| Tipo | Cartella |
|------|----------|
| person | `docs/persons/` |
| family | `docs/family/` |
| event | `docs/events/` |
| org:Forum | `docs/forum/` |
| org:Bank | `docs/bank/` |
| org:CentralBank | `docs/central-bank/` |
| org:AssetManager | `docs/asset-manager/` |
| org:PrivateEquity | `docs/private-equity/` |
| org:SWF | `docs/swf/` |
| org:Government | `docs/government/` |
| org:Foundation | `docs/foundation/` |
| org:ThinkTank | `docs/think-tank/` |
| org:Company | `docs/company/` |
| org:Agency | `docs/agency/` |
| org:Media | `docs/media/` |

Template: `templates/<tipo>.md`

Stile: dati verificabili, fonti citate, no speculazioni.

### 5. Crea stub per entita' referenziate

Per ogni org/person referenziata che non esiste:
```cypher
// Stub persona
MERGE (p:Person {id: 'ref-id'})
SET p.nationality = 'XXX'

// Stub org
MERGE (o:Organization {id: 'ref-id'})
SET o:Company, o.status = 'active'
```

### 6. Report

- Nodo creato/aggiornato (Person/Organization/Family/Event)
- Relazioni create (AFFILIATED_WITH, MEMBER_OF, STAKE_IN)
- Scheda .md creata (path)
- Stub creati

---

## Reference: Sub-labels e Cartelle

| Sub-label | Cartella | Esempi |
|-----------|----------|--------|
| Forum | docs/forum/ | Bilderberg, WEF, Trilaterale |
| Bank | docs/bank/ | Goldman Sachs, JPMorgan |
| CentralBank | docs/central-bank/ | Fed, BCE, BIS |
| AssetManager | docs/asset-manager/ | BlackRock, Vanguard |
| PrivateEquity | docs/private-equity/ | Warburg Pincus, Carlyle |
| SWF | docs/swf/ | GPFG, QIA, PIF |
| Government | docs/government/ | governo-usa, governo-italia |
| Foundation | docs/foundation/ | Gates Foundation, Open Society |
| ThinkTank | docs/think-tank/ | CFR, Rand, Aspen |
| Company | docs/company/ | Apple, Tesla |
| Agency | docs/agency/ | FMI, ONU, NATO |
| Media | docs/media/ | Washington Post, Economist |

## Reference: Role Mapping

| Role | Uso |
|------|-----|
| leader | Capo governo/stato |
| minister | Ministro |
| executive | CEO, Director |
| chairman | Chairman, Co-chairman |
| founder | Fondatore |
| board | Membro board |
| partner | Partner |
| advisor | Consigliere |
| member | Membro generico |
| steering | Comitato direttivo (forum) |
| ygl | WEF Young Global Leader |
| glt | WEF Global Leader for Tomorrow |
