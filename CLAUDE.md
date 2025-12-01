# DeepScript - Istruzioni per Claude Code

## Obiettivo del progetto

DeepScript e' un manuale di storia alternativa che racconta il periodo 1945-oggi non attraverso stati e nazioni, ma attraverso i **soggetti che hanno realmente esercitato il potere decisionale**: famiglie, dinastie industriali, reti finanziarie, forum transnazionali, individui-chiave.

### Tesi centrale

Il potere reale nel mondo post-1945 (e specialmente post-1991) e':
- **Transnazionale**: attraversa i confini degli stati
- **Finanziario**: i gestori patrimoniali hanno piu' potere dei governi
- **Reticolare**: opera attraverso forum informali (Bilderberg, Trilaterale, WEF)
- **Dinastico**: le grandi famiglie mantengono influenza transgenerazionale
- **Tecnocratico**: l'"expertise" sostituisce la legittimazione democratica

---

## Struttura del repository

```
deepscript/
├── CLAUDE.md           # Questo file - istruzioni per l'agente
├── STRUTTURA.md        # Indice del manuale e organizzazione capitoli
├── README.md           # Descrizione pubblica del progetto
├── istituzioni/        # Schede su organizzazioni e forum (20 schede)
├── persone/            # Profili biografici dei decisori (19 schede)
├── eventi/             # Snodi storici e decisioni chiave (13 schede)
├── family/             # Dinastie e famiglie con continuita' transgenerazionale
├── connessioni/        # Mappe delle relazioni tra entita' (da creare)
└── capitoli/           # Bozze dei capitoli del manuale (da creare)
```

### Schede esistenti

#### Istituzioni (24)
- `aspen-institute.md` - Think tank transatlantico
- `banca-mondiale.md` - Bretton Woods, veto USA, Washington Consensus
- `bce.md` - Banca Centrale Europea
- `big-three-sintesi.md` - BlackRock, Vanguard, State Street
- `bilderberg-trilaterale.md` - Forum elite transatlantiche
- `bis.md` - Bank for International Settlements
- `blackrock.md` - Maggior gestore patrimoniale
- `cfr.md` - Council on Foreign Relations
- `federal-reserve.md` - Banca centrale USA
- `fmi.md` - Fondo Monetario Internazionale
- `goldman-sachs.md` - Investment bank "Government Sachs"
- `gruppo-30.md` - Think tank banchieri centrali/privati
- `jpmorgan-chase.md` - Maggiore banca USA
- `morgan-stanley.md` - Spin-off Morgan 1935, eredita' dinastia Morgan
- `nato.md` - Alleanza militare, SACEUR americano
- `onu.md` - Consiglio Sicurezza, P5, potere di veto
- `open-society.md` - Fondazioni Soros
- `paypal-mafia.md` - Network Silicon Valley
- `rockefeller-foundation.md` - $6B, filantropia strategica, Green Revolution
- `state-street.md` - Terzo gestore patrimoniale
- `vanguard.md` - Secondo gestore patrimoniale
- `warburg-pincus.md` - $87B AUM, eredita' Warburg, Geithner
- `wef.md` - World Economic Forum
- `young-global-leaders.md` - Vivaio WEF per futuri leader under-40

