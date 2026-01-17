# PRD: DeepScript Explorer

## Problema

Il database Neo4j DeepScript contiene 4.000+ nodi e 7.000+ relazioni su reti di potere, ma manca un'interfaccia per esplorarlo visivamente e navigare le connessioni.

## Soluzione

Webapp single-page per cercare, visualizzare il grafo e leggere le schede markdown delle entità.

---

## User Stories

### US1: Ricerca
> Come utente, voglio cercare entità per nome per trovare rapidamente chi mi interessa.

**Acceptance Criteria:**
- Campo di ricerca sempre visibile
- Risultati mostrati mentre digito (debounce 300ms)
- Risultati raggruppati per tipo (Person, Organization, Family, Event)
- Click su risultato → carica nodo nel grafo

### US2: Visualizzazione Grafo
> Come utente, voglio vedere le connessioni di un'entità come grafo interattivo.

**Acceptance Criteria:**
- Nodo centrale + nodi connessi (1° livello)
- Colori diversi per tipo nodo
- Label visibili sui nodi
- Relazioni con etichetta (ruolo, periodo)
- Zoom e pan con mouse/touch

### US3: Espansione Grafo
> Come utente, voglio espandere un nodo per vedere le sue connessioni.

**Acceptance Criteria:**
- Click su nodo → espande connessioni (se non già caricate)
- Limite: max 100 nodi visibili (warning se superato)
- Doppio-click → centra e isola quel nodo
- Possibilità di rimuovere nodi dal grafo

### US4: Visualizzazione Scheda
> Come utente, voglio leggere la scheda dettagliata di un'entità.

**Acceptance Criteria:**
- Panel laterale con scheda markdown renderizzata
- Si apre al click su nodo (se scheda esiste)
- Indicatore se scheda non disponibile
- Scroll indipendente dal grafo

### US5: Navigazione Link
> Come utente, voglio cliccare i link nella scheda per navigare ad altre entità.

**Acceptance Criteria:**
- Link interni (`[[entity-id]]` o `[text](../type/entity.md)`) cliccabili
- Click → carica entità nel grafo + apre sua scheda
- Link esterni → nuova tab
- Breadcrumb/history per tornare indietro

---

## Architettura

```
┌─────────────────────────────────────────────────────┐
│                    Browser                          │
│  ┌─────────┐  ┌──────────────────┐  ┌───────────┐  │
│  │ Search  │  │   Graph Canvas   │  │  Scheda   │  │
│  │  Bar    │  │   (Cytoscape)    │  │  Panel    │  │
│  │         │  │                  │  │           │  │
│  │ Results │  │    ○───○         │  │  ## Title │  │
│  │  List   │  │    │   │         │  │  ...      │  │
│  │         │  │    ○───○───○     │  │  [link]   │  │
│  └─────────┘  └──────────────────┘  └───────────┘  │
└─────────────────────────────────────────────────────┘
        │                │                  │
        └────────────────┼──────────────────┘
                         │
                    Nuxt Server
                         │
              ┌──────────┴──────────┐
              │                     │
           Neo4j                 docs/*.md
```

## Layout

```
┌──────────────────────────────────────────────────────────┐
│  [🔍 Search...]                              DeepScript  │
├────────────┬─────────────────────────┬───────────────────┤
│            │                         │                   │
│  Results   │                         │     Scheda        │
│  ────────  │        GRAPH            │     ──────        │
│  ○ Draghi  │                         │     # Mario       │
│  ○ BCE     │         ○───○           │     Draghi        │
│  ○ Goldman │         │   │           │                   │
│            │         ○───○───○       │     **Nato**: ... │
│            │                         │     [[bce]]       │
│            │                         │                   │
├────────────┴─────────────────────────┴───────────────────┤
│  Nodes: 12  │  Edges: 18  │  Selected: mario-draghi      │
└──────────────────────────────────────────────────────────┘
```

- **Search panel** (sinistra, collassabile): 250px
- **Graph canvas** (centro): flex, min 60%
- **Scheda panel** (destra, collassabile): 350px
- **Status bar** (bottom): contatori e selezione

---

## API Endpoints

| Endpoint | Metodo | Descrizione |
|----------|--------|-------------|
| `/api/search` | GET | `?q=draghi` → risultati raggruppati |
| `/api/node/:id` | GET | Nodo + relazioni dirette |
| `/api/expand/:id` | GET | Solo relazioni (per espansione) |
| `/api/scheda/:type/:id` | GET | Contenuto markdown |

### Response Examples

**GET /api/search?q=drag**
```json
{
  "results": [
    {
      "id": "mario-draghi",
      "labels": ["Person"],
      "name": "Mario Draghi",
      "nationality": "IT"
    },
    {
      "id": "bce",
      "labels": ["Organization", "CentralBank"],
      "name": "BCE",
      "headquarters": "Frankfurt"
    }
  ],
  "total": 2
}
```

