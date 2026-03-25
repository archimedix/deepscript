# Piano: Espansione Schema per Storia Pre-Moderna

## Contesto

Il progetto gia' contiene dati che risalgono all'XI secolo (famiglia Benveniste, 1079) e al 1245 (Lamba Doria), ma lo schema assume strutture moderne. Il dato di fatto e' che **i dati hanno superato lo schema**: esistono gia' `repubblica-genova` (fondata 1005), `governo-ottomano` (1299-1922), `governo-sardegna` (1720-1861), ruoli come `military` usati 28 volte fuori dall'enum, tipi evento come `revolution` e `assassination` usati nei dati ma assenti dallo schema.

**Obiettivo**: Aggiornare lo schema per supportare correttamente entita' pre-moderne, mantenendo piena compatibilita' con i 5600+ persone, 5373+ organizzazioni e 241 famiglie esistenti.

**Principio guida**: Cambiamenti additivi, KISS, YAGNI. Non creare nuovi node type -- tutto resta Person, Organization, Family, Event.

**Arco temporale**: Tardo medioevo (~1100 AD) in avanti. Nessun supporto per date BCE.

**Riclassificazione nodi esistenti**: Incrementale, in un secondo momento.

---

## Fase 1: Schema (`db/schema.yaml`) ✅ COMPLETATA 2026-03-25

### 1A. Nuovi sublabel per stati storici

Aggiungere a `org_sublabels`:

```yaml
- Kingdom        # Regni pre-moderni (Napoli, Sardegna, Prussia)
- Empire         # Ottomano, Romano, Bizantino, Sacro Romano Impero
- CityState      # Venezia, Genova, Firenze, citta' anseatiche
- Principality   # Ducati, Granducati, Principati, Margraviati
```