#### Persone (24)
- `angela-merkel.md` - Cancelliera Germania, GLT 1992, leader UE de facto
- `bill-gates.md` - Microsoft, Gates Foundation
- `christine-lagarde.md` - BCE, ex-FMI
- `david-rockefeller.md` - Chase, CFR, Trilaterale
- `elon-musk.md` - Tesla, SpaceX, X
- `emmanuel-macron.md` - Presidente Francia, YGL 2016, ex-Rothschild
- `george-soros.md` - Open Society
- `gianni-agnelli.md` - FIAT, Bilderberg, Trilaterale, "Re d'Italia"
- `henry-kissinger.md` - NSA, Segretario di Stato
- `jacinda-ardern.md` - PM Nuova Zelanda, YGL 2014
- `jamie-dimon.md` - JPMorgan Chase CEO
- `jeff-bezos.md` - Amazon, Blue Origin
- `jerome-powell.md` - Fed Chair, ex-Carlyle Group
- `john-elkann.md` - EXOR, Stellantis, erede Agnelli
- `justin-trudeau.md` - PM Canada, YGL 2005, "penetriamo i gabinetti"
- `klaus-schwab.md` - WEF fondatore
- `larry-fink.md` - BlackRock CEO
- `mario-draghi.md` - BCE, Goldman, PM Italia
- `mario-monti.md` - Trilaterale, PM tecnico
- `peter-thiel.md` - PayPal, Palantir
- `robert-rubin.md` - Goldman, Tesoro, CFR
- `romano-prodi.md` - PM Italia, Commissione UE, Goldman advisor
- `tony-blair.md` - PM UK, GLT 1992, Tony Blair Institute
- `zbigniew-brzezinski.md` - Trilaterale, NSA Carter

#### Eventi (13)
- `1910-jekyll-island.md` - Riunione segreta, creazione Federal Reserve
- `1944-bretton-woods.md` - FMI, Banca Mondiale, sistema dollaro-oro
- `1971-fine-bretton-woods.md` - Nixon Shock
- `1973-crisi-petrolifera.md` - Embargo OPEC, petrodollaro
- `1973-fondazione-trilaterale.md` - Rockefeller, Brzezinski, forum triregionale
- `1991-dissoluzione-urss.md` - Crollo URSS, oligarchi
- `1992-tangentopoli.md` - Mani Pulite
- `1992-trattato-maastricht.md` - Nascita UE/Euro
- `1999-abolizione-glass-steagall.md` - Deregulation bancaria, Rubin-Citigroup
- `2001-11-settembre.md` - War on Terror
- `2008-crisi-finanziaria.md` - Lehman, bailout
- `2011-crisi-debito-sovrano.md` - Governo Monti
- `2020-pandemia-great-reset.md` - COVID-19, WEF

#### Famiglie/Dinastie (9)
- `rothschild.md` - Dinastia bancaria europea, 8 generazioni, 3 rami attivi
- `rockefeller.md` - Standard Oil → CFR, Trilaterale, governance globale
- `agnelli-elkann.md` - FIAT → Stellantis, "Re d'Italia", Bilderberg
- `morgan.md` - Architetti Federal Reserve, dinastia estinta, legacy JPMorgan
- `warburg.md` - Architetti Federal Reserve, M.M. Warburg, Warburg Pincus
- `bush.md` - Dinastia politica USA, 2 presidenti, CIA, declino
- `walton.md` - Walmart, $432B, famiglia piu' ricca del mondo
- `murdoch.md` - Media empire, Fox News, influenza conservatrice globale
- `dupont.md` - Chimica, Delaware, dinastia dispersa (3,500+ membri)

---

## Come strutturare i documenti

### Template per ISTITUZIONI

```markdown
# [Nome Istituzione]

> [Tagline: una frase che cattura l'essenza del potere esercitato]

## Executive Summary
[Tabella con metriche chiave: AUM, membri, anno fondazione, sede, leadership]

## Fondazione e Storia
- Chi l'ha fondata e perche'
- Contesto storico
- Evoluzione nel tempo

## Struttura e Governance
- Come funziona internamente
- Chi decide
- Meccanismi di selezione

## Potere e Influenza
- Che tipo di potere esercita
- Su chi/cosa
- Attraverso quali meccanismi

## Connessioni PowerLink
[CRITICO: Collegare sempre ad altre entita' del progetto]
- Individui in comune con altre organizzazioni
- Sovrapposizioni di membership
- Flussi finanziari
- Allineamenti ideologici

## Figure Chiave
[Lista delle persone associate, con link a /persone/ quando disponibili]

## Timeline
[Eventi chiave in ordine cronologico]

## Domande Aperte
[Cosa non sappiamo ancora, cosa investigare]

## Fonti
[Sempre includere: ufficiali, accademiche, giornalistiche, critiche]
```

### Template per PERSONE

