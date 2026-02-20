# Open Source Power Map

> Da GNU a GitHub: come il software libero e' diventato infrastruttura globale controllata da Big Tech

## Executive Summary

| Metrica | Valore |
|---------|--------|
| **Periodo** | 1969-2026 |
| **Valore stimato ecosistema** | $8.8T (lavoro equivalente) |
| **Progetti attivi** | 200M+ (solo GitHub) |
| **Fondazione dominante** | Linux Foundation (700+ progetti) |
| **Chokepoint** | GitHub (Microsoft) ~90% hosting codice |
| **Pattern centrale** | Corporate capture di infrastruttura comunitaria |

---

## Background Storico

### 1969-1982: Le Radici — Unix e la Cultura della Condivisione del Codice

L'open source non nasce nel 1983 con GNU. Le sue radici sono a [Bell Labs](../docs/company/bell-labs.md), il laboratorio R&D di [AT&T](../docs/company/att.md) a Murray Hill, New Jersey, dove nel 1969 [Ken Thompson](../docs/persons/ken-thompson.md) e [Dennis Ritchie](../docs/persons/dennis-ritchie.md) creano Unix — il sistema operativo che definira' l'architettura di tutto il computing moderno.

**Il contesto**: Bell Labs aveva partecipato al progetto Multics (MIT/GE/Bell Labs, finanziato DARPA). Quando Bell Labs si ritira, Thompson riscrive un sistema piu' semplice su un PDP-7 di scarto. Ritchie crea il linguaggio C nel 1972 per riscrivere Unix in modo portabile. [Brian Kernighan](../docs/persons/brian-kernighan.md) lo battezza "Unix" (gioco di parole su Multics) e nel 1978 pubblica con Ritchie "The C Programming Language" (K&R) — il libro di programmazione piu' influente di sempre.

**Il paradosso AT&T**: Per un decreto antitrust del 1956, AT&T non puo' commercializzare software. Unix viene quindi distribuito quasi gratuitamente alle universita' — con il codice sorgente incluso. E' la prima comunita' di condivisione del codice su larga scala, il proto-open-source. UC Berkeley diventa il secondo polo: [Bill Joy](../docs/persons/bill-joy.md) crea BSD Unix con TCP/IP integrato (le fondamenta di Internet).