**Perche'**: `Government` resta per gli stati-nazione moderni. Un regno non e' un "governo" -- ha una struttura di potere fondamentalmente diversa (sovranita' dinastica vs. esecutivo delegato). Questo risolve il problema `governo-italia`: gli stati pre-unitari diventano Kingdom/CityState/Principality.

### 1B. Nuovi sublabel per organizzazioni storiche

```yaml
- ReligiousOrder  # Templari, Gesuiti, Cavalieri Teutonici
- MilitaryOrder   # Ordine di Malta (quando distinto da religioso)
- Guild           # Gilde mercantili, Arti di Firenze
- TradingCompany  # VOC, East India Company, Compagnia Moscovita
```

### 1C. Aggiornare `docs_path_mapping`

```yaml
Kingdom: kingdom
Empire: empire
CityState: city-state
Principality: principality
ReligiousOrder: religious-order
MilitaryOrder: military-order
Guild: guild
TradingCompany: trading-company
```

### 1D. Aggiornare `type_mapping`

```yaml
# Stati storici
kingdom: Kingdom
regno: Kingdom
empire: Empire
impero: Empire
city-state: CityState
citta-stato: CityState
repubblica: CityState        # repubbliche pre-moderne (Venezia, Genova)
principality: Principality
principato: Principality
duchy: Principality
ducato: Principality
grand-duchy: Principality
margraviato: Principality

# Organizzazioni storiche
religious-order: ReligiousOrder
ordine-religioso: ReligiousOrder
military-order: MilitaryOrder
ordine-militare: MilitaryOrder
guild: Guild
gilda: Guild
arte: Guild
corporazione: Guild
trading-company: TradingCompany
compagnia-commerciale: TradingCompany
```

### 1E. Nuovi ruoli affiliazione (storici)

Aggiungere a `affiliation_roles`:

```yaml
# Historical / Pre-modern (6 roles)
- sovereign     # note: "King", "Sultan", "Emperor", "Doge", "Caliph"
- noble         # note: "Duke", "Count", "Baron", "Prince", "Marquis"
- clergy        # note: "Cardinal", "Bishop", "Abbot", "Pope", "Grand Master"
- military      # note: "Admiral", "General", "Commander", "Condottiero"
- merchant      # note: "Guild Master", "Factor", "Court Banker"
- vassal        # note: "Feudal lord", "Tributary"
```

**Nota**: `military` e' gia' usato 28 volte nei dati -- qui lo formalizziamo.

### 1F. Nuovi tipi relazione persona

Aggiungere a `person_relation_types`:

```yaml
- successor     # note: "political", "dynastic", "corporate" (gia' 50 occorrenze nei dati)
- ancestor      # note: "grandfather", "great-grandfather" (gia' 3 occorrenze)
```

### 1G. Nuovi tipi evento

Aggiungere a `event_types`:

```yaml
- revolution    # note: "uprising", "insurrection"
- assassination # note: "regicide", "execution"
- founding      # note: "charter", "establishment"
- conquest      # note: "siege", "invasion", "crusade"
- succession    # note: "coronation", "abdication", "interregnum"
- persecution   # note: "expulsion", "pogrom", "inquisition"
```

### 1H. Status organizzazione

Aggiungere a `org_status`:

```yaml
- conquered     # assorbito per conquista
- dissolved     # dissolto (es. Sacro Romano Impero)
```

### 1I. Convenzioni date

Aggiungere blocco commento:

```yaml
# Date conventions:
# - Integer years (e.g., 1453)
# - Imprecise dates: use note field (e.g., note: "circa 1450")
# - Earliest reliable data: ~1100 AD (tardo medioevo)
```

### 1J. Version bump

```yaml
meta:
  version: 4
  updated: 2026-03-25
```

---

## Fase 2: Aggiornamento comandi `/add` e `/report` ✅ COMPLETATA 2026-03-25

Aggiornare i comandi per supportare i nuovi sublabel storici, prima di usarli per la revisione dati.

### 2A. `/add` — Tipi supportati (riga 19)

Attuale: `person | org | family | event | gov`

Aggiungere shortcut per stati storici, oppure documentare l'uso di `/add org` con tipo specifico:

```
/add org repubblica-venezia    → tipo: city-state → sublabel: CityState
/add org regno-napoli          → tipo: kingdom → sublabel: Kingdom
/add org impero-ottomano       → tipo: empire → sublabel: Empire
/add org ducato-savoia         → tipo: principality → sublabel: Principality
/add org templari              → tipo: religious-order → sublabel: ReligiousOrder
```

### 2B. `/add` — Blocco Government (righe 240-250)

Estendere o affiancare con blocco per stati storici:

```cypher
// Kingdom / Empire / CityState / Principality
MERGE (o:Organization {id: 'nome-id'})
SET o:Kingdom,  // o Empire, CityState, Principality
    o.name = 'Nome Stato',
    o.founded = 1130,
    o.dissolved = 1861,       // anno fine (opzionale)
    o.headquarters = 'City',
    o.status = 'dissolved',   // o conquered, active
    o.tagline = 'Breve descrizione'
```

### 2C. `/add` — Ruoli storici (righe 252-256)

Aggiungere i ruoli storici alla ricerca leader:

```cypher
WHERE r.role IN ['leader', 'minister', 'sovereign', 'noble', 'clergy', 'military']
```

### 2D. `/add` — Sezione "Evita proliferazione" (righe 280-304)

Aggiungere esempi per entita' storiche:

| NON creare | USA invece | Ruolo | Note |
|------------|------------|-------|------|
| senato-venezia | repubblica-venezia | legislator | "Senatore" |
| gran-consiglio-venezia | repubblica-venezia | legislator | "Gran Consiglio" |
| corte-napoli | regno-napoli | sovereign | "Re" |
| cancelleria-impero | sacro-romano-impero | official | "Cancelliere" |

### 2E. `/add` — Tabella template (righe 262-269)

Aggiungere righe per stati e org storiche:

| Tipo | Template | Cartella output |
|------|----------|--------------------|
| org (historical state) | `templates/org.md` | `docs/{kingdom,empire,city-state,principality}/` |
| org (historical org) | `templates/org.md` | `docs/{religious-order,military-order,guild,trading-company}/` |

### 2F. `/report` — Query stati storici (minore)

Aggiungere nelle query di esempio per report GEOGRAFICO:

```cypher
// Stati storici nel territorio
MATCH (o:Organization)
WHERE (o:Kingdom OR o:Empire OR o:CityState OR o:Principality)
AND o.headquarters CONTAINS '{PAESE}'
RETURN o.id, labels(o), o.founded, o.dissolved
ORDER BY o.founded
```

---

## Fase 3: Revisione dati e schede ✅ COMPLETATA 2026-03-25

Dopo l'aggiornamento dello schema e dei comandi, verificare allineamento tra dati esistenti (Neo4j + db/*.yaml) e struttura schede (docs/).

### 3A. Audit dati Neo4j

- Identificare nodi con tipi/ruoli fuori dall'enum (gia' noti: `military` x28, `successor` x50, `ancestor` x3)
- Verificare che i nuovi event_types coprano i tipi gia' usati nei dati (`revolution`, `assassination`, etc.)
- Elencare organizzazioni che potrebbero beneficiare dei nuovi sublabel (es. ordini religiosi attualmente etichettati come Foundation o Agency)

### 3B. Audit struttura schede

- Verificare che le schede in `docs/` usino i path corretti secondo `docs_path_mapping`
- Identificare schede orfane (file .md senza nodo corrispondente in Neo4j)
- Identificare nodi senza scheda (nodi in Neo4j senza file .md corrispondente)
- Verificare coerenza dei template usati per le schede storiche vs moderne

### 3C. Creazione directory docs

```bash
mkdir -p docs/{kingdom,empire,city-state,principality,religious-order,military-order,guild,trading-company}
```

### 3D. Allineamento YAML di backup

- Eseguire `/export` per aggiornare i file `db/*.yaml` con lo stato corrente di Neo4j
- Verificare che i nuovi type_mapping vengano applicati correttamente nell'export

---

## Fase 4 (futura): Web App

Da fare dopo che dati e schede sono allineati.

### 4A. `app/server/utils/neo4j.ts` (riga 73-96)

Aggiungere al `docsPathMapping`:

