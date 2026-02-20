# OpenSearch Software Foundation

> Fork di Elasticsearch nato dalla guerra licensing AWS-Elastic, divenuto fondazione indipendente sotto Linux Foundation

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Fondazione** | 2021 (progetto), 2024 (fondazione LF) |
| **Sede** | San Francisco, USA |
| **Tipo** | Foundation (sotto Linux Foundation) |
| **Leadership** | Bianca Lewis, Executive Director |
| **Contributors** | 1.000+ contributors, 200+ maintainers |
| **Downloads** | 700M+ |
| **Status** | active |

---

## Glossario

| Termine | Definizione |
|---------|-------------|
| OpenSearch | Motore di ricerca e analisi distribuito, fork di Elasticsearch 7.10 |
| OpenSearch Dashboards | Fork di Kibana, tool di visualizzazione |
| SSPL | Server Side Public License, licenza di Elastic che scateno' il fork |
| TSC | Technical Steering Committee, organo tecnico della fondazione |

---

## Fondazione e Storia

| Dato | Dettaglio |
|------|-----------|
| **Origine** | Fork di Elasticsearch 7.10.2 e Kibana 7.10.2 (ultima versione Apache 2.0) |
| **Creatore** | Amazon Web Services |
| **Contesto** | Elastic cambio' licenza da Apache 2.0 a SSPL nel gennaio 2021, bloccando i cloud provider |
| **Obiettivo dichiarato** | Garantire un search engine completamente open source (Apache 2.0) |

### Timeline Storica

| Anno | Evento |
|------|--------|
| **Gen 2021** | Elastic annuncia cambio licenza Elasticsearch/Kibana da Apache 2.0 a SSPL |
| **Apr 2021** | AWS lancia OpenSearch come fork Apache 2.0 di Elasticsearch 7.10 |
| **2021** | Red Hat, Aiven, Logz.io, CrateDB collaborano allo sviluppo |
| **2022-2023** | Crescita rapida: adozione enterprise, nuove feature (vector search, ML) |
| **Set 2024** | AWS trasferisce OpenSearch alla Linux Foundation come fondazione indipendente |
| **Set 2024** | Elastic risponde aggiungendo AGPL come licenza, tornando formalmente open source |
| **2025** | Bianca Lewis nominata Executive Director della fondazione |

---

## Struttura e Governance

### Leadership

| Ruolo | Nome | Dal |
|-------|------|-----|
| Executive Director | [Bianca Lewis](../persons/bianca-lewis.md) | 2025 |
| Governing Board Chair | [Carl Meadows](../persons/carl-meadows.md) (AWS) | 2024 |

### Organi

- **Governing Board**: rappresentanti dei membri + chair del TSC
- **Technical Steering Committee (TSC)**: 15 membri da diverse organizzazioni (Aryn, AWS, ByteDance, IBM, Paessler, Salesforce, SAP, Uber)
- **Elezioni**: previste 2025-2026 per transizione a TSC interamente eletto

### Membri della Foundation

| Livello | Organizzazioni |
|---------|---------------|
| **Premier** | AWS, SAP, Uber |
| **General** | Aiven, Aryn, Atlassian, Canonical, DigitalOcean, Eliatra, Graylog, NetApp, Instaclustr, Portal26 |

---

## Il Fork: Anatomia di una Biforcazione

### Causa scatenante

Nel gennaio 2021 Elastic cambio' la licenza di Elasticsearch da Apache 2.0 a SSPL/Elastic License. La motivazione dichiarata: AWS vendeva "Amazon Elasticsearch Service" senza contribuire al progetto, creando confusione di brand.

### Reazione AWS

AWS fork il codice dall'ultima versione Apache 2.0 (7.10.2) e lancio' OpenSearch. La mossa fu sostenuta da altri attori dell'ecosistema: Red Hat, Aiven, Logz.io, CrateDB.

### Significato per il progetto DeepScript

Il caso OpenSearch/Elasticsearch illustra una dinamica di potere fondamentale nel tech:
- **Hyperscaler vs. Creator**: chi controlla il valore del software open source?
- **Foundation washing**: il trasferimento a una fondazione neutrale come legittimazione
- **Governance come strumento di potere**: chi siede nel TSC determina la direzione tecnica

---

## Connessioni PowerLink

### Organizzazioni correlate

| Organizzazione | Connessione |
|----------------|-------------|
| [Amazon/AWS](../company/amazon.md) | Creatore del fork, premier member |
| [Linux Foundation](../foundation/linux-foundation.md) | Host della fondazione |
| [Elastic](../company/elastic.md) | Progetto originale da cui OpenSearch e' stato forkato |
| [SAP](../company/sap.md) | Premier member |
| [Canonical](../companies/canonical.md) | General member |
| [Atlassian](../company/atlassian.md) | General member |
| [Red Hat](../companies/red-hat.md) | Collaboratore iniziale al fork |

### Figure chiave

| Persona | Ruolo |
|---------|-------|
| [Bianca Lewis](../persons/bianca-lewis.md) | Executive Director |
| [Carl Meadows](../persons/carl-meadows.md) | Governing Board Chair, AWS |
| [Shay Banon](../persons/shay-banon.md) | Creatore originale di Elasticsearch |

---

## Fonti

### Ufficiali
- [OpenSearch Foundation](https://opensearch.org/foundation/)
- [OpenSearch Project - GitHub](https://github.com/opensearch-project)

### Linux Foundation
- [LF Announces OpenSearch Software Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-opensearch-software-foundation-to-foster-open-collaboration-in-search-and-analytics)
- [Charting the Future of OpenSearch](https://www.linuxfoundation.org/blog/charting-the-future-of-opensearch)

### Analisi
- [OpenSearch: From Fork to Foundation - The New Stack](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation/)
- [AWS Brings OpenSearch Under the Linux Foundation - BigDataWire](https://www.bigdatawire.com/2024/09/20/aws-brings-opensearch-under-the-linux-foundation/)

---

*Ultimo aggiornamento: Febbraio 2026*