```markdown
# [Nome Cognome] (anno nascita - anno morte se applicabile)

> [Tagline: ruolo nel sistema di potere]

## Dati Essenziali
| Aspetto | Dettaglio |
|---------|-----------|
| Nascita | |
| Famiglia | |
| Formazione | |
| Patrimonio | |

## Carriera e Ruoli
[Timeline delle posizioni ricoperte]

## Rete di Connessioni
[CRITICO: mappare tutte le appartenenze]
- Istituzioni
- Forum (Bilderberg, Trilaterale, WEF, Aspen...)
- Consigli di amministrazione
- Fondazioni
- Relazioni personali chiave

## Potere Esercitato
- Decisioni documentate
- Influenza su policy
- Ruolo in momenti critici

## Citazioni Significative
[Dichiarazioni che rivelano visione e intenzioni]

## Controversie
[Critiche, scandali, conflitti di interesse]

## Fonti
```

### Template per EVENTI/SNODI

```markdown
# [Nome Evento] (Anno)

> [Perche' questo evento e' uno snodo di potere]

## Cosa Accadde
[Fatti essenziali]

## Chi Decise
[CRITICO: non "gli USA decisero" ma "chi specificamente"]
- Individui coinvolti
- Istituzioni coinvolte
- Processo decisionale

## Chi Beneficio'
[Analisi dei vincitori]

## Chi Perse
[Analisi dei perdenti]

## Connessioni
[Come questo evento si collega alla rete di potere]

## Conseguenze
[Effetti a breve e lungo termine]

## Fonti
```

### Template per FAMIGLIE/DINASTIE

```markdown
# Famiglia [Nome] ([Paese d'origine])

> [Tagline: essenza del potere dinastico esercitato]

## Dati della Dinastia

| Aspetto | Dettaglio |
|---------|-----------|
| **Origine** | [Paese, regione] |
| **Fondatore** | [Nome, periodo] |
| **Settore originario** | [Industria, finanza, terra...] |
| **Generazioni documentate** | [Numero] |
| **Patrimonio stimato** | [Attuale, se disponibile] |
| **Status attuale** | [Attiva/In declino/Estinta] |

---

## Albero Genealogico

[Usare diagramma ASCII o tabella per mostrare le generazioni]

```
FONDATORE (anni)
    |
+---+---+
|       |
FIGLIO1 FIGLIO2
    |
   ...
```

---

## Membri per Generazione

### 1a Generazione - Fondatori
| Nome | Anni | Ruolo | Potere Esercitato |
|------|------|-------|-------------------|
| | | | |

### 2a Generazione - Consolidamento
| Nome | Anni | Ruolo | Potere Esercitato |
|------|------|-------|-------------------|
| | | | |

### 3a Generazione - [Espansione/Transizione]
| Nome | Anni | Ruolo | Potere Esercitato |
|------|------|-------|-------------------|
| | | | |

### Generazione Attuale
| Nome | Anni | Ruolo | Status |
|------|------|-------|--------|
| | | | [Attivo/Ritirato/Deceduto] |

---

## Status dei Membri Viventi

| Nome | Eta' | Posizione Attuale | Ruolo nella Famiglia |
|------|------|-------------------|----------------------|
| | | | [Capo famiglia/Erede/Ramo cadetto] |

---

## Veicoli del Potere

### Aziende e Holding
| Entita' | Settore | Controllo | Fondazione |
|---------|---------|-----------|------------|
| | | | |

### Fondazioni e Filantropia
| Fondazione | Focus | AUM/Budget | Influenza |
|------------|-------|------------|-----------|
| | | | |

### Partecipazioni in Forum
| Forum | Membri della famiglia | Periodo |
|-------|----------------------|---------|
| Bilderberg | | |
| Trilaterale | | |
| CFR | | |
| WEF | | |

---

## Meccanismi di Successione

| Aspetto | Come Funziona |
|---------|---------------|
| **Selezione erede** | [Primogenitura/Merito/Designazione] |
| **Formazione eredi** | [Universita', apprendistato] |
| **Strutture legali** | [Trust, holding, fondazioni] |
| **Conflitti successori** | [Documentare se presenti] |

---

## Rete di Alleanze

### Matrimoni Strategici
| Membro | Coniuge | Famiglia del coniuge | Effetto |
|--------|---------|---------------------|---------|
| | | | |

### Alleanze con Altre Dinastie
| Famiglia | Tipo di Alleanza | Periodo |
|----------|------------------|---------|
| | | |

---

## Influenza Politica

| Paese | Tipo di Influenza | Periodo | Figure Chiave |
|-------|-------------------|---------|---------------|
| | [Diretta/Indiretta/Finanziamento] | | |

---

## Connessioni PowerLink

### Persone
[Link a schede individuali in /persone/]

### Istituzioni
[Link a schede in /istituzioni/]

### Eventi
[Link a snodi storici in /eventi/]

---

## Timeline Dinastica

| Anno | Evento | Generazione |
|------|--------|-------------|
| | | |

---

## Controversie e Critiche

| Tema | Periodo | Dettaglio |
|------|---------|-----------|
| | | |

---

## Domande Aperte

- [ ] [Domande sulla continuita' del potere]
- [ ] [Domande su eredi e successione]
- [ ] [Domande su patrimonio reale]

---

## Fonti

### Archivi familiari
### Biografie
### Giornalismo investigativo
### Documenti societari
```

