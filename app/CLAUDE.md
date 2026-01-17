# DeepScript Web App

Web app per esplorare il grafo DeepScript. Frontend per visualizzazione interattiva di persone, organizzazioni, famiglie ed eventi.

## Stack

- **Nuxt 4** + Vue 3
- **TailwindCSS** (dark theme)
- **Cytoscape.js** + cose-bilkent (visualizzazione grafo)
- **Neo4j** (backend via driver node)
- **marked** (rendering markdown)

## Struttura

```
app/
├── app/
│   ├── app.vue                    # Layout 3-panel
│   └── components/
│       ├── GraphCanvas.vue        # Grafo interattivo (Cytoscape)
│       ├── SearchPanel.vue        # Ricerca entita'
│       └── SchedaPanel.vue        # Viewer schede markdown
├── server/
│   ├── api/
│   │   ├── search.get.ts          # GET /api/search?q=...
│   │   ├── node/[id].get.ts       # GET /api/node/:id
│   │   └── scheda/[...path].get.ts # GET /api/scheda/:path
│   └── utils/
│       └── neo4j.ts               # Driver Neo4j + helpers
├── nuxt.config.ts
└── package.json
```

## Configurazione

Variabili ambiente in `.env` o runtime config:

```bash
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
```

## Comandi

```bash
npm install    # Installa dipendenze
npm run dev    # Dev server (http://localhost:3000)
npm run build  # Build produzione
```

## Architettura

### Layout (app.vue)

3 pannelli collassabili:
- **SearchPanel** (sx): ricerca full-text su Neo4j
- **GraphCanvas** (centro): visualizzazione grafo
- **SchedaPanel** (dx): preview scheda markdown

### API

| Endpoint | Descrizione |
|----------|-------------|
| `GET /api/search?q=term` | Ricerca nodi per nome/id |
| `GET /api/node/:id` | Nodo + relazioni + nodi connessi |
| `GET /api/scheda/:path` | Contenuto scheda markdown da `docs/` |

### Grafo (GraphCanvas.vue)

- **Click** su nodo: seleziona, mostra scheda
- **Double-click**: espande connessioni (merge nel grafo)
- **Filtri**: per tipo nodo (P/O/F/E) e tipo relazione
- **Layout**: COSE-Bilkent (default), concentric, circle, grid, tree

### Colori nodi

I colori seguono lo schema del progetto:

| Tipo | Colore |
|------|--------|
| Person | `#3B82F6` (blu) |
| Organization | `#10B981` (verde) |
| Family | `#8B5CF6` (viola) |
| Event | `#F59E0B` (arancio) |

Sublabel Organization (Bank, Government, Forum, etc.) hanno colori specifici.

### Schede

Le schede markdown in `docs/` sono visualizzate nel pannello destro. I link interni (`[[entity-id]]` o `[text](../type/id.md)`) sono cliccabili e caricano/espandono il nodo nel grafo.

## Convenzioni

- CSS variables in `:root` (app.vue) per theming
- Font: Instrument Serif (display), Outfit (body), JetBrains Mono (code)
- Neo4j query con regex case-insensitive per search
- Path schede calcolato da `getSchedaPath()` in neo4j.ts

## TODO

- [ ] Timeline view (vis-timeline gia' in deps)
- [ ] Export grafo (PNG/JSON)
- [ ] Filtri avanzati (date, nationality, role)
- [ ] Statistiche globali da Neo4j
