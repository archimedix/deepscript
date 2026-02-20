# HashiCorp

> Infrastruttura cloud come codice: da startup open source a sussidiaria IBM da $6.4 miliardi

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Fondazione** | 2012 |
| **Sede** | San Francisco, USA |
| **Tipo** | Company (cloud infrastructure) |
| **Leadership** | Dave McJannet, CEO |
| **Fondatori** | Mitchell Hashimoto, Armon Dadgar |
| **IPO** | 2021 (NASDAQ: HCP, $14B valuation) |
| **Status** | Acquisita da IBM (2024, $6.4B) |

---

## Fondazione e Storia

| Dato | Dettaglio |
|------|-----------|
| **Fondazione** | 2012, San Francisco |
| **Fondatori** | Mitchell Hashimoto, Armon Dadgar |
| **Contesto** | Esplosione del cloud computing, necessita' di gestire infrastruttura multi-cloud |
| **Obiettivo dichiarato** | Fornire strumenti open source per provisioning, sicurezza, networking e runtime dell'infrastruttura cloud |

Hashimoto e Dadgar si conobbero nel 2008 alla University of Washington. Hashimoto aveva gia' creato Vagrant, tool open source per ambienti di sviluppo virtualizzati. Nel 2012 fondarono HashiCorp per commercializzare un ecosistema di strumenti DevOps.

### Timeline Storica

| Anno | Evento |
|------|--------|
| **2012** | Fondazione da parte di Mitchell Hashimoto |
| **2013** | Armon Dadgar entra come co-founder |
| **2014** | Series A $10.2M (True Ventures, GGV Capital, Mayfield) |
| **2016** | Dave McJannet nominato CEO |
| **2018** | Raggiunge valutazione $1.9B (unicorn status), raccolta $100M |
| **2021** | IPO su NASDAQ, valutazione oltre $14B |
| **2023** | Cambio licenza da MPL a BSL 1.1 — controversia open source, fork OpenTofu |
| **2024** | Acquisizione da IBM per $6.4B ($35/azione) |

---

## Prodotti Chiave

| Prodotto | Funzione |
|----------|----------|
| **Terraform** | Infrastructure as Code (IaC) — provisioning multi-cloud |
| **Vault** | Secrets management, encryption, identity-based security |
| **Consul** | Service mesh, service discovery, networking |
| **Nomad** | Workload orchestration (alternativa a Kubernetes) |
| **Vagrant** | Ambienti di sviluppo virtualizzati (prodotto originale) |
| **Packer** | Creazione immagini macchine automatizzate |
| **Boundary** | Secure remote access |
| **Waypoint** | Application deployment workflow |

---

## Struttura e Governance

### Leadership

| Ruolo | Nome | Dal |
|-------|------|-----|
| CEO | [Dave McJannet](../persons/dave-mcjannet.md) | 2016 |
| CTO & Co-founder | [Armon Dadgar](../persons/armon-dadgar.md) | 2013 |
| Co-founder | [Mitchell Hashimoto](../persons/mitchell-hashimoto.md) | 2012 |

### Board (pre-acquisizione IBM)

| Nome | Ruolo |
|------|-------|
| Dave McJannet | CEO |
| Armon Dadgar | CTO |
| Susan St. Ledger | Director |
| Todd Ford | Director |
| David Henshall | Director |
| Glenn Solomon | Director (GGV Capital) |
| Sigal Zarmi | Director |

### Investitori Principali

| Investitore | Ruolo |
|-------------|-------|
| GGV Capital | Lead investor |
| Mayfield | Early investor |
| True Ventures | Series A |
| Redpoint Ventures | Growth investor |

---

## Controversia Licenza BSL (2023)

Il 10 agosto 2023 HashiCorp annuncio' il passaggio di tutti i prodotti dalla licenza Mozilla Public License (MPL) alla Business Source License (BSL 1.1). La BSL e' source-available ma restringe l'uso commerciale competitivo.

La comunita' open source reagi' con forza:
- **15 agosto 2023**: Manifesto OpenTF chiede il ripristino della licenza open source
- **25 agosto 2023**: Annunciato fork open source di Terraform
- **20 settembre 2023**: Il fork viene accettato dalla [Linux Foundation](../foundation/linux-foundation.md) come **OpenTofu** (licenza MPL 2.0)
- Oltre 33.000 stelle GitHub, 140+ aziende e 700+ individui a supporto

La decisione fu vista come precursore dell'acquisizione IBM, consolidando il controllo commerciale sui prodotti.

---

## Acquisizione IBM (2024)

IBM annuncio' l'acquisizione il 24 aprile 2024 per $6.4 miliardi ($35/azione in cash). Completata entro fine 2024.

**Rationale strategico**: integrare Terraform con Red Hat Ansible per creare una piattaforma hybrid cloud end-to-end. Gli azionisti principali (~43% del voto) firmarono un voting agreement a favore.

---

## Connessioni PowerLink

### Aziende correlate

| Azienda | Connessione |
|---------|-------------|
| [IBM](../company/ibm.md) | Acquirente (2024, $6.4B) |
| [Red Hat](../companies/red-hat.md) | Sinergie Ansible-Terraform (entrambe IBM) |
| [GitHub](../companies/github.md) | McJannet ex-VP Marketing |
| [Microsoft](../company/microsoft.md) | McJannet precedente ruolo |

### Fondazioni

| Fondazione | Relazione |
|------------|-----------|
| [Linux Foundation](../foundation/linux-foundation.md) | Ospita OpenTofu, fork di Terraform |

### Figure chiave

| Persona | Ruolo |
|---------|-------|
| [Mitchell Hashimoto](../persons/mitchell-hashimoto.md) | Co-founder |
| [Armon Dadgar](../persons/armon-dadgar.md) | Co-founder & CTO |
| [Dave McJannet](../persons/dave-mcjannet.md) | CEO |
| [Arvind Krishna](../persons/arvind-krishna.md) | CEO IBM (acquirente) |

---

## Critiche

| Tema | Dettaglio |
|------|-----------|
| **BSL license switch** | Passaggio da open source a source-available visto come tradimento della community |
| **Vendor lock-in** | Integrazione IBM potrebbe limitare interoperabilita' multi-cloud |
| **OpenTofu competition** | Fork supportato da Linux Foundation potrebbe erodere base utenti Terraform |

---

## Fonti

### Ufficiali
- [HashiCorp About](https://www.hashicorp.com/en/about)
- [IBM Newsroom - Acquisizione](https://newsroom.ibm.com/2024-04-24-IBM-to-Acquire-HashiCorp-Inc-Creating-a-Comprehensive-End-to-End-Hybrid-Cloud-Platform)

### Wikipedia
- [Wikipedia - HashiCorp](https://en.wikipedia.org/wiki/HashiCorp)

### Analisi
- [OpenTofu Manifesto](https://opentofu.org/manifesto/)
- [Mayfield - HashiCorp Journey](https://www.mayfield.com/founder-stories/the-hashicorp-journey-the-rise-of-a-cloud-powerhouse/)

---

*Ultimo aggiornamento: Febbraio 2026*
