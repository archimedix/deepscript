# Cellebrite

> Il leader mondiale della forensica mobile: dalla polizia di quartiere all'FBI, passando per regimi autoritari

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Fondazione** | 1999 |
| **Sede** | Petah Tikva, Israel |
| **Tipo** | Company (Digital Forensics) |
| **CEO** | Thomas E. Hogan (dal 2025) |
| **Chairman** | Adam H. Clammer (dal 2025) |
| **Revenue** | $401M (2024) |
| **Ticker** | CLBT (NASDAQ) |
| **Status** | active |

---

## Glossario

| Termine | Definizione |
|---------|-------------|
| **UFED** | Universal Forensic Extraction Device - prodotto flagship |
| **Physical Analyzer** | Software per analisi dati estratti |
| **NoviSpy** | Spyware usato da Serbia dopo sblocco con Cellebrite |

---

## Fondazione e Storia

| Dato | Dettaglio |
|------|-----------|
| **Fondazione** | 1999 |
| **Fondatori** | Avi Yablonka, Yaron Baratz, Yuval Aflalo |
| **Focus iniziale** | Phone-to-phone data transfer per carrier |
| **Pivot** | 2007: divisione mobile forensics per law enforcement |

### Timeline Storica

| Anno | Evento |
|------|--------|
| **1999** | Fondazione a Petah Tikva |
| **2007** | Acquisizione da Sun Corporation (Giappone) per $17.5M |
| **2007** | Lancio divisione mobile forensics |
| **2016** | Caso San Bernardino (possibile ruolo in sblocco iPhone FBI) |
| **2017** | Contratto ICE $2.2M |
| **2019** | Contratto ICE $30-35M |
| **2021** | IPO via SPAC, quotazione NASDAQ |
| **2021** | Signal rivela vulnerabilita' critiche in UFED |
| **2024** | Scandalo Serbia (Amnesty International) |
| **2024** | Revenue $401M (+23% YoY) |
| **2025 Jan** | Thomas Hogan diventa CEO |
| **2025 Feb** | Sospensione vendite a Serbia |
| **2025 Dec** | Acquisizione Corellium per $170M |

---

## Struttura e Governance

### Leadership

| Ruolo | Nome | Dal |
|-------|------|-----|
| **CEO** | Thomas E. Hogan | 2025 |
| **Chairman** | Adam H. Clammer | 2025 |
| **Ex-CEO** | Yossi Carmil | 2004-2024 |

### Azionariato

| Azionista | Stake | Note |
|-----------|-------|------|
| [Sun Corporation](sun-corporation.md) | Maggioranza | Giappone, dal 2007 |
| Public (NASDAQ) | - | Ticker CLBT |

---

## Prodotti

| Prodotto | Funzione |
|----------|----------|
| **UFED Touch/4PC** | Estrazione dati da dispositivi mobili |
| **Physical Analyzer** | Analisi forense dati estratti |
| **UFED Cloud** | Estrazione dati da cloud accounts |
| **Pathfinder** | Analisi link e pattern |
| **Corellium** | Virtualizzazione iOS (acquisita 2025) |

### Capacita' UFED

- Bypass password e encryption
- Estrazione testi, call logs, foto, video
- Dati app (Signal, WhatsApp, Telegram)
- Location history
- File cancellati

---

## Clienti

### USA - Agenzie Federali

| Agenzia | Contratti | Note |
|---------|-----------|------|
| **DEA** | 371 ordini | Top cliente |
| **ICE** | 216 ordini | $11M contratto 2025 |
| **FBI** | 199 ordini | Possibile ruolo San Bernardino |
| **US Army** | 106 ordini | - |
| **State Dept** | 93 ordini | - |
| **CBP** | 83 ordini | $6.1M 2009-2024 |
| **Coast Guard** | 60 ordini | - |
| **US Navy** | 55 ordini | - |
| **Marshals** | 28 ordini | - |
| **Secret Service** | 25 ordini | - |

**Totale**: 2,800+ clienti government in North America (14/15 Cabinet departments)

