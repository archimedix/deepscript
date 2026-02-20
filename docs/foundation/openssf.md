# Open Source Security Foundation (OpenSSF)

> Governance della sicurezza del software open source globale: dalla risposta a Log4Shell alla protezione della supply chain

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Fondazione** | Agosto 2020 |
| **Sede** | San Francisco, USA |
| **Tipo** | Foundation (sussidiaria Linux Foundation) |
| **Leadership** | Omkhar Arasaratnam (General Manager, dal 2023) |
| **Funding** | $30M+ (pledges White House Summit 2022) |
| **Status** | active |

---

## Glossario

| Termine | Definizione |
|---------|-------------|
| **Supply chain attack** | Compromissione di dipendenze software per infiltrare sistemi a valle |
| **SBOM** | Software Bill of Materials, inventario dei componenti di un software |
| **SLSA** | Supply-chain Levels for Software Artifacts, framework di sicurezza |
| **Sigstore** | Infrastruttura per firma crittografica di artefatti software |
| **Scorecard** | Tool automatico per valutare la sicurezza di progetti open source |
| **CII** | Core Infrastructure Initiative, predecessore di OpenSSF |

---

## Fondazione e Storia

| Dato | Dettaglio |
|------|-----------|
| **Fondazione** | 3 agosto 2020 |
| **Predecessori** | Core Infrastructure Initiative (CII, Linux Foundation), Open Source Security Coalition (OSSC, GitHub Security Lab), JOSSI (Google) |
| **Fondatori** | GitHub, Google, IBM, JPMorgan Chase, Microsoft, NCC Group, OWASP, Red Hat |
| **Contesto** | Fusione di iniziative frammentate di sicurezza open source sotto un'unica governance |
| **Obiettivo dichiarato** | Migliorare la sicurezza del software open source attraverso collaborazione cross-industry |

### Timeline Storica

| Anno | Evento |
|------|--------|
| **2014** | Heartbleed (OpenSSL) porta alla creazione della Core Infrastructure Initiative nella Linux Foundation |
| **2020** | Fusione di CII, OSSC e JOSSI in OpenSSF (agosto) |
| **2021** | Brian Behlendorf nominato primo General Manager; $10M in nuovi commitments; lancio Sigstore |
| **2021 dic** | Vulnerabilita' Log4Shell (Log4j) scuote l'ecosistema software globale |
| **2022 gen** | White House Open Source Software Security Summit post-Log4Shell |
| **2022 mag** | Secondo summit: $30M in pledges da Amazon, Google, Intel, Microsoft, VMware e altri |
| **2023** | Omkhar Arasaratnam diventa GM; Behlendorf passa a CTO |
| **2024** | Backdoor scoperta in XZ Utils conferma la centralita' della supply chain security |

---

## Struttura e Governance

### Leadership Attuale

| Ruolo | Nome | Dal |
|-------|------|-----|
| General Manager | [Omkhar Arasaratnam](../persons/omkhar-arasaratnam.md) | 2023 |

### Leadership Precedente

| Ruolo | Nome | Periodo |
|-------|------|---------|
| General Manager, poi CTO | [Brian Behlendorf](../persons/brian-behlendorf.md) | 2021-2023 |

### Organi Direttivi

- **Governing Board (GB)**: decisioni budget e strategia, include rappresentanti corporate e un Security Community Individual Representative
- **Technical Advisory Council (TAC)**: strategia tecnica complessiva
- **Working Groups**: gestiti autonomamente dai maintainer dei progetti

---

## Membri Fondatori

| Azienda | Paese | Settore |
|---------|-------|---------|
| [Google](../company/google.md) | USA | Tech |
| [Microsoft](../company/microsoft.md) | USA | Tech |
| [GitHub](../company/github.md) | USA | Tech (sussidiaria Microsoft) |
| [IBM](../company/ibm.md) | USA | Tech |
| [Red Hat](../company/red-hat.md) | USA | Tech (sussidiaria IBM) |
| [JPMorgan Chase](../bank/jpmorgan-chase.md) | USA | Finance |
| NCC Group | GBR | Cybersecurity |
| OWASP Foundation | USA | Security (non-profit) |

---

## Progetti Chiave

| Progetto | Funzione |
|----------|----------|
| **Sigstore** | Firma crittografica di artefatti software (signing, transparency log) |
| **SLSA** | Framework per intergita' della supply chain (livelli 1-4) |
| **Scorecard** | Valutazione automatica della sicurezza di progetti OSS |
| **Alpha-Omega** | Investimento diretto nella sicurezza dei progetti piu' critici |
| **Package Analysis** | Analisi automatica di pacchetti sospetti su registri pubblici |
| **GUAC** | Graph for Understanding Artifact Composition, grafo delle dipendenze |

---

## Connessioni PowerLink

### Organizzazione madre

| Organizzazione | Relazione |
|----------------|-----------|
| [Linux Foundation](../foundation/linux-foundation.md) | Parent organization |

### Figure chiave nel DB

| Persona | Ruolo |
|---------|-------|
| [Brian Behlendorf](../persons/brian-behlendorf.md) | GM fondatore 2021-2023, CTO |
| [Omkhar Arasaratnam](../persons/omkhar-arasaratnam.md) | General Manager (dal 2023) |

### Organizzazioni sorelle (Linux Foundation)

| Organizzazione | Relazione |
|----------------|-----------|
| [CNCF](../foundation/cncf.md) | Sorella sotto Linux Foundation, focus infrastruttura cloud |

### Evento chiave

| Evento | Relazione |
|--------|-----------|
| White House OSS Security Summit (gen 2022) | Catalizzatore post-Log4Shell, visibilita' politica |
| White House follow-up (mag 2022) | $30M in pledges da 37 aziende |

---

## Rilevanza Geopolitica

OpenSSF rappresenta il punto d'incontro tra sicurezza nazionale e open source. La presenza di JPMorgan Chase tra i fondatori segnala che la supply chain security e' una preoccupazione del settore finanziario, non solo tech. I summit alla Casa Bianca nel 2022 hanno elevato la sicurezza OSS a questione di sicurezza nazionale USA. La backdoor XZ Utils del 2024 — scoperta quasi per caso — ha confermato che un singolo maintainer sovraccarico puo' diventare un vettore di attacco statale.

---

## Fonti

### Ufficiali
- [OpenSSF - Sito ufficiale](https://openssf.org/)
- [OpenSSF - About](https://openssf.org/about/)
- [OpenSSF GitHub](https://github.com/ossf)

### Wikipedia
- [Wikipedia - Open Source Security Foundation](https://en.wikipedia.org/wiki/Open_Source_Security_Foundation)

### Analisi
- [Linux Foundation - OpenSSF Reflection and Future](https://www.linuxfoundation.org/blog/blog/open-source-security-foundation-openssf-reflection-and-future)
- [Linux Foundation - White House Summit](https://www.linuxfoundation.org/press/press-release/the-openssf-and-the-linux-foundation-address-software-supply-chain-security-challenges-at-white-house-summit)

---

*Ultimo aggiornamento: Febbraio 2026*