**L'infrastruttura invisibile**: Negli anni '80, [Rob Pike](../docs/persons/rob-pike.md) si unisce al gruppo. Con Thompson crea Plan 9 (1989), UTF-8 (1992, l'encoding che oggi copre >98% del web), e i concetti che confluiranno in Go. Kernighan pubblica i libri che diffondono la filosofia Unix nel mondo.

| Anno | Evento | Impatto |
|------|--------|---------|
| **1969** | Thompson e Ritchie creano Unix a Bell Labs | Base di Linux, macOS, Android, internet |
| **1972** | Ritchie crea il linguaggio C | Base di quasi tutti i sistemi operativi e database |
| **1977** | Kernighan co-crea AWK | Tool processing dati, precursore Perl/Python |
| **1978** | K&R pubblicano "The C Programming Language" | Forma generazioni di programmatori |
| **1979** | AT&T commercializza Unix (post-revisione antitrust) | Fine della distribuzione libera → genera la spinta per GNU |
| **1983** | Turing Award a Thompson e Ritchie | |

**Il link diretto con GNU**: Quando AT&T commercializza Unix nel 1979, chiudendo il codice sorgente, Stallman perde l'accesso al software che usava al MIT AI Lab. La frustrazione per la chiusura di Unix e' la motivazione diretta per il lancio del progetto GNU nel 1983. Senza Unix libero, nasce il movimento per il software libero. Il paradosso e' completo: Bell Labs crea la cultura della condivisione del codice, AT&T la distrugge, e la reazione genera il movimento che trasformera' il mondo.

### 1983-1997: L'Era del Software Libero

Il movimento nasce nel 1983 quando [Richard Stallman](../docs/persons/richard-stallman.md) lancia il progetto GNU al MIT AI Lab, seguito nel 1985 dalla fondazione della [Free Software Foundation](../docs/foundation/free-software-foundation.md) (FSF). La visione di Stallman e' filosofica: il software deve essere libero (free as in freedom) per garantire la liberta' degli utenti. GNU intende ricreare Unix senza il codice proprietario di AT&T.

Il momento trasformativo arriva nel 1991: [Linus Torvalds](../docs/persons/linus-torvalds.md), studente finlandese di 21 anni all'Universita' di Helsinki, pubblica il kernel Linux. La combinazione GNU/Linux crea il primo sistema operativo completamente libero, sfidando il duopolio Microsoft-Apple.

Nel 1997 [Eric S. Raymond](../docs/persons/eric-raymond.md) pubblica "The Cathedral and the Bazaar", il manifesto che teorizza il modello di sviluppo distribuito dell'open source.

### 1998: Netscape Libera il Codice — il Momento Fondativo

L'effetto di "The Cathedral and the Bazaar" e' immediato: nel gennaio 1998 [Netscape](../docs/companies/netscape.md) rilascia il codice sorgente del suo browser. E' l'evento che trasforma l'open source da filosofia a strategia industriale.

**Contesto**: [Jim Clark](../docs/persons/jim-clark.md) (ex professore Stanford, fondatore [Silicon Graphics](../docs/companies/silicon-graphics.md)) e [Marc Andreessen](../docs/persons/marc-andreessen.md) (creatore di NCSA Mosaic, 22 anni) avevano fondato Netscape nel 1994 con $4M di Clark. L'IPO del 1995 (azioni raddoppiate al primo giorno, market cap $2.2B) aveva lanciato la rivoluzione dot-com. Ma la browser war contro Microsoft Internet Explorer stava erodendo il dominio di Netscape: IE era gratuito e integrato in Windows.

**La decisione**: Il CEO [Jim Barksdale](../docs/persons/jim-barksdale.md) (ex COO FedEx, reclutato nel 1995) e il team decidono che l'unica via per sopravvivere e' rendere il browser open source. [Brendan Eich](../docs/persons/brendan-eich.md) — che nel maggio 1995 aveva creato JavaScript in 10 giorni — e [Mitchell Baker](../docs/persons/mitchell-baker.md) (legal dept) co-fondano mozilla.org per gestire il progetto.

**L'eredita'**: AOL acquisisce Netscape per $4.2B nel 1999, ma il codice liberato sopravvive. Da mozilla.org nasce la [Mozilla Foundation](../docs/foundation/mozilla-foundation.md) (2003), e da li' Firefox — l'unico browser non corporate che sopravvive fino a oggi.

**Netscape come incubatore di potere**: gli alumni di Netscape hanno fondato o guidato istituzioni chiave dell'ecosistema tech-open source:

| Alumni | A Netscape | Dopo |
|--------|-----------|------|
| [Marc Andreessen](../docs/persons/marc-andreessen.md) | Co-founder, VP Technology | [Andreessen Horowitz](../docs/private-equity/andreessen-horowitz.md) ($90B+ AUM), board [Meta](../docs/company/meta.md), advisor Trump/DOGE |
| [Ben Horowitz](../docs/persons/ben-horowitz.md) | PM, VP Directory | Co-founder [a16z](../docs/private-equity/andreessen-horowitz.md) |
| [Brendan Eich](../docs/persons/brendan-eich.md) | Creator JavaScript | Co-founder [Mozilla](../docs/foundation/mozilla-foundation.md), CEO [Brave Software](../docs/companies/brave-software.md) (browser anti-sorveglianza) |
| [Mitchell Baker](../docs/persons/mitchell-baker.md) | Legal dept | Fondatrice [Mozilla Foundation](../docs/foundation/mozilla-foundation.md), Chair 2003-2025 |
| [Jim Barksdale](../docs/persons/jim-barksdale.md) | CEO | Board [In-Q-Tel](../docs/private-equity/in-q-tel.md) (CIA venture fund), PFIAB (intelligence) |
| [Jim Clark](../docs/persons/jim-clark.md) | Co-founder, Chairman | Founder Healtheon/WebMD |

**Nota**: Clark ed Eich provenivano entrambi da [Silicon Graphics](../docs/companies/silicon-graphics.md), la workstation company fondata da Clark nel 1982 con i suoi studenti Stanford. Il percorso Stanford → SGI → Netscape → Mozilla illustra come un singolo nodo accademico possa generare catene di istituzioni tech.

### 1998: La Scissione Ideologica

Il 3 febbraio 1998, in una riunione strategica a Palo Alto, [Christine Peterson](../docs/persons/christine-peterson.md) del Foresight Institute conia il termine "open source" per sostituire "free software", ritenuto troppo ambiguo per il mondo business. Partecipano Raymond, Todd Anderson, John "maddog" Hall, Larry Augustin, Sam Ockman.

In aprile, [Tim O'Reilly](../docs/persons/tim-oreilly.md) organizza il primo Open Source Summit (originariamente "Freeware Summit") a Palo Alto. Presenti i leader dei principali progetti: Torvalds, Brian Behlendorf, Guido van Rossum, Larry Wall, Jamie Zawinski.

Raymond e [Bruce Perens](../docs/persons/bruce-perens.md) fondano la [Open Source Initiative](../docs/foundation/open-source-initiative.md) (OSI) per promuovere il nuovo brand. Perens adatta le Debian Free Software Guidelines nella Open Source Definition.

**La scissione e' strategica, non tecnica**: Stallman rifiuta il rebranding, vedendolo come una capitolazione alle corporations. Ha ragione su un punto: il termine "open source" apre la porta alla corporate capture che seguira'.

E' significativo che Perens, proveniente da 12 anni in Pixar (1987-1999), porti nel movimento una sensibilita' corporate che Raymond (autodidatta, mai in una grande azienda) non ha. Dopo aver lasciato OSI nel 1999, Perens entra in Hewlett-Packard come Senior Global Strategist per Linux e Open Source (2000-2002) — uno dei primi ruoli corporate dedicati all'open source.

### 1999-2007: Istituzionalizzazione

| Anno | Evento |
|------|--------|
| 1992 | Fondazione [S.u.S.E.](../docs/companies/suse.md) a Norimberga (Dyroff, Fehr, Steinbild, Mantel) — prima distribuzione Linux enterprise europea. [Ray Noorda](../docs/persons/ray-noorda.md) fonda il [Canopy Group](../docs/companies/canopy-group.md) (VC, Noorda Family Trust). |
| 1993 | Ago: [Ian Murdock](../docs/persons/ian-murdock.md) (studente alla [Purdue](../docs/university/purdue.md), 20 anni) fonda il [Debian Project](../docs/foundation/debian.md), la prima distribuzione Linux interamente comunitaria. Pubblica il Debian Manifesto (gen 1994). Il nome combina Debra (compagna) e Ian. [Bob Young](../docs/persons/bob-young.md) (Hamilton, Ontario) e [Marc Ewing](../docs/persons/marc-ewing.md) (ex IBM, [Carnegie Mellon](../docs/university/carnegie-mellon.md) CS 1992) fondano [Red Hat](../docs/companies/red-hat.md) a Durham, NC — Young vendeva software Linux per posta, Ewing aveva creato la sua distribuzione (nome dal suo cappello rosso da lacrosse della Cornell). |
| 1994 | Bob Young co-fonda Linux Journal, una delle prime riviste dedicate a Linux |
| 1995 | [Michael Widenius](../docs/persons/michael-widenius.md) (FIN, "Monty", dropout Helsinki Univ. of Technology) e [David Axmark](../docs/persons/david-axmark.md) (SWE, Uppsala 1980-84) fondano [MySQL AB](../docs/company/mysql-ab.md) a Uppsala con Allan Larsson. Modello dual licensing (GPL + commerciale) ispirato ad Aladdin Ghostscript. Il nome combina "My" (figlia di Widenius) e SQL |
| 1995 | Canopy Group finanzia Caldera Systems (distribuzione Linux commerciale). Novell vende asset Unix a Santa Cruz Operation (ma mantiene i copyright) |
| 1996 | Caldera (Noorda) lancia causa DR-DOS vs Microsoft per pratiche anti-competitive |
| 1996 | [Bruce Perens](../docs/persons/bruce-perens.md) diventa DPL di [Debian](../docs/foundation/debian.md) (1996-1997), introduce il Debian Social Contract e le Debian Free Software Guidelines (DFSG) — base della futura Open Source Definition |
| 1997 | Fondazione di [Software in the Public Interest](../docs/foundation/spi.md) (SPI) da Murdock e Perens — umbrella legale per Debian. [Miguel de Icaza](../docs/persons/miguel-de-icaza.md) e Federico Mena lanciano il progetto GNOME come desktop environment libero. [Eric Schmidt](../docs/persons/eric-schmidt.md) diventa CEO di [Novell](../docs/companies/novell.md) |
| 1999 | De Icaza e [Nat Friedman](../docs/persons/nat-friedman.md) (MIT CS 1999) fondano [Ximian](../docs/companies/ximian.md) (Helix Code) per commercializzare GNOME. Fondazione [Apache Software Foundation](../docs/foundation/apache-foundation.md) ([Brian Behlendorf](../docs/persons/brian-behlendorf.md) co-fondatore) |
| 2000 | De Icaza e Friedman co-fondano la [GNOME Foundation](../docs/foundation/gnome-foundation.md) con Compaq, Eazel, IBM, Red Hat, Sun, VA Linux. Friedman primo Chairman |
| 2000 | [Sun Microsystems](../docs/company/sun-microsystems.md) open-source OpenOffice.org (da StarOffice, acquisita 1999) e NetBeans — primo rilascio massivo di software proprietario come open source da un'azienda Fortune 500 |
| 2000 | Settlement causa DR-DOS: Microsoft paga $275M a Caldera. Caldera acquista asset Unix da Santa Cruz Operation → diventa Caldera International |
| 2001 | Schmidt lascia Novell per Google. De Icaza lancia il Mono Project (implementazione open source di .NET su Linux) — controverso per dipendenza da tecnologia Microsoft |
| 2002 | Caldera International rinominata [The SCO Group](../docs/companies/sco-group.md) (Darl McBride CEO, Ralph Yarro Chairman). Pivot da distribuzione Linux a monetizzazione IP Unix |
| 2003 | Mar: SCO causa IBM per $1B (poi $5B), sostenendo violazione IP Unix in Linux. Crea divisione SCOsource per vendere licenze Unix a utenti Linux. Novell controcausa: possiede ancora i copyright Unix. Microsoft acquista licenze SCOsource. Novell acquisisce [Ximian](../docs/companies/ximian.md) (ago) e [SUSE](../docs/companies/suse.md) (nov) — la piu' grande azienda networking USA compra la principale distribuzione Linux europea. De Icaza VP Developer Platform, Friedman VP R&D. Fondazione [Mozilla Foundation](../docs/foundation/mozilla-foundation.md) ([Mitchell Baker](../docs/persons/mitchell-baker.md), [Mitch Kapor](../docs/persons/mitch-kapor.md) founding chair) |
| 1998 | Ratifica della Debian Constitution (2 dic) — governance democratica formalizzata: DPL eletto annualmente |
| 1999 | [Red Hat](../docs/companies/red-hat.md) IPO su NASDAQ (11 agosto). [Bob Young](../docs/persons/bob-young.md) lascia la carica di CEO. Primo modello di successo commerciale open source |
| 2000 | Marc Ewing lascia Red Hat dopo l'IPO. Si ritira a Jackson, Wyoming |
| 2003 | Red Hat Enterprise Linux (RHEL) sostituisce Red Hat Linux: pivot al modello subscription enterprise. Red Hat diventa la prima azienda open source a superare $1B di revenue (2012) |
| 2001 | [Marten Mickos](../docs/persons/marten-mickos.md) (FIN-USA, MSc Aalto) diventa CEO di [MySQL AB](../docs/company/mysql-ab.md) — professionalizza l'azienda, guida i round VC. Primo round scandinavo |
| 2003 | MySQL AB Series B: [Benchmark Capital](../docs/private-equity/benchmark-capital.md) e [Index Ventures](../docs/private-equity/index-ventures.md) (~$20M). MySQL diventa il database piu' diffuso nel web (stack LAMP) |
| 2006 | MySQL AB Series C: [IVP](../docs/private-equity/institutional-venture-partners.md) lead, [Intel Capital](../docs/private-equity/intel-capital.md), [Red Hat](../docs/companies/red-hat.md), SAP Ventures (~$18.5M) |
| 2004 | IBM trasferisce Eclipse a fondazione indipendente: nasce la [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) con [Mike Milinkovich](../docs/persons/mike-milinkovich.md) (ex Oracle VP) come primo Executive Director. [Mark Shuttleworth](../docs/persons/mark-shuttleworth.md) (ZAF-GBR, fondatore [Canonical](../docs/companies/canonical.md), ex Thawte venduta a VeriSign per $575M, secondo turista spaziale 2002) recluta sviluppatori [Debian](../docs/foundation/debian.md) e lancia Ubuntu — finanziando interamente l'azienda senza investitori esterni |
| 2005 | Torvalds crea Git, che rivoluziona la collaborazione. Fondazione Open Invention Network (patent pool difensivo pro-Linux, catalizzato dalla minaccia SCO) |
| 2005 | [Sun Microsystems](../docs/company/sun-microsystems.md) open-source OpenSolaris (kernel sotto CDDL), ZFS (file system) e GlassFish (application server) |
| 2006 | Sun open-source Java sotto GPL — il linguaggio con ~9M sviluppatori diventa libero. Un report UE indica Sun come il piu' grande contributore corporate all'open source al mondo, superando i cinque successivi contributori commerciali combinati |
| 2006 | Accordo Microsoft-Novell: patent covenant e interoperability per SUSE Linux. Microsoft riconosce commercialmente Linux per la prima volta. $300M+ a Novell |
| 2006 | Ray Noorda muore (9 ottobre). Accordo Microsoft-Novell |
| 2007 | Giudice Kimball: Novell possiede i copyright Unix → colpo fatale a SCO. SCO Group Chapter 11 bankruptcy (set). Delisted da NASDAQ (dic). Fusione OSDL + Free Standards Group = [Linux Foundation](../docs/foundation/linux-foundation.md), con [Jim Zemlin](../docs/persons/jim-zemlin.md) executive director |

---

## Struttura Attuale del Potere

### Le Tre Fondazioni

| Fondazione | Fondazione | Revenue | Progetti | Modello |
|------------|-----------|---------|----------|---------|
| [Linux Foundation](../docs/foundation/linux-foundation.md) | 2007 | $311M proiettati 2025 (42.7% membership) | 700+ ([CNCF](../docs/foundation/cncf.md), [OpenSSF](../docs/foundation/openssf.md), OpenTofu, Valkey) | Corporate-led, umbrella |
| [Apache Software Foundation](../docs/foundation/apache-foundation.md) | 1999 | ~$5M/anno | 350+ | Meritocratico, volunteer-driven. Fondatori: Fielding (primo Chairman, inventore REST), Jagielski (board dal 1999, unico fondatore ancora in carica), Laurie (Apache-SSL → Google Security), Behlendorf (→ WEF → OSTP → LF) |
| [Free Software Foundation](../docs/foundation/free-software-foundation.md) | 1985 | ~$1.5M/anno | GNU, licenze GPL | Ideologico, activist. Governance riformata 2021-2024: union seat, board partecipativo, Code of Ethics |
| [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) | 2004 | ~$50M+ | 400+ (Jakarta EE, Eclipse IDE, SDV, Oniro, Theia, Adoptium) | Corporate-led, AISBL belga. Ponte Europa-Cina via Oniro/OpenHarmony |

### Eclipse Foundation: la Quarta Fondazione (e il Polo Europeo)

La [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) (2004, Bruxelles) e' la fondazione open source che il report tendeva a sottovalutare — ma la sua rilevanza per DeepScript e' significativa. Nata come spin-off di [IBM](../docs/companies/ibm.md) (che creo' Eclipse IDE nel 2001), si e' trasformata sotto la guida ventennale di [Mike Milinkovich](../docs/persons/mike-milinkovich.md) (CAN, Executive Director dal 2004) in un polo europeo di governance open source industriale.

**Il percorso Milinkovich** e' emblematico della generazione pre-Linux Foundation: Bell Northern Research (1983) → Object Technology International → IBM VisualAge (acquisizione, 1996) → Oracle VP (2002) → Eclipse Foundation ED (2004). Il filo conduttore e' l'IDE e la piattaforma Java enterprise — lo stesso terreno che genera Jakarta EE (ex Java EE, trasferita da [Oracle](../docs/company/oracle.md) nel 2017). Milinkovich e' stato anche Director e Treasurer della [OSI](../docs/foundation/open-source-initiative.md) (2012-2018), collegando le due istituzioni.

**Strategic Members** (2025): [IBM](../docs/companies/ibm.md), [Microsoft](../docs/company/microsoft.md), [Oracle](../docs/company/oracle.md), [Huawei](../docs/companies/huawei.md), [Red Hat](../docs/companies/red-hat.md), [SAP](../docs/company/sap.md), [Bosch](../docs/company/bosch.md), ESA, Fujitsu, Ericsson, Mercedes-Benz, Fraunhofer, CEA LIST. Il board 2025 riflette la forte componente europea (6 membri su 21 da Germania, Francia, organizzazioni europee) e la presenza industriale (automotive, aerospace, telecom) che la Linux Foundation non ha con la stessa intensita'.

**Tre elementi chiave per DeepScript:**

1. **La ri-incorporazione europea (2020)**: Eclipse si e' ri-incorporata come AISBL (diritto belga) a Bruxelles, segnalando una strategia di autonomia dagli USA. E' l'unica grande fondazione open source con sede legale e operativa nell'UE — la Linux Foundation Europe (2022) e' solo una filiale.

2. **Il ponte Cina-Europa via Oniro**: Il progetto Oniro collega Eclipse a [OpenAtom Foundation](../docs/foundation/openatom-foundation.md)/Huawei per un OS open source IoT basato su OpenHarmony. E' il canale piu' diretto di collaborazione tecnica open source tra Europa e Cina — in un contesto di crescente decoupling.

3. **Eclipse SDV (Software-Defined Vehicle)**: Il working group SDV con Bosch, Mercedes-Benz e BMW posiziona Eclipse come standard de facto per il software automotive europeo — un settore dove la Linux Foundation (via AGL/Automotive Grade Linux) e' meno radicata in Europa.

**Eclipse vs Linux Foundation**: Se la LF e' il modello "umbrella corporate americana" ($311M, 700+ progetti), Eclipse e' il modello "fondazione industriale europea" (400+ progetti, forte in Java enterprise, automotive, IoT). La sovrapposizione cresce, ma Eclipse mantiene una nicchia distinta — e una governance piu' europea.

La Linux Foundation e' la vincitrice indiscussa: un modello "foundation of foundations" dove le corporations pagano membership fees per governare i progetti. Nata nel 2007 dalla fusione di OSDL (fondato 2000 da IBM, HP, Intel) e Free Standards Group (Zemlin ED dal 2004), la LF ha 1000+ membri. I Platinum ($500K/anno, seggio board garantito) includono AT&T, Cisco, Fujitsu, [Google](../docs/companies/google.md), Hitachi, [Huawei](../docs/companies/huawei.md), [IBM](../docs/companies/ibm.md), [Intel](../docs/companies/intel.md), [Meta](../docs/companies/meta.md), [Microsoft](../docs/companies/microsoft.md), NEC, [Oracle](../docs/companies/oracle.md), [Qualcomm](../docs/companies/qualcomm.md), [Samsung](../docs/companies/samsung.md), Tencent, VMware. Sub-foundations: [CNCF](../docs/foundation/cncf.md) (Kubernetes, 2015, 200+ progetti, 244K+ contributori in 193 paesi — leadership: [Dan Kohn](../docs/persons/dan-kohn.md) founding ED morto 2020 → [Priyanka Sharma](../docs/persons/priyanka-sharma.md) GM/ED 2020-2025 → [Jonathan Bryce](../docs/persons/jonathan-bryce.md) ED dal 2025, [Chris Aniszczyk](../docs/persons/chris-aniszczyk.md) CTO dal 2015; platinum founding members: Google, Red Hat, IBM, Huawei, Intel, Cisco, VMware, Docker — Kubernetes donato da Google come seed technology nel 2015), [OpenInfra Foundation](../docs/foundation/openinfra-foundation.md) (member foundation dal marzo 2025, governa [OpenStack](../docs/foundation/openstack.md), Kata Containers, StarlingX, Zuul), [Hyperledger/LFDT](../docs/foundation/hyperledger.md) (blockchain, 2015), [OpenSSF](../docs/foundation/openssf.md) (sicurezza supply chain, 2020, nata dalla fusione di Core Infrastructure Initiative + OSSC + JOSSI — leadership: [Brian Behlendorf](../docs/persons/brian-behlendorf.md) primo GM 2021-2023 poi CTO → [Omkhar Arasaratnam](../docs/persons/omkhar-arasaratnam.md) GM dal 2023, ex security leadership Google e JPMorgan Chase; founding members: GitHub, Google, IBM, JPMorgan Chase, Microsoft, NCC Group, OWASP, Red Hat — catalizzata dalla vulnerabilita' Log4Shell dic 2021 e dai White House OSS Security Summits gen/mag 2022 dove 37 aziende hanno pledged $30M), LF AI & Data, LF Energy, LF Networking, RISC-V International. Solo il 15% del codice del kernel Linux e' ancora prodotto da volontari. La LF e' stata criticata per aver ridotto la spesa effettiva su Linux a minimi storici mentre si espandeva in AI, cloud e blockchain.

La [Open Source Initiative](../docs/foundation/open-source-initiative.md), l'ente che definisce cosa sia "open source", e' ~95% finanziata da corporations secondo i documenti IRS. L'OSI e' in crisi profonda dal 2024: la pubblicazione della Open Source AI Definition 1.0 (OSAID), che non richiede la pubblicazione dei dati di training AI, ha spaccato la community. Il primo ED Stefano Maffulli si e' dimesso nel settembre 2025, le elezioni board 2025 sono state contestate per irregolarita', e il board ha sospeso le elezioni 2026 per "ridisegnare il processo". Deb Bryant (ex OSPO Red Hat, ex Deputy CIO Oregon) guida come interim ED, affiancata dal Vice Chair Thierry Carrez (GM OpenInfra) e dal board director Carlo Piana (avvocato italiano, legale del caso antitrust Microsoft-UE via FSFE). Jim Zemlin (ED della Linux Foundation) percepisce $1.15M/anno.

### GNOME Foundation: il Desktop Libero e i Suoi Fondatori

La [GNOME Foundation](../docs/foundation/gnome-foundation.md) (2000) governa il desktop environment libero dominante per Linux. Fondata formalmente nel 2001 da Compaq, Eazel, Helix Code (Ximian), IBM, Red Hat, Sun Microsystems e VA Linux Systems, il progetto GNOME era stato lanciato nel 1997 da [Miguel de Icaza](../docs/persons/miguel-de-icaza.md) come alternativa libera a KDE.

La fondazione e' il caso piu' puro della traiettoria hacker → imprenditore → corporate:
- **De Icaza** (UNAM dropout, MEX): GNOME → Mono (.NET su Linux, controverso) → Xamarin → Microsoft Distinguished Engineer → Xibbon (game dev)
- **Friedman** (MIT CS 1999, USA): GNOME Foundation Chairman → Ximian/Xamarin → Microsoft CVP → GitHub CEO → NFDG ($1.1B AI VC) → Meta Superintelligence Labs VP

Advisory Board attuale: Red Hat (top contributor, ~17% code), Google, Canonical, SUSE, Debian. La GNOME Foundation attraversa una crisi: turnover di Executive Director e fundraising insufficiente nel 2024, riflettendo il problema strutturale di dipendenza corporate che affligge l'intero ecosistema.

### Le Distribuzioni Linux: il Cuore Commerciale

Le distribuzioni Linux sono il punto dove il codice comunitario diventa prodotto commerciale — e dove si concentra il potere economico dell'open source.

**[Red Hat](../docs/companies/red-hat.md)** (1993): fondata da [Bob Young](../docs/persons/bob-young.md) (CAN-USA, BA History, U. Toronto) e [Marc Ewing](../docs/persons/marc-ewing.md) (USA, BS CS Carnegie Mellon 1992, ex IBM) in un appartamento a Durham, NC. Young vendeva software Linux per posta, Ewing aveva creato la sua distribuzione. IPO NASDAQ 1999. Prima azienda open source a superare $1B di revenue (2012). Acquisita da [IBM](../docs/companies/ibm.md) per $34B nel 2019 — la piu' grande acquisizione software della storia al momento. CEO attuale: Matt Hicks (dal 2022). Il percorso startup-in-un-closet → IPO → $34B illustra la traiettoria completa della cattura corporate dell'open source.

**[Debian](../docs/foundation/debian.md)** (1993): fondata da [Ian Murdock](../docs/persons/ian-murdock.md) (USA, BS CS Purdue 1996, morto 2015) come prima distribuzione Linux interamente comunitaria. Governance democratica (DPL eletto annualmente, Constitution ratificata 1998). [Bruce Perens](../docs/persons/bruce-perens.md) (DPL 1996-1997) introduce il Debian Social Contract e le DFSG, che diventano la base della Open Source Definition. [Software in the Public Interest](../docs/foundation/spi.md) (SPI, 1997) come umbrella legale. Debian resta il modello di governance non-corporate piu' duraturo — ma il suo codice alimenta Ubuntu (Canonical) e decine di derivate commerciali.

**[Canonical](../docs/companies/canonical.md)** (2004): fondata e interamente posseduta da [Mark Shuttleworth](../docs/persons/mark-shuttleworth.md) (ZAF-GBR, BSc Finance UCT). Shuttleworth aveva venduto Thawte a VeriSign per $575M (1999) e volato sulla ISS come secondo turista spaziale ($20M, 2002). Ha reclutato sviluppatori Debian per creare Ubuntu. Revenue $292M (2024), mai quotata in borsa nonostante rumors dal 2017. Nessun investitore esterno — caso raro di finanziamento filantropico-imprenditoriale nell'open source.

**Il pattern delle distribuzioni**:
- **Debian** → governance comunitaria, nessun profitto, alimenta l'ecosistema
- **Red Hat** → modello subscription enterprise, acquisita da IBM ($34B)
- **Ubuntu/Canonical** → finanziata da un singolo miliardario, ponte tra community e enterprise
- **SUSE** → catena PE ventennale (Novell → Attachmate → Micro Focus → EQT)

Il flusso e' sempre lo stesso: codice comunitario (Debian, kernel Linux) → distribuzione commerciale → acquisizione corporate/PE → estrazione di valore. L'unica variante e' Canonical, dove il proprietario unico impedisce (per ora) la cattura finanziaria.

### GitHub: Il Chokepoint

[GitHub](../docs/companies/github.md), acquisita da [Microsoft](../docs/company/microsoft.md) per $7.5B nel 2018, ospita ~90% del codice open source mondiale (150M+ sviluppatori, 1B+ repository, $2B ARR nel 2024).

**I fondatori**: GitHub nasce nel 2008 da quattro sviluppatori autodidatti/dropout — [Tom Preston-Werner](../docs/persons/tom-preston-werner.md) (Harvey Mudd dropout, creatore di Jekyll e Semantic Versioning), [Chris Wanstrath](../docs/persons/chris-wanstrath.md) (U. Cincinnati dropout per CNET), [P.J. Hyett](../docs/persons/pj-hyett.md) (BS CS North Central College, CNET) e [Scott Chacon](../docs/persons/scott-chacon.md). Wanstrath e Hyett gestivano una consulenza Ruby on Rails prima di fondare GitHub. Preston-Werner lascia da CEO nel 2014 dopo accuse di harassment; Wanstrath guida l'azienda fino alla vendita a Microsoft.

**La diaspora post-$7.5B**: I fondatori hanno disperso il capitale in direzioni significative per DeepScript:

| Fondatore | Post-GitHub | Rilevanza |
|-----------|-------------|-----------|
| [Tom Preston-Werner](../docs/persons/tom-preston-werner.md) | [Preston-Werner Ventures](../docs/private-equity/preston-werner-ventures.md) ($100M Fund I, 2025; 175+ angel investments tra cui Stripe, Cursor, Netlify, Supabase) | Pattern **open source founder → VC**: chi ha creato l'infrastruttura finanzia la prossima generazione |
| [Chris Wanstrath](../docs/persons/chris-wanstrath.md) | Microsoft Technical Fellow + co-fondatore Ladybird Browser Initiative (2024, con Andreas Kling) | Browser indipendente no-ads/no-corporate deals — **parallelo a Brave** (Eich), altro tentativo di usare l'open source contro il modello di sorveglianza |
| [Nat Friedman](../docs/persons/nat-friedman.md) | NFDG ($1.1B AI VC) → VP Meta Superintelligence Labs | Pattern **open source → AI**: vedi sezione 16 |
| [Thomas Dohmke](../docs/persons/thomas-dohmke.md) | [Entire](../docs/companies/entire.md) ($60M seed, $300M valuation, 2026) | Agentic AI coding platform. Investitori: [Felicis](../docs/private-equity/felicis.md) (lead), [Madrona](../docs/private-equity/madrona.md), [M12](../docs/private-equity/m12.md) (Microsoft Ventures), [Basis Set](../docs/private-equity/basis-set.md). Angel: [Jerry Yang](../docs/persons/jerry-yang.md) (Yahoo/Stanford/CFR), [Garry Tan](../docs/persons/garry-tan.md) (Y Combinator), Olivier Pomel (Datadog) |

**CEO post-acquisizione**:

| CEO | Periodo | Background |
|-----|---------|------------|
| [Nat Friedman](../docs/persons/nat-friedman.md) | 2018-2021 | MIT CS 1999, co-fondatore Ximian/GNOME Foundation/Xamarin. Post: NFDG → Meta MSL |
| [Thomas Dohmke](../docs/persons/thomas-dohmke.md) | 2021-2025 | DEU. PhD Mechanical Engineering. Co-fondatore HockeyApp (acquisita da Microsoft 2015). Ha lanciato Copilot (20M+ utenti) |

**Agosto 2025**: Dohmke lascia e Microsoft non nomina un successore. GitHub viene integrata nella divisione CoreAI, senza CEO autonomo — la piattaforma perde la sua ultima parvenza di indipendenza per diventare un componente interno della strategia AI di Microsoft.

**Il percorso Friedman** e' emblematico della convergenza open source → AI: da hacker GNOME/Linux al MIT → co-founder Ximian/Xamarin → CEO GitHub sotto Microsoft → venture capitalist AI con NFDG ($1.1B, portfolio: Perplexity, ElevenLabs, SSI) → VP di Meta Superintelligence Labs. Il suo partner [Alexandr Wang](../docs/persons/alexandr-wang.md) (MIT dropout, fondatore [Scale AI](../docs/companies/scale-ai.md), contratti Pentagono) e' diventato Chief AI Officer di Meta — il piu' giovane miliardario self-made al mondo a 24 anni. Meta ha acquisito il 49% di Scale AI per ~$14.3B. Il pattern aperto da Friedman e Wang nel 2025 — open source credentials → AI venture capital → big tech superintelligence labs — rappresenta il nuovo fronte della conversione del capitale tecnico open source in potere AI.

GitHub Copilot, lanciato nel 2021, rappresenta il caso piu' controverso di estrazione di valore: un'AI addestrata sul codice open source della community, venduta come servizio premium da Microsoft. La class action Doe v. GitHub (2022) contesta la violazione delle licenze open source.

### GitLab: l'Alternativa Open-Core dalla Periferia

Se GitHub e' il chokepoint, [GitLab](../docs/companies/gitlab.md) (NASDAQ: GTLB) e' l'unica alternativa credibile — e il suo percorso illustra un pattern diverso ma parallelo di convergenza tra open source e grande finanza.

**Le origini periferiche**: Nel 2011 [Dmytro Zaporozhets](../docs/persons/dmitriy-zaporozhets.md) (UKR, BSc Automotive Engineering, Kharkiv), sviluppatore in una societa' IT a Kharkiv, crea GitLab come progetto open-source perche' trova GitHub scomodo. Lavora da una casa senza acqua corrente, insieme a Valery Sizov. Per 18 mesi resta un hobby. Nel 2012 [Sid Sijbrandij](../docs/persons/sid-sijbrandij.md) (NLD, MSc Management Science, University of Twente), che in precedenza costruiva sottomarini ricreativi per U-Boat Worx e lavorava al Ministero della Giustizia olandese, scopre il progetto e propone di commercializzarlo. La divisione e' netta: Zaporozhets al tech, Sijbrandij al business.

**Il percorso finanziario**: GitLab Inc. (2014) attraversa la classica escalation di capitale:

| Round | Anno | Lead | Importo |
|-------|------|------|---------|
| Seed | 2015 | [Y Combinator](../docs/private-equity/y-combinator.md) | Winter 2015 batch |
| Series A | 2015 | [Khosla Ventures](../docs/private-equity/khosla-ventures.md) | $4M |
| Series C | 2016 | [GV (Google Ventures)](../docs/companies/google-ventures.md) | $20M |
| Series D | 2018 | [ICONIQ Capital](../docs/companies/iconiq-capital.md) | $100M |
| Series E | 2019 | [Goldman Sachs](../docs/bank/goldman-sachs.md) + ICONIQ | $268M (val. $2.7B) |
| IPO | 2021 | NASDAQ (GTLB) | ~$650M (val. ~$11B) |

**La struttura di controllo**: Dual-class stock (Class B = 10x voting). Post-IPO, gli asset manager istituzionali entrano: [Vanguard](../docs/asset-manager/vanguard.md) (~8.4%), GV (~7.15% shares ma 22.2% voting power), [ICONIQ](../docs/companies/iconiq-capital.md) (~5.51%), [BlackRock](../docs/asset-manager/blackrock.md) (~5.39%). Il pattern e' identico a GitHub pre-acquisizione: capitale VC → IPO → Big Three come azionisti dominanti.

**La transizione**: Zaporozhets, dopo 10 anni esatti, lascia GitLab nel novembre 2021 — presente al NASDAQ per l'IPO, poi addio. GitLab istituisce il "DZ Award" in suo onore. Nel 2023 Sijbrandij rivela una diagnosi di osteosarcoma; nel dicembre 2024 cede il ruolo di CEO a [Bill Staples](../docs/persons/bill-staples.md) (ex New Relic), diventando Executive Chair.

**L'ecosistema Sijbrandij**: Parallelamente a GitLab, Sijbrandij fonda [Open Core Ventures](../docs/private-equity/open-core-ventures.md) (2020), un fondo VC dedicato esclusivamente a startup open-core — il modello che ha reso GitLab un unicorno. Fonda anche la Sijbrandij Foundation (2022, filantropia: cancro, energia solare, citta') e Kilo Code (2025). Il pattern e' lo stesso di Preston-Werner (GitHub → PWV): **open source founder → VC che finanzia la prossima generazione**.

**GitLab vs GitHub — due modelli di cattura**:

| | GitHub | GitLab |
|---|--------|--------|
| **Fondazione** | 2008, San Francisco | 2011, Kharkiv (UKR) |
| **Modello** | Closed source → freemium | Open-core (CE MIT + EE) |
| **Acquisizione** | Microsoft $7.5B (2018) | IPO indipendente (2021) |
| **Controllo** | Microsoft 100% | Dual-class, founder chair |
| **Revenue** | $2B ARR (2024) | ~$634M (FY2024) |
| **Remote** | Uffici + remote | 100% remote-first dal giorno 1 |
| **CEO 2025** | Nessuno (integrata in CoreAI) | Bill Staples (CEO autonomo) |

GitLab rappresenta il contromodello: open-core, remote-first, IPO indipendente, dual-class per proteggere il controllo dei founder. Ma la struttura azionaria post-IPO (Vanguard, BlackRock, Goldman Sachs, ICONIQ) mostra che anche l'alternativa "indipendente" finisce nel portafoglio degli stessi attori finanziari che possiedono Microsoft.

**Nota**: [Matt Mullenweg](../docs/persons/matt-mullenweg.md) (Automattic/WordPress) ha investito in GitLab tramite [Audrey Capital](../docs/private-equity/audrey-capital.md) — uno dei pochi crosslink diretti tra le due maggiori piattaforme open source indipendenti.

### OpenStack e OpenInfra: dal Cloud Pubblico alla Consolidazione

[OpenStack](../docs/foundation/openstack.md), lanciato nel 2010 come progetto congiunto di [Rackspace](../docs/companies/rackspace.md) e NASA, e' la piattaforma open source per cloud computing IaaS piu' diffusa al mondo. Nato dalla fusione del codice NASA Nebula (compute) e Rackspace Cloud Files (storage), il progetto ha dimostrato che l'open source poteva sfidare AWS nel cloud infrastrutturale.

**Il ruolo di Rackspace**: Fondata nel 1996 da Richard Yoo (dropout Trinity University), capitalizzata da Graham Weston ($1.25M seed, 1998), finanziata da Sequoia Capital (2000), IPO al NYSE nel 2008. [Jonathan Bryce](../docs/persons/jonathan-bryce.md), web developer Rackspace dal 2000, co-crea con Todd Morey la piattaforma Rackspace Cloud (Mosso) che diventa il nucleo di OpenStack. Nel 2016 [Apollo Global Management](../docs/private-equity/apollo-global.md) acquisisce Rackspace per $4.3B (take private), re-IPO al Nasdaq nel 2020 con Apollo che mantiene ~65%. Il percorso startup → IPO → private equity → re-IPO e' un caso di studio sulla finanziarizzazione dell'infrastruttura open source.

**La governance**: La OpenStack Foundation (2012) — rinominata [OpenInfra Foundation](../docs/foundation/openinfra-foundation.md) nel 2020 — ha governato il progetto con un modello a tre terzi: Platinum Members (nominati), Gold Members (eletti), Individual Members (eletti). Platinum Members 2025: Ant Group, Cachengo, Ericsson, Huawei, Okestro, Rackspace, Wind River. Oltre a OpenStack, la foundation governa Kata Containers (container security), StarlingX (edge), Zuul (CI/CD).

**La consolidazione 2025**: Nel marzo 2025, OpenInfra Foundation annuncia l'ingresso nella Linux Foundation come member foundation. Bryce viene nominato ED Cloud & Infrastructure della LF e contemporaneamente ED della CNCF (sostituendo [Priyanka Sharma](../docs/persons/priyanka-sharma.md), Stanford CS 2009, ex Google/LightStep/GitLab, GM/ED CNCF 2020-2025). La mossa unifica sotto un unico ombrello le due anime del cloud open source: VM/bare metal (OpenStack) e containers/Kubernetes (CNCF). Bryce mantiene anche il ruolo in OpenInfra — una concentrazione di potere infrastrutturale senza precedenti.

**Il pattern Rackspace → OpenStack → OpenInfra → Linux Foundation** chiude un cerchio: un progetto nato come alternativa open source ad AWS finisce governato dalla stessa mega-foundation che governa Kubernetes, Hyperledger e 700+ altri progetti — con il suo fondatore (Bryce) che passa da un'azienda acquisita da Apollo a controllare la governance cloud di tutta la Linux Foundation.

### Blockchain Open Source: il Ponte Finanza-Tech

**Nota tecnica**: L'intera infrastruttura blockchain si basa sui Merkle Trees, inventati da [Ralph Merkle](../docs/persons/ralph-merkle.md) (board [Foresight Institute](../docs/think-tank/foresight-institute.md)) negli anni '70 — la stessa struttura dati che Torvalds usa in Git. Il co-inventore della crittografia a chiave pubblica e' dunque il nonno tecnico sia del version control che della blockchain.

[Hyperledger](../docs/foundation/hyperledger.md) (2015, rebrand [LF Decentralized Trust](../docs/foundation/hyperledger.md) nel 2024) rappresenta il caso piu' chiaro di corporate capture nel blockchain: una sub-foundation della Linux Foundation con 30 founding members che includono le principali banche e tech companies globali ([IBM](../docs/companies/ibm.md), [JP Morgan](../docs/bank/jp-morgan.md), [Accenture](../docs/companies/accenture.md), [SWIFT](../docs/agency/swift.md), [Wells Fargo](../docs/bank/wells-fargo.md), [Deutsche Boerse](../docs/companies/deutsche-boerse.md), [ABN AMRO](../docs/bank/abn-amro.md), [BNY Mellon](../docs/bank/bny-mellon.md), [State Street](../docs/asset-manager/state-street.md)). IBM ha dominato con Fabric, il framework blockchain enterprise piu' diffuso.

[ConsenSys](../docs/companies/consensys.md), fondata nel 2015 da [Joseph Lubin](../docs/persons/joseph-lubin.md) (co-fondatore Ethereum, ex-VP Goldman Sachs, Princeton BSE), e' il braccio commerciale di Ethereum. Controlla MetaMask (100M+ utenti, wallet dominante) e Infura (gateway critico per sviluppatori Ethereum). La traiettoria e' significativa per DeepScript:

| Fase | Dettaglio |
|------|-----------|
| **Goldman Sachs** | Lubin VP Technology, Private Wealth Management |
| **Ethereum** | Co-fondatore 2014 con [Vitalik Buterin](../docs/persons/vitalik-buterin.md) |
| **ConsenSys** | Fondatore 2015, valutazione $7B (2022) |
| **Investitori** | [JP Morgan](../docs/bank/jp-morgan.md), [Microsoft](../docs/companies/microsoft.md), [Mastercard](../docs/companies/mastercard.md), [UBS](../docs/bank/ubs.md) |
| **IPO 2025** | Con JPMorgan e Goldman Sachs come advisor |
| **SEC** | Accusata 2024 per MetaMask Staking (securities non registrate) |

Il percorso Goldman Sachs → Ethereum → ConsenSys → IPO con Goldman e JPMorgan chiude il cerchio: la finanza tradizionale finanzia l'infrastruttura "decentralizzata", poi la riporta nel mainstream via IPO. La SEC lawsuit (2024) — con ConsenSys che fa causa alla SEC per definire ETH come non-security — rappresenta la battaglia per chi regola questa nuova infrastruttura.

### La Saga SCO vs Linux: il Test Legale Esistenziale (2003-2021)

Prima delle licensing wars, l'open source ha affrontato una minaccia esistenziale: la causa [SCO Group](../docs/companies/sco-group.md) vs [IBM](../docs/companies/ibm.md), il piu' importante test legale per la legittimita' di Linux.

**La catena proprietaria**: [Ray Noorda](../docs/persons/ray-noorda.md), CEO di [Novell](../docs/companies/novell.md) dal 1982 al 1994, aveva costruito il colosso NetWare (70% market share networking). Dopo Novell, fondo' il [Canopy Group](../docs/companies/canopy-group.md) (1992) come veicolo VC e finanzio' Caldera Systems (1995), una distribuzione Linux commerciale. In parallelo, Noorda — che Bill Gates defini' portatore di una "tremendous vendetta" — uso' Caldera per lanciare una causa contro Microsoft per pratiche anti-competitive su DR-DOS, ottenendo un settlement di $275M nel 2000.

**Il pivot fatale**: Nel 2000 Caldera acquisto' gli asset Unix dalla Santa Cruz Operation (che li aveva comprati da Novell nel 1995). Nel 2002, sotto la nuova leadership di Darl McBride (CEO) e Ralph Yarro (Chairman, head del Canopy Group), Caldera si rinomino' [The SCO Group](../docs/companies/sco-group.md) e lancio' una causa da $1B contro IBM, sostenendo che IBM avesse inserito codice Unix proprietario nel kernel Linux. SCO creo' la divisione SCOsource per vendere licenze Unix agli utenti Linux.

**L'ironia suprema**: Noorda aveva investito in Linux per promuoverlo; la sua stessa creatura fu trasformata in una macchina anti-Linux. Microsoft acquisto' licenze SCOsource durante la causa — alimentando sospetti di sostegno indiretto alla strategia anti-Linux.

**La vittoria di Novell**: La controparte decisiva fu proprio Novell, che nel 2003 intervenne dichiarando di possedere ancora i copyright Unix. Nel 2007 il giudice Kimball diede ragione a Novell; nel 2010 una giuria unanime confermo': i copyright non furono mai trasferiti. SCO entro' in Chapter 11 (settembre 2007). Il settlement finale nel 2021 — IBM pago' $14.25M al trustee fallimentare — chiuse 18 anni di contenzioso.

**Significato**: La vittoria confermo' la legittimita' legale di Linux e dimostro' che le strategie IP-trolling contro l'open source erano insostenibili. Il caso accelero' la creazione di meccanismi difensivi come l'Open Invention Network (2005). La comunita' open source — guidata dal sito Groklaw di Pamela Jones — smonto' sistematicamente le pretese di SCO, dimostrando il potere dell'analisi collettiva distribuita.

### Big Tech e Open Source: Strategia di Cattura

| Azienda | Acquisizioni OS | Contributi | Strategia |
|---------|----------------|------------|-----------|
| [Microsoft](../docs/company/microsoft.md) | GitHub ($7.5B), npm, Xamarin | VS Code, TypeScript | Controlla la piattaforma + monetizza via AI |
| [IBM](../docs/company/ibm.md) | [Red Hat](../docs/company/red-hat.md) ($34B), [HashiCorp](../docs/company/hashicorp.md) ($6.4B) | [Eclipse](../docs/foundation/eclipse-foundation.md) (creatore originale 2001), OpenJ9 | Compra i leader dell'enterprise OS; creo' Eclipse poi lo cedette a fondazione indipendente |
| [Google](../docs/company/google.md) | - | Kubernetes, Android, Chromium, TensorFlow | Open source come moat per servizi cloud |
| [Amazon](../docs/company/amazon.md)/AWS | - | [OpenSearch](../docs/foundation/opensearch.md) (fork→LF), Valkey (fork→LF) | Monetizza OS altrui come managed service; fork e dona a LF per neutralizzare |
| [Meta](../docs/company/meta.md) | - | React, PyTorch, LLaMA | Open source come strategia anti-Google/OpenAI |
| [Salesforce](../docs/companies/salesforce.md) | Heroku ($212M), [Slack](../docs/companies/slack.md) ($27.7B), MuleSoft ($6.5B) | Heroku (PaaS Ruby/Node), contributi Apache Phoenix | Integra infrastruttura OS nel proprio stack SaaS; finanzia ecosistema via Ventures (MongoDB, Automattic $300M, Anthropic). $73.4B in acquisizioni totali (2006-2025). [Benioff](../docs/persons/marc-benioff.md) WEF Trustee |
| [Sun Microsystems](../docs/company/sun-microsystems.md) † | [MySQL AB](../docs/company/mysql-ab.md) ($1B) | Java (GPL), OpenOffice, OpenSolaris, ZFS, NFS, NetBeans, GlassFish | **Il precursore**: piu' grande contributore corporate OS al mondo (report UE 2006). Rilascio' piu' codice proprietario di chiunque, ma mori' di commoditization (Linux su x86 vs Solaris su SPARC). Acquisita Oracle $7.4B (2010) |

**I progetti anti-corporate**: Fondatori di aziende vendute a Big Tech hanno usato il capitale per costruire infrastruttura indipendente — percorso inverso rispetto alla corporate capture:
- **Brave** (2015): [Brendan Eich](../docs/persons/brendan-eich.md) (Netscape → Mozilla → Brave), Chromium-based, blocca tracker, finanziato via Basic Attention Token (ICO $35M, 2017)
- **Ladybird** (2024): [Chris Wanstrath](../docs/persons/chris-wanstrath.md) (GitHub → Microsoft → Ladybird), engine from scratch (no Chromium/WebKit), no-profit, no pubblicita', no deal corporate. Release prevista estate 2026
- **Ghostty** (2024): [Mitchell Hashimoto](../docs/persons/mitchell-hashimoto.md) (HashiCorp → IBM exit → Ghostty), terminal emulator GPU-accelerated scritto in Zig, nonprofit via Hack Club. Rifiuta esplicitamente il modello VC per dev tools

Il pattern e' significativo: chi ha incassato miliardi dalla vendita a Big Tech reinveste in infrastruttura open source che sfida il modello corporate — ma con risorse che solo un exit miliardario puo' fornire.

**Il pattern IBM** e' emblematico: dopo aver acquisito Red Hat per $34B (2019, la piu' grande acquisizione software della storia), IBM compra [HashiCorp](../docs/companies/hashicorp.md) per $6.4B (annuncio apr 2024, completamento feb 2025) — proprio dopo che HashiCorp aveva abbandonato la licenza open source. [Jim Whitehurst](../docs/persons/james-whitehurst.md), CEO di Red Hat, diventa presidente IBM ma lascia dopo soli 14 mesi. [Armon Dadgar](../docs/persons/armon-dadgar.md), co-fondatore e CTO di HashiCorp, assume un ruolo prominente in IBM Software per supervisionare la roadmap tecnica, mentre il co-fondatore [Mitchell Hashimoto](../docs/persons/mitchell-hashimoto.md) aveva gia' lasciato l'azienda nel 2023 per dedicarsi a Ghostty.