```typescript
Kingdom: 'kingdom',
Empire: 'empire',
CityState: 'city-state',
Principality: 'principality',
ReligiousOrder: 'religious-order',
MilitaryOrder: 'military-order',
Guild: 'guild',
TradingCompany: 'trading-company',
// Bug fix: sublabel gia' in schema ma mancanti qui
SecretSociety: 'secret-society',
Sect: 'sect',
ReligiousInstitution: 'religious-institution',
Airline: 'airline',
```

### 4B. `app/app/components/GraphCanvas.vue`

Aggiungere a `nodeColors` (riga 201+):

```typescript
// Historical states (toni caldi ambra/terra)
Kingdom: '#B45309',
Empire: '#92400E',
CityState: '#A16207',
Principality: '#CA8A04',
// Historical orgs
ReligiousOrder: '#7C2D12',
MilitaryOrder: '#78716C',
Guild: '#A8A29E',
TradingCompany: '#0D9488',
// Missing existing sublabels
SecretSociety: '#1E1B4B',
Sect: '#312E81',
ReligiousInstitution: '#4338CA',
Airline: '#0284C7',
```

Aggiungere all'array `sublabels` (riga 365-367):

```typescript
const sublabels = ['Bank', 'CentralBank', 'AssetManager', 'PrivateEquity', 'HedgeFund', 'SWF',
  'Government', 'Agency', 'Party', 'Foundation', 'ThinkTank', 'University',
  'Company', 'Defense', 'Pharma', 'Automaker', 'SportsClub', 'Media', 'Forum',
  'Kingdom', 'Empire', 'CityState', 'Principality',
  'ReligiousOrder', 'MilitaryOrder', 'Guild', 'TradingCompany',
  'SecretSociety', 'Sect', 'ReligiousInstitution', 'Airline']
```

### 4C. `app/app/components/SearchPanel.vue`

Aggiungere a `sublabelConfig` (riga 224+):

```typescript
// Historical states
Kingdom: { short: 'KNG', class: 'type-kingdom' },
Empire: { short: 'EMP', class: 'type-empire' },
CityState: { short: 'CS', class: 'type-citystate' },
Principality: { short: 'PRI', class: 'type-principality' },
// Historical orgs
ReligiousOrder: { short: 'RO', class: 'type-religiousorder' },
MilitaryOrder: { short: 'MO', class: 'type-militaryorder' },
Guild: { short: 'GLD', class: 'type-guild' },
TradingCompany: { short: 'TC', class: 'type-tradingcompany' },
// Missing existing
SecretSociety: { short: 'SS', class: 'type-secretsociety' },
Sect: { short: 'SCT', class: 'type-sect' },
ReligiousInstitution: { short: 'RI', class: 'type-religiousinstitution' },
Airline: { short: 'AIR', class: 'type-airline' },
```

Aggiungere classi CSS e sezione legenda "Historical" con palette ambra/terra.

---

## Cosa NON fare (YAGNI)

- **Nessun nuovo node type** -- tutto resta Person, Organization, Family, Event
- **Nessun campo `precision` per le date** -- il campo `note` basta per i casi rari
- **Nessun campo `era`** -- il framework event+report gestisce gia' il raggruppamento temporale
- **Nessun campo `branches` sulle famiglie** -- i rami sono documentati nella scheda .md
- **Nessuna modifica agli script di migrazione** -- `import_yaml.py` e `export_neo4j.py` leggono lo schema dinamicamente, i nuovi type_mapping funzionano automaticamente
- **Nessun template nuovo** -- il template org.md e' abbastanza generico per stati storici
- **Nessun supporto date BCE** -- l'arco temporale parte dal tardo medioevo (~1100 AD)
- **Nessuna riclassificazione nodi esistenti** -- governo-ottomano, governo-sardegna, repubblica-genova restano come sono per ora; riclassificazione incrementale in seguito

---

## Verifica

1. Dopo le modifiche a schema.yaml, verificare con: `python3 migration/lib/schema.py` (se ha un self-test)
2. Creare un nodo di test: `/add org repubblica-venezia` (tipo city-state)
3. Verificare che `/export` lo esporti correttamente
4. Verificare che `/import --dry-run` lo reimporti correttamente

---

## File da modificare

| Fase | File | Tipo modifica |
|------|------|---------------|
| 1 | `db/schema.yaml` | Sublabel, type_mapping, docs_path_mapping, ruoli, enum, version |
| 2 | `.claude/commands/add.md` | Tipi storici, ruoli, Cypher, anti-proliferazione |
| 2 | `.claude/commands/report.md` | Query esempio per stati storici |
| 3 | Neo4j (via query) | Audit nodi/ruoli fuori enum |
| 3 | `db/*.yaml` | Export aggiornato |
| 3 | `docs/` | Audit schede, creazione directory |
| 4 | `app/server/utils/neo4j.ts` | docsPathMapping (+ fix sublabel mancanti) |
| 4 | `app/app/components/GraphCanvas.vue` | nodeColors + sublabels array |
| 4 | `app/app/components/SearchPanel.vue` | sublabelConfig + CSS + legenda |
