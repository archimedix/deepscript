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
    MCP Protocol
         │
┌────────┴────────┐
│   Claude Code   │  ← /add, /export commands
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐  ┌───────┐
│docs/  │  │ db/   │
│ .md   │  │ YAML  │
└───────┘  └───────┘
(schede)   (backup)
```

---

## Struttura Cartelle

```
deepscript/
├── CLAUDE.md              # Questo file
├── db/                    # YAML esportati (backup, NON editare)
│   ├── persons.yaml
│   ├── organizations.yaml
│   ├── families.yaml
│   └── events.yaml
├── docs/                  # Tutte le schede .md
│   ├── persons/           # Persone
│   ├── forum/             # Forum (Bilderberg, WEF, etc.)
│   ├── bank/              # Banche
│   ├── central-bank/      # Banche centrali
│   ├── asset-manager/     # Asset manager
│   ├── private-equity/    # Private equity
│   ├── swf/               # Sovereign wealth funds
│   ├── government/        # Governi
│   ├── foundation/        # Fondazioni
│   ├── think-tank/        # Think tank
│   ├── company/           # Aziende
│   ├── pharma/            # Aziende farmaceutiche
│   ├── agency/            # Agenzie internazionali
│   ├── sports-club/       # Club sportivi
│   ├── automaker/         # Case automobilistiche
│   ├── family/            # Dinastie
│   ├── events/            # Eventi storici
│   └── media/             # Media
├── templates/             # Template schede
├── migration/             # Script migrazione/export
└── archive/               # YAML legacy (read-only)
```

### Path Schede (deterministico)

Il path della scheda e' calcolato da label + id:
```
docs/{cartella}/{id}.md
```

| Label | Cartella |
|-------|----------|
| Person | `docs/persons/` |
| Family | `docs/family/` |
| Event | `docs/events/` |
| Organization:Forum | `docs/forum/` |
| Organization:Bank | `docs/bank/` |
| Organization:CentralBank | `docs/central-bank/` |
| Organization:AssetManager | `docs/asset-manager/` |
| Organization:PrivateEquity | `docs/private-equity/` |
| Organization:SWF | `docs/swf/` |
| Organization:Government | `docs/government/` |
| Organization:Foundation | `docs/foundation/` |
| Organization:ThinkTank | `docs/think-tank/` |
| Organization:Company | `docs/company/` |
| Organization:Pharma | `docs/pharma/` |
| Organization:Agency | `docs/agency/` |
| Organization:SportsClub | `docs/sports-club/` |
| Organization:Automaker | `docs/automaker/` |
| Organization:Media | `docs/media/` |

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

### Node Types

| Label | Proprieta' |
|-------|-----------|
| Person | id, born, died, nationality, family |
| Organization | id, name, founded, headquarters, status, sector |
| Family | id, origin, founder, sector, generations, status |
| Event | id, year, month, type, location, outcome |

### Sub-labels Organization

| Sub-label | Esempi |
|-----------|--------|
| Forum | Bilderberg, WEF, Trilaterale |
| Bank | Goldman Sachs, JPMorgan |
| CentralBank | Fed, BCE, BIS |
| AssetManager | BlackRock, Vanguard |
| PrivateEquity | Warburg Pincus, Carlyle |
| SWF | GPFG, QIA, PIF |
| Government | governo-usa, governo-italia |
| Foundation | Gates Foundation, Open Society |
| ThinkTank | CFR, Rand, Aspen |
| Company | Apple, Tesla, CFG, FSG |
| Pharma | Pfizer, Moderna, Roche, GSK |
| Agency | FMI, ONU, NATO, FIFA, IOC |
| SportsClub | PSG, Manchester City, AC Milan |
| Automaker | BMW, Toyota, Stellantis, Geely |
| Media | Washington Post, Economist |

### Relationships

| Tipo | Da | A | Proprieta' |
|------|-----|-----|-----------|
| AFFILIATED_WITH | Person | Organization | role, from, to, note |
| STAKE_IN | Organization | Organization | role, share, from, to |
| MEMBER_OF | Person | Family | generation, role |
| RELATED_TO | Person | Person | type, from, to |
| PARTICIPATED_IN | Person | Event | role |

### Ruoli (role property)

| Ruolo | Uso |
|-------|-----|
| leader | Capo governo/stato |
| minister | Ministro |
| executive | CEO, Director |
| chairman | Chairman |
| founder | Fondatore |
| board | Membro board |
| partner | Partner |
| advisor | Consigliere |
| member | Membro generico |
| steering | Comitato direttivo |
| ygl | WEF Young Global Leader |
| glt | WEF Global Leader for Tomorrow |

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

## File Legacy (Read-Only)

I file YAML in `archive/` (`persone.yaml`, `istituzioni.yaml`, etc.) sono **archivio storico**.
NON modificarli. Usa Neo4j per i dati correnti.

---

*Ultimo aggiornamento: 9 Dicembre 2025*
