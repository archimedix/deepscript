# SWIFT

> Il sistema nervoso della finanza globale: 11,000 banche, 42 milioni di messaggi al giorno, e l'arma geopolitica dell'Occidente

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Nome completo** | Society for Worldwide Interbank Financial Telecommunication |
| **Fondazione** | 3 maggio 1973 |
| **Sede** | La Hulpe, Belgio |
| **Tipo** | Cooperativa di diritto belga |
| **Membri** | 11,000+ istituzioni finanziarie |
| **Paesi** | 200+ |
| **Messaggi/giorno** | 42+ milioni |
| **Dipendenti** | ~3,500 |
| **Status** | Active |

---

## Cos'e' SWIFT

SWIFT non e' un sistema di pagamento - e' un sistema di **messaggistica** tra banche. Quando una banca trasferisce denaro a un'altra, SWIFT trasmette il messaggio che descrive la transazione.

| Cosa FA | Cosa NON FA |
|---------|-------------|
| Trasmette istruzioni di pagamento | Non muove denaro fisicamente |
| Standardizza formati messaggi | Non detiene fondi |
| Identifica banche (codici BIC) | Non esegue settlement |
| Connette 11,000+ istituzioni | Non e' una banca centrale |

---

## Fondazione e Storia

### Origini (1973)

| Dato | Dettaglio |
|------|-----------|
| **Data** | 3 maggio 1973 |
| **Fondatori** | 239 banche da 15 paesi |
| **Sede scelta** | Belgio (neutrale, sede CEE) |
| **Primo messaggio** | 19 ottobre 1977 |
| **Problema risolto** | Sostituire Telex, lento e insicuro |

### Timeline

| Anno | Evento |
|------|--------|
| **1973** | Fondazione a Bruxelles |
| **1977** | Primo messaggio SWIFT |
| **1987** | 2,200 banche in 62 paesi |
| **2001** | SWIFTNet (IP-based) |
| **2012** | **Iran disconnesso** (sanzioni nucleari) |
| **2016** | Attacco hacker Bangladesh ($81M rubati) |
| **2022** | **Russia: 7 banche disconnesse** (invasione Ucraina) |
| **2025** | Ban transazionale completo su Russia |

---

## Struttura e Governance

### Forma Giuridica

SWIFT e' una **cooperativa di diritto belga**, posseduta e controllata dai suoi membri:

| Aspetto | Dettaglio |
|---------|-----------|
| **Tipo** | Societe Cooperative |
| **Azionisti** | ~3,500 istituzioni finanziarie |
| **Board** | 25 direttori da banche membri |
| **Voto** | Proporzionale al traffico messaggi |

### Oversight

SWIFT e' supervisionato dal **G10 Oversight Forum** coordinato dalla National Bank of Belgium:

| Banca Centrale | Paese |
|----------------|-------|
| National Bank of Belgium | Belgio (lead) |
| Federal Reserve | USA |
| BCE | Eurozona |
| Bank of England | UK |
| Bank of Japan | Giappone |
| + altre G10 | - |

---

## Come Funziona

### Il Messaggio SWIFT

```
Banca A (Milano)                    Banca B (New York)
     |                                    |
     |------ Messaggio SWIFT ----------->|
     |  "Trasferisci $1M da conto X       |
     |   a conto Y"                       |
     |                                    |
     |<----- Conferma SWIFT -------------|
```

### Codice BIC/SWIFT

Ogni istituzione ha un codice identificativo:

| Esempio | Significato |
|---------|-------------|
| BNPAFRPP | BNP Paribas, Francia, Parigi |
| CHASUS33 | JPMorgan Chase, USA |
| DEUTDEFF | Deutsche Bank, Germania, Francoforte |

---

## SWIFT come Arma Geopolitica

### Il Caso Iran (2012)

| Aspetto | Dettaglio |
|---------|-----------|
| **Motivo** | Sanzioni UE per programma nucleare |
| **Data** | 17 marzo 2012 |
| **Effetto** | 30+ banche iraniane disconnesse |
| **Impatto** | Iran escluso da sistema finanziario globale |
| **Fine** | 2016 (JCPOA), poi ripristino parziale sanzioni 2018 |

### Il Caso Russia (2022-2025)