**GET /api/node/mario-draghi**
```json
{
  "node": {
    "id": "mario-draghi",
    "labels": ["Person"],
    "name": "Mario Draghi",
    "nationality": "IT",
    "born": 1947,
    "schedasPath": "persons/mario-draghi"
  },
  "edges": [
    {
      "id": "e1",
      "source": "mario-draghi",
      "target": "bce",
      "type": "AFFILIATED_WITH",
      "role": "leader",
      "from": 2011,
      "to": 2019,
      "note": "President"
    },
    {
      "id": "e2",
      "source": "mario-draghi",
      "target": "goldman-sachs",
      "type": "AFFILIATED_WITH",
      "role": "executive",
      "from": 2002,
      "to": 2005,
      "note": "Vice Chairman"
    }
  ],
  "connectedNodes": [
    {
      "id": "bce",
      "labels": ["Organization", "CentralBank"],
      "name": "BCE",
      "schedasPath": "central-bank/bce"
    },
    {
      "id": "goldman-sachs",
      "labels": ["Organization", "Bank"],
      "name": "Goldman Sachs",
      "schedasPath": "bank/goldman-sachs"
    }
  ]
}
```

**GET /api/scheda/persons/mario-draghi**
```json
{
  "exists": true,
  "content": "# Mario Draghi\n\n**Nato**: 1947, Roma\n\n## Affiliazioni\n- [[bce]] (2011-2019)\n- [[goldman-sachs]] (2002-2005)\n...",
  "internalLinks": [
    {"id": "bce", "type": "CentralBank"},
    {"id": "goldman-sachs", "type": "Bank"},
    {"id": "bilderberg", "type": "Forum"}
  ]
}
```

> **Note**: `schedasPath` è calcolato usando `docs_path_mapping` da schema.yaml.
> Se il file `docs/{schedasPath}.md` non esiste, `schedasPath` è `null`.

---

## Componenti UI

| Componente | Responsabilità |
|------------|----------------|
| `SearchBar.vue` | Input + debounce + chiamata API |
| `SearchResults.vue` | Lista risultati raggruppata |
| `GraphCanvas.vue` | Wrapper Cytoscape, gestione eventi |
| `SchedaPanel.vue` | Render markdown + intercetta link |
| `NodeTooltip.vue` | Hover info su nodi |
| `StatusBar.vue` | Contatori e stato |

---

## Interazioni

### Flow: Ricerca → Grafo → Scheda

```
User digita "draghi"
       │
       ▼
SearchBar emette @search
       │
       ▼
API /api/search?q=draghi
       │
       ▼
SearchResults mostra lista
       │
User clicca "Mario Draghi"
       │
       ▼
API /api/node/mario-draghi
       │
       ▼
GraphCanvas renderizza nodo + connessioni
       │
       ▼
API /api/scheda/persons/mario-draghi
       │
       ▼
SchedaPanel mostra markdown
       │
User clicca link [[bce]]
       │
       ▼
GraphCanvas centra su BCE (o lo aggiunge)
       │
       ▼
API /api/scheda/organizations/bce
       │
       ▼
SchedaPanel aggiorna contenuto
```

---

## Schema Database

> **Reference**: `db/schema.yaml` (source of truth)

### Node Types

| Label | Sublabels | Colore | Shape |
|-------|-----------|--------|-------|
| **Person** | - | `#3B82F6` blue | ellipse |
| **Organization** | Forum, Company, Bank, CentralBank, AssetManager, PrivateEquity, HedgeFund, SWF, Government, Party, Foundation, ThinkTank, University, Agency, Media, Defense, Pharma, SportsClub, Automaker | `#10B981` green | round-rectangle |
| **Family** | - | `#8B5CF6` purple | diamond |
| **Event** | - | `#F59E0B` amber | octagon |

### Relationships

| Tipo | From → To | Properties | Stile Grafo |
|------|-----------|------------|-------------|
| `AFFILIATED_WITH` | Person → Organization | role, from, to, note | solid, gray |
| `STAKE_IN` | Organization → Organization | role, share, from, to, note | dashed, green |
| `MEMBER_OF` | Person → Family | generation, role, note | solid, purple |
| `RELATED_TO` | Person → Person | type, note | dotted, blue |
| `PARTICIPATED_IN` | Person → Event | role, note | solid, amber |
| `INVOLVED_IN` | Organization → Event | role, note | dashed, amber |

### Docs Path Mapping

Il path della scheda è determinato da label/sublabel:
```
docs/{folder}/{id}.md
```

Mapping (da `db/schema.yaml`):
- Person → `persons/`
- Family → `family/`
- Event → `events/`
- Forum → `forum/`
- Bank → `bank/`
- CentralBank → `central-bank/`
- Company → `company/`
- ... (vedi schema.yaml per lista completa)

---

## Stack

| Layer | Tecnologia |
|-------|------------|
| Framework | Nuxt 3 |
| UI | Tailwind CSS |
| Graph | Cytoscape.js |
| Markdown | marked |
| State | Pinia (opzionale, useState può bastare) |

---

## Non-Goals (v1)

- ❌ Mappa geografica
- ❌ Timeline
- ❌ Autenticazione
- ❌ Editing dati
- ❌ Export/download
- ❌ Mobile-first (desktop priority)

---

## Metriche Successo

- Ricerca restituisce risultati in < 200ms
- Grafo renderizza 100 nodi senza lag
- Navigazione scheda → scheda fluida
- Zero errori console in uso normale
