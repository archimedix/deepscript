# DeepScript - Istruzioni per Claude Code

## Obiettivo

Manuale di storia 1945-oggi attraverso i **soggetti del potere reale**: famiglie, dinastie, reti finanziarie, forum transnazionali, individui-chiave.

**Tesi**: Il potere post-1945 e' transnazionale, finanziario, reticolare, dinastico, tecnocratico.

---

## Architettura

**Neo4j e' la fonte di verita'**. I file YAML in `db/` sono backup.

```
┌─────────────────┐
│     Neo4j       │  ← Source of truth
│  (graph DB)     │
└────────┬────────┘
         │
    ┌────┴────────────────┐
    │                     │
MCP Protocol         Neo4j Driver
    │                     │
┌───┴───┐           ┌─────┴─────┐
│Claude │           │  Web App  │  ← app/ (Nuxt)
│ Code  │           │ Explorer  │
└───┬───┘           └─────┬─────┘
    │                     │
┌───┴───┐           ┌─────┴─────┐
│docs/  │           │  Browser  │
│ .md   │           │   UI      │
└───────┘           └───────────┘
```

---

## Struttura Cartelle

```
deepscript/
├── CLAUDE.md              # Questo file
├── app/                   # Web App Explorer (Nuxt 4)
│   ├── CLAUDE.md          # Docs specifiche app
│   ├── app/               # Vue components
│   └── server/            # API endpoints
├── db/                    # Database files
│   ├── schema.yaml        # SOURCE OF TRUTH per lo schema
│   ├── persons.yaml       # Backup (NON editare)
│   ├── organizations.yaml
│   ├── families.yaml
│   └── events.yaml
├── docs/                  # Schede .md (vedi schema.yaml per mapping)
├── templates/             # Template schede
├── migration/             # Script migrazione
│   ├── lib/               # Libreria condivisa
│   │   └── schema.py      # Loader per schema.yaml
│   ├── import_yaml.py
│   └── export_neo4j.py
└── archive/               # YAML legacy (read-only)
```

### Path Schede (deterministico)

Il path della scheda e' calcolato da label + id:
```
docs/{cartella}/{id}.md
```

Il mapping label -> cartella e' definito in `db/schema.yaml` (sezione `docs_path_mapping`).

---

produci risultati KISS e YAGNI

## Workflow Operativo

### Aggiungere una nuova entita': `/add`

Usa il comando `/add <tipo> <nome>`:
```
/add person mario-rossi
/add org bilderberg
/add family rockefeller
/add event 2008-crisi
```

Il comando:
1. Cerca info (WebSearch)
2. Crea/aggiorna nodo in Neo4j
3. Crea relazioni AFFILIATED_WITH
4. Crea scheda .md in `docs/{cartella}/{id}.md`
5. Crea stub per entita' referenziate

### Esportare backup: `/export`

Esegui `/export` per salvare i dati Neo4j su `db/*.yaml`.

Fai export periodicamente per:
- Backup
- Git versioning
- Lavoro offline

### Importare da YAML: `/import`

Esegui `/import` per caricare dati da `db/*.yaml` in Neo4j.

```bash
/import              # Merge con dati esistenti
/import --dry-run    # Preview senza modifiche
/import --clear      # Reset completo (cancella tutto)
```

Usa per:
- Restore da backup
- Bulk import dopo modifiche YAML
- Sync da altro ambiente

### Query dirette Neo4j

Puoi interrogare Neo4j direttamente:

```cypher
-- Chi e' affiliato a Bilderberg E Goldman Sachs?
MATCH (p:Person)-[:AFFILIATED_WITH]->(:Organization {id: 'bilderberg'})
MATCH (p)-[:AFFILIATED_WITH]->(:Organization {id: 'goldman-sachs'})
RETURN p.id, p.nationality

-- Top 20 connettori
MATCH (p:Person)-[r:AFFILIATED_WITH]->()
RETURN p.id, count(r) as conn
ORDER BY conn DESC LIMIT 20

-- Path piu' breve tra due persone
MATCH path = shortestPath(
  (:Person {id: 'mario-draghi'})-[*..4]-(:Person {id: 'larry-fink'})
)
RETURN path
```

---

## Schema Neo4j

> **Source of Truth**: `db/schema.yaml`
>
> Lo schema completo (node types, sublabels, relationships, ruoli, enum) e' definito in `db/schema.yaml`.
> Tutti gli script e skills leggono da questo file.

### Quick Reference

