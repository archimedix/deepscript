# DeepScript - Istruzioni per Claude Code

## Obiettivo

Manuale di storia 1945-oggi attraverso i **soggetti del potere reale**: famiglie, dinastie, reti finanziarie, forum transnazionali, individui-chiave.

**Tesi**: Il potere post-1945 e' transnazionale, finanziario, reticolare, dinastico, tecnocratico.

---

## Struttura

```
deepscript/
├── CLAUDE.md           # Istruzioni agente
├── index.yaml          # DATABASE CENTRALIZZATO - fonte di verita'
├── templates/          # Template schede
├── istituzioni/        # Schede organizzazioni
├── persone/            # Schede persone
├── eventi/             # Schede eventi
├── family/             # Schede dinastie
```

---

## index.yaml - Fonte di verita'

**LEGGI SEMPRE index.yaml prima di lavorare.** Contiene:
- Tutte le persone, istituzioni, eventi, famiglie
- Affiliazioni (singola fonte di verita' per membership)
- Enum dei valori standard (ruoli, tipi)
- Relazioni speciali (mentore, revolving door, alleanze)

### Convenzioni

- **Con scheda**: ha campo `file: percorso/file.md`
- **Stub (senza scheda)**: NON ha campo `file`
- **Ruoli e tipi**: usa SOLO valori dalla sezione `enum:` di index.yaml

---

## Workflow operativo

### Quando crei un documento:

1. **Crea PRIMA l'entry in index.yaml**
2. Usa il template da `templates/`
3. Aggiungi org/persone referenziate come stub se non esistono

### Quando modifichi un documento:

1. **Aggiorna index.yaml** con nuove affiliazioni/connessioni
2. Aggiorna sezione "Connessioni" nei documenti coinvolti

### Quando aggiungi una connessione:

1. Verifica che entrambe le entita' esistano in index.yaml
2. Aggiungi stub se mancano
3. Usa ruoli standard dall'enum

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

*Ultimo aggiornamento: Dicembre 2025*
