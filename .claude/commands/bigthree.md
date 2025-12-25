---
description: Aggiungi un nuovo stato al report Big Three
argument-hint: <stato>
---

Aggiungi le partecipazioni Big Three (BlackRock, Vanguard, State Street) per: **$ARGUMENTS**

## Step 1: Verifica database Neo4j

Esegui questa query per trovare aziende esistenti dello stato e le connessioni Big Three:

```cypher
// Aziende dello stato con connessioni Big Three esistenti
MATCH (company)
WHERE (company:Company OR company:Bank OR company:Pharma OR company:Automaker)
  AND company.headquarters CONTAINS '$ARGUMENTS'
OPTIONAL MATCH (am:AssetManager)-[s:STAKE_IN]->(company)
WHERE am.id IN ['blackrock', 'vanguard', 'state-street']
RETURN company.id, company.name, company.headquarters,
       collect({asset_manager: am.id, share: s.share}) as big_three_stakes
ORDER BY company.name
```

Elenca:
- Aziende già presenti nel DB
- Connessioni STAKE_IN già esistenti con share %
- Connessioni mancanti da aggiungere

## Step 2: Ricerca nuove informazioni

Per le aziende dell'indice principale (es. IBEX 35, AEX, SMI):

1. **Cerca market cap attuale** in EUR/USD
2. **Cerca quote Big Three aggregate** (BlackRock + Vanguard + State Street)
3. Usa tasso EUR/USD ~1.04

## Step 3: Aggiorna report

Aggiungi sezione a `reports/big-three-assets.md`:

```markdown
## [Nome Stato] ([Nome Indice])

| Azienda | Market Cap ($B) | Big Three % | Big Three ($B) |
|---------|-----------------|-------------|----------------|
| ...     | ...             | ...         | ...            |

**Totale Big Three [Stato]**: ~**$X.X miliardi**
```

- Inserisci prima di "Riepilogo Aggregato Europa"
- Ordina per market cap decrescente
- Aggiorna tabella riepilogo con nuovo paese

## Step 4: Aggiorna database Neo4j

Per ogni azienda con dati Big Three, aggiungi le relazioni mancanti:

```cypher
// Crea azienda se non esiste
MERGE (c:Organization:Company {id: 'nome-azienda'})
ON CREATE SET c.name = 'Nome Azienda', c.headquarters = 'Stato'

// Aggiungi stake BlackRock
MATCH (am:AssetManager {id: 'blackrock'})
MATCH (c:Company {id: 'nome-azienda'})
MERGE (am)-[s:STAKE_IN]->(c)
SET s.share = 'X.X%', s.year = 2025

// Aggiungi stake Vanguard
MATCH (am:AssetManager {id: 'vanguard'})
MATCH (c:Company {id: 'nome-azienda'})
MERGE (am)-[s:STAKE_IN]->(c)
SET s.share = 'X.X%', s.year = 2025

// Aggiungi stake State Street
MATCH (am:AssetManager {id: 'state-street'})
MATCH (c:Company {id: 'nome-azienda'})
MERGE (am)-[s:STAKE_IN]->(c)
SET s.share = 'X.X%', s.year = 2025
```

## Output atteso

1. Lista aziende trovate nel DB con stato connessioni
2. Sezione paese aggiunta al report
3. Tabella riepilogo aggiornata
4. Conferma relazioni STAKE_IN create/aggiornate in Neo4j