---

## Metodologia di ricerca

### Quando cerchi informazioni su un nuovo soggetto:

1. **Identifica il tipo**: E' un'istituzione, una persona, un evento, o una famiglia/dinastia?

2. **Cerca le connessioni PRIMA dei dettagli**:
   - In quali forum appare? (Bilderberg, Trilaterale, WEF, Aspen, CFR...)
   - Con quali altre entita' del progetto e' collegato?
   - Chi sono i suoi mentori/protetti?
   - Quali board condivide con altri?

3. **Usa fonti multiple**:
   - Fonti ufficiali (siti istituzionali, documenti SEC, liste membri)
   - Wikipedia (come punto di partenza, mai come fonte unica)
   - Ricerca accademica (Harvard Law, LSE, Cambridge...)
   - Giornalismo investigativo
   - Fonti critiche (verificando sempre l'affidabilita')

4. **Privilegia i fatti verificabili**:
   - Date, nomi, ruoli, cifre
   - Documenti pubblici
   - Dichiarazioni registrate
   - Evita speculazioni non supportate

### Quando aggiorni un documento esistente:

1. **Leggi prima i documenti correlati** per capire le connessioni esistenti
2. **Cerca sovrapposizioni** con altri soggetti del progetto
3. **Aggiorna la sezione "Connessioni PowerLink"** in tutti i documenti coinvolti
4. **Mantieni le "Domande Aperte"** aggiornate

---

## Ricerca di connessioni

### Pattern da cercare sempre:

1. **Membership multipla**: Chi appare in 2+ forum/istituzioni?
2. **Percorsi formativi comuni**: Harvard, Yale, LSE, Oxford...
3. **Passaggi pubblico-privato**: Da governo a finanza e viceversa
4. **Ruoli in momenti di crisi**: Chi fu chiamato a "risolvere" le crisi?
5. **Relazioni mentor-protetto**: Chi ha lanciato chi?
6. **Sovrapposizioni nei board**: Chi siede insieme?
7. **Flussi filantropici**: Quali fondazioni finanziano cosa?

### Domande-guida per ogni soggetto:

- Chi lo ha formato/lanciato?
- Con chi condivide appartenenze?
- Quale potere specifico esercita?
- In quali decisioni cruciali e' stato coinvolto?
- Chi sono i suoi successori/eredi?

---

## Priorita' di ricerca

### Da fare

**Manutenzione:**
- [ ] Aggiungere connessioni mancanti tra documenti
- [ ] Verificare e aggiornare dati (AUM, membership, leadership)
- [ ] Popolare le sezioni "Domande Aperte"