---

## Le Licensing Wars

### Il Ciclo della Cattura

Il pattern si ripete dal 2018:

1. Progetto open source diventa infrastruttura critica
2. AWS lo offre come managed service senza contribuire
3. L'azienda originale cambia licenza (source-available)
4. La community forka il progetto
5. Il fork finisce sotto la Linux Foundation

### Timeline dei Cambi di Licenza

| Anno | Progetto | Da | A | Fork |
|------|----------|----|----|------|
| 2018 | MongoDB | AGPL | SSPL | - |
| 2021 | Elasticsearch | Apache 2.0 | SSPL | **[OpenSearch](../docs/foundation/opensearch.md)** (AWS→LF) |
| 2023 | Terraform (HashiCorp) | MPL 2.0 | BSL 1.1 | **OpenTofu** (LF) |
| 2024 | Redis | BSD 3-Clause | SSPL | **Valkey** (LF) |
| 2024 | Elastic (reversal) | SSPL | AGPL | Primo ritorno a licenza OS |

La SSPL (Server Side Public License) di MongoDB e' stata esplicitamente rifiutata dalla OSI, Red Hat e Debian come non conforme alla Open Source Definition. La BSL (Business Source License) e' "source-available" ma non open source.

### Case Study: MongoDB — SSPL come Modello Originale

[MongoDB](../docs/companies/mongodb.md) e' l'azienda che ha creato la SSPL e stabilito il precedente per tutte le licensing wars successive. La sua storia illustra il percorso da progetto open source a corporate licensing:

**Origini DoubleClick**: I tre co-fondatori — [Dwight Merriman](../docs/persons/dwight-merriman.md) (CTO), [Eliot Horowitz](../docs/persons/eliot-horowitz.md) (engineer) e [Kevin Ryan](../docs/persons/kevin-ryan.md) (CEO) — provenivano tutti da [DoubleClick](../docs/companies/doubleclick.md), l'azienda di ad-tech fondata nel 1995 e poi acquisita da Google per $3.1B. L'esperienza dei limiti dei DB relazionali nel servire 400K+ ads/secondo fu la scintilla per creare MongoDB nel 2007 (come 10gen).

**Il percorso verso SSPL**: MongoDB nacque open source (AGPL), fece IPO nel 2017 (NASDAQ: MDB, $192M) sotto la guida del CEO operativo [Dev Ittycheria](../docs/persons/dev-ittycheria.md) (ex BladeLogic, $900M exit a BMC), e passo' a SSPL nel 2018 — la prima grande azienda open source a chiudere la licenza contro i cloud provider.

**La connessione intelligence**: Tra gli early investors di MongoDB figura [In-Q-Tel](../docs/companies/in-q-tel.md) (il braccio venture capital della CIA), insieme a [Sequoia Capital](../docs/private-equity/sequoia-capital.md), [Goldman Sachs](../docs/bank/goldman-sachs.md) e [Intel Capital](../docs/companies/intel.md). L'interesse dell'intelligence USA per un database NoSQL merita attenzione.

**Connessione CFR**: Kevin Ryan, co-fondatore e Chairman MongoDB dal 2017, e' membro del [Council on Foreign Relations](../docs/forum/cfr.md) — ponte diretto tra l'infrastruttura database globale e l'establishment di politica estera USA.

### Case Study: Elastic vs. AWS — Anatomia di una Licensing War

Il caso [Elastic](../docs/company/elastic.md)/[OpenSearch](../docs/foundation/opensearch.md) e' il piu' completo esempio del ciclo cattura-fork-fondazione:

**Gli attori:**
- [Shay Banon](../docs/persons/shay-banon.md) (ISR, 1979): crea Elasticsearch nel 2009 dopo aver sviluppato Compass (framework Java/Lucene) nel 2005. Fonda Elastic NV nel 2012 con [Steven Schuurman](../docs/persons/steven-schuurman.md) (NLD), [Simon Willnauer](../docs/persons/simon-willnauer.md) (DEU, Apache Lucene committer) e [Uri Boness](../docs/persons/uri-boness.md) (ISR)
- [Chetan Puttagunta](../docs/persons/chetan-puttagunta.md) (USA, Stanford EE): General Partner di [Benchmark Capital](../docs/private-equity/benchmark-capital.md) (dal 2018, ex NEA). Lead investor in Elastic, MongoDB, MuleSoft — l'architetto finanziario del modello "open source → enterprise SaaS". Forbes Midas List per 5 anni consecutivi. Chairman Elastic dal 2024

**Cronologia:**
1. **2010-2020**: Elasticsearch cresce come standard de facto per enterprise search sotto Apache 2.0. IPO 2018 (NYSE: ESTC, ~$2.5B)
2. **2019-2020**: AWS lancia "Amazon Elasticsearch Service" senza contributi significativi, sfruttando il brand
3. **Gen 2021**: Banon annuncia "Doubling Down on Open" — cambio a SSPL/Elastic License
4. **Apr 2021**: AWS forka come OpenSearch (Apache 2.0), sostenuto da Red Hat, Aiven, Logz.io, CrateDB
5. **Gen 2022**: [Ashutosh Kulkarni](../docs/persons/ashutosh-kulkarni.md) promosso CEO; Banon diventa CTO
6. **Set 2024**: AWS trasferisce OpenSearch alla [Linux Foundation](../docs/foundation/linux-foundation.md) come OpenSearch Software Foundation (premier members: AWS, SAP, Uber)
7. **Set 2024**: Elastic risponde aggiungendo AGPL v3 — primo "reversal" nella storia delle licensing wars

**Il ruolo del capitale VC:** Puttagunta (prima NEA, poi Benchmark) ha investito sia in MongoDB che in Elastic — entrambe hanno adottato SSPL. Il pattern suggerisce che la strategia licensing non e' solo una reazione ad AWS, ma un modello deliberato sostenuto dai VC per proteggere il valore dell'investimento. La SSPL e' nata in MongoDB, dove anche [In-Q-Tel](../docs/companies/in-q-tel.md) (CIA), [Sequoia Capital](../docs/private-equity/sequoia-capital.md) e [Goldman Sachs](../docs/bank/goldman-sachs.md) erano investitori — il cambio di licenza protegge anche i loro interessi.

**Board Elastic — ponte finanza-tech:** [Shelley Leibowitz](../docs/persons/shelley-leibowitz.md) (USA), Independent Director dal 2021, illustra il pattern CIO-to-Board: ex CIO Morgan Stanley e World Bank, ora nel board di Morgan Stanley e Elastic, lifetime member CFR. Porta governance finanziaria tradizionale nelle aziende open source.

---

## La Crisi di Sostenibilita'

### Il Problema Strutturale

L'ecosistema open source genera un valore stimato di $8.8 trilioni in lavoro equivalente (Harvard/Linux Foundation), ma l'86% dell'investimento e' lavoro in-kind (dipendenti aziendali che contribuiscono sul tempo aziendale). I maintainer indipendenti sono cronicamente sotto-finanziati.

### XZ Utils: Il Wake-Up Call (marzo 2024)

Il caso piu' drammatico: un attore (pseudonimo "Jia Tan") ha impiegato 3 anni (2021-2024) per infiltrarsi come co-maintainer di xz-utils, una libreria di compressione usata da quasi tutte le distribuzioni Linux. Ha inserito una backdoor (CVE-2024-3094, CVSS 10.0) che avrebbe dato accesso remoto via SSH a centinaia di milioni di sistemi.

La backdoor e' stata scoperta per caso il 28 marzo 2024 da Andres Freund, sviluppatore Microsoft/PostgreSQL, mentre investigava un problema di performance. Alex Stamos l'ha definita potenzialmente la backdoor piu' efficace mai impiantata in un software.

**La causa profonda**: un singolo maintainer esaurito (Lasse Collin) era stato manipolato tramite social engineering (account sockpuppet) per cedere accesso al progetto.

### Iniziative di Finanziamento

| Iniziativa | Budget | Anno | Sponsor |
|-----------|--------|------|---------|
| Sovereign Tech Fund (Germania) | EUR 23.5M | 2022-2024 | Governo Federale Tedesco |
| [OpenSSF](../docs/foundation/openssf.md) | $30M+ (pledges 2022) | 2020 | Linux Foundation (Google, Microsoft, IBM, JPMorgan Chase, Red Hat, GitHub) |
| GitHub Sponsors | - | 2019 | Microsoft |
| Open Source Pledge | $2K/dev/anno | 2024 | Multiple |
| [HeroDevs](../docs/company/herodevs.md) Sustainability Fund | $20M (grants $2.5K-$250K) | 2025 | [HeroDevs](../docs/company/herodevs.md) ([Aaron Frost](../docs/persons/aaron-frost.md)). Donazioni totali >$4M dal 2021, >$2M nel 2024 (Vue >$40K, Bootstrap >$40K) |
| [PSG Equity](../docs/private-equity/psg-equity.md) → HeroDevs | $125M | 2025 | Growth investment in HeroDevs — PE entra nel business del supporto EOL open source |

---

## Dimensione Geopolitica

### USA: Dominio di Default

Gli USA controllano l'infrastruttura open source globale:
- **GitHub** (Microsoft): piattaforma dominante, gia' bloccata in Iran, Crimea, Cuba, Corea del Nord, Siria
- **Linux Foundation**: sede a San Francisco, governance corporate americana
- **Copilot/AI**: Microsoft monetizza il lavoro della community globale

### UE: Sovranita' Digitale

L'Europa risponde con regolamentazione, advocacy e investimenti:
- **[FSFE](../docs/foundation/fsfe.md)** (2001-): la Free Software Foundation Europe, fondata da [Georg C. F. Greve](../docs/persons/georg-greve.md), e' il principale attore di advocacy per il software libero a livello europeo. Sotto la presidenza di [Matthias Kirschner](../docs/persons/matthias-kirschner.md) (2015-) ha lanciato la campagna "Public Money? Public Code!" (19.000+ firme, 150+ org) e portato il caso Apple alla Corte di Giustizia EU. La FSFE ha anche coordinato l'intervento nel caso antitrust EU vs Microsoft (2004-2007) e rappresentato la societa' civile al WSIS dell'ONU (2003-2005)
- **Legge svizzera EMBAG** (2023): prima legislazione nazionale che implementa "Public Money, Public Code" by default per il governo federale — vittoria diretta della campagna FSFE
- **Cyber Resilience Act (CRA)** (dic 2024): standard di cybersecurity per prodotti digitali, incluse dipendenze open source. Controverso perche' impone obblighi ai maintainer
- **EuroStack**: framework del cancelliere tedesco Friedrich Merz per ridurre dipendenza dagli hyperscaler USA
- **Sovereign Tech Fund**: finanziamento diretto a 60+ progetti open source
- **[Eclipse Foundation](../docs/foundation/eclipse-foundation.md)** (AISBL, 2020): unica grande fondazione open source con sede legale nell'UE (Bruxelles). Strategic members europei: Bosch, Mercedes-Benz, ESA, SAP, Ericsson, Fraunhofer. [Mike Milinkovich](../docs/persons/mike-milinkovich.md) ED dal 2004. Eclipse SDV come standard automotive europeo
- **Linux Foundation Europe** (2022): tentativo di decentralizzazione

### Cina: Ecosistema Parallelo

Le sanzioni USA su [Huawei](../docs/company/huawei.md) (2019) hanno accelerato la costruzione di un'infrastruttura open source autonoma, inserita nel 14° Piano Quinquennale (2021) come priorita' strategica nazionale:
- **[OpenAtom Foundation](../docs/foundation/openatom-foundation.md)** (2020): prima fondazione open source cinese, co-fondata da Alibaba, Baidu, Huawei, [Inspur](../docs/companies/inspur.md), [Qihoo 360](../docs/companies/qihoo-360.md), Tencent, China Merchants Bank. Supervisione diretta MIIT (Ministry of Industry and Information Technology); la costituzione impone la "leadership comprensiva del PCC". Chairman [Cheng Xiaoming](../docs/persons/cheng-xiaoming.md) (2023-): revolving door esemplare MIIT → Huawei SVP → OpenAtom. Il profilo dei fondatori rivela la natura dual-use: Inspur (Entity List 2023, server per supercomputer militari) e Qihoo 360 (Entity List 2024, collaborazione PLA in cybersecurity) affiancano colossi civili. Annual Report 2022: 33-45% dipendenti affiliati a PCC/Lega Giovanile
- **OpenHarmony**: OS open source (120M+ righe di codice, dic 2024), 30+ distribuzioni settoriali. Partnership con [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) per progetto Oniro (dal 2021) — il canale piu' diretto di collaborazione open source Europa-Cina, con [Carlo Piana](../docs/persons/carlo-piana.md) nello steering committee e [Deb Bryant](../docs/persons/deb-bryant.md) come policy adviser (fino al 2025)
- **openEuler**: distribuzione Linux Huawei per infrastruttura critica, adottata da SOE in energia, telecom, finanza
- **openKylin**: desktop OS nazionale
- **Gitee/GitCode**: alternative domestiche a GitHub (12M utenti su Gitee)

---

## Figure Chiave

### Pre-Fondatori: lo Unix Team di Bell Labs

