# DeepScript - Istruzioni per Agenti

## Obiettivo

Database di potere 1945-oggi: persone, organizzazioni, famiglie, eventi.
**Neo4j e' la fonte di verita'**. I file YAML in `db/` sono backup.

---

## REGOLA CRITICA: Tool Calling

**DEVI usare i tool MCP per ogni operazione. MAI simulare.**

| Azione | Tool OBBLIGATORIO |
|--------|-------------------|
| Query Neo4j (lettura) | `neo4j-cypher_read-cypher` |
| Scrivi/Modifica Neo4j | `neo4j-cypher_write-cypher` |
| Cerca sul web | `WebSearch` |
| Leggi pagina web | `WebFetch` |
| Leggi file | `Read` |
| Scrivi file | `Write` |
| Modifica file | `Edit` |
| Cerca file | `Glob` |
| Cerca contenuto | `Grep` |

### Errori da Evitare

```
ERRORE: Scrivere "Ho creato il nodo mario-draghi in Neo4j" senza chiamare il tool.
CORRETTO: Chiamare neo4j-cypher_write-cypher con la query Cypher.

ERRORE: Scrivere "Ho scritto il file docs/persons/mario-draghi.md" senza chiamare Write.
CORRETTO: Chiamare Write con file_path e content.
```

**Se non chiami il tool, l'operazione NON viene eseguita.**

---

## Schema Neo4j

### Nodi

| Label | Proprieta' |
|-------|-----------|
| Person | id, name, born, died, nationality |
| Organization | id, name, founded, headquarters, status, sector |
| Family | id, origin, founder, sector, status |
| Event | id, year, type, location, outcome |

### Sub-label Organization

Forum, Bank, CentralBank, AssetManager, PrivateEquity, HedgeFund, SWF, Government, Foundation, ThinkTank, Company, Defense, University, Pharma, Agency, SportsClub, Automaker, Media, Airline

### Relazioni

| Tipo | Da → A | Proprieta' |
|------|--------|-----------|
| AFFILIATED_WITH | Person → Organization | role, from, to, note |
| STAKE_IN | Organization → Organization | share, from, to |
| MEMBER_OF | Person → Family | generation, role |
| RELATED_TO | Person → Person | type |
| PARTICIPATED_IN | Person → Event | role |

### Ruoli (role property)

leader, minister, executive, chairman, founder, board, partner, advisor, member, steering, ygl, glt, legislator

---

## Paths Schede

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
| Organization:Defense | `docs/defense/` |
| Organization:University | `docs/university/` |
| Organization:Pharma | `docs/pharma/` |
| Organization:Agency | `docs/agency/` |
| Organization:SportsClub | `docs/sports-club/` |
| Organization:Automaker | `docs/automaker/` |
| Organization:Media | `docs/media/` |

---

## Comandi

I comandi dettagliati sono in `.opencode/commands/`:

| Comando | File | Descrizione |
|---------|------|-------------|
| `/add <tipo> <id>` | `add.md` | Aggiungi persona/org/famiglia/evento |
| `/export` | `export.md` | Esporta Neo4j → db/*.yaml |
| `/import` | `import.md` | Importa db/*.yaml → Neo4j |

**Tipi per /add**: person, org, family, event, gov

- `person` - Persona fisica
- `org` - Organizzazione generica (verrà chiesto il tipo specifico: Bank, Company, Forum, ecc.)
- `gov` - Organizzazione governativa (shortcut per org di tipo Government)
- `family` - Famiglia/dinastia
- `event` - Evento storico

---

## Stile Output

- Dati verificabili, fonti citate
- Nazionalita' in ISO 3166-1 alpha-3: ITA, USA, DEU, GBR, FRA
- Doppia nazionalita': DEU-USA, FRA-LBN
- Leggi template prima di creare schede: `templates/{tipo}.md`
- Mai speculazioni o sensazionalismo

---

## Query Cypher Utili

```cypher
-- Verifica se persona esiste
MATCH (p:Person {id: 'ID'}) RETURN p

-- Verifica se organizzazione esiste
MATCH (o:Organization {id: 'ID'}) RETURN o, labels(o)

-- Crea persona
MERGE (p:Person {id: 'ID'})
SET p.name = 'Nome', p.born = 1970, p.nationality = 'ITA'

-- Crea affiliazione
MATCH (p:Person {id: 'person-id'})
MATCH (o:Organization {id: 'org-id'})
MERGE (p)-[r:AFFILIATED_WITH]->(o)
SET r.role = 'executive', r.from = 2020
```

---

*Siamo nel 2026. Usa sempre l'anno corrente nelle ricerche web.*