**Persone da aggiungere:**
- [ ] Janet Yellen (Tesoro, ex-Fed)
- [ ] Mark Zuckerberg (Meta)
- [ ] Enrico Letta (PD, Sciences Po)
- [ ] Paul Volcker (ex-Fed Chair) — protetto Rockefeller
- [ ] Alan Greenspan (ex-Fed Chair)
- [ ] J. Pierpont Morgan (1837-1913) — architetto Fed, creo' US Steel/GE
- [ ] Nelson Rockefeller (1908-1979) — VP USA, Governatore NY
- [ ] George H.W. Bush (1924-2018) — Presidente, CIA Director
- [ ] George W. Bush (1946-) — Presidente, Guerra Iraq
- [ ] Jacob Rothschild (1936-2024) — RIT Capital, 4° Barone
- [ ] Sergio Marchionne (1952-2018) — CEO FCA, alleanza Fiat-Chrysler
- [ ] Sam Walton (1918-1992) — Fondatore Walmart

**Istituzioni da aggiungere:**
- [ ] SWIFT
- [ ] Carlyle Group — Private equity, connessioni Bush/Powell

**Eventi da aggiungere:**
- [ ] 1907 Panico bancario — J.P. Morgan salva il sistema, precursore Fed
- [ ] 1911 Antitrust Standard Oil — Spezzata in 34 compagnie
- [ ] 1933 Glass-Steagall Act — Separazione banche, fine era Morgan
- [ ] 1980 Scissione Rothschild UK — Jacob vs Evelyn, nascita RIT
- [ ] 2000 Fusione Chase-JPMorgan — Unione dinastie Morgan-Rockefeller
- [ ] 2021 Creazione Stellantis — FCA + PSA, John Elkann architetto

**Famiglie da aggiungere:**
- [ ] Koch (USA) — Petrolio, finanziamento politico conservatore
- [ ] Pritzker (USA) — Hyatt, politica Illinois, Penny Pritzker

---

## Tono e stile

### Da fare:
- Usare dati concreti e verificabili
- Citare le fonti
- Mostrare le connessioni documentate
- Ammettere quando non si sa qualcosa
- Distinguere fatti da interpretazioni
- Usare tabelle e schemi per chiarezza

### Da evitare:
- Toni sensazionalistici
- Affermazioni non supportate
- Complottismo semplificatorio ("loro controllano tutto")
- Demonizzazione moralistica
- Negare la complessita' (esistono conflitti interni alle elite)

### Principio guida:
> "Segui il potere, documenta le connessioni, lascia che i fatti parlino"

---

## Comandi utili

Quando lavori su questo progetto, puoi usare questi prompt:

- **"Analizza [nome] e trova le connessioni con le entita' esistenti"**
- **"Aggiorna [documento] con le informazioni piu' recenti"**
- **"Cerca sovrapposizioni tra [entita' A] e [entita' B]"**
- **"Crea una scheda per [nuova persona/istituzione]"**
- **"Quali domande aperte dovremmo investigare per [soggetto]?"**
- **"Trova i super-connettori che collegano [lista di entita']"**

---

## Note finali

### L'Italia come caso di studio
Il progetto ha un focus particolare sull'Italia come "laboratorio" della governance tecnocratica. Quando analizzi qualsiasi soggetto, cerca sempre:
- Connessioni con l'Italia
- Italiani nelle membership
- Ruolo nei governi "tecnici" italiani
- Presenza in Aspen Italia, Ispi, altri think tank italiani

### Aggiornamento continuo
I dati cambiano. Leadership, AUM, membership vanno verificati periodicamente. Includi sempre la data dell'ultimo aggiornamento in fondo ai documenti.

### Il confine metodologico
Questo progetto documenta connessioni reali e potere verificabile. Non e' un progetto complottista. La differenza:
- **Analisi del potere**: "Queste persone siedono insieme in questi forum e hanno preso queste decisioni"
- **Complottismo**: "Un gruppo segreto controlla tutto secondo un piano"

La realta' e' piu' complessa: esistono reti di potere, ma anche conflitti, errori, conseguenze non intenzionali.

---

*Ultimo aggiornamento: Dicembre 2025*