| Persona | Ruolo | Impatto |
|---------|-------|---------|
| [Ken Thompson](../docs/persons/ken-thompson.md) | Co-creatore Unix (1969), B, Plan 9, UTF-8, Go | [UC Berkeley](../docs/university/uc-berkeley.md) (BS+MS EE 1965-66). [Bell Labs](../docs/company/bell-labs.md) 1966-2000, poi [Google](../docs/company/google.md) Distinguished Engineer 2006-oggi. Turing Award 1983, National Medal of Technology 1998, Japan Prize 2011. Co-creo' Go (2009) — il linguaggio alla base di Docker, Kubernetes e dell'infrastruttura cloud. La lezione Turing "Reflections on Trusting Trust" (1984) anticipo' i problemi di supply chain security che esplodono 40 anni dopo (XZ Utils 2024) |
| [Dennis Ritchie](../docs/persons/dennis-ritchie.md) | Creatore C (1972), co-creatore Unix | [Harvard](../docs/university/harvard.md) (BS Physics 1963). Bell Labs 1967-2007 (Head System Software Research, [Lucent](../docs/company/lucent-technologies.md)). Turing Award 1983. Padre Alistair Ritchie era scienziato Bell Labs — dinastia di ricerca. Morto ~12 ott 2011, una settimana dopo Steve Jobs, nell'indifferenza dei media — pur avendo creato le fondamenta su cui ogni prodotto Apple funziona |
| [Brian Kernighan](../docs/persons/brian-kernighan.md) | Co-autore K&R, AWK, battezzatore di Unix | [U of Toronto](../docs/university/university-of-toronto.md) (BASc 1964), [Princeton](../docs/university/princeton.md) (PhD EE 1969). Bell Labs 1969-2000, poi Professor CS Princeton 2000-oggi. National Academy of Engineering 2002. Ha reso leggibili Unix e C al mondo — senza K&R, il C sarebbe rimasto un linguaggio interno. Insegna "Computers in Our World" alla futura classe dirigente USA |
| [Rob Pike](../docs/persons/rob-pike.md) | Co-creatore Plan 9, UTF-8, Go | CAN. U of Toronto (BS Physics 1977). Bell Labs 1980-2002, Google 2002-oggi. Medaglia d'argento olimpica tiro con l'arco (1980). Co-creo' UTF-8 con Thompson (1992, su un tovagliolo in un diner del NJ) — l'encoding che ha reso possibile un web multilingue |

### Fondatori e Ideologi