| Data | Azione |
|------|--------|
| **26 Feb 2022** | UE/USA/UK annunciano esclusione banche russe |
| **12 Mar 2022** | 7 banche russe disconnesse |
| **2023** | Estensione a piu' banche |
| **2025** | Ban transazionale completo |

**Banche russe disconnesse:**
- VTB Bank
- Bank Rossiya
- Promsvyazbank
- Novikombank
- VEB.RF (banca sviluppo)
- Otkritie
- Sovcombank

**Esclusa:** Sberbank (inizialmente) e Gazprombank (pagamenti energia)

### Perche' Funziona

| Fattore | Spiegazione |
|---------|-------------|
| **Monopolio de facto** | Nessuna alternativa reale globale |
| **Giurisdizione belga** | UE decide, non USA |
| **Effetto immediato** | Banca disconnessa = isolata |

### Alternative in Sviluppo

| Sistema | Paese | Status |
|---------|-------|--------|
| **SPFS** | Russia | Operativo, 500+ banche domestiche |
| **CIPS** | Cina | Operativo, 1,400+ membri |
| **Mir** | Russia | Carte, non messaggistica |

---

## Sede: La Hulpe, Belgio

SWIFT ha sede a La Hulpe, comune a 20km da Bruxelles:

| Aspetto | Dettaglio |
|---------|-----------|
| **Indirizzo** | Avenue Adele 1, 1310 La Hulpe |
| **Tipo** | Campus tecnologico |
| **Scelta Belgio** | Neutralita', sede CEE, multilinguismo |
| **Data center** | USA (Virginia), Paesi Bassi, Svizzera |

---

## Connessioni DeepScript

### Il Triangolo Benelux dell'Infrastruttura Finanziaria

SWIFT fa parte del sistema di infrastruttura finanziaria critica concentrato nel Benelux:

| Sistema | Sede | Funzione | Controllo |
|---------|------|----------|-----------|
| **SWIFT** | Belgio | Messaggistica | Cooperativa |
| **[Euroclear](euroclear.md)** | Belgio | Settlement, Custody | Mutualizzata |
| **[Clearstream](clearstream.md)** | Lussemburgo | Settlement, Custody | Deutsche Borse |

### Organizzazioni

| Entita' | Connessione |
|---------|-------------|
| [Euroclear](euroclear.md) | Partner settlement, stesso paese |
| [Clearstream](clearstream.md) | Partner settlement, Lussemburgo |
| [BIS](../central-bank/bis.md) | Oversight via G10 |
| [BCE](../central-bank/bce.md) | Oversight, utente principale |
| [National Bank of Belgium](../central-bank/nbb.md) | Supervisore principale |

### Contesto Geopolitico

| Tema | Relazione |
|------|-----------|
| Sanzioni Iran | Strumento esclusione 2012-2016 |
| Sanzioni Russia | Strumento esclusione 2022- |
| Alternativa cinese (CIPS) | Sfida al monopolio |
| De-dollarizzazione | SWIFT associato a sistema USD |

---

## Dati Quantitativi

| Metrica | Valore (2024) |
|---------|---------------|
| Messaggi/giorno | 42+ milioni |
| Messaggi/anno | 11+ miliardi |
| Membri | 11,000+ istituzioni |
| Paesi | 200+ |
| Dipendenti | ~3,500 |
| Tipi messaggi | 600+ (MT e MX/ISO 20022) |

---

## Domande Aperte

- [ ] Leadership attuale e background
- [ ] Dettagli governance (composizione board)
- [ ] Evoluzione verso ISO 20022
- [ ] Risposta a alternative CIPS/SPFS
- [ ] Ruolo in sanzioni future

---

## Fonti

### Ufficiali
- [SWIFT - About Us](https://www.swift.com/about-us)
- [SWIFT - History](https://www.swift.com/about-us/history)

### Wikipedia
- [SWIFT](https://en.wikipedia.org/wiki/SWIFT)
- [2022 SWIFT ban](https://en.wikipedia.org/wiki/2022_SWIFT_ban)

### News
- [Reuters - Russia SWIFT ban](https://www.reuters.com/business/finance/eu-excludes-seven-russian-banks-swift-official-journal-2022-03-02/)
- [BBC - What is SWIFT](https://www.bbc.com/news/business-60521822)

---

*Ultimo aggiornamento: Dicembre 2025*
