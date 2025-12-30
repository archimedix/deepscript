# Equifax Inc.

> Il data breach del 2017 che espose 148 milioni di americani: anatomia di un fallimento sistemico

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Fondazione** | 1899 |
| **Sede** | Atlanta, Georgia, USA |
| **Tipo** | Data broker, Credit reporting |
| **Chairman** | Mark L. Feidler (2017-) |
| **CEO** | Mark W. Begor (2018-) |
| **Dipendenti** | ~14,000 |
| **Revenue** | ~$5.7B (2024) |
| **Status** | active |
| **Listing** | NYSE: EFX |

---

## Glossario

| Termine | Definizione |
|---------|-------------|
| **Credit Bureau** | Agenzia che raccoglie e vende dati creditizi su consumatori |
| **Big Three** | Equifax, Experian, TransUnion - oligopolio globale credit reporting |
| **Data Breach** | Violazione sicurezza con furto dati |

---

## Fondazione e Storia

| Dato | Dettaglio |
|------|-----------|
| **Fondazione** | 1899 |
| **Fondatori** | Cator e Guy Woolford (Atlanta, Georgia) |
| **Nome originale** | Retail Credit Company |
| **Metodo iniziale** | Merchants che annotavano debitori (prompt/slow/cash) |
| **Incorporazione** | 1913 |

### Timeline Storica

| Anno | Evento |
|------|--------|
| **1899** | Fondazione come Retail Credit Company |
| **1913** | Incorporazione |
| **1920** | 37 uffici in USA e Canada |
| **1960** | Piu' grande credit bureau USA |
| **1975** | Cambio nome in Equifax |
| **2017** | Data breach: 148M americani esposti |
| **2017** | CEO Richard Smith si dimette |
| **2018** | Mark Begor nominato CEO |
| **2019** | Settlement $700M con regolatori |
| **2024** | Cloud transformation completata |

---

## Struttura e Governance

### Leadership Attuale

| Ruolo | Nome | Dal |
|-------|------|-----|
| Chairman | Mark L. Feidler | 2017 |
| CEO | Mark W. Begor | 2018 |

### Mark L. Feidler (Chairman)

| Aspetto | Dettaglio |
|---------|-----------|
| **Background** | BellSouth President/COO, Cingular Wireless COO |
| **Equifax** | Director dal 2007, Chairman dal 2017 |
| **Attuale** | Founding Partner MSouth Equity Partners |

### Mark W. Begor (CEO)

| Aspetto | Dettaglio |
|---------|-----------|
| **Background** | 35 anni in GE |
| **GE Capital** | CEO Real Estate, CEO Retail Finance (Synchrony) |
| **Warburg Pincus** | Executive 2016-2018 |
| **Equifax** | CEO dal 2018 |
| **Altri board** | Raymond James Financial |

---

## Il Data Breach 2017

### Dimensioni

| Metrica | Valore |
|---------|--------|
| **Americani colpiti** | 147.9 milioni |
| **Britannici colpiti** | 15.2 milioni |
| **Canadesi colpiti** | ~19,000 |
| **Durata intrusione** | 76 giorni (maggio-luglio 2017) |
| **Scoperta** | 29 luglio 2017 |

### Causa Tecnica

| Fattore | Dettaglio |
|---------|-----------|
| **Vulnerabilita'** | CVE-2017-5638 (Apache Struts) |
| **Patch disponibile** | Si', ma non applicata |
| **Credenziali** | Username/password di default ("admin") |
| **2FA** | Assente su account high-access |

### Conseguenze

| Aspetto | Dettaglio |
|---------|-----------|
| **Settlement** | Fino a $700M |
| **Risarcimento consumatori** | Fino a $425M |
| **CEO dimesso** | Richard Smith (settembre 2017) |
| **Insider trading** | CIO Jun Ying condannato (4 mesi carcere) |
| **Insider trading** | Engineer Sudhakar Reddy accusato |

---

## Business Model

### Dati Gestiti

| Metrica | Valore |
|---------|--------|
| **Consumer profiles** | 800+ milioni |
| **Business profiles** | 88+ milioni |
| **Paesi** | 24 |

### Segmenti

| Segmento | Descrizione |
|----------|-------------|
| **Workforce Solutions** | Verifica reddito e impiego |
| **U.S. Information Solutions** | Credit data USA |
| **International** | Operazioni globali |

---

## Il "Big Three" Credit Bureau

```
              CREDIT REPORTING OLIGOPOLY
                        │
       ┌────────────────┼────────────────┐
       │                │                │
       ▼                ▼                ▼
   EQUIFAX          EXPERIAN        TRANSUNION
   (USA)           (UK/Ireland)        (USA)
   1899              1996              1968
       │                │                │
       └────────────────┴────────────────┘
                        │
                        ▼
              CONSUMATORI GLOBALI
            (pochi possono evitare)
```

---

## Pattern: GE → Private Equity → Corporate

```
GE CAPITAL                    WARBURG PINCUS              EQUIFAX
(35 anni)                        (2 anni)                   (CEO)
    │                               │                         │
    │  CEO Synchrony                │                         │
    │  CEO Real Estate              │  Executive              │
    │  CEO Energy Mgmt              │  Partner                │
    │                               │                         │
    └───────────(2016)──────────────┴────────(2018)───────────┘
                     Mark Begor
```

CEO Begor porta expertise GE Capital nel credit reporting.

---

## Connessioni DeepScript

### Organizzazioni correlate

| Organizzazione | Relazione |
|----------------|-----------|
| [Experian](experian.md) | Competitor (Big Three) |
| TransUnion | Competitor (Big Three) |
| [Warburg Pincus](../private-equity/warburg-pincus.md) | CEO Begor ex-Executive |
| GE Capital | CEO Begor 35 anni carriera |

---

## Critiche

| Tema | Dettaglio |
|------|-----------|
| **2017 Breach** | Uno dei peggiori data breach della storia |
| **Negligenza** | Patch non applicata, credenziali default |
| **Insider trading** | Dirigenti vendettero azioni prima della disclosure |
| **Consent** | Consumatori non scelgono di essere tracciati |
| **Oligopolio** | Poca competizione, potere di mercato |

---

## Fonti

### Ufficiali
- [Equifax - About Us](https://www.equifax.com/about-equifax/)
- [Equifax - Leadership](https://www.equifax.com/about-equifax/leadership/)
- [Equifax Investor Relations](https://investor.equifax.com/)

### Biografie
- [Wikipedia - Equifax](https://en.wikipedia.org/wiki/Equifax)
- [Wikipedia - 2017 Equifax data breach](https://en.wikipedia.org/wiki/2017_Equifax_data_breach)

### Analisi
- [CSO Online - Equifax breach FAQ](https://www.csoonline.com/article/567833/equifax-data-breach-faq-what-happened-who-was-affected-what-was-the-impact.html)
- [CFPB - Equifax Settlement](https://www.consumerfinance.gov/equifax-settlement/)

---

*Ultimo aggiornamento: Dicembre 2025*