### Internazionali

| Categoria | Paesi |
|-----------|-------|
| **EU** | 25/27 paesi |
| **Controversi (ex)** | Russia, Belarus, Cina (sospesi) |
| **Controversi** | Turchia, UAE, Bangladesh, Myanmar |

---

## Controversie

### San Bernardino (2016)

| Aspetto | Dettaglio |
|---------|-----------|
| **Caso** | FBI vs Apple per sblocco iPhone terrorista |
| **Ruolo Cellebrite** | Ampiamente riportato ma mai confermato |
| **Alternativa** | WaPo: Azimuth Security (Australia) |

### Serbia (2024-2025)

| Aspetto | Dettaglio |
|---------|-----------|
| **Report** | Amnesty International, dicembre 2024 |
| **Vittime** | Giornalista, attivista ambientale |
| **Metodo** | UFED + installazione spyware NoviSpy |
| **Risposta** | Cellebrite sospende Serbia, febbraio 2025 |

### Regimi Autoritari

| Paese | Accuse |
|-------|--------|
| Bangladesh | Death squads |
| Myanmar | Giunta militare |
| Belarus | Repressione opposizione |
| Russia | Sorveglianza dissidenti |
| Hong Kong | Proteste 2019 |

### Vulnerabilita' Signal (2021)

Moxie Marlinspike (Signal) ha dimostrato:
- Falle critiche in UFED e Physical Analyzer
- Possibilita' di eseguire codice malevolo
- Manipolazione report forensi passati e futuri

---

## Connessioni PowerLink

### Ecosistema Sorveglianza Israeliano

| Azienda | Tipo | Relazione |
|---------|------|-----------|
| [NSO Group](nso-group.md) | Spyware (Pegasus) | Competitor, stesso ecosistema |
| [Paragon](paragon.md) | Spyware (Graphite) | Competitor |
| [Unit 8200](../agency/unit-8200.md) | Intelligence IDF | Fonte talenti |

### Clienti Chiave

| Entita' | Connessione |
|---------|-------------|
| [FBI](../agency/fbi.md) | 199+ contratti |
| ICE | $30M+ contratti |
| DEA | Top cliente (371 ordini) |

### Investitori

| Entita' | Connessione |
|---------|-------------|
| [Sun Corporation](sun-corporation.md) | Majority owner (Giappone) |

---

## Pattern: Dual-Use Surveillance Tech

```
Cellebrite (forensics) ←──────→ NSO Group (spyware)
         │                              │
         │    Stesso ecosistema:        │
         │    - Clienti sovrapposti     │
         │    - Talenti Unit 8200       │
         │    - Export Israel MoD       │
         │                              │
         ▼                              ▼
    Law Enforcement              Intelligence
    (FBI, ICE, EU police)        (Regimi autoritari)
```

---

## Metriche Finanziarie

| Metrica | 2023 | 2024 |
|---------|------|------|
| **Revenue** | $326M | $401M |
| **Growth** | - | +23% |
| **ARR** | $317M | $396M |

---

## Fonti

### Ufficiali
- [Cellebrite](https://cellebrite.com/)
- [Cellebrite IR](https://investors.cellebrite.com/)

### Wikipedia
- [Cellebrite - Wikipedia](https://en.wikipedia.org/wiki/Cellebrite)

### Giornalismo Investigativo
- [The Intercept - Cellebrite Government Spread](https://theintercept.com/2022/02/08/cellebrite-phone-hacking-government-agencies/)
- [Amnesty - Serbia Report](https://www.amnesty.org/)
- [Signal - Cellebrite Vulnerabilities](https://signal.org/blog/cellebrite-vulnerabilities/)
- [Calcalist - CEO Interview](https://www.calcalistech.com/ctechnews/article/lhck15vtj)

### Human Rights
- [AFSC Investigate](https://investigate.afsc.org/company/cellebrite-di)
- [Center for Human Rights and Privacy](https://www.cehrp.org/tags/cellebrite/)

---

*Ultimo aggiornamento: Gennaio 2026*