| Persona | Ruolo | Impatto |
|---------|-------|---------|
| [Richard Stallman](../docs/persons/richard-stallman.md) | Fondatore FSF/GNU (1983) | Harvard (BA Physics 1974), MIT AI Lab dal 1971. Creatore del copyleft, GPL. Dimesso da FSF 2019, rientrato nel board 2021 con forte controversia. Resta board member ma non presidente |
| [Zoë Kooyman](../docs/persons/zoe-kooyman.md) | Executive Director FSF (2022-) | NLD. University of Amsterdam (BA Media, MA Moving Image). FSF dal 2019. Guida la transizione post-Stallman |
| [Ian Kelling](../docs/persons/ian-kelling.md) | Presidente board FSF (2025-) | SDSU (BS CS). Senior SysAdmin FSF, primo staff-president. Primo union seat nel board (2021) |
| [Linus Torvalds](../docs/persons/linus-torvalds.md) | Creatore Linux (1991), Git (2005) | University of Helsinki (MSc CS 1996). Transmeta 1997-2003, poi Fellow Linux Foundation. Millennium Technology Prize 2012 |
| [Eric S. Raymond](../docs/persons/eric-raymond.md) | Co-fondatore OSI (1998) | UPenn (math/philosophy, non completato), autodidatta in programmazione. "The Cathedral and the Bazaar". Bannato dalle mailing list OSI nel 2020 |
| [Bruce Perens](../docs/persons/bruce-perens.md) | Co-fondatore OSI, DPL Debian (1996-97) | Ex Pixar (1987-1999), poi HP Senior Strategist Linux/OS (2000-2002). Ha lasciato OSI nel 1999, tornando verso posizioni free software. Autore DFSG → Open Source Definition. Fondatore Open Research Institute (2018) |
| [Ian Murdock](../docs/persons/ian-murdock.md) | Fondatore [Debian](../docs/foundation/debian.md) (1993) | Purdue (BS CS 1996). Ha fondato Debian a 20 anni e [SPI](../docs/foundation/spi.md) (1997). Sun Microsystems/Oracle VP (2007-2014), Docker (2015). Morto il 28 dic 2015 a San Francisco |
| [Tim O'Reilly](../docs/persons/tim-oreilly.md) | Fondatore O'Reilly Media | IRL-USA. Harvard (BA Classics 1975). Organizzatore primo Open Source Summit 1998. Ha popolarizzato il termine verso il business. Co-fondatore [OATV](../docs/private-equity/oatv.md) (VC, 2005). Board [Code for America](../docs/foundation/code-for-america.md). Visiting Professor UCL. Ponte open source → civic tech → governo |
| [Christine Peterson](../docs/persons/christine-peterson.md) | Co-fondatrice [Foresight Institute](../docs/think-tank/foresight-institute.md) | MIT (BS Chemistry). Ha coniato il termine "open source" (3 feb 1998). Advisory board MIRI (AI safety). Partner di [Ralph Merkle](../docs/persons/ralph-merkle.md) |
| [K. Eric Drexler](../docs/persons/eric-drexler.md) | Co-fondatore [Foresight Institute](../docs/think-tank/foresight-institute.md) | MIT (BS/MS/PhD, primo PhD in nanotecnologia molecolare 1991). Senior Research Fellow, Oxford FHI. Connessione nanotech-AI safety-open source |
| [Ralph Merkle](../docs/persons/ralph-merkle.md) | Board [Foresight Institute](../docs/think-tank/foresight-institute.md), co-inventore crittografia a chiave pubblica | UC Berkeley (BS CS 1974), Stanford (PhD EE 1979). Inventore Merkle Trees (struttura dati fondamentale per Git e blockchain), Merkle-Damgard construction (hashing). Xerox PARC, Georgia Tech, faculty [Singularity University](../docs/university/singularity-university.md). Feynman Prize 1998. National Inventors Hall of Fame 2011. Partner di Peterson |
| [Allison Duettmann](../docs/persons/allison-duettmann.md) | President & CEO [Foresight Institute](../docs/think-tank/foresight-institute.md) (2017-) | DEU. University of York (BA PPE), LSE (MS Phil & Public Policy, AI Safety). Co-iniziato AI Safety Grant Program, Longevity Prize, Norm Hardy Prize. Ponte Foresight verso ecosistema AI safety e Effective Altruism |

### Governatori Istituzionali

| Persona | Ruolo | Background |
|---------|-------|------------|
| [Georg C. F. Greve](../docs/persons/georg-greve.md) | Founding President FSFE (2001-2009) | DEU. Fisico (Univ. Hamburg), speaker europeo GNU. Caso antitrust Microsoft, WSIS ONU. Croce al Merito tedesca. Post-FSFE: Kolab Systems, Vereign AG (SSI, Zug) |
| [Matthias Kirschner](../docs/persons/matthias-kirschner.md) | President FSFE (2015-) | DEU. Politologo (Univ. Potsdam). Primo stagista FSFE (2004). Campagna "Public Money? Public Code!", caso Apple alla CGUE |
| [Jim Zemlin](../docs/persons/jim-zemlin.md) | Executive Director, Linux Foundation (2004-) | University of Minnesota (BA), [Sophia University](../docs/university/sophia-university.md) Tokyo. Western Wireless → Corio → FSG (2004) → Linux Foundation (2007). Board [Global Economic Symposium](../docs/forums/global-economic-symposium.md). $1.15M/anno. Ha trasformato LF in umbrella per 700+ progetti |
| [Mike Milinkovich](../docs/persons/mike-milinkovich.md) | Executive Director, [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) (2004-) | CAN. [Carleton University](../docs/university/carleton-university.md) (MSc Info Systems, BComm). BNR (1983) → OTI → [IBM](../docs/companies/ibm.md) VisualAge (1996) → [Oracle](../docs/company/oracle.md) VP (2002) → Eclipse Foundation (2004). [OSI](../docs/foundation/open-source-initiative.md) Board Director e Treasurer (2012-2018). 20+ anni alla guida, ponte Java enterprise → automotive/IoT → sovranita' digitale europea |
| [Mitchell Baker](../docs/persons/mitchell-baker.md) | Fondatrice Mozilla (2003-2025) | Avvocata. Fenwick & West (IP law 1990-93) → Sun Microsystems (AGC 1993-94) → Netscape (1994-2003, scrive MPL/NPL) → fonda Mozilla Foundation (2003). BA Chinese Studies UC Berkeley (1979, anno scambio a Peking University), JD Boalt Hall (1987). Chair Mozilla 2003-2025, CEO Mozilla Corp 2005-08 e 2020-24. Compenso $6.9M (2022) controverso. Lascia tutti i board feb 2025 |
| [Stefano Maffulli](../docs/persons/stefano-maffulli.md) | Primo Executive Director OSI (2021-2025) | Italiano. Co-fondatore FSFE Italia (2001-2007), community manager OpenStack. BA Architecture (UniFi), Executive MBA (MIP PoliMi). Dimesso set 2025 durante crisi OSAID |
| [Deb Bryant](../docs/persons/deb-bryant.md) | Interim ED OSI (2025-) | Ex Senior Dir. OSPO Red Hat (2014-2022), ex Deputy State CIO Oregon. Fondatrice GOSCON e OSU Open Source Lab. Board Emeritus OSI (9 anni). Policy Adviser Eclipse Foundation |
| [Thierry Carrez](../docs/persons/thierry-carrez.md) | Vice Chair OSI; GM OpenInfra Foundation | Francese. Ex Technical Lead Ubuntu Server (Canonical), ex VP Engineering OpenStack. PSF Fellow. UTC Compiegne (Ingenieur 1996) |
| [Carlo Piana](../docs/persons/carlo-piana.md) | Board Director OSI (ex Chair) | Italiano. Avvocato IT law Milano. Fondatore Array (2008). Ex General Counsel FSFE per 10+ anni. Legale caso antitrust Microsoft-UE (FSFE/Samba). Laurea Giurisprudenza UniMi 1992 |
| [Brian Behlendorf](../docs/persons/brian-behlendorf.md) | Co-fondatore Apache, Vice Chair EFF | UC Berkeley. CTO WEF (2011-2012, report diretto a Schwab). Advisor Casa Bianca OSTP (2009-2010). ED [Hyperledger](../docs/foundation/hyperledger.md) (LF, 2016-2021) — ha guidato 30 founding members tra cui [IBM](../docs/companies/ibm.md), [Intel](../docs/companies/intel.md), [JP Morgan](../docs/bank/jp-morgan.md), [Accenture](../docs/companies/accenture.md), [SWIFT](../docs/agency/swift.md), [Wells Fargo](../docs/bank/wells-fargo.md), [Deutsche Boerse](../docs/companies/deutsche-boerse.md). GM/CTO [OpenSSF](../docs/foundation/openssf.md) (2021-2023). Ponte open source → governo → forum globali |
| [Jonathan Bryce](../docs/persons/jonathan-bryce.md) | ED Cloud & Infra LF, ED CNCF, ED OpenInfra (2025-) | USA. Web developer [Rackspace](../docs/companies/rackspace.md) dal 2000, co-fondatore Rackspace Cloud, co-creatore [OpenStack](../docs/foundation/openstack.md) (2010). ED OpenStack/[OpenInfra Foundation](../docs/foundation/openinfra-foundation.md) dal 2012. Dal 2025 triplo ruolo: unifica governance cloud VM (OpenStack) e containers (Kubernetes/CNCF) sotto Linux Foundation |
| [Priyanka Sharma](../docs/persons/priyanka-sharma.md) | Ex ED CNCF (2020-2025) | IND-USA. Stanford (BS CS 2009). Google → LightStep → [GitLab](../docs/companies/gitlab.md) (Dir. Cloud Native Alliances) → CNCF GM/ED. Membro fondatore OpenTracing. Ha guidato la crescita di Kubernetes da progetto a ecosistema dominante |
| [Omkhar Arasaratnam](../docs/persons/omkhar-arasaratnam.md) | GM OpenSSF (2023-2024), poi [LinkedIn](../docs/companies/linkedin.md) | CAN-USA. 25+ anni in cybersecurity. Percorso autodidatta (no laurea formale): IBM → TD Bank (Chief Security Architect) → [Deutsche Bank](../docs/banks/deutsche-bank.md) (CTO of CISO) → [Credit Suisse](../docs/banks/credit-suisse.md) (Head PM & Eng. Cyber Security) → [JPMorgan Chase](../docs/banks/jpmorgan-chase.md) (Head Data Protection Eng.) → [Google](../docs/companies/google.md) (Dir. Eng. Regulated Cloud) → OpenSSF GM → LinkedIn (Distinguished Engineer for Security, ott 2024). Successore di Behlendorf alla guida della sicurezza della supply chain open source |

### Privacy Infrastructure

| Persona | Ruolo | Background |
|---------|-------|------------|
| [Roger Dingledine](../docs/persons/roger-dingledine.md) | Co-fondatore, Project Leader [Tor Project](../docs/foundation/tor-project.md) | MIT (BS Math + CS&E 2000, MEng EECS, allievo Rivest/RSA). Free Haven Project → NRL → Tor. MIT TR35 2006. Foreign Policy Top 100 2012 |
| [Nick Mathewson](../docs/persons/nick-mathewson.md) | Co-fondatore, Chief Architect [Tor Project](../docs/foundation/tor-project.md) | MIT (BS CS, MEng CS & Linguistics 2002, allievo Liskov/Turing Award). Maintainer libevent. Foreign Policy Top 100 2012 |
| [Paul Syverson](../docs/persons/paul-syverson.md) | Inventore onion routing, co-fondatore [Tor Project](../docs/foundation/tor-project.md) | Indiana University (MA Philosophy & Math). Matematico NRL/CHACS (~1990-oggi). ACM Fellow 2014. Dipendente DoD che ha creato lo strumento anti-sorveglianza piu' usato al mondo |
| [Shari Steele](../docs/persons/shari-steele.md) | ED [EFF](../docs/foundation/eff.md) (2000-2015), ED [Tor Project](../docs/foundation/tor-project.md) (2015-2018) | Widener (JD), Georgetown (LLM), West Chester (MA). Unica persona ad aver guidato sia EFF che Tor. Co-fondatrice Bridges.org. Ponte EFF→Tor |
| [Isabela Bagueros](../docs/persons/isabela-bagueros.md) | ED [Tor Project](../docs/foundation/tor-project.md) (2018-oggi) | BRA. Unifenas. Free software Brasile → governo Lula (migrazione IT Presidenza) → Twitter PM International → Tor. Ha ridotto dipendenza da fondi gov USA dall'80% al 35% |
| [Alissa Cooper](../docs/persons/alissa-cooper.md) | Board Chair [Tor Project](../docs/foundation/tor-project.md), ex IETF Chair | Stanford (BS+MS CS), Oxford (DPhil OII). CDT Chief Computer Scientist → Cisco Fellow/VP → IETF Chair 2017-2021 (prima donna) → Tor Board Chair → ED Knight-Georgetown Institute (2024). Profilo tripartito: industria, standard, diritti digitali |

### Antagonisti e Anti-Eroi

| Persona | Ruolo | Impatto |
|---------|-------|---------|
| [Ray Noorda](../docs/persons/ray-noorda.md) | CEO Novell 1982-1994, fondatore Canopy Group | NLD-USA. Figlio immigrati olandesi. University of Utah (BS Engineering 1949). GE 1949-71. Costrui' l'impero Novell/NetWare, finanziatore di Caldera (Linux) e della causa DR-DOS vs Microsoft ($275M). La sua creatura (Caldera/SCO) fu rivoltata contro Linux da Yarro e McBride. Conio' "co-opetition" (1992). Morto 2006 |
| Darl McBride | CEO SCO Group 2002-2007 | Ex executive Novell e FranklinCovey. Trasformo' Caldera da distribuzione Linux in macchina anti-Linux. Lancio' causa da $1B vs IBM. Chapter 11 nel 2007 |
| Ralph Yarro | Chairman SCO, Head Canopy Group | Protege' di Noorda al Canopy Group. Considerato la mente dietro la strategia SCO vs IBM. Licenziato da Noorda nel 2004 per self-dealing |

### Acquisitori Corporate

| Persona | Ruolo | Acquisizione |
|---------|-------|-------------|
| [Bob Young](../docs/persons/bob-young.md) | Co-fondatore [Red Hat](../docs/companies/red-hat.md) | CAN-USA. BA History, U. Toronto. CEO Red Hat 1993-1999. Co-fondatore Linux Journal (1994). Poi fondatore Lulu.com (2002, self-publishing) e proprietario Hamilton Tiger-Cats (CFL, 2003). Pattern fondatore open source → imprenditore seriale |
| [Marc Ewing](../docs/persons/marc-ewing.md) | Co-fondatore [Red Hat](../docs/companies/red-hat.md) | BS CS Carnegie Mellon 1992, ex IBM. CTO Red Hat 1993-2000. Ritirato dal tech dopo IPO. Figlio di programmatore IBM — Red Hat nata dal lavoro di customizzazione Linux in IBM |
| [Mark Shuttleworth](../docs/persons/mark-shuttleworth.md) | Fondatore [Canonical](../docs/companies/canonical.md)/Ubuntu | ZAF-GBR. BSc Finance UCT. Thawte → VeriSign $575M (1999). Secondo turista spaziale (ISS, $20M, 2002). Debian Developer → fonda Canonical (2004). Unico proprietario, revenue $292M (2024), nessun investitore esterno |
| [Sid Sijbrandij](../docs/persons/sid-sijbrandij.md) | Co-fondatore [GitLab](../docs/companies/gitlab.md), Executive Chair | NLD. MSc Management Science, University of Twente. Ex U-Boat Worx (sottomarini ricreativi) e Min. Giustizia olandese. CEO GitLab 2014-2024. IPO NASDAQ 2021 (~$11B). Diagnosi osteosarcoma 2023. Anche fondatore [Open Core Ventures](../docs/private-equity/open-core-ventures.md) (VC open-core, 2020), Sijbrandij Foundation (2022), Kilo Code (2025). Pattern: career atipico → open source → IPO → VC che finanzia prossima generazione |
| [Dmytro Zaporozhets](../docs/persons/dmitriy-zaporozhets.md) | Creatore [GitLab](../docs/companies/gitlab.md) | UKR. BSc Automotive Engineering, Kharkiv. Crea GitLab nel 2011 da una casa senza acqua corrente. CTO 2014-2018, Engineering Fellow 2018-2021. Lascia dopo esattamente 10 anni. Forbes: 23° tra i 100 ucraini piu' ricchi (~$450M, <5% shares). Resta a Kharkiv. Il developer periferico che ha creato un'alternativa da $11B a GitHub — e poi se n'e' andato |
| [Michael Widenius](../docs/persons/michael-widenius.md) | Co-fondatore [MySQL AB](../docs/company/mysql-ab.md), fondatore [MariaDB](../docs/company/mariadb.md) | FIN. Dropout Helsinki Univ. of Technology. Main author MySQL. CTO MySQL AB 1995-2008, vendita a Sun $1B (guadagno €16.6M, top 10 Finland). Forka MySQL in MariaDB (2009). Co-fonda [MariaDB Foundation](../docs/foundation/mariadb-foundation.md) (2012), [OpenOcean](../docs/private-equity/openocean.md) VC (2008). Caso archetipico: fondatore vende a corporate → forka per preservare indipendenza |
| [David Axmark](../docs/persons/david-axmark.md) | Co-fondatore [MySQL AB](../docs/company/mysql-ab.md) | SWE. Uppsala 1980-84. Pioniere dual licensing (modello Ghostscript). Co-fonda [MariaDB Foundation](../docs/foundation/mariadb-foundation.md) (2012). Director [OrangeHRM](../docs/company/orangehrm.md) |
| [Marten Mickos](../docs/persons/marten-mickos.md) | Serial CEO open source | FIN-USA. MSc Aalto. CEO MySQL AB (2001-08, guida exit $1B) → SVP Sun → EIR [Benchmark](../docs/private-equity/benchmark-capital.md)/[Index](../docs/private-equity/index-ventures.md) → CEO Eucalyptus (→ HP $acq) → board [Nokia](../docs/company/nokia.md) → CEO [HackerOne](../docs/company/hackerone.md) (2015-24) → EIR Aalto (2025). Honorary Consul Finland in SF 2019-24. Pattern: open source CEO → VC revolving door → security → ritorno all'accademia |
| [Satya Nadella](../docs/persons/satya-nadella.md) | CEO Microsoft | GitHub ($7.5B, 2018) |
| [Marc Benioff](../docs/persons/marc-benioff.md) | Founder & CEO [Salesforce](../docs/companies/salesforce.md) | USA. BS USC 1986. Oracle VP (youngest ever, mentor [Larry Ellison](../docs/persons/larry-ellison.md)) → Salesforce (1999, $37.9B revenue FY2025). Acquisizioni: Heroku ($212M, 2010, PaaS Ruby), MuleSoft ($6.5B, 2018, API integration), Tableau ($15.7B, 2019), Slack ($27.7B, 2021). Salesforce Ventures: investor [MongoDB](../docs/companies/mongodb.md), [Automattic](../docs/company/automattic.md) ($300M Series D), Anthropic, Cohere. Owner TIME Magazine ($109M, 2018). WEF Board of Trustees (2016), Chair Centre for 4th Industrial Revolution. Co-fondatore Pledge 1%. [Jim Jagielski](../docs/persons/jim-jagielski.md) (fondatore Apache) Head of Open Source. CTO Slack: [Parker Harris](../docs/persons/parker-harris.md) (co-fondatore Salesforce, Middlebury BA). Pattern: acquisitore enterprise che integra infrastruttura open source (Heroku, Slack) nel proprio stack proprietario, e finanzia l'ecosistema via Ventures — modello diverso dalla cattura diretta (IBM/Red Hat) |
| [Arvind Krishna](../docs/persons/arvind-krishna.md) | CEO IBM | [Red Hat](../docs/companies/red-hat.md) ($34B, 2019), [HashiCorp](../docs/companies/hashicorp.md) ($6.4B, 2024) |
| [Mitchell Hashimoto](../docs/persons/mitchell-hashimoto.md) | Co-fondatore [HashiCorp](../docs/companies/hashicorp.md) | USA. UW CS. Creatore Vagrant/Terraform. CEO 2012-2016, CTO 2016-2021, esce 2023. Fonda Ghostty (nonprofit terminal, Zig). Pattern: fondatore OS → exit miliardario → tool indipendente |
| [Armon Dadgar](../docs/persons/armon-dadgar.md) | Co-fondatore e CTO [HashiCorp](../docs/companies/hashicorp.md) | USA (origini iraniane). UW CS a 16 anni. CTO 2013-2024 → IBM Software 2025. Forbes 30 Under 30. Guida roadmap tecnica post-acquisizione |
| [Miguel de Icaza](../docs/persons/miguel-de-icaza.md) | Co-fondatore GNOME/Mono/Xamarin | MEX-USA. UNAM dropout. GNOME (1997) → Ximian (1999) → Mono (2001) → Novell VP → Xamarin CEO (2011) → Microsoft Distinguished Engineer (2016-2022) → Xibbon (game dev, 2022). FSF Award 1999, TIME 100 2000. Il suo percorso dalla filosofia free software al corporate open source e' il caso piu' emblematico della transizione |
| [Nat Friedman](../docs/persons/nat-friedman.md) | CEO GitHub 2018-2021, VP Meta MSL 2025 | MIT CS 1999. GNOME Foundation Chairman → Ximian/Xamarin con de Icaza → Microsoft CVP → GitHub CEO → NFDG ($1.1B AI VC con Daniel Gross) → Meta Superintelligence Labs. TIME 100 AI 2025 |
| [Alexandr Wang](../docs/persons/alexandr-wang.md) | Chief AI Officer Meta 2025 | MIT dropout. Scale AI founder/CEO ($29B valuation), contratti Pentagono. Meta acquisisce 49% Scale AI. Co-lead Meta Superintelligence Labs con Friedman. Piu' giovane miliardario self-made (24 anni). TIME 100 AI 2025 |
| [Thomas Dohmke](../docs/persons/thomas-dohmke.md) | CEO GitHub 2021-2025, fondatore [Entire](../docs/companies/entire.md) | DEU. TU Berlin (Computer Engineering), U. Glasgow (PhD). Co-fondatore HockeyApp (acquisita Microsoft 2014). VP/CPO Microsoft → CEO GitHub (Copilot). Ago 2025: lascia GitHub, fonda Entire (piattaforma agentic coding). Feb 2026: $60M seed (record dev tools) guidato da Felicis, con M12 (Microsoft Ventures) — **il cordone ombelicale Microsoft non si recide mai** |
| [Joel Spolsky](../docs/persons/joel-spolsky.md) | Co-fondatore [Stack Overflow](../docs/companies/stack-overflow.md), [Fog Creek](../docs/companies/fog-creek-software.md), Trello | USA-ISR. IDF Paracadutisti → [Yale](../docs/university/yale.md) (BS CS summa cum laude 1991) → [Microsoft](../docs/company/microsoft.md) (PM Excel VBA) → Fog Creek (2000, FogBugz, Trello, Glitch) → Stack Overflow (co-fondatore & CEO 2008-2019, Chairman). Blog "Joel on Software" tra i piu' influenti 2000-2015. Trello acquisito da [Atlassian](../docs/companies/atlassian.md) $425M (2017). Stack Overflow acquisito da [Prosus](../docs/companies/prosus.md)/[Naspers](../docs/companies/naspers.md) $1.8B (2021). Attualmente co-fondatore [HASH](../docs/companies/hash.md), Chairman Glitch e SO. Pattern: IDF → Ivy League → Big Tech → serial founder con due exit miliardarie |
| [Jeff Atwood](../docs/persons/jeff-atwood.md) | Co-fondatore [Stack Overflow](../docs/companies/stack-overflow.md) e [Discourse](../docs/companies/discourse.md) | USA. [U. Virginia](../docs/university/university-of-virginia.md) (BA Environmental Science 1992). Blog "Coding Horror" (2004). Co-fonda SO con Spolsky (2008, lascia 2012). Fonda [Discourse](../docs/companies/discourse.md) (2013, forum open source, funding [Greylock](../docs/private-equity/greylock.md)/First Round/SV Angel). CEO Discourse 2013-2023, poi Executive Chairman. Piattaforma adottata da community Mozilla, Rust, Ubuntu. Filantropicamente attivo: $8M a 8 non-profit nel 2025 |
| [Melissa Di Donato](../docs/persons/melissa-di-donato.md) | CEO SUSE 2019-2023 | Bronx → American Univ. (BA Russian/PoliSci, MBA) → IBM → Oracle → Salesforce → SAP CRO Cloud → SUSE (prima donna CEO, guida IPO 2021) → Kyriba Chair/CEO + board Porsche + NED JP Morgan Europe + NED UK Gov DSIT. Ponte enterprise proprietary → open source → finanza europea |
| [Matt Mullenweg](../docs/persons/matt-mullenweg.md) | Fondatore [Automattic](../docs/company/automattic.md)/WordPress | USA. Houston. HSPVA (jazz), U. Houston dropout (PoliSci/Philosophy, 2004). Co-crea WordPress (2003, fork b2/cafelog). CNET developer (2004-05). Fonda Automattic (2005, $7.5B valuation 2021, $896M funding totale). Fonda [WordPress Foundation](../docs/foundation/wordpress-foundation.md) (2010, controlla trademark). Principal [Audrey Capital](../docs/private-equity/audrey-capital.md) (2008, portfolio: SpaceX, Stripe, GitLab, Telegram, Sonos, Ring). WEF Young Global Leader 2015. Heinz Award 2016. Net worth ~$400M. **Tripla posizione unica**: controlla simultaneamente il progetto open source (WordPress.org), la no-profit (WordPress Foundation) e l'azienda commerciale ($7.5B Automattic) — la concentrazione di potere piu' estrema nell'ecosistema open source. Investitori Automattic: Salesforce Ventures ($300M Series D), Tiger Global, BlackRock (marked down 10% nel 2024). Board: Toni Schneider (ex CEO, True Ventures), Sue Decker (ex CFO/President Yahoo!), Gen. Ann Dunwoody (prima donna 4 stelle nella storia militare USA). Acquisizioni: WooCommerce ($30M, 2015), Tumblr (~$3M da Verizon, 2019 — Yahoo pago' $1.1B nel 2013), Beeper (2024). Controversia WP Engine 2024: definisce WP Engine "cancer to WordPress", blocca >1M siti, perde ingiunzione preliminare. >150 dipendenti lasciano. Riduce contributi WordPress open source da ~4.000 ore/settimana a 45 (gen 2025). Class action da clienti WP Engine (feb 2025) |
| [Aaron Frost](../docs/persons/aaron-frost.md) | Fondatore [HeroDevs](../docs/company/herodevs.md) | USA. Sandy, Utah. Salt Lake Community College (AS CS 2010). Soprannome "Frosty". Co-fondatore ng-conf (prima conferenza Angular al mondo). Angular GDE Google. Ex Domo, SaltStack. Fonda HeroDevs (2018) dopo annuncio EOL AngularJS: modello Never-Ending Support (NES), drop-in replacement sicuri per software open source deprecato. Da $0 a $10M+ ARR bootstrapped (senza VC). Acquisisce Xeol (NYC, ex Y Combinator, EOL detection intelligence, feb 2025). Lancia $20M Open Source Sustainability Fund (giu 2025). [PSG Equity](../docs/private-equity/psg-equity.md) investe $125M (lug 2025, tra i piu' grandi first round nello Utah). Pattern emergente: monetizzazione del "debito tecnico collettivo" dell'open source come nuovo modello di business |

---

## Connessioni con l'Ecosistema DeepScript

### [EFF](../docs/foundation/eff.md) e Open Source

La [Electronic Frontier Foundation](../docs/foundation/eff.md) e' il ponte tra diritti digitali e open source:
- [John Gilmore](../docs/persons/john-gilmore.md) (co-fondatore EFF, board FSF): Cypherpunks + free software. Rimosso dal board EFF nel 2021 per dispute di governance — stesso pattern dei fondatori OSI
- [Mitch Kapor](../docs/persons/mitch-kapor.md) (co-fondatore EFF, founding chair Mozilla): venture capital + open source
- [Brian Behlendorf](../docs/persons/brian-behlendorf.md) (Vice Chair EFF, co-fondatore Apache): governance open source
- [Bruce Schneier](../docs/persons/bruce-schneier.md) (board EFF, ex IBM): sicurezza + open source
- [Pamela Samuelson](../docs/persons/pamela-samuelson.md) (board EFF, UC Berkeley): massima esperta USA di copyright law e software, co-fondatrice Authors Alliance — rilevante per le licensing wars
- [Jonathan Zittrain](../docs/persons/jonathan-zittrain.md) (board EFF, YGL [WEF](../docs/forum/wef.md)): accademia + policy

**Contributo legale EFF**: il caso Bernstein v. US (1993-1999), con [Cindy Cohn](../docs/persons/cindy-cohn.md) lead attorney, ha stabilito che il codice crittografico e' protetto dal First Amendment (free speech). Senza questo precedente, la distribuzione di software open source contenente crittografia sarebbe rimasta illegale. L'EFF ha anche co-sponsorizzato [Let's Encrypt](../docs/foundation/lets-encrypt.md), infrastruttura open source che ha reso gratuiti i certificati SSL per il web.

**Il ponte EFF → Tor**: [Shari Steele](../docs/persons/shari-steele.md) (Staff Attorney 1992 → ED EFF 2000-2015 → ED [Tor Project](../docs/foundation/tor-project.md) 2015-2018) e' l'unica persona ad aver guidato entrambe le organizzazioni. Cohn la sostituisce come ED EFF e poi entra nel board Tor (2016). L'EFF ha finanziato lo sviluppo di Tor nel 2004-2006, prima della fondazione del Tor Project. Il revolving door EFF-Tor cementa il legame tra il movimento legale dei diritti digitali e l'infrastruttura tecnica della privacy.

### Forum Transnazionali

| Forum | Connessione OS |
|-------|---------------|
| [WEF](../docs/forum/wef.md) | [Brian Behlendorf](../docs/persons/brian-behlendorf.md) CTO (2011-2012, report diretto a Klaus Schwab). [Marc Benioff](../docs/persons/marc-benioff.md) Board of Trustees (2016-), Chair Centre for 4th Industrial Revolution — il WEF Trustee piu' connesso all'ecosistema OS via Salesforce Ventures (investor Automattic, MongoDB, Anthropic). Jonathan Zittrain (YGL). [Matt Mullenweg](../docs/persons/matt-mullenweg.md) YGL 2015. Tech leaders regolarmente a Davos |
| [Bilderberg](../docs/forum/bilderberg.md) | Eric Schmidt (Google), Satya Nadella (Microsoft) partecipanti |
| [CFR](../docs/forum/cfr.md) | Tarah Wheeler (Senior Fellow, board EFF). [Kevin Ryan](../docs/persons/kevin-ryan.md) (member, co-founder MongoDB Chairman, Yale/INSEAD) |
| [Trilateral Commission](../docs/forum/trilateral-commission.md) | [Joi Ito](../docs/persons/joi-ito.md) membro dal 2002 (invitato da Yotaro Kobayashi, Fuji-Xerox). Connessione open source-Giappone-forum transnazionali |
| Civic tech pipeline | O'Reilly (Gov 2.0 Summit) → [Code for America](../docs/foundation/code-for-america.md) (Pahlka) → Casa Bianca (USDS) → [Niskanen Center](../docs/think-tank/niskanen-center.md) (Pahlka Senior Fellow) |

### Creative Commons: dal Software Libero ai Contenuti Liberi

[Creative Commons](../docs/foundation/creative-commons.md) (2001) e' l'estensione del modello copyleft dal codice ai contenuti — e condivide fondatori e rete con l'ecosistema open source:

- **[Hal Abelson](../docs/persons/hal-abelson.md)** (MIT): co-fondatore FSF (1985) E CC (2001) — l'unico nodo che collega direttamente le due istituzioni fondative della liberta' digitale
- **[Lawrence Lessig](../docs/persons/lawrence-lessig.md)** (Stanford/Harvard): teorico "Code is Law", crea CC come risposta alla sconfitta in *Eldred v. Ashcroft* (2003) — stessa logica di Stallman con GNU: se non puoi cambiare il sistema, crea un'alternativa
- **[Joi Ito](../docs/persons/joi-ito.md)**: Chairman CC (2006-08) → CEO CC (2008-12) → MIT Media Lab (2011-19) → board Mozilla — il connettore seriale tra open source, open content, accademia e forum transnazionali
- **[James Boyle](../docs/persons/james-boyle.md)** (Duke Law): Board Chair CC (2008-09), teorico della "seconda enclosure" della conoscenza — il framework che lega copyright extension, privatizzazione del digitale e risposta open

**Pattern**: CC replica il modello FSF (licenze libere come risposta al copyright) ma per contenuti, dati e ricerca scientifica. La sovrapposizione dei fondatori (Abelson in entrambe) conferma che si tratta di un unico movimento con due bracci operativi.

### Mozilla Foundation: il Board come Ponte Governo-Open Source

Il board Mozilla Foundation (2025) rappresenta un caso di studio sulla convergenza tra open source, filantropia e potere governativo:

| Board member | Background | Pattern |
|-------------|-----------|---------|
| [Mitchell Baker](../docs/persons/mitchell-baker.md) | Fondatrice, Chair 2003-2025 | Legale tech → open source → Internet Hall of Fame |
| [Nicole Wong](../docs/persons/nicole-wong.md) | Board Chair dal 2024 | Google VP → White House Deputy CTO → Mozilla |
| [Nabiha Syed](../docs/persons/nabiha-syed.md) | Executive Director dal 2024 | BuzzFeed Legal → The Markup CEO → Mozilla. WEF AI Governance Alliance |
| [Mark Surman](../docs/persons/mark-surman.md) | President, ED dal 2008 | telecentre.org → Mozilla. WEF member, co-chair European AI Fund |
| [Alondra Nelson](../docs/persons/alondra-nelson.md) | Board member | SSRC President → White House acting Director OSTP (architetto AI Bill of Rights) → IAS Princeton → Mozilla. UN AI Advisory Body. TIME100 AI 2023 |
| [Helen King-Turvey](../docs/persons/helen-turvey.md) | Board member | CEO Shuttleworth Foundation → Mozilla board. Board Open Knowledge Foundation. Filantropia open-source |
| [Mitch Kapor](../docs/persons/mitch-kapor.md) | Founding Chair | Co-fondatore EFF, fondatore Lotus. Investitore iniziale $300K |
| [Joi Ito](../docs/persons/joi-ito.md) | Board member | JPN-USA. Dropout Tufts/U. Chicago. Digital Garage co-founder (1994) → Creative Commons Chairman/CEO (2003-) → MIT Media Lab Director (2011-2019, resigned per scandalo [Epstein](../docs/persons/jeffrey-epstein.md)) → Mozilla board. [WEF](../docs/forum/wef.md) GLT 2001, [Trilateral Commission](../docs/forum/trilateral-commission.md) 2002-. Riabilitato: President [Chiba Institute of Technology](../docs/university/chiba-institute-technology.md) (2023-), Kazakhstan AI Council (2025). Connettore VC-governance-open source tra USA e Giappone |
| [Brian Behlendorf](../docs/persons/brian-behlendorf.md) | Board member | Apache → WEF CTO → White House → OpenSSF |

**Pattern emergente**: tre board member su sei attuali provengono dal governo USA (Wong da White House Deputy CTO, Nelson da OSTP acting Director, Syed connessa a WEF AI Governance). Il board Mozilla non e' piu' un gruppo di tecnici open source — e' un nodo nel revolving door tech-governo-filantropia.

**Il ponte Shuttleworth-Mozilla**: [Helen King-Turvey](../docs/persons/helen-turvey.md) rappresenta la connessione con la filantropia open-source sudafricana. Come CEO della Shuttleworth Foundation (fino alla chiusura nel 2024), ha gestito Fellowship milionarie per fondatori di impatto sociale. La convergenza con Mozilla (board) e Open Knowledge Foundation (board) la posiziona come connettore tra filantropia e governance dell'internet aperto.

**Il caso Nelson**: [Alondra Nelson](../docs/persons/alondra-nelson.md) e' il caso piu' significativo di revolving door accademia-governo-open source. Sociologa a Yale (2003-09), Columbia (2009-19) e Princeton IAS (2019-), diventa la prima donna di colore a guidare l'OSTP (acting Director, 2022). All'OSTP crea il Blueprint for an AI Bill of Rights, poi fondamento dell'Executive Order Biden su AI. Tornata all'accademia, entra nel board Mozilla, nell'UN AI Advisory Body, e come Distinguished Senior Fellow al Center for American Progress. Il suo percorso — da sociologia della razza e tecnologia a policy AI al massimo livello — illustra come la competenza su etica e tecnologia si sia convertita in potere istituzionale.

### Tor Project: il Paradosso Militare dell'Open Source

Il [Tor Project](../docs/foundation/tor-project.md) rappresenta il caso piu' estremo di tecnologia open source nata nel complesso militare-industriale USA e diventata infrastruttura globale per la privacy civile.

**Genesi NRL → MIT → Open Source**: [Paul Syverson](../docs/persons/paul-syverson.md) (matematico NRL, Indiana University, ACM Fellow) inventa l'onion routing nel 1995 come progetto della Marina USA. Recluta [Roger Dingledine](../docs/persons/roger-dingledine.md) (MIT 2000, allievo di Ronald Rivest/RSA) e [Nick Mathewson](../docs/persons/nick-mathewson.md) (MIT 2002, allievo di Barbara Liskov/Turing Award) per sviluppare la seconda generazione. Alpha Tor rilasciata nel 2002, Tor Project fondato nel 2006 come 501(c)(3).

**Il pipeline EFF → Tor**: La catena di leadership esecutiva rivela il legame organico tra le due organizzazioni:
- [Shari Steele](../docs/persons/shari-steele.md): 23 anni all'EFF (Staff Attorney 1992 → ED 2000-2015), poi ED Tor (2015-2018). Unica persona ad aver guidato entrambe.
- [Cindy Cohn](../docs/persons/cindy-cohn.md): succede a Steele come ED EFF (2015), entra nel board Tor (2016).
- [Isabela Bagueros](../docs/persons/isabela-bagueros.md): succede a Steele come ED Tor (2018). Background: free software Brasile → governo Lula (migrazione IT Presidenza) → [Twitter](../docs/companies/twitter.md) Product Manager → Tor. Sotto la sua guida, la quota di fondi governativi USA e' scesa dall'80% al 35%.

**Board Chair**: [Alissa Cooper](../docs/persons/alissa-cooper.md) (Stanford BS+MS CS, Oxford DPhil, prima donna IETF Chair 2017-2021, Cisco Fellow) porta nella governance di Tor la prospettiva degli standard Internet e dell'industria tech. Dal 2024 ED del Knight-Georgetown Institute.

**Finanziamento**: Budget ~$7.3M (2024). Fonti storiche: DARPA, NRL, State Department, EFF, Mozilla. Il paradosso: il governo USA finanzia uno strumento anti-sorveglianza perche' la rete funziona solo con molti utenti diversi — se la usassero solo gli agenti, sarebbero identificabili.

### Connessioni Italiane

L'Italia ha una presenza sorprendente nella governance open source globale, concentrata su OSI e FSF:

| Persona | Organizzazione | Ruolo | Background |
|---------|---------------|-------|------------|
| [Stefano Maffulli](../docs/persons/stefano-maffulli.md) | OSI | Primo ED (2021-2025) | Co-fondatore FSFE Italia (2001-2007), community manager OpenStack. BA Architecture UniFi, MBA MIP PoliMi |
| [Carlo Piana](../docs/persons/carlo-piana.md) | OSI, [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) | Board Director OSI (ex Chair); Steering Committee Eclipse (Oniro WG) | Avvocato IT law Milano, fondatore Array (2008). Ex General Counsel FSFE 10+ anni. Legale caso antitrust Microsoft-UE (Commissione Europea → Corte di Giustizia, vittoria su tutti i fronti). Primo advisory board per legislazione open source nel procurement pubblico italiano. Il ruolo in Eclipse Oniro lo posiziona nel ponte Europa-Cina sull'open source |
| [Maria Chiara Pievatolo](../docs/persons/maria-chiara-pievatolo.md) | FSF | Board member (2024-) | Universita' di Pisa, presidente AISA, trustee Nexa Center |

Maffulli e Piana condividono un percorso comune: entrambi hanno iniziato con la [FSFE](../docs/foundation/fsfe.md) — Maffulli co-fondando il capitolo italiano (2001-2007), Piana come General Counsel per oltre un decennio — per poi convergere nella governance OSI. Piana ha inoltre un ruolo di Steering Committee nella [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) (Oniro WG) e ha contribuito a creare precedenti legali fondamentali sull'interoperabilita' software in Europa. Il percorso FSFE → OSI rappresenta il pattern italiano nel software libero: advocacy europea prima, governance globale poi.

L'Italia ha adottato il Codice dell'Amministrazione Digitale che promuove l'uso di software open source nella PA (con Piana nel primo advisory board), ma resta marginale nel panorama globale.

### FSFE: Il Polo Europeo del Software Libero

La [FSFE](../docs/foundation/fsfe.md), fondata nel 2001 da [Georg C. F. Greve](../docs/persons/georg-greve.md) (fisico tedesco, speaker europeo del GNU Project dal 1998), ha costruito il polo europeo dell'advocacy del software libero indipendente dalla FSF americana.

| Leader | Periodo | Contributo |
|--------|---------|------------|
| [Georg Greve](../docs/persons/georg-greve.md) | 2001-2009 | Fondazione, caso antitrust Microsoft, rappresentanza WSIS ONU. Croce al Merito tedesca 2009. Post-FSFE fonda [Kolab Systems](../docs/company/kolab-systems.md) e [Vereign](../docs/company/vereign.md) (Self-Sovereign Identity, Zug) |
| Karsten Gerloff | 2009-2015 | Consolidamento |
| [Matthias Kirschner](../docs/persons/matthias-kirschner.md) | 2015-oggi | Primo stagista FSFE (2004), poi presidente. Politologo (Univ. Potsdam). Campagna PMPC, caso Apple alla CGUE |

**Il ponte Greve**: Greve incarna la transizione del movimento dal software libero all'imprenditoria tech europea. Da speaker GNU passa a fondare FSFE, poi entra brevemente in [Google](../docs/company/google.md) (2007-2008, open standards), infine fonda due aziende in Svizzera. Il suo percorso anticipa il tema della sovranita' digitale europea che emerge 15 anni dopo con EuroStack.

**Il pattern FSFE-Italia**: La FSFE e' l'unica organizzazione open source globale dove l'Italia ha avuto un ruolo fondativo. [Stefano Maffulli](../docs/persons/stefano-maffulli.md) co-fonda il capitolo italiano (2001), [Carlo Piana](../docs/persons/carlo-piana.md) ne diventa General Counsel. Entrambi migrano poi verso la governance OSI — portando l'approccio europeo (legale, policy-oriented) nel contesto globale.

---

## Pattern e Osservazioni

### 1. Corporate Capture Completa
Il software libero nato come movimento anti-corporate e' stato completamente catturato dalle corporations. I principali progetti open source sono oggi finanziati e governati da Big Tech attraverso la Linux Foundation.

### 2. Chokepoint GitHub
GitHub (Microsoft) controlla ~90% dell'hosting del codice open source. Un singolo punto di controllo aziendale per un'infrastruttura critica globale. Le sanzioni USA dimostrano che e' uno strumento geopolitico.

### 3. AI come Nuovo Fronte di Estrazione
Copilot/Codex rappresentano un nuovo livello di estrazione: il lavoro collettivo della community viene usato per addestrare AI proprietarie vendute come servizio. La class action Doe v. GitHub (2022) potrebbe ridefinire i confini.

### 4. Fragilita' Infrastrutturale
XZ Utils dimostra che l'infrastruttura digitale mondiale dipende da maintainer non pagati, vulnerabili a social engineering e burnout. Un problema di sicurezza nazionale, non solo etico.

### 5. Frammentazione Geopolitica
Tre modelli in competizione:
- **USA**: laissez-faire, corporate-led
- **UE**: regolamentazione + finanziamento pubblico
- **Cina**: ecosistema parallelo, state-directed

### 6. La Saga SCO: l'Anti-Linux che Legittimo' Linux

Il caso SCO vs IBM (2003-2021) dimostra tre pattern: (a) il capitale tecnico puo' essere rivoltato contro se stesso — Noorda investi' in Linux ma la sua Caldera fu trasformata in arma anti-Linux; (b) le cause IP-trolling contro l'open source sono insostenibili quando la comunita' si mobilita (Groklaw); (c) le corporations possono giocare su entrambi i fronti — Microsoft acquisto' licenze SCOsource mentre finanziava la Linux Foundation. La catena [Ximian](../docs/companies/ximian.md) (1999) → [Novell](../docs/companies/novell.md) (2003) → Attachmate layoffs (2011) → [Xamarin](../docs/companies/xamarin.md) (2011) → Microsoft (2016) mostra anche la resilienza dei progetti open source: il progetto Mono ha attraversato quattro proprietari mantenendo lo stesso nucleo tecnico (de Icaza), sopravvivendo a acquisizioni, layoff e cause legali.

### 7. Il Crogiolo Netscape: da Browser Company a Incubatore di Potere
Una singola azienda (1994-1999, ~5 anni di vita) ha generato: il primo VC fund da $90B+ (a16z), il browser open source dominante (Firefox/Mozilla), il linguaggio di programmazione piu' usato al mondo (JavaScript), un browser anti-sorveglianza (Brave), e un ponte diretto tra Silicon Valley e intelligence USA (Barksdale → In-Q-Tel/PFIAB). Il pattern SGI → Netscape → Mozilla mostra come il potere accademico (Clark a Stanford) si converta in potere tech (SGI), poi in potere finanziario (IPO/VC) e infine in potere politico (Andreessen advisor Trump, Barksdale advisor intelligence). La decisione di liberare il codice nel 1998 — presa sotto pressione competitiva da Microsoft — e' l'atto fondativo dell'open source come strategia industriale.

### 8. Il Crogiolo DoubleClick: da Ad-Tech a Database Globale

Un'altra azienda di breve vita ha generato un ecosistema di potere. [DoubleClick](../docs/companies/doubleclick.md) (1995-2007) — fondata da [Dwight Merriman](../docs/persons/dwight-merriman.md) e [Kevin O'Connor](../docs/persons/kevin-oconnor.md) nel seminterrato di O'Connor ad Alpharetta, Georgia — ha prodotto il trio che ha creato [MongoDB](../docs/companies/mongodb.md) e, tramite [AlleyCorp](../docs/companies/alleycorp.md), un intero ecosistema di Silicon Alley (New York):

| Alumni DoubleClick | Ruolo in DC | Dopo |
|-------------------|-------------|------|
| [Dwight Merriman](../docs/persons/dwight-merriman.md) | Co-founder, CTO | Co-founder MongoDB, AlleyCorp, ShopWiki. Owner Era Motorsport (IMSA) |
| [Kevin Ryan](../docs/persons/kevin-ryan.md) | CEO | Co-founder MongoDB (Chairman), AlleyCorp. Fondatore Business Insider, Gilt Groupe. Membro [CFR](../docs/forum/cfr.md). Yale/INSEAD |
| [Eliot Horowitz](../docs/persons/eliot-horowitz.md) | Engineer (intern poi R&D) | Co-founder MongoDB (CTO, ha scritto il core codebase). Fondatore [Viam](../docs/companies/viam.md) (robotica). Brown CS |

Il parallelo con Netscape e' strutturale: un'azienda della prima ondata internet (ad-tech per DoubleClick, browser per Netscape) produce i fondatori di una infrastruttura critica (MongoDB per i database, Mozilla per il browser) e di veicoli finanziari (AlleyCorp per il VC, a16z per il VC). La differenza e' che il network DoubleClick e' rimasto concentrato su New York (Silicon Alley), creando un polo alternativo a San Francisco. Ryan, con le sue credenziali Yale + INSEAD + CFR + Human Rights Watch, incarna il ponte tra tech entrepreneurship e establishment USA in modo diverso da Barksdale (intelligence) o Andreessen (politica).

La successione alla guida di MongoDB e' significativa: dal fondatore-tecnico (Merriman CTO) al CEO operativo-VC ([Dev Ittycheria](../docs/persons/dev-ittycheria.md), ex Greylock Partners e BladeLogic, Lead Director Datadog), fino al CEO di scalata enterprise ([CJ Desai](../docs/persons/cj-desai.md), ex ServiceNow/Cloudflare, board [MSCI](../docs/companies/msci.md)). Ogni transizione avvicina MongoDB al mondo della finanza: Ittycheria porta il VC, Desai porta i financial indices.

### 9. Il Crogiolo MIT e il Nodo Foresight
Il MIT e' il nodo formativo centrale del movimento del software libero: Stallman (AI Lab 1971-1984), Peterson (BS Chemistry), Drexler (BS/MS/PhD, primo PhD nanotech). Il [Foresight Institute](../docs/think-tank/foresight-institute.md) (Peterson + Drexler, 1986) e' il ponte tra nanotecnologia, AI safety e open source — Peterson conia "open source" nel 1998.

Il Foresight e' anche un nodo di convergenza piu' ampio: [Ralph Merkle](../docs/persons/ralph-merkle.md) (board Foresight, partner di Peterson) ha inventato i Merkle Trees — la struttura dati che rende possibile sia Git (creato da Torvalds nel 2005) sia la blockchain. [Peter Diamandis](../docs/persons/peter-diamandis.md) (board Foresight) ha co-fondato la [Singularity University](../docs/university/singularity-university.md) (2008) con [Ray Kurzweil](../docs/persons/ray-kurzweil.md), finanziata da Google/[Larry Page](../docs/persons/larry-page.md) e ospitata al NASA Ames. Merkle e' faculty anche alla Singularity University. La CEO attuale [Allison Duettmann](../docs/persons/allison-duettmann.md) (DEU, dal 2017) ha spostato il focus verso AI safety e longevita', collegando Foresight all'ecosistema Effective Altruism. Il percorso e' significativo: un think tank nato dalla nanotecnologia (1986) genera il termine "open source" (1998), incuba la crittografia che abilita Git e blockchain (Merkle Trees), e confluisce nel network futurista-AI che include Singularity University, Google e il circuito EA/AI safety.

### 10. Lo Scisma e le Sue Conseguenze
La scissione free software/open source del 1998 non e' solo terminologica. Perens, co-fondatore OSI, lascia gia' nel 1999 per tornare verso posizioni free software. Raymond viene bannato dalla stessa OSI nel 2020. Stallman, dimesso dalla FSF nel 2019, rientra nel 2021. Gilmore, co-fondatore EFF, viene rimosso dal board EFF nel 2021 per dispute di governance. Nessuno dei fondatori originali controlla piu' le istituzioni che ha creato — il potere e' passato ai manager istituzionali (Zemlin, Maffulli) e alle corporations. La FSF post-Stallman ha tentato una riforma partecipativa (2021-2025): union seat nel board, Code of Ethics, processo di nomina aperto (83 candidature nel 2024). Ian Kelling, primo staff-president (2025), rappresenta il passaggio dai fondatori carismatici ai tecnici interni.

### 11. Il Modello FSFE: Advocacy → Policy → Legge
La FSFE rappresenta un modello alternativo alla corporate capture: advocacy politica che produce risultati legislativi concreti. Il percorso "Public Money? Public Code!" → legge svizzera EMBAG (2023) dimostra che il software libero puo' avanzare per via politica, non solo tecnica. Il fondatore Greve incarna la transizione: da speaker GNU a lobbista EU a imprenditore tech (Kolab, Vereign). Il suo successore Kirschner, politologo, conferma la svolta: la battaglia per il software libero in Europa si combatte nei parlamenti, non nei repository.

### 12. I Fondatori Apache: dal Codice al Potere

La ASF (1999) offre il caso piu' chiaro di come il potere tecnico si converta in potere istituzionale. I quattro fondatori principali illustrano traiettorie divergenti ma complementari:

| Fondatore | Traiettoria | Pattern |
|-----------|-------------|---------|
| [Behlendorf](../docs/persons/brian-behlendorf.md) | Apache → Casa Bianca (OSTP 2009) → WEF (CTO 2011) → Hyperledger (LF 2016) → OpenSSF (GM 2021, CTO 2023) | **Revolving door** open source-governo-forum globale |
| [Fielding](../docs/persons/roy-fielding.md) | Apache (1o Chairman) → HTTP/REST → Day Software → Adobe (Senior Principal Scientist) | **Standardizzazione** come potere: il suo PhD (REST, 2000) definisce l'architettura delle API globali |
| [Jagielski](../docs/persons/jim-jagielski.md) | NASA → Apache (board dal 1999 senza interruzioni) → OSI board → Salesforce (Head of Open Source) | **Gatekeeper** istituzionale: unico fondatore ancora nella governance ASF |
| [Laurie](../docs/persons/ben-laurie.md) | Apache-SSL → OpenSSL core team → Google (Director Security & Transparency) → Cambridge | **Sicurezza** come leva: da Apache-SSL a Certificate Transparency (Levchin Prize 2024) |

Behlendorf e' il caso piu' significativo per DeepScript: un programmatore che scrive un web server nel 1995, viene advisor alla Casa Bianca sotto Obama (2009), poi CTO del WEF di Klaus Schwab a Ginevra (2011), poi governa la blockchain enterprise (Hyperledger) e la sicurezza della supply chain globale (OpenSSF). Il percorso dimostra che chi controlla l'infrastruttura tecnica accede al potere politico e finanziario.

### 13. Open Source → Civic Tech → Governo: il Pipeline di O'Reilly

Tim O'Reilly non e' solo il promotore del termine "open source" (1998) — ha costruito un pipeline completo dall'ideologia open source al potere governativo:

1. **O'Reilly Media** (1978): forma generazioni di sviluppatori, pubblica i testi fondamentali
2. **Open Source Summit** (1998): legittima l'open source nel mondo business
3. **"Web 2.0"** (2004): ridefinisce il paradigma del web partecipativo
4. **OATV** (2005): venture capital focalizzato su "alpha geeks" e tecnologie aperte ($51M)
5. **Gov 2.0 Summit** (2009): applica i principi open source al governo → genera [Code for America](../docs/foundation/code-for-america.md)

[Jennifer Pahlka](../docs/persons/jennifer-pahlka.md), gia' in O'Reilly Media, fonda Code for America (2009) come "Teach for America del tech". Il modello CfA — inserire sviluppatori nelle burocrazie — diventa il prototipo della USDS (United States Digital Service) quando Pahlka entra alla Casa Bianca come Deputy CTO sotto Obama (2013-2014). Il percorso O'Reilly Media → CfA → Casa Bianca → USDS e' il revolving door open source piu' diretto mai documentato.

La CEO attuale [Amanda Renteria](../docs/persons/amanda-renteria.md) (dal 2020) incarna un pattern diverso: Goldman Sachs → Senato (prima Latina Chief of Staff) → campagna Clinton 2016 → civic tech. Sotto la sua guida, CfA ha ottenuto $100M per modernizzare il safety net digitale.

**La discontinuita' DOGE (2025)**: Pahlka ha co-fondato l'ufficio che e' diventato DOGE sotto l'amministrazione Trump. La sua critica pubblica alla trasformazione come "irresponsabile" segna la rottura tra l'ideale civic tech (governo come piattaforma aperta) e l'uso politico della "efficienza digitale".

### 14. Blockchain Open Source: il Ritorno della Finanza Tradizionale
Hyperledger (2015) e ConsenSys (2015) dimostrano che la "decentralizzazione" blockchain e' stata catturata dalla finanza tradizionale ancora piu' velocemente del software libero. Il Governing Board di Hyperledger include rappresentanti di JP Morgan, Accenture, DTCC. ConsenSys, fondata da un ex-Goldman Sachs, e' finanziata da JP Morgan, Microsoft, Mastercard, UBS — e si prepara all'IPO con Goldman e JPMorgan come advisor. Il percorso e' lineare: Goldman Sachs (Lubin VP) → Ethereum co-founder → ConsenSys CEO → investimento JP Morgan → IPO con Goldman. L'infrastruttura "decentralizzata" (MetaMask 100M+ utenti, Infura gateway critico) e' di fatto un chokepoint controllato da un singolo attore con legami profondi con Wall Street.

### 15. La Grande Consolidazione Cloud (2025)

Il 2025 segna la convergenza delle due anime del cloud open source sotto un unico tetto. [OpenStack](../docs/foundation/openstack.md) (VM/bare metal, 2010) e Kubernetes/[CNCF](../docs/foundation/cncf.md) (containers, 2015) erano nati come approcci concorrenti: il primo da [Rackspace](../docs/companies/rackspace.md) e NASA, il secondo da Google. Per 15 anni hanno operato con governance separate. Nel 2025, [OpenInfra Foundation](../docs/foundation/openinfra-foundation.md) entra nella Linux Foundation e [Jonathan Bryce](../docs/persons/jonathan-bryce.md) assume il triplo ruolo di ED Cloud & Infrastructure LF, ED CNCF ed ED OpenInfra — riunificando l'intero stack cloud open source sotto una persona e un'organizzazione. Il percorso di Bryce e' emblematico: web developer → co-fondatore Rackspace Cloud → co-creatore OpenStack → ED della foundation → ED dell'intera infrastruttura cloud della Linux Foundation. La sua predecessora alla CNCF, [Priyanka Sharma](../docs/persons/priyanka-sharma.md) (Stanford CS, ex Google/LightStep/GitLab), aveva guidato la crescita esplosiva di Kubernetes durante i 5 anni di mandato. Il pattern e' chiaro: frammentazione iniziale → maturazione → consolidazione sotto Linux Foundation → governance corporate unificata. L'intero cloud infrastrutturale open source — che alimenta AI, edge computing e cloud ibrido — dipende ora da un singolo ombrello istituzionale.

### 16. MySQL → MariaDB: il Fork Archetipico (2008-2012)

Il percorso [MySQL AB](../docs/company/mysql-ab.md) → Sun → Oracle → MariaDB e' il caso originario del pattern "corporate capture → community fork" che si ripete poi in MongoDB/SSPL, Elasticsearch/OpenSearch, Terraform/OpenTofu, Redis/Valkey.

```
MySQL AB (1995, Uppsala, Widenius/Axmark/Larsson)
  ├── VC: Benchmark, Index ($20M, 2003), IVP, Intel, Red Hat, SAP ($18.5M, 2006)
  ├── CEO: Mickos (2001-08, professionalizza → exit)
  └── Sun Microsystems acquisisce per $1B (2008)
        └── Oracle acquisisce Sun per $7.4B (2010)
              └── MySQL sotto controllo Oracle
                    └── Widenius forka → MariaDB (2009)
                          └── MariaDB Foundation (2012, non-profit Delaware)
                                ├── Sponsor: Amazon, Alibaba, IBM, Intel, ServiceNow
                                └── CEO: Anna Widenius (2025, moglie del fondatore)
```

**Il modello**: MySQL AB pioniera il dual licensing (GPL + commerciale) che diventa standard per l'open source commerciale. La vendita a Sun e il passaggio a Oracle provocano la reazione comunitaria: Widenius forka l'intera base di codice. La [MariaDB Foundation](../docs/foundation/mariadb-foundation.md) nasce come garanzia di indipendenza — stessa funzione che OpenTofu, Valkey e OpenSearch avranno un decennio dopo.

**La rete VC**: [Benchmark Capital](../docs/private-equity/benchmark-capital.md) investe in MySQL AB (Series B 2003) e poi in Elastic — [Chetan Puttagunta](../docs/persons/chetan-puttagunta.md) (Benchmark) diventa Chairman Elastic. Lo stesso fondo plasma due generazioni di licensing wars. Mickos, dopo MySQL, diventa EIR proprio a Benchmark e Index Ventures — il circuito CEO-VC e' chiuso.

**Il pattern familiare**: MySQL prende nome dalla figlia My, MariaDB dalla figlia Maria. Nel 2025, la moglie Anna Widenius diventa CEO della MariaDB Foundation. Il controllo familiare — benche' non-profit — resta un tema anche nell'open source "comunitario".

### 17. Il Triangolo delle Distribuzioni: Community → Enterprise → Capture

Le tre maggiori distribuzioni Linux illustrano tre modelli di potere diversi:
- **[Debian](../docs/foundation/debian.md)** (Murdock, 1993): governance democratica, nessun profitto, DPL annuale, SPI come umbrella. Il codice alimenta Ubuntu e derivate ma il progetto resta indipendente. Modello comunitario puro.
- **[Red Hat](../docs/companies/red-hat.md)** (Young/Ewing, 1993): da startup in un closet a IPO (1999) a $34B IBM (2019). Il subscription model (RHEL) ha dimostrato che l'open source puo' essere un business da miliardi — ma ha anche aperto la strada alla cattura corporate (restrizione codice sorgente 2023, nascita fork AlmaLinux/Rocky Linux).
- **[Canonical](../docs/companies/canonical.md)** (Shuttleworth, 2004): finanziata da un singolo miliardario ($575M Thawte exit), nessun investitore esterno, revenue $292M. Caso unico di mecenatismo tech: Shuttleworth sceglie di non quotare l'azienda, mantenendo il controllo totale.

Il flusso codice → valore e' sempre lo stesso: Debian produce il codice comunitario → Ubuntu/RHEL lo commercializzano → IBM/PE estraggono il valore finanziario. I contributori volontari di Debian creano l'infrastruttura, le corporation monetizzano.

### 18. La Catena PE: da Novell a OpenText via Private Equity

Il percorso di [SUSE](../docs/companies/suse.md) — la distribuzione Linux enterprise piu' importante d'Europa — illustra come il private equity ha estratto valore dall'open source attraverso una catena di acquisizioni durata 20 anni:

```
SUSE (1992, Norimberga)
  → Novell (2003, $cash) ← Eric Schmidt CEO 1997-2001, poi Google
    → Attachmate (2011, $2.2B) ← PE: Golden Gate Capital + Francisco Partners + Thoma Bravo
      → CPTN Holdings ($450M, 882 brevetti) ← Microsoft + Apple + Oracle + EMC
      → Micro Focus (2014, $1.2B)
        → EQT AB (2018, $2.535B) ← solo SUSE estratta
          → IPO Francoforte (2021, €30/azione)
          → Delisting (2023, private di nuovo)
        → OpenText (2023, $5.8B) ← il resto (Novell, NetIQ, Attachmate)
```

Ogni passaggio ha generato valore per il PE e perso governance comunitaria. La vicenda CPTN Holdings e' particolarmente significativa: un consorzio guidato da [Microsoft](../docs/companies/microsoft.md) ha acquistato 882 brevetti [Novell](../docs/companies/novell.md) per $450M — brevetti originariamente sviluppati per il networking che diventano strumenti di pressione nelle patent wars. L'[OSI](../docs/foundation/open-source-initiative.md) contesto' l'operazione presso il German Federal Cartel Office.

[Melissa Di Donato](../docs/persons/melissa-di-donato.md), CEO SUSE 2019-2023, incarna il revolving door enterprise → open source → finanza: da CRO SAP Cloud a prima donna CEO di SUSE (guida IPO 2021), poi Chair/CEO Kyriba, board Porsche e NED JP Morgan Europe e UK Government DSIT. Il suo predecessore [Nils Brauckmann](../docs/persons/nils-brauckmann.md) e il successore [Dirk-Peter van Leeuwen](../docs/persons/dirk-peter-van-leeuwen.md) (ex Red Hat, quasi 20 anni nel concorrente diretto) completano il quadro di una leadership che ruota tra le stesse aziende.

Il pattern e' chiaro: il PE (Golden Gate, Francisco Partners, Thoma Bravo, EQT) ha trasformato un'azienda Linux fondata da quattro sviluppatori tedeschi in un asset finanziario da miliardi, passando attraverso cinque proprietari in due decenni. L'open source resta il motore di valore — ma il valore viene estratto da Wall Street.

### 19. Il Pipeline Open Source → AI Superintelligence (2025)

Il 2025 segna l'emergere di un nuovo pattern: le credenziali open source come trampolino verso il controllo dell'AI. Il caso piu' emblematico e' [Nat Friedman](../docs/persons/nat-friedman.md): hacker GNOME al MIT → co-fondatore Ximian/Xamarin → CEO GitHub (Microsoft) → venture capitalist AI ($1.1B NFDG fund, portfolio: Perplexity, ElevenLabs, SSI, Character.ai) → VP Product di Meta Superintelligence Labs. Il suo partner [Alexandr Wang](../docs/persons/alexandr-wang.md), dropout MIT e fondatore di [Scale AI](../docs/companies/scale-ai.md) (contratti Pentagono per valutazione LLM militari), diventa Chief AI Officer di Meta — con Meta che acquisisce il 49% di Scale AI per ~$14.3B.

Il pattern Friedman-Wang e' significativo: chi ha costruito credibilita' nell'open source (GNOME, GitHub) e nell'infrastruttura AI (data labeling per il Pentagono) controlla ora i laboratori di superintelligenza di una delle piu' grandi aziende tech del mondo. La traiettoria completa — open source credentials → AI venture capital → big tech superintelligence — rappresenta l'ultimo stadio della conversione del capitale tecnico comunitario in potere concentrato. [Miguel de Icaza](../docs/persons/miguel-de-icaza.md), partner ventennale di Friedman (GNOME, Ximian, Xamarin), ha seguito un percorso parallelo ma divergente: dopo Microsoft, fonda Xibbon (game dev tools) — restando nell'imprenditoria indie anziche' entrare nel circuito AI.

Il terzo CEO GitHub, [Thomas Dohmke](../docs/persons/thomas-dohmke.md), segue una variante del pattern: lascia GitHub (ago 2025) e fonda [Entire](../docs/companies/entire.md), piattaforma open source per collaborazione sviluppatori-agenti AI. Il seed round record ($60M, valutazione $300M, feb 2026) rivela la rete: lead [Felicis](../docs/private-equity/felicis.md), con [M12](../docs/private-equity/m12.md) (Microsoft Ventures) — il cordone ombelicale con Redmond non si recide mai. Gli angel investors sono un who's who della tech aristocracy: [Jerry Yang](../docs/persons/jerry-yang.md) (co-fondatore Yahoo, Chair Stanford Board, CFR, Brookings China Advisory Council), [Garry Tan](../docs/persons/garry-tan.md) (CEO Y Combinator), Olivier Pomel (CEO Datadog). Il primo prodotto, Checkpoints, e' open source e traccia il contesto dietro al codice generato da agenti AI — integrando Claude Code e Gemini CLI. Tre CEO GitHub, tre traiettorie: Friedman verso la superintelligenza (Meta), Dohmke verso l'infrastruttura agentica (Entire), Wanstrath verso il browser indipendente (Ladybird). Il chokepoint GitHub non genera solo valore per Microsoft — genera i leader del prossimo ciclo.

### 20. WordPress: il Caso Mullenweg — Potere Individuale sull'Open Source

La disputa [Mullenweg](../docs/persons/matt-mullenweg.md)/[Automattic](../docs/company/automattic.md) vs [WP Engine](../docs/company/wp-engine.md)/[Silver Lake](../docs/private-equity/silver-lake.md) (2024-) e' il caso piu' esplicito di concentrazione di potere individuale nell'open source. WordPress alimenta il 43% di tutti i siti web al mondo. Mullenweg controlla tre leve simultaneamente: il progetto open source (WordPress.org, infrastruttura plugin/temi/aggiornamenti), la no-profit (WordPress Foundation, trademark), l'azienda commerciale (Automattic, $7.5B, investitori: Salesforce Ventures, Tiger Global, BlackRock). Nessun'altra figura nell'open source detiene un potere comparabile su una singola piattaforma.

Il conflitto esplode nel settembre 2024 quando Mullenweg definisce WP Engine — il piu' grande hosting WordPress indipendente, majority owned da Silver Lake ($250M, 2018), 1.5M+ clienti — "a cancer to WordPress". Dopo che WP Engine rifiuta una richiesta di licenza da ~$32M/anno (8% dei ricavi), Mullenweg blocca l'accesso di WP Engine a WordPress.org, interrompendo aggiornamenti e plugin per oltre un milione di siti. WP Engine fa causa per estorsione e abuso di potere (ott 2024). Il tribunale (giudice Martinez-Olguin, N.D. California) emette ingiunzione preliminare a favore di WP Engine (dic 2024). Le conseguenze: >150 dipendenti lasciano Automattic, contributi WordPress ridotti da ~4.000 ore/settimana a 45, class action da clienti WP Engine (feb 2025), BlackRock marca giu' investimento del 10%.

Il caso illustra un pattern specifico dell'open source: la **vulnerabilita' del "benevolent dictator"**. Finche' il fondatore agisce nell'interesse della comunita', il modello funziona (Torvalds/Linux, van Rossum/Python). Quando il fondatore usa l'infrastruttura comunitaria per fini commerciali — o per punire un concorrente — il sistema crolla. La differenza con il caso Stallman (ideologico) o il caso HashiCorp (licensing) e' che Mullenweg ha usato direttamente l'infrastruttura .org come arma commerciale.

### 21. HeroDevs: il Business del Debito Tecnico Collettivo

[HeroDevs](../docs/company/herodevs.md) ([Aaron Frost](../docs/persons/aaron-frost.md), Sandy Utah, 2018) rappresenta un modello emergente: monetizzare il supporto per software open source dopo il suo end-of-life. Il prodotto "Never-Ending Support" (NES) offre drop-in replacement sicuri per framework deprecati (AngularJS, Vue 2, Drupal 7, .NET EOL) — servendo governi e grandi aziende che dipendono da software che la comunita' ha abbandonato.

Il profilo e' inusuale nel panorama open source: Frost non e' un fondatore di progetto ne' un VC, ma un community builder (co-fondatore ng-conf, Angular GDE) che ha identificato un gap strutturale — l'assenza di incentivi per mantenere software deprecato. HeroDevs ha raggiunto $10M+ ARR senza venture capital, poi ha chiuso un round da $125M con [PSG Equity](../docs/private-equity/psg-equity.md) (lug 2025) e lanciato un Sustainability Fund da $20M per i maintainer. L'acquisizione di Xeol (ex Y Combinator, EOL detection per 100K+ pacchetti) completa il modello: detect + support.

Il pattern e' significativo per due motivi: (1) dimostra che la crisi di sostenibilita' dell'open source puo' generare nuovi modelli di business, non solo donazioni; (2) il fatto che PSG Equity (growth PE) investa $125M in una first round segnala che Wall Street vede il debito tecnico open source come un mercato da miliardi. E' l'altra faccia della corporate capture: invece di catturare il progetto attivo, si cattura il valore residuo del progetto abbandonato.

### 22. Il Pipeline Militare → Open Source: il Caso Tor

Il [Tor Project](../docs/foundation/tor-project.md) rivela un pattern distinto dalla corporate capture: la **military capture inversa**. La tecnologia nasce al NRL (1995), viene rilasciata come open source (2004), e finanziata dal governo USA perche' la rete di anonimato funziona solo con molti utenti civili. Il pattern NRL → MIT → Open Source ricalca il trasferimento DARPA → universita' → startup che ha generato Internet stessa. I mentori MIT dei co-fondatori — Rivest (RSA) e Liskov (Turing Award) — collegano Tor al cuore dell'establishment crittografico.

La catena di successione ED (Steele da EFF → Bagueros da Twitter/Brasile) mostra come il potere organizzativo nell'open source privacy passi da avvocati dei diritti digitali a manager tech internazionali. La Board Chair [Alissa Cooper](../docs/persons/alissa-cooper.md) (Stanford, Oxford, IETF Chair, Cisco Fellow) incarna la convergenza standard Internet / industria / diritti digitali — un profilo tripartito unico nell'ecosistema.

### 23. Stack Overflow e Discourse: l'Infrastruttura della Conoscenza Developer

Se GitHub e' il chokepoint del *codice*, [Stack Overflow](../docs/companies/stack-overflow.md) e' il chokepoint della *conoscenza*. Fondato nel 2008 da [Joel Spolsky](../docs/persons/joel-spolsky.md) (IDF → Yale → Microsoft) e [Jeff Atwood](../docs/persons/jeff-atwood.md) (U. Virginia, blog Coding Horror) come alternativa aperta a Experts-Exchange, SO e' diventato il repository di Q&A consultato da 100M+ sviluppatori al mese.

Il pattern di cattura e' analogo a GitHub: crescita comunitaria → funding VC ([Andreessen Horowitz](../docs/private-equity/andreessen-horowitz.md) Series D $40M, [GIC](../docs/swf/gic.md) Series E $85M, [Silver Lake](../docs/private-equity/silver-lake.md), [Index Ventures](../docs/private-equity/index-ventures.md), [Spark Capital](../docs/companies/spark-capital.md)) → acquisizione corporate ([Prosus](../docs/companies/prosus.md)/[Naspers](../docs/companies/naspers.md) $1.8B, 2021). La conoscenza collettiva di milioni di developer e' ora proprieta' di un conglomerato tech sudafricano.

La traiettoria di Spolsky e' significativa: dal servizio militare israeliano (IDF Paracadutisti) a Yale, poi Microsoft (design VBA in Excel), poi serial founder con due exit miliardarie — Trello ($425M ad [Atlassian](../docs/companies/atlassian.md), 2017) e Stack Overflow ($1.8B a Prosus, 2021). Il suo blog "Joel on Software" ha plasmato la cultura dev per 15 anni, il "Joel Test" e' diventato standard de facto per valutare team software. E' il raro caso di un individuo che ha creato *sia* l'infrastruttura (SO) *sia* la cultura (blog) dell'ecosistema developer.

Atwood, dopo aver lasciato SO nel 2012, ha fondato [Discourse](../docs/companies/discourse.md) (2013) — piattaforma forum open source che ha sostituito il software bulletin board obsoleto. Con funding da [Greylock](../docs/private-equity/greylock.md), First Round e SV Angel, Discourse e' stato adottato da community come Mozilla, Rust, Ubuntu, diventando l'infrastruttura di *discussione* come SO e' l'infrastruttura di *conoscenza*. Il parallelo con WordPress e' diretto: Atwood voleva creare il "WordPress dei forum".

Il pattern complessivo: due blogger influenti (Spolsky con "Joel on Software", Atwood con "Coding Horror") convertono il capitale reputazionale in infrastruttura comunitaria, che viene poi catturata dal capitale finanziario. La rete di investitori (a16z, GIC, Silver Lake, Greylock) e' la stessa che opera nelle altre acquisizioni dell'ecosistema.

### 24. La Crisi OSI e il Dilemma AI (2024-2026)
L'OSI, custode della definizione di "open source", si trova al centro della crisi piu' grave della sua storia. La OSAID 1.0 (Open Source AI Definition, ottobre 2024) non richiede la pubblicazione dei dati di training — una scelta che la Software Freedom Conservancy ha definito una contraddizione dei principi fondamentali. Meta usa il termine "open source" per Llama nonostante restrizioni incompatibili con la OSD. Il primo ED Maffulli si dimette nel settembre 2025. Le elezioni board 2025 sono contestate per irregolarita' procedurali (nomination timing, confusione sui seggi). Il board sospende le elezioni 2026 per "ridisegnare il processo". Deb Bryant (veterana OSPO/policy, 9 anni di board) assume come interim ED. Il pattern e' lo stesso delle altre istituzioni open source: crisi di legittimita' → transizione leadership → incertezza sul futuro. La differenza: l'OSI non ha un Zemlin (corporate manager forte) ne' un Stallman (fondatore carismatico) — ha un board di professionisti (Carrez da OpenInfra, Piana dall'IT law europeo) che deve ridefinire il ruolo dell'organizzazione nell'era AI.

