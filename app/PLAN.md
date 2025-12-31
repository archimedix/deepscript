# Piano: Webapp DeepScript

## Obiettivo
Webapp per esplorare il database Neo4j DeepScript con ricerca, filtri, visualizzazione grafo, mappe e timeline.

## Stack Tecnologico

| Componente | Tecnologia |
|------------|------------|
| Framework | **Nuxt 3** (Vue 3 full-stack) |
| Styling | Tailwind CSS |
| State | Pinia (integrato in Nuxt) |
| Database | neo4j-driver |
| Graph | Cytoscape.js + cose-bilkent |
| Mappe | Leaflet + MarkerCluster |
| Timeline | vis-timeline |
| Markdown | marked + highlight.js |

## Struttura Cartelle

```
app/
├── nuxt.config.ts
├── package.json
├── tailwind.config.js
│
├── server/                      # Backend (API routes Nuxt)
│   ├── api/
│   │   ├── nodes/
│   │   │   ├── index.get.ts     # GET /api/nodes
│   │   │   └── [id].get.ts      # GET /api/nodes/:id
│   │   ├── search.get.ts        # GET /api/search
│   │   ├── graph/
│   │   │   └── subgraph.post.ts # POST /api/graph/subgraph
│   │   ├── docs/
│   │   │   └── [...path].get.ts # GET /api/docs/:type/:id
│   │   └── stats.get.ts         # GET /api/stats
│   └── utils/
│       ├── neo4j.ts             # Neo4j connection singleton
│       └── markdown.ts          # .md file reader
│
├── composables/
│   ├── useNodes.ts              # API wrapper per nodi
│   ├── useCytoscape.ts          # Cytoscape instance
│   ├── useLeaflet.ts            # Leaflet instance
│   └── useTimeline.ts           # vis-timeline wrapper
│
├── components/
│   ├── layout/
│   │   ├── AppHeader.vue
│   │   └── AppSidebar.vue
│   ├── graph/
│   │   ├── NetworkGraph.vue
│   │   └── GraphControls.vue
│   ├── map/
│   │   └── PowerMap.vue
│   ├── timeline/
│   │   └── ChronologyTimeline.vue
│   ├── search/
│   │   ├── SearchBar.vue
│   │   └── SearchResults.vue
│   └── detail/
│       ├── EntityDetail.vue
│       └── MarkdownRenderer.vue
│
├── pages/
│   ├── index.vue                # Home
│   ├── graph.vue                # Network explorer
│   ├── map.vue                  # Geographic view
│   ├── timeline.vue             # Chronology
│   └── entity/
│       └── [...slug].vue        # Dettaglio entita
│
├── stores/
│   ├── graph.ts
│   └── search.ts
│
└── public/
```

## API Endpoints

```
GET  /api/nodes              # Lista nodi (paginata, filtri)
GET  /api/nodes/:id          # Singolo nodo + connessioni
GET  /api/search?q=          # Ricerca fulltext
POST /api/graph/subgraph     # Subgraph da nodeIds + depth
GET  /api/docs/:type/:id     # Scheda markdown
GET  /api/stats              # Conteggi per tipo/nazionalita
```

## Fasi di Implementazione

### Fase 1: Fondamenta
1. `npx nuxi init app` + configurazione Tailwind
2. Connessione Neo4j in `server/utils/neo4j.ts`
3. API: `/api/nodes`, `/api/search`, `/api/docs/[...path]`
4. UI: Layout con header + sidebar, SearchBar
5. Pagina dettaglio con rendering markdown

**Deliverable**: Ricerca funzionante + visualizzazione schede

### Fase 2: Network Graph
1. Integrazione Cytoscape.js (client-only component)
2. Componente NetworkGraph.vue
3. Click nodo -> espandi connessioni
4. Filtri per tipo nodo/relazione
5. Layout algorithms (COSE, breadthfirst)

**Deliverable**: Grafo navigabile interattivo

### Fase 3: Power Map
1. Integrazione Leaflet + MarkerCluster
2. Mapping headquarters -> coordinate
3. Click marker -> lista entita
4. Filtri per tipo

**Deliverable**: Mappa geografica

### Fase 4: Timeline
1. Integrazione vis-timeline
2. Eventi, nascite, fondazioni, periodi affiliazione
3. Zoom e filtri temporali

**Deliverable**: Timeline cronologica

## File di Riferimento

- `../CLAUDE.md` - Schema Neo4j e convenzioni
- `../docs/persons/mario-draghi.md` - Esempio scheda persona
- `../templates/` - Template schede

## Note Architetturali

- **Nuxt 3**: Full-stack in un solo progetto, API routes integrate in `/server/api/`
- **Credenziali**: Neo4j credentials in `.env`, mai esposte al client
- **Client-only**: Cytoscape, Leaflet, vis-timeline come `<ClientOnly>` components
- **Performance**: Paginazione, subgraph queries, lazy loading (max 200 nodi visibili)
- **KISS**: No auth, no deployment complesso, sviluppo locale con `npm run dev`

## Dati Database

- **4.087 nodi**: 2.053 persone, 1.738 organizzazioni, 96 famiglie, 19 eventi
- **6.951 relazioni**: AFFILIATED_WITH, STAKE_IN, MEMBER_OF, RELATED_TO
- **994 schede markdown** in docs/