**Node Types**: Person, Organization, Family, Event

**Organization Sublabels**: Forum, Company, Bank, CentralBank, AssetManager, PrivateEquity, HedgeFund, SWF, Government, Foundation, ThinkTank, University, Agency, Media, Defense, Pharma, SportsClub, Automaker

**Relationships**:
- `AFFILIATED_WITH`: Person -> Organization (role, from, to, note)
- `STAKE_IN`: Organization -> Organization (role, share, from, to, note)
- `MEMBER_OF`: Person -> Family (generation, role)
- `RELATED_TO`: Person -> Person (type, note)
- `PARTICIPATED_IN`: Person -> Event (role)
- `INVOLVED_IN`: Organization -> Event (role)

**Ruoli comuni**: leader, minister, executive, chairman, founder, board, partner, advisor, member, steering, ygl, glt

Per dettagli completi (enum, mapping, validazione) vedi `db/schema.yaml`.

---

## Metodologia Ricerca

### Pattern da cercare:
- Membership multipla (2+ forum/istituzioni)
- Passaggi pubblico-privato (revolving door)
- Relazioni mentor-protetto
- Ruoli in momenti di crisi
- Sovrapposizioni nei board

### Fonti:
- Ufficiali (siti, SEC, liste membri)
- Wikipedia (punto di partenza, mai unica)
- Giornalismo investigativo
- Fonti critiche (verificando affidabilita')

### Focus Italia:
Cerca sempre connessioni italiane, presenza in Aspen Italia, ISPI, governi tecnici.

---

## Tono e Stile

**Fare**: Dati verificabili, fonti citate, connessioni documentate, tabelle chiare

**Evitare**: Sensazionalismo, speculazioni, complottismo semplificatorio

> "Segui il potere, documenta le connessioni, lascia che i fatti parlino"

---

## Framework Report

### Tipi di Documento

| Tipo | Definizione | Span Temporale | Path |
|------|-------------|----------------|------|
| **Event** | Fatto puntuale con data, luogo, decisori | Giorni/mesi | `docs/events/` |
| **Report** | Percorso/analisi attraverso tempo e spazio | Generazioni/ere | `reports/` |
| **Scheda** | Entita' di riferimento (persona, org, famiglia) | N/A | `docs/{tipo}/` |

### Sottotipi Report

| Sottotipo | Focus | Esempio |
|-----------|-------|---------|
| **STORICO** | Era/periodo | `cold-war-intelligence-origins.md` |
| **TEMATICO** | Pattern/fenomeno | `whistleblowers-power-exposed.md` |
| **GEOGRAFICO** | Mappa regionale | `korea-power-map.md` |

### Relazione Event-Report-Scheda

```
Events (fatti) ──────► Neo4j ◄────── Schede (entita')
       │                                    │
       │                                    │
       └──────► Reports (percorsi) ◄────────┘
                       │
                       ▼
              Chronology Index (output finale)
```

**Regole:**
- Events = fatti puntuali, link a schede
- Reports = narrative, RIFERISCONO eventi (non duplicano)
- Schede = dati puri, no narrative
- Neo4j = fonte di verita' per relazioni

### Naming Convention

| Tipo | Pattern | Esempio |
|------|---------|---------|
| Event | `{anno}-{slug}.md` | `1948-elezioni-italiane.md` |
| Report storico | `{tema}-{periodo}.md` | `cold-war-intelligence-origins.md` |
| Report tematico | `{tema}.md` | `whistleblowers-power-exposed.md` |
| Report geografico | `{regione}-power-map.md` | `korea-power-map.md` |

### Indici

I report hanno due indici in `reports/`:
- `00-chronology-index.md` - Timeline 1942-oggi con link a eventi e report
- `00-thematic-index.md` - Raggruppamento per tema

---

## Web App Explorer

Interfaccia grafica per esplorare il grafo. Vedi `app/CLAUDE.md` per dettagli.

```bash
cd app
npm install
npm run dev    # http://localhost:3000
```

Funzionalita':
- Ricerca full-text entita'
- Visualizzazione grafo interattivo (Cytoscape)
- Preview schede markdown
- Filtri per tipo nodo/relazione

---

## File Legacy (Read-Only)

I file YAML in `archive/` (`persone.yaml`, `istituzioni.yaml`, etc.) sono **archivio storico**.
NON modificarli. Usa Neo4j per i dati correnti.

---

*Ultimo aggiornamento: 12 Gennaio 2026*
