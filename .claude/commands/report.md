---
description: Genera o aggiorna un power map report
argument-hint: <topic>
---

Genera o aggiorna un report power map per: **$ARGUMENTS**

## Step 1: Identifica il tipo di report

Analizza l'argomento `$ARGUMENTS` per determinare:

| Pattern | Tipo | Nome file | Esempio |
|---------|------|-----------|---------|
| Nome paese | GEOGRAFICO | `{paese}-power-map.md` | Iraq → `iraq-power-map.md` |
| Tema specifico | TEMATICO | `{tema}.md` | basi-usa-world → `basi-usa-world.md` |
| Settore | TEMATICO | `{settore}-power.md` | pharma → `pharma-power.md` |

## Step 2: Verifica se il report esiste

```bash
ls reports/ | grep -i "$ARGUMENTS"
```

**Se NON esiste** → vai a [Workflow CREAZIONE](#workflow-creazione-nuovo-report)
**Se ESISTE** → vai a [Workflow AGGIORNAMENTO](#workflow-aggiornamento-report-esistente)

---

# Workflow CREAZIONE (nuovo report)

## C1: Analizza dati Neo4j esistenti

### Per report GEOGRAFICO (paese):

```cypher
// Persone del paese con affiliazioni
MATCH (p:Person)-[r:AFFILIATED_WITH]->(o:Organization)
WHERE p.nationality CONTAINS '{ISO_CODE}'
RETURN p.id, p.name, p.born, collect({org: o.id, role: r.role}) as affiliations
ORDER BY size(affiliations) DESC
LIMIT 50

// Organizzazioni con HQ nel paese
MATCH (o:Organization)
WHERE o.headquarters CONTAINS '{PAESE}'
OPTIONAL MATCH (p:Person)-[r:AFFILIATED_WITH]->(o)
RETURN o.id, labels(o), o.name, count(p) as members
ORDER BY members DESC

// Governi e leader
MATCH (g:Organization:Government)
WHERE g.id CONTAINS '{paese}'
OPTIONAL MATCH (p:Person)-[r:AFFILIATED_WITH]->(g)
WHERE r.role IN ['leader', 'minister']
RETURN g.id, p.id, p.name, r.role, r.from, r.to
ORDER BY r.from DESC

// Eventi nel paese
MATCH (e:Event)
WHERE e.location CONTAINS '{PAESE}'
RETURN e.id, e.year, e.type
ORDER BY e.year

// Connessioni internazionali (forum)
MATCH (p:Person)-[:AFFILIATED_WITH]->(forum:Forum)
WHERE p.nationality CONTAINS '{ISO_CODE}'
RETURN p.id, forum.id
```

### Per report TEMATICO:

```cypher
// Cerca entità correlate al tema
MATCH (n)
WHERE n.id CONTAINS '{tema}' OR n.name CONTAINS '{Tema}'
RETURN n.id, labels(n)

// Cerca per settore/sublabel se applicabile
MATCH (o:Organization:{Sublabel})
OPTIONAL MATCH (p:Person)-[r:AFFILIATED_WITH]->(o)
RETURN o.id, o.name, collect(p.id) as key_people
```

## C2: Ricerca web completa

Usa WebSearch per costruire il quadro completo:
- Storia e background del tema/paese
- Figure chiave storiche e attuali
- Eventi determinanti
- Connessioni internazionali
- Statistiche (PIL, popolazione, etc.)
- Sviluppi recenti (2024-2025)

Focus DeepScript:
- Forum transnazionali (Bilderberg, WEF, CFR, Trilateral, Aspen)
- Revolving door pubblico-privato
- Ruolo banche/asset manager (Big Three)
- Connessioni italiane

## C3: Aggiungi entità a Neo4j

Per ogni persona/org rilevante trovata:

```cypher
// Persona
MERGE (p:Person {id: 'nuovo-id'})
SET p.name = 'Nome', p.nationality = 'XXX', p.born = YYYY

// Organizzazione
MERGE (o:Organization {id: 'org-id'})
SET o:Sublabel, o.name = 'Nome', o.headquarters = 'City, Country'

// Affiliazione
MATCH (p:Person {id: 'person-id'})
MATCH (o:Organization {id: 'org-id'})
MERGE (p)-[r:AFFILIATED_WITH]->(o)
SET r.role = 'ruolo', r.from = YYYY
```

**Priorità:**
1. Leader politici attuali e storici
2. Figure nei forum transnazionali
3. Manager aziende/banche strategiche
4. Connettori (persone in 2+ org rilevanti)

## C4: Crea il report

### Struttura GEOGRAFICO:

```markdown
# {Paese} Power Map

> Sintesi del sistema di potere in una frase

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Sistema** | ... |
| **Leader** | [Nome](../docs/persons/id.md) |
| **PIL** | $XXB |
| **Popolazione** | XXM |

---

## Storia del Potere

### Periodo 1 (date)
### Periodo 2 (date)

---

## Struttura Attuale

### Governo
| Ruolo | Persona | Background |

### Economia
### Forum Internazionali

---

## Connessioni Internazionali

### Con USA
### Con UE

---

## Pattern e Osservazioni

---

## Timeline

| Anno | Evento |

---

## Fonti
```

### Struttura TEMATICO:

```markdown
# {Tema}

> Sintesi in una frase

## Executive Summary

---

## Background Storico

---

## Attori Chiave

### Persone
### Organizzazioni

---

## Dinamiche e Pattern

---

## Timeline

---

## Fonti
```

## C5: Aggiorna indici

### Per report GEOGRAFICO:

Aggiungi alla sezione regionale appropriata in `00-thematic-index.md` (sezione "Geografie"):

| Regione | Paesi |
|---------|-------|
| Americhe | US, CA, MX, BR |
| Europa | UK, FR, DE, IT, ES, NL, BE, LU, CH, AT, IE, PL, HU, RO, GR, NO, SE, FI, DK, RU, EU |
| Asia-Pacifico | CN, JP, KR, IN, SG, ID, TH |
| Medio Oriente | SA, AE, IL, IR, IQ, LB, BH, TR |
| Africa | ZA, ... |

### Per report TEMATICO/SETTORIALE:

Aggiungi alla sezione settoriale appropriata in `00-thematic-index.md`:
- Media, Pharma, Automotive, Luxury, Sport, Tech, Difesa, Finanza, Education

### Per ENTRAMBI:

Se il report ha timeline significativa (3+ eventi), aggiungi anche a `00-chronology-index.md` nel periodo appropriato

---

# Workflow AGGIORNAMENTO (report esistente)

## U1: Leggi il report esistente

Leggi `reports/{nome-report}.md` per capire:
- Cosa è già documentato
- Struttura e sezioni esistenti
- Ultima data/periodo coperto
- Gap evidenti

## U2: Cerca novità nel database

```cypher
// Nuove persone del paese/tema aggiunte di recente
MATCH (p:Person)
WHERE p.nationality CONTAINS '{ISO_CODE}'
  OR p.id CONTAINS '{tema}'
RETURN p.id, p.name

// Nuove affiliazioni rilevanti
MATCH (p:Person)-[r:AFFILIATED_WITH]->(o:Organization)
WHERE (p.nationality CONTAINS '{ISO_CODE}' OR o.headquarters CONTAINS '{PAESE}')
RETURN p.id, o.id, r.role, r.from

// Nuovi eventi
MATCH (e:Event)
WHERE e.location CONTAINS '{PAESE}' OR e.id CONTAINS '{tema}'
RETURN e.id, e.year
```

Confronta con il report: cosa c'è nel DB che manca nel report?

## U3: Ricerca web per aggiornamenti

Cerca sviluppi recenti (2024-2025):
- Cambi di leadership
- Nuove nomine in forum/aziende
- Eventi significativi
- Nuove connessioni emerse
- Aggiornamenti statistiche

**Query tipo:**
- "{paese/tema} 2025 news"
- "{persona chiave} new role 2025"
- "{paese} Bilderberg WEF Davos 2025"

## U4: Aggiungi nuove entità a Neo4j

Come in C3, aggiungi persone/org/relazioni scoperte.

## U5: Aggiorna il report

**NON riscrivere tutto.** Aggiorna chirurgicamente:

1. **Executive Summary**: Aggiorna metriche se cambiate
2. **Sezione "Struttura Attuale"**: Nuovi leader/ministri
3. **Timeline**: Aggiungi nuovi eventi
4. **Nuove sezioni**: Solo se gap significativo

**Formato aggiornamenti:**
- Integra fluidamente nel testo esistente
- Aggiungi righe a tabelle esistenti
- Estendi timeline con nuovi eventi
- Aggiungi sottosezioni se serve

## U6: Segnala modifiche

Elenca cosa è stato aggiornato:
- Sezioni modificate
- Nuove entità aggiunte al DB
- Nuovi link/riferimenti

---

# Output atteso

## Per CREAZIONE:
1. Analisi dati Neo4j esistenti
2. Sintesi ricerca web
3. Entità create in Neo4j (lista)
4. Report creato: `reports/{nome}.md`
5. Indici aggiornati

## Per AGGIORNAMENTO:
1. Stato report esistente
2. Novità trovate (DB + web)
3. Entità aggiunte in Neo4j
4. Sezioni aggiornate nel report
5. Riepilogo modifiche
