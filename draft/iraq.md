Riepilogo Iraq Power Map

  Ho completato l'analisi e l'aggiornamento del database. Ecco cosa e' stato fatto:

  Entita' Aggiunte al Database

  Organizzazioni (9)
  ┌──────────────────────┬─────────────────────────────────┬────────────┐
  │          ID          │              Nome               │    Tipo    │
  ├──────────────────────┼─────────────────────────────────┼────────────┤
  │ governo-iraq         │ Government of Iraq              │ Government │
  ├──────────────────────┼─────────────────────────────────┼────────────┤
  │ cpa-iraq             │ Coalition Provisional Authority │ Agency     │
  ├──────────────────────┼─────────────────────────────────┼────────────┤
  │ office-special-plans │ Office of Special Plans         │ Agency     │
  ├──────────────────────┼─────────────────────────────────┼────────────┤
  │ hashd-al-shaabi      │ Popular Mobilization Forces     │ Defense    │
  ├──────────────────────┼─────────────────────────────────┼────────────┤
  │ halliburton          │ Halliburton                     │ Company    │
  ├──────────────────────┼─────────────────────────────────┼────────────┤
  │ kbr                  │ KBR Inc                         │ Company    │
  ├──────────────────────┼─────────────────────────────────┼────────────┤
  │ bechtel              │ Bechtel Corporation             │ Company    │
  └──────────────────────┴─────────────────────────────────┴────────────┘
  Persone (13)
  ┌─────────────────────────┬──────────────┬──────────────────────────┐
  │           ID            │ Nazionalita' │       Ruolo Chiave       │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ nouri-al-maliki         │ Iraq         │ PM 2006-2014             │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ haider-al-abadi         │ Iraq         │ PM 2014-2018             │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ mustafa-al-kadhimi      │ Iraq         │ PM 2020-2022             │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ mohammed-shia-al-sudani │ Iraq         │ PM 2022-                 │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ ibrahim-al-jaafari      │ Iraq         │ PM 2005-2006             │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ jalal-talabani          │ Iraq         │ Presidente 2005-2014     │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ ahmed-chalabi           │ Iraq         │ Governing Council        │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ ayad-allawi             │ Iraq         │ PM provvisorio 2004      │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ ali-sistani             │ Iraq         │ Grande Ayatollah         │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ abu-mahdi-al-muhandis   │ Iraq         │ Deputy PMF (ucciso 2020) │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ douglas-feith           │ USA          │ Capo OSP                 │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ jay-garner              │ USA          │ Primo amministratore CPA │
  ├─────────────────────────┼──────────────┼──────────────────────────┤
  │ erik-prince             │ USA          │ Fondatore Blackwater     │
  └─────────────────────────┴──────────────┴──────────────────────────┘
  Eventi (7)
  - 2003-invasione-iraq
  - 2003-cpa-costituzione
  - 2003-de-baathification
  - 2003-iraqi-army-dissolution
  - 2007-nisour-square
  - 2014-isis-mosul
  - 2020-assassinio-soleimani

  Connessioni Chiave Esistenti

  Il database ora documenta le connessioni tra:
  - Neoconservatori PNAC → Invasione (Wolfowitz, Feith, Perle, Khalilzad)
  - CPA → Occupazione (Bremer, Garner, Senor, Chalabi, Allawi)
  - Iran/IRGC → PMF (Soleimani, Muhandis)
  - Contractors → Ricostruzione/Sicurezza (Cheney-Halliburton, Prince-Blackwater)


  - Organization:Party: baath-party
    - founded: 1951
    - dissolved: 2003
    - status: banned
    - ideology: Ba'athism, Arab nationalism, Arab socialism

  Persone Create (stub)
  ┌────────────────────────┬────────────────────────┬───────────────┬──────────────┐
  │           ID           │          Nome          │ Nascita-Morte │ Nazionalita' │
  ├────────────────────────┼────────────────────────┼───────────────┼──────────────┤
  │ ahmed-hassan-al-bakr   │ Ahmed Hassan al-Bakr   │ 1914-1982     │ IRQ          │
  ├────────────────────────┼────────────────────────┼───────────────┼──────────────┤
  │ izzat-ibrahim-al-douri │ Izzat Ibrahim al-Douri │ 1942-2020     │ IRQ          │
  ├────────────────────────┼────────────────────────┼───────────────┼──────────────┤
  │ tariq-aziz             │ Tariq Aziz             │ 1936-2015     │ IRQ          │
  ├────────────────────────┼────────────────────────┼───────────────┼──────────────┤
  │ michel-aflaq           │ Michel Aflaq           │ 1910-1989     │ SYR          │
  └────────────────────────┴────────────────────────┴───────────────┴──────────────┘
  Relazioni Create

  AFFILIATED_WITH baath-party:
  ┌────────────────────────┬─────────┬───────────┐
  │        Persona         │  Ruolo  │  Periodo  │
  ├────────────────────────┼─────────┼───────────┤
  │ michel-aflaq           │ founder │ 1947-1989 │
  ├────────────────────────┼─────────┼───────────┤
  │ tariq-aziz             │ member  │ 1958-2003 │
  ├────────────────────────┼─────────┼───────────┤
  │ ahmed-hassan-al-bakr   │ leader  │ 1968-1979 │
  ├────────────────────────┼─────────┼───────────┤
  │ saddam-hussein         │ leader  │ 1979-2003 │
  ├────────────────────────┼─────────┼───────────┤
  │ izzat-ibrahim-al-douri │ leader  │ 1979-2003 │
  └────────────────────────┴─────────┴───────────┘
  AFFILIATED_WITH governo-iraq:
  ┌──────────────────────┬──────────┬─────────────────────────────┐
  │       Persona        │  Ruolo   │            Note             │
  ├──────────────────────┼──────────┼─────────────────────────────┤
  │ ahmed-hassan-al-bakr │ leader   │ President 1968-1979         │
  ├──────────────────────┼──────────┼─────────────────────────────┤
  └──────────────────────┴──────────┴─────────────────────────────┘
  Scheda Creata

  - docs/party/baath-party.md

EVENTI:
[v] 1980-iran-iraq-war
[v] 1990-invasione-kuwait
[v] 2003-invasione-iraq
2006-esecuzione-saddam


  rendon-group
  al-bilad-islamic-bank

  Bunnatine Greenhouse (whistleblower)

Ho 3 @docs/events 1980-iran-iraq-war, 1990-invasione-kuwait e 2003-invasione-iraq. Puoi aggiornare uno o tutti gli eventi se ritieni di avere nuove informazioni utili ed importanti