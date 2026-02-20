# Elastic NV

> Piattaforma search/observability/security: da progetto open source a public company, epicentro della battaglia licensing cloud vs. community

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Fondazione** | 2012 |
| **Sede** | Amsterdam, Paesi Bassi (operativa: San Francisco) |
| **Tipo** | Company (software) |
| **Leadership** | Ashutosh Kulkarni, CEO |
| **Ticker** | ESTC (NYSE) |
| **Dipendenti** | ~3.400 |
| **Status** | active |

---

## Glossario

| Termine | Definizione |
|---------|-------------|
| Elasticsearch | Motore di ricerca e analisi distribuito basato su Apache Lucene |
| Kibana | Tool di visualizzazione e dashboard per dati Elasticsearch |
| ELK Stack | Elasticsearch + Logstash + Kibana, stack standard per log analysis |
| SSPL | Server Side Public License, licenza creata da MongoDB e adottata da Elastic nel 2021 |
| AGPL | Affero GPL, licenza copyleft approvata OSI, adottata da Elastic nel 2024 |
| OpenSearch | Fork Apache 2.0 di Elasticsearch creato da AWS nel 2021 |

---

## Fondazione e Storia

| Dato | Dettaglio |
|------|-----------|
| **Fondazione** | 2012, Amsterdam |
| **Fondatori** | Shay Banon, Steven Schuurman, Simon Willnauer, Uri Boness |
| **Contesto** | Banon sviluppo' Elasticsearch nel 2009-2010 come progetto open source; nel 2012 fondo' l'azienda per commercializzarlo |
| **Obiettivo dichiarato** | Rendere i dati utilizzabili in tempo reale su larga scala |

### Timeline Storica

| Anno | Evento |
|------|--------|
| **2004** | Shay Banon inizia a lavorare su Compass (precursore di Elasticsearch) |
| **2010** | Prima release pubblica di Elasticsearch (Apache 2.0) |
| **2012** | Fondazione di Elastic (inizialmente Elasticsearch BV) |
| **2013-2014** | Funding rounds da Benchmark Capital, Index Ventures, NEA |
| **2015** | Rebrand da Elasticsearch a Elastic |
| **2018** | IPO su NYSE (ticker ESTC), valutazione ~$2.5B |
| **2021** | Cambio licenza da Apache 2.0 a SSPL/Elastic License: rottura con la community open source |
| **2021** | AWS lancia OpenSearch, fork Apache 2.0 di Elasticsearch |
| **2022** | Ashutosh Kulkarni promosso CEO; Banon diventa CTO |
| **2024** | Ritorno all'open source: aggiunta licenza AGPL v3 come opzione |
| **2024** | Chetan Puttagunta diventa Chairman del Board |

---

## Struttura e Governance

### Leadership Attuale

| Ruolo | Nome | Dal |
|-------|------|-----|
| CEO | Ashutosh Kulkarni | 2022 |
| CTO & Co-founder | Shay Banon | 2012 |
| CFO | Navam Welihinda | 2025 |
| CPO | Ken Exner | 2023 |
| Chairman | Chetan Puttagunta (Benchmark Capital) | 2024 |

### Board of Directors

| Nome | Ruolo | Background |
|------|-------|------------|
| [Chetan Puttagunta](../persons/chetan-puttagunta.md) | Chairman | General Partner, Benchmark Capital |
| [Shay Banon](../persons/shay-banon.md) | Executive Director | Co-founder, CTO |
| [Steven Schuurman](../persons/steven-schuurman.md) | Director | Co-founder |
| [Ashutosh Kulkarni](../persons/ashutosh-kulkarni.md) | Director | CEO |
| [Shelley Leibowitz](../persons/shelley-leibowitz.md) | Independent | Ex-BlackRock Managing Director |
| [Caryn Marooney](../persons/caryn-marooney.md) | Independent | Ex-Meta VP Communications |
| [Paul Auvil](../persons/paul-auvil.md) | Independent | Finance veteran |

---

## La Battaglia delle Licenze

### Il conflitto AWS-Elastic

La vicenda licensing e' centrale per comprendere le dinamiche di potere nel software open source:

1. **2010-2020**: Elasticsearch cresce come standard de facto per enterprise search sotto Apache 2.0
2. **2019-2020**: AWS lancia "Amazon Elasticsearch Service" senza contribuire significativamente al codice
3. **Gennaio 2021**: Elastic cambia licenza a SSPL/Elastic License, bloccando di fatto i cloud provider dal rivendere il prodotto
4. **Aprile 2021**: AWS fork il progetto come OpenSearch (Apache 2.0), sostenuto da Red Hat, Aiven, Logz.io, CrateDB
5. **Settembre 2024**: Elastic aggiunge AGPL v3 come opzione, tornando formalmente open source

### Significato sistemico

Il caso Elastic e' paradigmatico della tensione tra:
- **Creator economy**: chi sviluppa il software vuole catturarne il valore
- **Cloud hyperscalers**: AWS, Azure, GCP possono monetizzare qualsiasi software open source
- **Community**: gli utenti vogliono garanzie di apertura e continuita'

---

## Investitori Chiave

| Investitore | Tipo | Ruolo |
|-------------|------|-------|
| [Benchmark Capital](../private-equity/benchmark-capital.md) | VC | Lead investor, Chairman nel board |
| [Index Ventures](../private-equity/index-ventures.md) | VC | Early investor |
| NEA | VC | Series funding |

---

## Connessioni PowerLink

### Organizzazioni correlate

| Organizzazione | Connessione |
|----------------|-------------|
| [Amazon/AWS](../company/amazon.md) | Competitore diretto (OpenSearch fork) |
| [Red Hat](../companies/red-hat.md) | Partner nel fork OpenSearch |
| [MongoDB](../company/mongodb.md) | Pioniere SSPL, stessa strategia licensing |

### Figure chiave

| Persona | Ruolo |
|---------|-------|
| [Shay Banon](../persons/shay-banon.md) | Co-founder, CTO, architetto del progetto |
| [Chetan Puttagunta](../persons/chetan-puttagunta.md) | Chairman, link con Benchmark Capital |

---

## Fonti

### Ufficiali
- [Elastic - About](https://www.elastic.co/about)
- [Elastic - Board of Directors](https://www.elastic.co/about/board)
- [Elastic IR](https://ir.elastic.co/)

### Wikipedia
- [Elastic NV - Wikipedia](https://en.wikipedia.org/wiki/Elastic_NV)
- [SSPL - Wikipedia](https://en.wikipedia.org/wiki/Server_Side_Public_License)

### Analisi
- [Elastic's Return to Open Source - Revenera](https://www.revenera.com/blog/software-composition-analysis/elastics-return-to-open-source/)
- [Elastic's Journey from Apache 2.0 to AGPL 3 - Pureinsights](https://pureinsights.com/blog/2024/elastics-journey-from-apache-2-0-to-agpl-3/)

---

*Ultimo aggiornamento: Febbraio 2026*
