# DeepScript - Istruzioni per Claude Code

## Obiettivo

Manuale di storia 1945-oggi attraverso i **soggetti del potere reale**: famiglie, dinastie, reti finanziarie, forum transnazionali, individui-chiave.

**Tesi**: Il potere post-1945 e' transnazionale, finanziario, reticolare, dinastico, tecnocratico.

---

## Struttura

```
deepscript/
├── CLAUDE.md           # Istruzioni agente
├── index.yaml          # Config, enum, todo, relazioni
├── persone.yaml        # Database persone
├── istituzioni.yaml    # Database istituzioni
├── eventi.yaml         # Database eventi
├── media.yaml          # Database media
├── famiglie.yaml       # Database famiglie
├── templates/          # Template schede
├── istituzioni/        # Schede organizzazioni (.md)
├── persone/            # Schede persone (.md)
├── eventi/             # Schede eventi (.md)
├── family/             # Schede dinastie (.md)
├── media/              # Schede media (.md)
```

---
produci risultati KISS e YAGNI

## Database YAML - Fonte di verita'

Il database e' diviso in file separati per gestibilita':

| File | Contenuto |
|------|-----------|
| `index.yaml` | Config, enum, todo, relazioni |
| `persone.yaml` | Tutti gli individui con affiliazioni |
| `istituzioni.yaml` | Tutte le organizzazioni con stakeholders |
| `eventi.yaml` | Eventi storici |
| `media.yaml` | Testate e gruppi editoriali |
| `famiglie.yaml` | Dinastie |

**Prima di lavorare**, leggi il file YAML pertinente:
- Aggiungi persona? -> `persone.yaml`
- Aggiungi istituzione? -> `istituzioni.yaml`
- Cerca enum/ruoli validi? -> `index.yaml`

### Convenzioni base

- **Con scheda**: ha campo `file: percorso/file.md`
- **Stub (senza scheda)**: NON ha campo `file`
- **Ruoli e tipi**: usa SOLO valori dalla sezione `enum:` di index.yaml

### Campo `stakeholders` (nelle istituzioni)

Il campo `stakeholders` e' unificato per persone E organizzazioni:

```yaml
# Persone (leadership, membri)
- {persona: larry-fink, ruolo: ceo-fondatore, dal: 1988}
- {persona: mario-draghi, ruolo: partecipante}

# Organizzazioni (holdings, partnership)
- {org: apple, ruolo: holding, percentuale: "6.5%"}
- {org: microsoft, ruolo: partner}
```

**Ruoli per organizzazioni** (enum `ruoli_stakeholder`):
- `holding`: X possiede quote di Y
- `controllata`: X controlla Y (>50%)
- `partner`: alleanza strategica
- `cliente`: relazione commerciale

### Campo `affiliazioni` (nelle persone)

Lista delle organizzazioni a cui la persona appartiene:

```yaml
affiliazioni:
  - {org: blackrock, ruolo: ceo-fondatore, dal: 1988}
  - {org: wef, ruolo: co-chairman}
  - {org: trilaterale, ruolo: membro}
```

---

## Workflow operativo

### Quando crei una nuova scheda:

1. **Leggi il file YAML pertinente** per verificare contesto
2. **Crea entry nel file YAML corretto** con campo `file:`
   - Persona -> `persone.yaml`
   - Istituzione -> `istituzioni.yaml`
   - Evento -> `eventi.yaml`
   - Media -> `media.yaml`
   - Famiglia -> `famiglie.yaml`
3. **Aggiungi stakeholders/affiliazioni** nell'entry
4. **Crea stub** per entita' referenziate che non esistono
5. **Crea il file .md** usando template da `templates/`
6. **Aggiorna crosslink** nelle schede correlate

### Quando modifichi un documento:

1. **Aggiorna il file YAML** con nuove affiliazioni/connessioni
2. **Aggiorna stakeholders** in `istituzioni.yaml`
3. **Aggiorna sezione "Connessioni"** nei documenti .md coinvolti

### Quando aggiungi una connessione:

1. Verifica che entrambe le entita' esistano nei file YAML
2. Aggiungi stub se mancano
3. Usa ruoli standard dall'enum (`index.yaml`)
4. Se e' una partecipazione azionaria, usa formato:
   `{org: nome, ruolo: holding, percentuale: "X%"}`

### Checklist crosslink (IMPORTANTE)

Quando aggiungi un'entita', verifica e aggiorna:

- [ ] Entry nel file YAML corretto con tutti i campi
- [ ] Affiliazioni della persona in `persone.yaml`
- [ ] Stakeholders dell'istituzione in `istituzioni.yaml`
- [ ] Sezione "Documenti Correlati" nei file .md collegati
- [ ] Membri delle famiglie in `famiglie.yaml`

### Esempio: Aggiungere una nuova persona

```yaml
# 1. In persone.yaml:
mario-rossi:
  file: persone/mario-rossi.md
  nato: 1960
  naz: ITA
  affiliazioni:
    - {org: goldman-sachs, ruolo: partner, dal: 1990, al: 2000}
    - {org: governo-italia, ruolo: ministro, dal: 2001, al: 2005}
    - {org: bilderberg, ruolo: partecipante}

# 2. In istituzioni.yaml, aggiorna stakeholders:
goldman-sachs:
  stakeholders:
    - {persona: mario-rossi, ruolo: partner, dal: 1990, al: 2000}  # AGGIUNGI

# 3. Crea persone/mario-rossi.md dal template
# 4. Aggiorna "Documenti Correlati" in goldman-sachs.md
```

---

## Metodologia ricerca

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

## Tono e stile

**Fare**: Dati verificabili, fonti citate, connessioni documentate, tabelle chiare

**Evitare**: Sensazionalismo, speculazioni, complottismo semplificatorio

> "Segui il potere, documenta le connessioni, lascia che i fatti parlino"

---

## Riferimento rapido enum

Consulta sempre `index.yaml` sezione `enum:` per i valori validi:

| Categoria | Esempi |
|-----------|--------|
| `ruoli_governo` | capo-governo, ministro, governatore |
| `ruoli_corporate` | ceo, chairman, board, partner |
| `ruoli_forum` | steering, membro, partecipante |
| `ruoli_stakeholder` | holding, controllata, partner |
| `tipi_istituzione` | forum, bank, asset-manager, fondazione |
| `settori_aziende` | tech, energy, finance, healthcare |

---

*Ultimo aggiornamento: 2 Dicembre 2025*