### 25. Sun Microsystems: il Campione Corporate che Perse la Guerra

[Sun Microsystems](../docs/company/sun-microsystems.md) (1982-2010) e' il caso piu' paradossale dell'open source: l'azienda che contribui' piu' codice proprietario di chiunque — e che mori' proprio per la rivoluzione open source che aveva alimentato.

**I numeri**: Un report UE 2006 indica Sun come il piu' grande contributore corporate all'open source al mondo, superando i cinque successivi contributori commerciali combinati. Le release: NFS (1985, primo protocollo open per file sharing), OpenOffice.org e NetBeans (2000), OpenSolaris e ZFS (2005), Java GPL (2006), MySQL (acquisizione $1B, 2008). Nessun'altra azienda ha rilasciato cosi' tanto codice proprietario come open source.

**Il paradosso**: Sun credeva che l'open source avrebbe rafforzato il suo ecosistema (Solaris/SPARC). Invece, Linux su hardware x86 commodity rese irrilevante il valore differenziale di Solaris. Sun finanziava la rivoluzione che la distruggeva: il suo CTO [Eric Schmidt](../docs/persons/eric-schmidt.md) (1983-1997) porto' la cultura open source a Google; [Bill Joy](../docs/persons/bill-joy.md) (co-fondatore) aveva creato BSD Unix con TCP/IP integrato — le fondamenta di Internet; [Mitchell Baker](../docs/persons/mitchell-baker.md) (associate general counsel) fondo' Mozilla; [John Gilmore](../docs/persons/john-gilmore.md) (5th employee) co-fondo' la EFF. La "farm system della Silicon Valley" formava i leader che avrebbero reso obsoleto il suo modello di business.

