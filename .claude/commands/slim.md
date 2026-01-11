---
description: Compatta un report lungo riducendo i token senza perdere info importanti
argument-hint: <report-name>
---

Se `$ARGUMENTS` e' vuoto, rispondi solo: "Uso: /slim <nome-report>" e fermati.

---

Compatta il report: **$ARGUMENTS**

## Obiettivo

Ridurre le dimensioni del report mantenendo le informazioni essenziali per DeepScript.

## Step 1: Identifica il report

```bash
ls reports/ | grep -i "$ARGUMENTS"
```

Leggi il report completo per analizzarlo.

## Step 2: Analisi contenuto

Identifica e classifica le sezioni:

### DA MANTENERE (priorita' alta)
| Tipo | Cosa cercare | Azione |
|------|--------------|--------|
| **Executive Summary** | Tabella metriche, sintesi | Mantieni intatto |
| **Pattern/Lezioni** | Sezioni "Pattern", "Lezioni", "Osservazioni" | Mantieni, sono il cuore analitico |
| **Link a schede** | `../docs/.../*.md` | Mantieni SOLO se il file esiste |
| **Fonti** | Sezione "Fonti" con URL | Mantieni |
| **TODO** | Cose da implementare, gap, domande aperte | Mantieni ed evidenzia |
| **Timeline essenziale** | Eventi chiave con date | Mantieni in forma compatta |

### DA COMPATTARE (ridurre)
| Tipo | Cosa cercare | Azione |
|------|--------------|--------|
| **Diagrammi ASCII** | Blocchi ``` con box/frecce | Rimuovi o riduci a 3-4 righe max |
| **Tabelle espanse** | Tabelle con 10+ righe di dettagli minori | Riduci a top 5-10 entry |
| **Citazioni** | Blocchi > con quote lunghe | Rimuovi o riduci a 1 frase |
| **Narrative descrittive** | Paragrafi lunghi che spiegano cose note | Riduci a 1-2 frasi |

### DA RIMUOVERE (eliminare)
| Tipo | Cosa cercare | Azione |
|------|--------------|--------|
| **Revisioni** | "Schede create", "Stub creati", "Aggiornamento X" | Rimuovi completamente |
| **Status/Versioni** | "Versione X.0", "Status:", changelog | Rimuovi, tieni solo data |
| **Link rotti** | Link a schede che non esistono | Rimuovi il link, tieni il nome |
| **Ripetizioni** | Info gia' presente altrove nel report | Rimuovi duplicati |
| **Sezioni vuote** | Sezioni con placeholder o "TODO" vuoti | Rimuovi |

## Step 3: Verifica link

Per ogni link `../docs/.../*.md` nel report:

```bash
# Verifica se il file esiste
ls docs/persons/nome.md 2>/dev/null || echo "BROKEN: nome.md"
```

- Se esiste: mantieni link
- Se non esiste: rimuovi parentesi quadre, tieni solo il nome

**Esempio:**
```markdown
# Prima (link rotto)
[Mario Rossi](../docs/persons/mario-rossi.md) fu ministro

# Dopo (nome senza link)
Mario Rossi fu ministro
```

## Step 4: Compatta sezioni

### Diagrammi ASCII
```markdown
# Prima (20 righe)
```
                    STRUTTURA COMPLESSA
                           |
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
    NODO 1             NODO 2             NODO 3
        |                  |                  |
        ...               ...               ...
```

# Dopo (rimosso o 3 righe)
**Struttura**: NODO 1 + NODO 2 + NODO 3 (interconnessi)
```

### Tabelle lunghe
```markdown
# Prima (50 righe)
| Persona | Ruolo | Anno | Dettaglio 1 | Dettaglio 2 | ... |

# Dopo (top 10)
| Persona | Ruolo chiave |
(solo le figure piu' rilevanti per i pattern)
```

### Sezioni narrative
```markdown
# Prima (paragrafo di 10 righe che spiega il contesto storico)

# Dopo (1-2 frasi che catturano l'essenza)
```

## Step 5: Struttura finale compatta

Il report compattato deve seguire questa struttura:

```markdown
# {Titolo}

> Sintesi in una frase

## Executive Summary
(tabella metriche - invariata)

---

## Pattern Chiave
(bullet points dei pattern piu' importanti)

---

## Attori Principali
(tabella compatta top 10-15, con link validi)

---

## Timeline Essenziale
| Anno | Evento chiave |
(solo eventi fondamentali, max 20 righe)

---

## Gap e TODO
(cose da investigare, domande aperte)

---

## Fonti
(invariata)

---

*Ultimo aggiornamento: {data}*
```

## Step 6: Esegui compattazione

1. Crea backup: `cp reports/{nome}.md reports/{nome}.backup.md`
2. Riscrivi il report con la struttura compatta
3. Verifica riduzione: `wc -l reports/{nome}.md`

## Step 7: Report finale

Riporta:
- Righe prima: X
- Righe dopo: Y
- Riduzione: Z%
- Pattern mantenuti: lista
- TODO identificati: lista

## Regole

1. **Mai perdere pattern analitici** - Sono il valore del report
2. **Mai perdere fonti** - Sono la base di verificabilita'
3. **Mai perdere TODO** - Sono il lavoro futuro
4. **Preferisci tabelle a prose** - Piu' dense di info
5. **Un link rotto e' peggio di nessun link** - Rimuovi link non funzionanti
6. **Obiettivo: non superare le 1000 righe** - Dimezza mantenendo l'essenza
