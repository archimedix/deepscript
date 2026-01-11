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
- tipo: person | org | family | event | gov
- nome: identificativo (es. "mario-draghi", "rockefeller", "bilderberg", "governo-italia")

Se manca tipo o nome, chiedi all'utente.

## Workflow

### 1. Verifica se esiste in Neo4j

```cypher
// Per persona
MATCH (p:Person {id: 'nome-id'}) RETURN p

// Per organizzazione
MATCH (o:Organization {id: 'nome-id'}) RETURN o, labels(o)

// Per famiglia
MATCH (f:Family {id: 'nome-id'}) RETURN f

// Per evento
MATCH (e:Event {id: 'nome-id'}) RETURN e

// Per governo (shortcut per Organization:Government)
MATCH (g:Organization:Government {id: 'nome-id'}) RETURN g
```

Controlla se esiste gia' la scheda in `docs/`.
- Se nodo esiste E scheda esiste → gia' documentata.
- Se nodo esiste MA scheda non esiste → stub, procedi a documentare.
- Se nodo non esiste → nuova entita'.

Ricorda, ora siamo nel 2025, quando fai le ricerche usa sempre l'anno corrente

### 2. Cerca crosslinks nel database esistente

**PRIMA di cercare sul web**, interroga Neo4j per trovare connessioni potenziali:

```cypher
// Per persona: chi e' gia' affiliato alla stessa org?
MATCH (p:Person)-[:AFFILIATED_WITH]->(o:Organization)
WHERE o.id IN ['org-rilevanti']
RETURN p.id, o.id

// Per organizzazione: chi e' gia' nel DB che potrebbe essere affiliato?
MATCH (p:Person)
WHERE p.nationality IN ['nazionalita-rilevanti']
RETURN p.id, p.born, p.nationality

// Cerca relazioni esistenti con entita' simili
MATCH (o:Organization)
WHERE o.sector = 'settore-simile' OR o:SublabelSimile
RETURN o.id, labels(o)
```

**Crea le relazioni trovate:**
- Person gia' nel DB → nuova org: AFFILIATED_WITH
- Org esistente → nuova org: STAKE_IN (membership, partnership)
- Person esistente → nuova person: RELATED_TO (colleague, mentor, etc.)

### 3. Cerca informazioni sul web

WebSearch per:
- Fonti ufficiali, Wikipedia, SEC
- Ruoli e affiliazioni
- Connessioni con entita' del progetto

Focus su:
- Forum (Bilderberg, Trilaterale, WEF, CFR, Aspen)
- Revolving door pubblico-privato
- Connessioni italiane

**Cerca anche figure correlate rilevanti** per il progetto:
- Predecessori/successori in ruoli chiave
- Collaboratori stretti
- Figure di collegamento con altre entita' nel DB

### 4. Aggiungi a Neo4j

**Person:**
```cypher
MERGE (p:Person {id: 'nome-id'})
SET p.name = 'Nome Completo',
    p.born = 1970,
    p.nationality = 'ITA'  // Codice ISO 3166-1 alpha-3
```

**Formato nationality:**
- Usa sempre codice ISO 3166-1 alpha-3 (es. `ITA`, `USA`, `DEU`, `GBR`)
- Doppia nazionalita': formato `ISO-ISO` (es. `DEU-USA`, `FRA-LBN`)
- Mai nomi estesi (`Italia`, `Germany`) o formati misti (`USA/Italy`)

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

**Event:**
```cypher
MERGE (e:Event {id: 'nome-id'})
SET e.year = 2008,
    e.type = 'crisis',
    e.location = 'USA'
```

**Government (shortcut `gov`):**
```cypher
MERGE (g:Organization {id: 'governo-paese'})
SET g:Government,
    g.name = 'Governo di [Paese]',
    g.founded = 1948,
    g.headquarters = 'City, Country',
    g.system = 'republic',  // monarchy, republic, etc.
    g.status = 'active'
```

Per i governi, cerca e documenta:
- **Capi di Stato/Governo**: presidenti, re, primi ministri (role: `leader`)
- **Ministri chiave**: economia, esteri, difesa (role: `minister`)
- **Timeline leader**: successione storica dei capi
- **Relazioni con org nel DB**: banche centrali, SWF, aziende di stato

### 5. Crea scheda markdown

**IMPORTANTE:** Leggi il template corrispondente e usalo come base per la scheda.

| Tipo | Template | Cartella output |
|------|----------|-----------------|
| person | `templates/person.md` | `docs/persons/` |
| family | `templates/family.md` | `docs/family/` |
| event | `templates/event.md` | `docs/events/` |
| org | `templates/org.md` | vedi tabella sub-label |
| org:Media | `templates/media.md` | `docs/media/` |
| gov | `templates/gov.md` | `docs/government/` |

**Sub-label → Cartella**: Vedi `db/schema.yaml` sezione `docs_path_mapping`

**Workflow scheda:**
1. Leggi il template: `Read templates/{tipo}.md`
2. Compila con i dati raccolti dalla ricerca
3. Scrivi in `docs/{cartella}/{id}.md`

Stile: dati verificabili, fonti citate, no speculazioni.

### 6. Evita proliferazione di Organization

**IMPORTANTE:** Prima di creare una nuova Organization, verifica se puoi usare un'org esistente con un ruolo appropriato.

**Regola generale:** Usa il campo `note` per specificare dettagli, non creare nuove org.

| NON creare | USA invece | Ruolo | Note |
|------------|------------|-------|------|
| camera-deputati-italia | governo-italia | legislator | "Deputato" |
| senato-italia | governo-italia | legislator | "Senatore" |
| congresso-usa | governo-usa | legislator | "Representative", "Senator" |
| casa-bianca | governo-usa | leader/advisor | "NSA", "Chief of Staff" |
| tesoro-usa | governo-usa | minister | "Secretary of Treasury" |
| pentagono | governo-usa | minister | "Secretary of Defense" |
| farnesina | governo-italia | minister | "Min. Esteri" |
| nato-pa | nato | member | "Assemblea Parlamentare" |
| fed-board | federal-reserve | board | "Governor", "Vice Chair" |

**Quando creare una nuova org:**
- Forum/network transnazionali (Bilderberg, Trilateral, WEF)
- Banche e istituzioni finanziarie specifiche
- Aziende
- Think tank e fondazioni con identita' propria
- Agenzie internazionali (NATO, ONU, FMI, UE)

**Consulta `db/schema.yaml`** per l'elenco completo dei ruoli disponibili (affiliation_roles).

### 7. Crea stub per entita' referenziate

Per ogni org/person referenziata che non esiste:
```cypher
// Stub persona
MERGE (p:Person {id: 'ref-id'})
SET p.name = 'Nome Completo',
    p.nationality = 'XXX'

// Stub org
MERGE (o:Organization {id: 'ref-id'})
SET o:Company, o.name = 'Nome Organizzazione', o.status = 'active'
```

### 8. Report

- Nodo creato/aggiornato (Person/Organization/Family/Event)
- Relazioni create (AFFILIATED_WITH, MEMBER_OF, STAKE_IN)
- Scheda .md creata (path)
- Stub creati

---

## Reference

**Schema completo**: `db/schema.yaml`
- `org_sublabels`: Sublabels Organization disponibili
- `affiliation_roles`: Ruoli Person → Organization
- `stake_roles`: Ruoli Organization → Organization
- `type_mapping`: Mapping tipo → sublabel
- `docs_path_mapping`: Mapping label → cartella docs