**Il pattern**: Da $200B+ di market cap (2001) a $7.4B acquisizione Oracle (2010). [Scott McNealy](../docs/persons/scott-mcnealy.md) (CEO per 22 anni, Harvard BA, Stanford MBA) resistette alla transizione cloud. [James Gosling](../docs/persons/james-gosling.md) (creatore Java) lascio' immediatamente dopo l'acquisizione Oracle citando problemi etici. [Michael Widenius](../docs/persons/michael-widenius.md) forko' MySQL in MariaDB — il fork archetipico che si ripete un decennio dopo in MongoDB, Elastic, Terraform, Redis.

**L'eredita' nel grafo del potere**: Il seed di [Kleiner Perkins](../docs/private-equity/kleiner-perkins.md) ($300K, [John Doerr](../docs/persons/john-doerr.md) board) genera una rete che domina il tech per quattro decenni: Khosla → Khosla Ventures ($15B AUM), Joy → KP partner, Schmidt → CEO Google/Chairman Alphabet/Bilderberg/Trilateral/CFR/Pentagon advisor, Bechtolsheim → primo investor Google ($100K → miliardi) e co-fondatore Arista Networks ($29B patrimonio). Sun non era solo un'azienda tech — era un nodo generatore di potere finanziario, istituzionale e governativo.

### 26. Bell Labs → Google: la Pipeline dell'Infrastruttura Invisibile

Il percorso dello Unix team di [Bell Labs](../docs/company/bell-labs.md) verso [Google](../docs/company/google.md) e' la catena di trasmissione piu' lunga dell'intero ecosistema — dal 1969 al 2009, quarant'anni di continuita' tecnica e culturale.

**La catena**:
```
Bell Labs (1969)                    Google (2002-2009)
    │                                    │
    ├── Unix (1969)                      ├── Go (2009)
    ├── C (1972)                         ├── UTF-8 (standard web)
    ├── Plan 9 (1989)                    ├── Kubernetes
    └── UTF-8 (1992)                     └── Cloud infrastructure
         │                                    │
    Thompson ────(2006)──────────────► Google Distinguished Engineer
    Pike ────────(2002)──────────────► Google Distinguished Engineer
    Kernighan ───(2000)──► Princeton ──► pipeline talenti Google
```

**Il paradosso militare-industriale**: Bell Labs era il braccio R&D di [AT&T](../docs/company/att.md), che operava in partnership diretta con la [NSA](../docs/agency/nsa.md) (descritta come "unica e specialmente produttiva"). Il sistema crittografico SIGSALY (WWII), le spolette di prossimita', la ricerca sulla sorveglianza — tutto nasceva nello stesso edificio di Murray Hill dove Thompson e Ritchie creavano Unix. Le fondamenta del software libero (Unix → GNU → Linux) sono nate in un laboratorio del complesso militare-industriale americano finanziato dal monopolio telefonico.

**Go come eredita' finale**: Il linguaggio Go (2009), creato da Thompson, Pike e Robert Griesemer a Google, e' l'ultimo prodotto della tradizione Bell Labs. Docker, Kubernetes, Terraform, Prometheus — l'intero stack cloud-native — sono scritti in Go. L'infrastruttura che alimenta AI, cloud computing e DevOps globale discende direttamente dalla cultura Unix di Bell Labs, passata attraverso Google.

**Il pattern**: Ogni ciclo produce tecnologia fondamentale — Unix/C negli anni '70, Plan 9/UTF-8 nei '90, Go negli anni 2000 — ma il potere si sposta dall'ente di ricerca (Bell Labs) all'employer successivo (Google). Bell Labs perde i suoi migliori ricercatori dopo la divestiture AT&T (1984) e lo spin-off Lucent (1996); Google li raccoglie. Il monopolio AT&T finanziava ricerca pura per 30 anni; il monopolio Google la capitalizza in infrastruttura di scala.

---

## Timeline

| Anno | Evento |
|------|--------|
| 1969 | [Ken Thompson](../docs/persons/ken-thompson.md) e [Dennis Ritchie](../docs/persons/dennis-ritchie.md) creano Unix a [Bell Labs](../docs/company/bell-labs.md) |
| 1972 | Ritchie crea il linguaggio C; Thompson riscrive Unix in C |
| 1977 | [Brian Kernighan](../docs/persons/brian-kernighan.md) co-crea AWK con Aho e Weinberger |
| 1978 | Kernighan e Ritchie pubblicano "The C Programming Language" (K&R) |
| 1979 | AT&T commercializza Unix, chiudendo il codice sorgente — impulso diretto per GNU |
| 1983 | Stallman lancia il progetto GNU. Turing Award a Thompson e Ritchie |
| 1985 | Fondazione FSF |
| 1985 | [Sun Microsystems](../docs/company/sun-microsystems.md) rilascia NFS (Network File System) come protocollo aperto — primo standard open per file sharing di rete |
| 1989 | Thompson, Pike, Ritchie iniziano Plan 9 from Bell Labs — OS successore di Unix |
| 1991 | Torvalds rilascia Linux |
| 1992 | Thompson e [Rob Pike](../docs/persons/rob-pike.md) creano UTF-8 (oggi >98% del web). Noorda (CEO Novell) fonda [Canopy Group](../docs/companies/canopy-group.md) (VC). Fondazione [S.u.S.E.](../docs/companies/suse.md) a Norimberga |
| 1993 | Ago: [Ian Murdock](../docs/persons/ian-murdock.md) (studente Purdue) fonda [Debian](../docs/foundation/debian.md). [Bob Young](../docs/persons/bob-young.md) e [Marc Ewing](../docs/persons/marc-ewing.md) fondano [Red Hat](../docs/companies/red-hat.md) a Durham, NC |
| 1994 | [Jim Clark](../docs/persons/jim-clark.md) (ex Stanford, founder SGI) e [Marc Andreessen](../docs/persons/marc-andreessen.md) (22, NCSA Mosaic) fondano [Netscape](../docs/companies/netscape.md). Noorda lascia Novell |
| 1995 | IPO Netscape (market cap $2.2B al primo giorno). [Brendan Eich](../docs/persons/brendan-eich.md) crea JavaScript in 10 giorni. Browser war vs Microsoft IE |
| 1997 | Raymond pubblica "The Cathedral and the Bazaar" |
| 1998 | Gen: Netscape rilascia il codice sorgente del browser (Eich e [Mitchell Baker](../docs/persons/mitchell-baker.md) co-fondano mozilla.org). Feb: Peterson conia "open source". Fondazione OSI (Raymond, Perens). Apr: Primo Open Source Summit (O'Reilly) |
| 1995 | [Paul Syverson](../docs/persons/paul-syverson.md) (NRL) inventa l'onion routing con Goldschlag e Reed al Naval Research Laboratory — tecnologia alla base di Tor |
| 1995 | Canopy Group finanzia Caldera Systems (distribuzione Linux). Novell vende asset Unix a Santa Cruz Operation |
| 1996 | Caldera (Noorda) lancia causa DR-DOS vs Microsoft |
| 1997 | Fondazione [SPI](../docs/foundation/spi.md) (Murdock, Perens) — umbrella legale per Debian |
| 1998 | Ratifica Debian Constitution (2 dic) — governance democratica formalizzata |
| 1999 | [Red Hat](../docs/companies/red-hat.md) IPO su NASDAQ (11 ago). Bob Young lascia CEO. AOL acquisisce Netscape per $4.2B. Clark esce con $1.2B. Barksdale fonda The Barksdale Group. De Icaza e Friedman fondano [Ximian](../docs/companies/ximian.md) |
| 1999 | Bernstein v. US: il codice crittografico e' free speech (First Amendment). Caso EFF con [Cindy Cohn](../docs/persons/cindy-cohn.md) lead attorney — precedente legale fondamentale per la distribuzione di software libero |
| 1999 | Fondazione Apache Software Foundation ([Roy T. Fielding](../docs/persons/roy-fielding.md) primo Chairman, [Jim Jagielski](../docs/persons/jim-jagielski.md), [Ben Laurie](../docs/persons/ben-laurie.md), Behlendorf tra i 21 fondatori) |
| 2001 | [Lawrence Lessig](../docs/persons/lawrence-lessig.md) (Stanford), [Hal Abelson](../docs/persons/hal-abelson.md) (MIT) e [Eric Eldred](../docs/persons/eric-eldred.md) fondano [Creative Commons](../docs/foundation/creative-commons.md) — estensione del modello copyleft dal software ai contenuti. Abelson e' co-fondatore anche della FSF (1985): il nodo MIT che collega liberta' del software e liberta' dei contenuti. [James Boyle](../docs/persons/james-boyle.md) (Duke Law) nel founding board, teorizza la "seconda enclosure" della conoscenza. Georg Greve fonda la [FSFE](../docs/foundation/fsfe.md), sister organization europea della FSF. Co-fondato capitolo italiano (Maffulli) |
| 2002 | Dic: primo set di licenze Creative Commons pubblicato (CC BY, CC BY-SA, CC0). Lessig rappresenta Eldred alla Supreme Court in *Eldred v. Ashcroft* contro il Sonny Bono Copyright Term Extension Act |
| 2003 | Gen: Supreme Court decide *Eldred v. Ashcroft* 7-2 contro Eldred — CC nasce come "ritirata strategica": se non si puo' cambiare la legge, si creano licenze alternative. [Joi Ito](../docs/persons/joi-ito.md) entra nel board CC |
| 2002 | Fielding lascia ASF chairmanship, diventa Chief Scientist a Day Software. Jagielski primo Chair Apache Incubator |
| 2000 | [Sun Microsystems](../docs/company/sun-microsystems.md) open-source OpenOffice.org (da StarOffice) e NetBeans. Settlement DR-DOS: Microsoft paga $275M a Caldera. Caldera acquista asset Unix da Santa Cruz Operation. Thompson e Kernighan lasciano Bell Labs (Thompson va in pensione, Kernighan a Princeton) |
| 2002 | [Rob Pike](../docs/persons/rob-pike.md) lascia Bell Labs per Google — inizio migrazione Unix team. Alpha di Tor rilasciata (20 set). [Roger Dingledine](../docs/persons/roger-dingledine.md) (MIT, allievo Rivest) e [Nick Mathewson](../docs/persons/nick-mathewson.md) (MIT, allievo Liskov) sviluppano la seconda generazione dell'onion routing per NRL |
| 2002 | Caldera International → [SCO Group](../docs/companies/sco-group.md) (Darl McBride CEO, Ralph Yarro Chairman) |
| 2003 | Mar: SCO causa IBM per $1B, sostiene violazione IP Unix in Linux. Novell controcausa: possiede ancora i copyright Unix. Microsoft acquista licenze SCOsource. Fondazione [Mozilla Foundation](../docs/foundation/mozilla-foundation.md) (Baker, Kapor founding chair $300K). Novell acquisisce [Ximian](../docs/companies/ximian.md) (ago) e SUSE (nov) |
| 2004 | Noorda licenzia Yarro dal Canopy Group per self-dealing |
| 2005 | Torvalds crea Git. Fondazione Open Invention Network. Sun open-source OpenSolaris (kernel sotto CDDL), ZFS e GlassFish |
| 2006 | [Ken Thompson](../docs/persons/ken-thompson.md) entra a Google come Distinguished Engineer — riunisce lo Unix team (Pike gia' dal 2002). Sun open-source Java sotto GPL (~9M sviluppatori). Report UE: Sun piu' grande contributore corporate open source al mondo. Fondazione [The Tor Project](../docs/foundation/tor-project.md) Inc. come 501(c)(3). Co-fondatori: Dingledine, Mathewson, Syverson. [McNealy](../docs/persons/scott-mcnealy.md) lascia CEO Sun dopo 22 anni, [Jonathan Schwartz](../docs/persons/jonathan-schwartz.md) CEO |
| 2007 | Fondazione Linux Foundation (Zemlin ED) |
| 2006 | Ben Laurie entra in Google come Director of Security |
| 2008 | Gen: [Sun Microsystems](../docs/company/sun-microsystems.md) acquisisce [MySQL AB](../docs/company/mysql-ab.md) per ~$1B. [Marten Mickos](../docs/persons/marten-mickos.md) SVP Sun, lascia mar 2009. [Michael Widenius](../docs/persons/michael-widenius.md) guadagna €16.6M. Co-fonda [OpenOcean](../docs/private-equity/openocean.md) VC con Patrik Backman |
| 2008 | [Joel Spolsky](../docs/persons/joel-spolsky.md) (IDF → [Yale](../docs/university/yale.md) → [Microsoft](../docs/company/microsoft.md) → [Fog Creek](../docs/companies/fog-creek-software.md)) e [Jeff Atwood](../docs/persons/jeff-atwood.md) (blog Coding Horror) co-fondano [Stack Overflow](../docs/companies/stack-overflow.md) — piattaforma Q&A che diventa l'infrastruttura di conoscenza per 100M+ dev/mese. Fondazione GitHub. Behlendorf advisor campagna Obama. [Rackspace](../docs/companies/rackspace.md) IPO al NYSE ($187.5M) |
| 2009 | Thompson, Pike e Griesemer lanciano Go a Google — ultimo prodotto della tradizione Unix/Bell Labs, futuro linguaggio di Docker/Kubernetes. Widenius lascia Sun, fonda Monty Program Ab, forka MySQL in [MariaDB](../docs/company/mariadb.md) (nome dalla figlia Maria). Mickos EIR a [Benchmark](../docs/private-equity/benchmark-capital.md) e [Index Ventures](../docs/private-equity/index-ventures.md). Behlendorf advisor alla Casa Bianca (OSTP, open data/APIs). O'Reilly organizza Gov 2.0 Summit → [Jennifer Pahlka](../docs/persons/jennifer-pahlka.md) fonda [Code for America](../docs/foundation/code-for-america.md) |
| 2010 | Lug: Rackspace e NASA lanciano [OpenStack](../docs/foundation/openstack.md) a OSCON Portland. Prima release "Austin" (ott). Adobe acquisisce Day Software (Fielding diventa Senior Principal Scientist) |
| 2011 | Morte di [Dennis Ritchie](../docs/persons/dennis-ritchie.md) (~12 ott), creatore del C e co-creatore di Unix — una settimana dopo Steve Jobs, nell'indifferenza mediatica. Behlendorf CTO del World Economic Forum a Ginevra (report a Klaus Schwab). Jagielski board OSI. [Dmytro Zaporozhets](../docs/persons/dmitriy-zaporozhets.md) e Valery Sizov creano [GitLab](../docs/companies/gitlab.md) come progetto open-source a Kharkiv (Ucraina) |
| 2012 | [Jeff Atwood](../docs/persons/jeff-atwood.md) lascia Stack Overflow |
| 2013 | Atwood fonda [Discourse](../docs/companies/discourse.md) (Civilized Discourse Construction Kit) — forum open source, funding [Greylock](../docs/private-equity/greylock.md), First Round, SV Angel. Pahlka Deputy CTO Casa Bianca (Obama). Co-fonda United States Digital Service (USDS) |
| 2012 | Dic: Widenius, [David Axmark](../docs/persons/david-axmark.md) e Allan Larsson fondano la [MariaDB Foundation](../docs/foundation/mariadb-foundation.md) — non-profit (Delaware) per salvaguardare MariaDB. Mickos board [Nokia](../docs/company/nokia.md) (2012-15) |
| 2012 | [Mitchell Hashimoto](../docs/persons/mitchell-hashimoto.md) (UW CS, creatore di Vagrant) fonda [HashiCorp](../docs/companies/hashicorp.md) a San Francisco. [Armon Dadgar](../docs/persons/armon-dadgar.md) (UW CS, iscritto a 16 anni, origini iraniane) entra come co-fondatore nel 2013. Set: OpenStack Foundation fondata come ente indipendente ([Jonathan Bryce](../docs/persons/jonathan-bryce.md) ED). Board: 1/3 Platinum, 1/3 Gold, 1/3 Individual Members |
| 2011 | [Attachmate](../docs/companies/attachmate.md) (PE: Golden Gate Capital, Francisco Partners, Thoma Bravo) acquisisce [Novell](../docs/companies/novell.md) per $2.2B. CPTN Holdings (Microsoft, Apple, Oracle, EMC) compra 882 brevetti Novell per $450M. SUSE separata come business unit. De Icaza e Friedman co-fondano [Xamarin](../docs/companies/xamarin.md) (cross-platform mobile dev con C#) dopo abbandono Mono |
| 2015 | Fondazione CNCF (sotto Linux Foundation). Fondazione [Hyperledger](../docs/foundation/hyperledger.md) (Linux Foundation, 30 founding members tra cui IBM, JP Morgan, SWIFT). Fondazione [ConsenSys](../docs/companies/consensys.md) (Lubin, ex-Goldman Sachs). Fondazione [Niskanen Center](../docs/think-tank/niskanen-center.md) (Jerry Taylor, scissione Cato Institute) |
| 2016 | Microsoft acquisisce Xamarin (de Icaza e Friedman entrano come executives). [Alexandr Wang](../docs/persons/alexandr-wang.md) (19 anni, dropout MIT) fonda [Scale AI](../docs/companies/scale-ai.md). [Apollo Global Management](../docs/private-equity/apollo-global.md) acquisisce Rackspace per $4.3B (take private) |
| 2014 | [Micro Focus](../docs/companies/micro-focus.md) acquisisce Attachmate Group per $1.2B. SUSE scorporata come entita' distinta. [Sid Sijbrandij](../docs/persons/sid-sijbrandij.md) e [Zaporozhets](../docs/persons/dmitriy-zaporozhets.md) fondano [GitLab Inc.](../docs/companies/gitlab.md) |
| 2007 | [Dwight Merriman](../docs/persons/dwight-merriman.md), [Eliot Horowitz](../docs/persons/eliot-horowitz.md) e [Kevin Ryan](../docs/persons/kevin-ryan.md) (trio ex-[DoubleClick](../docs/companies/doubleclick.md)) fondano 10gen (poi [MongoDB](../docs/companies/mongodb.md)). Investimento [In-Q-Tel](../docs/companies/in-q-tel.md) (CIA) |
| 2008 | [Tom Preston-Werner](../docs/persons/tom-preston-werner.md), [Chris Wanstrath](../docs/persons/chris-wanstrath.md), [P.J. Hyett](../docs/persons/pj-hyett.md) e Scott Chacon fondano [GitHub](../docs/companies/github.md) (ex consulenti RoR e sviluppatori CNET) |
| 2014 | Preston-Werner lascia da CEO GitHub dopo accuse di harassment; Wanstrath torna CEO |
| 2017 | [MongoDB](../docs/companies/mongodb.md) IPO su NASDAQ (MDB, $192M, val. $1.6B). [Dev Ittycheria](../docs/persons/dev-ittycheria.md) CEO dal 2014 |
| 2018 | Microsoft acquisisce GitHub per $7.5B (Wanstrath → Technical Fellow, Friedman CEO). MongoDB passa a SSPL (prima azienda, crea il precedente). [EQT AB](../docs/private-equity/eqt-partners.md) acquisisce [SUSE](../docs/companies/suse.md) da Micro Focus per $2.535B |
| 2015 | Dic: morte di [Ian Murdock](../docs/persons/ian-murdock.md), fondatore Debian, a San Francisco (42 anni) |
| 2017 | Oracle trasferisce Java EE alla [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) → diventa Jakarta EE. De facto standard enterprise Java sotto governance Eclipse |
| 2019 | IBM acquisisce [Red Hat](../docs/companies/red-hat.md) per $34B — piu' grande acquisizione software della storia. Stallman si dimette da FSF. Sanzioni USA su Huawei. [Melissa Di Donato](../docs/persons/melissa-di-donato.md) (ex CRO SAP Cloud) nominata CEO SUSE — prima donna alla guida |
| 2020 | [Eclipse Foundation](../docs/foundation/eclipse-foundation.md) si ri-incorpora come AISBL in Belgio (Bruxelles) — unica grande fondazione open source con sede legale nell'UE. OpenStack Foundation si rinomina [OpenInfra Foundation](../docs/foundation/openinfra-foundation.md), scope ampliato a Kata Containers, StarlingX, Zuul. Rackspace re-IPO al Nasdaq (Apollo mantiene ~65%). [Priyanka Sharma](../docs/persons/priyanka-sharma.md) nominata GM della CNCF (Stanford CS, ex Google/LightStep/GitLab). Fondazione [OpenSSF](../docs/foundation/openssf.md) (ago, fusione CII+OSSC+JOSSI; founding members: GitHub, Google, IBM, JPMorgan Chase, Microsoft, NCC Group, OWASP, Red Hat). Giu: fondazione [OpenAtom Foundation](../docs/foundation/openatom-foundation.md) a Beijing — prima fondazione open source cinese, co-fondata da Alibaba, Baidu, Huawei, Inspur, Qihoo 360, Tencent, China Merchants Bank; sotto supervisione MIIT |
| 2010 | Gen: [Oracle](../docs/company/oracle.md) completa acquisizione Sun Microsystems ($7.4B) — MySQL passa a Oracle. Mickos diventa CEO Eucalyptus Systems. Giuria unanime: Novell non trasferi' copyright Unix a SCO. Linux legittimato definitivamente |
| 2021 | Giu: [Prosus](../docs/companies/prosus.md) ([Naspers](../docs/companies/naspers.md)) acquisisce [Stack Overflow](../docs/companies/stack-overflow.md) per $1.8B. Investitori pre-exit: [Andreessen Horowitz](../docs/private-equity/andreessen-horowitz.md), [Index Ventures](../docs/private-equity/index-ventures.md), [GIC](../docs/swf/gic.md), [Silver Lake](../docs/private-equity/silver-lake.md). Spolsky diventa Chairman. Ott: [GitLab](../docs/companies/gitlab.md) IPO su NASDAQ (GTLB, val. ~$11B, raccolta ~$650M) — Zaporozhets presente al NASDAQ per la cerimonia. Nov: Zaporozhets lascia GitLab dopo 10 anni esatti; istituito "DZ Award". Nov: settlement finale SCO vs IBM ($14.25M al trustee). Stallman rientra nel board FSF (controversia). Riforme governance FSF: union seat, Board Agreement, Code of Ethics. Lancio GitHub Copilot. [Elastic](../docs/company/elastic.md) cambia licenza Elasticsearch a SSPL → AWS fork come [OpenSearch](../docs/foundation/opensearch.md) (Apache 2.0). Friedman lascia GitHub, fonda NFDG con [Daniel Gross](../docs/persons/daniel-gross.md) (AI venture fund, poi $1.1B). Wang (Scale AI) diventa piu' giovane miliardario self-made (24 anni). SUSE IPO alla Borsa di Francoforte (mag, €30/azione) — tra le piu' grandi IPO open source europee |
| 2022 | Gen: White House OSS Security Summit post-Log4Shell (OpenSSF + Linux Foundation convocati). Mag: secondo summit, $30M pledges da 37 aziende (Amazon, Google, Intel, Microsoft, VMware). Zoë Kooyman Executive Director FSF. Class action Doe v. GitHub (Copilot). Sovereign Tech Fund (Germania). Linux Foundation Europe |
| 2023 | HashiCorp abbandona licenza open (Terraform -> BSL). Fork OpenTofu. Svizzera adotta legge EMBAG: "Public Money, Public Code" by default (vittoria campagna FSFE). EQT ritira SUSE dal mercato (delisting). [Dirk-Peter van Leeuwen](../docs/persons/dirk-peter-van-leeuwen.md) (ex Red Hat, 20 anni) nuovo CEO SUSE. Di Donato → Chair/CEO Kyriba + board Porsche + NED JP Morgan Europe. [OpenText](../docs/companies/opentext.md) acquisisce Micro Focus per $5.8B (eredita Novell, NetIQ, Attachmate). [Cheng Xiaoming](../docs/persons/cheng-xiaoming.md) (ex-MIIT, ex-Huawei SVP) diventa Chairman OpenAtom Foundation — consolida revolving door partito-industria nell'open source cinese |
| 2024 | Backdoor XZ Utils (CVE-2024-3094). Apr: IBM annuncia acquisizione HashiCorp per $6.4B ($35/azione). Redis -> SSPL, fork Valkey. EU Cyber Resilience Act. FSF: tre nuovi board members (Gilmore, Pievatolo, Haralanova). Laurie vince Levchin Prize. Hyperledger rebrand → LF Decentralized Trust (100+ membri). ConsenSys fa causa a SEC per classificazione ETH; SEC accusa ConsenSys per MetaMask Staking. Set: AWS trasferisce [OpenSearch](../docs/foundation/opensearch.md) alla [Linux Foundation](../docs/foundation/linux-foundation.md) come OpenSearch Software Foundation (premier: AWS, SAP, Uber; general: Aiven, Atlassian, Canonical, DigitalOcean, +6). [Elastic](../docs/company/elastic.md) risponde aggiungendo AGPL v3 — primo "reversal" nelle licensing wars. [Chetan Puttagunta](../docs/persons/chetan-puttagunta.md) ([Benchmark](../docs/private-equity/benchmark-capital.md)) diventa Chairman Elastic; [Ashutosh Kulkarni](../docs/persons/ashutosh-kulkarni.md) CEO. Dic: [Mitchell Hashimoto](../docs/persons/mitchell-hashimoto.md) rilascia Ghostty 1.0 (terminal emulator in Zig, dopo 2 anni di beta privata). **Disputa WordPress**: set: [Mullenweg](../docs/persons/matt-mullenweg.md) definisce [WP Engine](../docs/company/wp-engine.md) "cancer to WordPress", blocca accesso WordPress.org (>1M siti interrotti); ott: WP Engine ([Silver Lake](../docs/private-equity/silver-lake.md) majority) fa causa ad [Automattic](../docs/company/automattic.md) per estorsione e abuso di potere; dic: tribunale emette ingiunzione pro-WP Engine. >150 dipendenti lasciano Automattic. BlackRock marca giu' investimento Automattic del 10% |
| 2024 | Wanstrath e Andreas Kling co-fondano Ladybird Browser Initiative (browser indipendente, no corporate deals, release prevista estate 2026). Dic: [Sid Sijbrandij](../docs/persons/sid-sijbrandij.md) (diagnosi osteosarcoma 2023) cede CEO GitLab a [Bill Staples](../docs/persons/bill-staples.md) (ex New Relic), diventa Executive Chair |
| 2025 | Feb: IBM completa acquisizione [HashiCorp](../docs/companies/hashicorp.md); [Armon Dadgar](../docs/persons/armon-dadgar.md) CTO in IBM Software. Ghostty diventa nonprofit via Hack Club ([Mitchell Hashimoto](../docs/persons/mitchell-hashimoto.md)). Gen: Wang (Scale AI) presente all'inaugurazione Trump e al WEF Davos. De Icaza lascia Microsoft (mar 2022), fonda Xibbon (game dev tools, Boston). Mar: [OpenInfra Foundation annuncia ingresso nella Linux Foundation](../docs/foundation/openinfra-foundation.md) come member foundation (approvazione unanime entrambi i board). Ian Kelling presidente FSF (primo staff-president). Maffulli si dimette da OSI (set). Deb Bryant interim ED OSI. Elezioni board OSI contestate. FSFE porta caso Apple alla CGUE. EuroStack (Merz). Feb: [WP Engine](../docs/company/wp-engine.md) class action da clienti per abuso di potere Mullenweg/Automattic. Gen: Automattic riduce contributi WordPress open source da ~4.000 ore/settimana a 45. [HeroDevs](../docs/company/herodevs.md) acquisisce Xeol (NYC, ex YC, EOL detection). Giu: HeroDevs lancia $20M Sustainability Fund. Lug: [PSG Equity](../docs/private-equity/psg-equity.md) investe $125M in HeroDevs (tra i piu' grandi first round nello Utah). FSF celebra 40esimo. USDS → DOGE. Baker lascia board Mozilla (feb). ConsenSys prepara IPO con JPMorgan e Goldman Sachs. Giu: Priyanka Sharma lascia CNCF dopo 5 anni; [Jonathan Bryce](../docs/persons/jonathan-bryce.md) nominato ED Cloud & Infrastructure LF + ED CNCF + ED OpenInfra (triplo ruolo, unifica cloud VM e containers sotto un'unica leadership), [Chris Aniszczyk](../docs/persons/chris-aniszczyk.md) CTO Cloud & Infrastructure. Ago: Dohmke lascia GitHub; Microsoft integra GitHub in CoreAI division senza CEO autonomo. Set: Gajen Kandiah nominato CEO Rackspace. Ott: Preston-Werner annuncia [PWV](../docs/private-equity/preston-werner-ventures.md) Fund I ($100M, pre-seed/seed AI e software). Giu: Meta acquisisce 49% di [Scale AI](../docs/companies/scale-ai.md) (~$14.3B); [Alexandr Wang](../docs/persons/alexandr-wang.md) diventa primo Chief AI Officer di Meta, head of Meta Superintelligence Labs; [Nat Friedman](../docs/persons/nat-friedman.md) VP Product & Applied Research MSL. Ott: [Omkhar Arasaratnam](../docs/persons/omkhar-arasaratnam.md) lascia OpenSSF per LinkedIn (Distinguished Engineer for Security). Nov: [CJ Desai](../docs/persons/cj-desai.md) (ex ServiceNow COO, ex Cloudflare, board [MSCI](../docs/companies/msci.md)) succede a Ittycheria come CEO [MongoDB](../docs/companies/mongodb.md); Ittycheria resta Board advisor. [Eliot Horowitz](../docs/persons/eliot-horowitz.md) (ex CTO MongoDB) raccoglie $30M Serie C per [Viam](../docs/companies/viam.md) (robotica, USV lead) |
| 2026 | Feb: [Thomas Dohmke](../docs/persons/thomas-dohmke.md) lancia [Entire](../docs/companies/entire.md) con $60M seed (record dev tools), valutazione $300M. Lead: Felicis. Partecipano M12 (Microsoft Ventures), Madrona, Basis Set. Angel investors: [Jerry Yang](../docs/persons/jerry-yang.md) (co-fondatore Yahoo, Chair Stanford Board, CFR, Brookings China Advisory), [Garry Tan](../docs/persons/garry-tan.md) (CEO Y Combinator). Primo prodotto: Checkpoints (open source, tracciabilita' codice AI-generated, integra Claude Code e Gemini CLI). Board OSI sospende elezioni, ridisegna processo elettorale |

---

## Fonti

### Istituzionali
- [Open Source Initiative - History](https://opensource.org/about/history-of-the-open-source-initiative)
- [Linux Foundation](https://www.linuxfoundation.org)
- [Free Software Foundation](https://www.fsf.org)
- [Apache Software Foundation](https://www.apache.org)
- [Creative Commons](https://creativecommons.org/)

### Analisi
- [Linux Foundation - State of Open Source Funding 2024](https://www.linuxfoundation.org/blog/understanding-the-state-of-open-source-funding-in-2024)
- [Jamestown Foundation - Open-Source Technology and PRC National Strategy](https://jamestown.org/program/open-source-technology-and-prc-national-strategy-part-i/)
- [Real Instituto Elcano - Can open source secure Europe's digital infrastructure?](https://www.realinstitutoelcano.org/en/analyses/can-open-source-secure-europes-digital-infrastructure/)

### Casi Legali
- [Joseph Saveri Law Firm - GitHub Copilot Litigation](https://www.saverilawfirm.com/our-cases/github-copilot-intellectual-property-litigation)
- [XZ Utils Backdoor - Wikipedia](https://en.wikipedia.org/wiki/XZ_Utils_backdoor)

### WordPress / WP Engine / Automattic
- [TechCrunch - WordPress vs WP Engine drama explained](https://techcrunch.com/2025/01/12/wordpress-vs-wp-engine-drama-explained/)
- [CNBC - WordPress CEO goes nuclear on Silver Lake, WP Engine](https://www.cnbc.com/2024/10/05/wordpress-ceo-matt-mullenweg-goes-nuclear-on-silver-lake-wp-engine-.html)
- [CEO Today - Mullenweg: Biggest Failure, $7.5B Crisis](https://www.ceotodaymagazine.com/2025/10/matt-mullenweg-tumblr-failure-wp-engine-legal-war-valuation-crisis/)

### HeroDevs / Sostenibilita' Open Source
- [PR Newswire - HeroDevs $20M Sustainability Fund](https://www.prnewswire.com/news-releases/herodevs-launches-20-million-sustainability-fund-for-open-source-creators-to-secure-end-of-life-software-302488703.html)
- [HeroDevs - $125M PSG Investment](https://www.herodevs.com/blog-posts/herodevs-announces-125-million-strategic-growth-investment-from-psg)
- [Utah Business - How Aaron Frost founded HeroDevs](https://www.utahbusiness.com/entrepreneurship/2025/04/24/aaron-frost-founder-herodevs-software-engineers/)

### Eventi
- [OpenSSF - XZ Backdoor CVE-2024-3094](https://openssf.org/blog/2024/03/30/xz-backdoor-cve-2024-3094/)

---

*Ultimo aggiornamento: Febbraio 2026*
