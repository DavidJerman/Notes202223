# Umetna inteligenca kolokvij 2

## Predstavitev znanja

+ Znanje predstavimo z **izjavami (dejstva)**, iz njih tvorimo **sklepe**.
+ V računalništvu jim rečemo **stavki**. **Baza znanja** pa je množica vseh teh stavkov.
+ **Logika** je formalna predstavitev znanja.
+ Sintaksa vs semantika
+ Resničen vs neresničen stavek
+ Logično sledi == entails

### Algoritem sklepanja

+ **Algoritem sklepanja** iz baze znanja izpelje nove stavke
+ Če izpelje samo stavke, ki logično sledijo je **smiseln**
+ Če izpelje vsak možen stavek je **poln**

### Sintaksa - pojmi

+ Boolova logika - **resničnostne vrednosti**
+ Atomarni stavek - nedeljiv stavek
+ Izjave zapišemo z **velikimi črkami**
+ Ne-atomarni stavki sestavljeni iz atomarnih stavkov in **logičnih povezav**

### Logične povezave

+ **Konjunkcija** - in
+ **Disjunkcija** - ali
+ **Implikacija** - če potem
+ **Ekvivalenca** - če in samo če
+ **Negacija** - ne
+ **Prioriteta** - negacija, konjunkcija, disjunkcija, implikacija, ekvivalenca

### Semantika - pojmi

+ Logične vrednost so lahko **resnične** ali **neresnične** (true, false)
+ **Interpretacija** je dodelitev logičnih fiksnih vrednosti bazi znanja - torej neko
  besedilo v katerem zamenjamo vse izjave z resničnimi ali neresničnimi vrednostmi
+ **Pravilnostna tabela**

### Zakoni

+ **Komutativnost** - A in B == B in A
+ **Asociativnost** - (A in B) in C == A in (B in C)
+ **Distributivnost** - A in (B ali C) == (A in B) ali (A in C)
+ **De Morganovi zakoni** - ne (A in B) == ne A ali ne B
+ **Idempotentnost** - A in A == A
+ **Absorbcija** - A in (A ali B) == A
+ **Dvojna negacija** - ne (ne A) == A
+ **Implikacija** - A če potem B == ne A ali B
+ **Kontrapozicija** - A če potem B == ne B če potem ne A

### Veljavnost in izpolnjivost

+ **Tavtologija** - izjava, ki je vedno resnična
+ **Protislovje** - izjava, ki je vedno neresnična
+ Stavek je **izpolnjiv**, če obstaja interpretacija, ki ga naredi resničnega

### Pravila sklepanja

+ **Modus ponens** - A če potem B, A, torej B
+ **Modus tolens** - A če potem B, ne B, torej ne A
+ **Dokaz s protislovjem** - A, ne A, torej B

+ Aksiomi --> izpeljani stavki (teoremi) --> dokažemo z dokazom zgoraj

### Resolucija

+ **Resolucija** je pravilo sklepanja, ki se uporablja pri avtomatskem sklepanju
+ Bazira na **klavzulah** - to so disjunkcije atomarnih stavkov (literalov)
  Skratka važno je, da se v stavkih nahajajo samo disjunkcije

#### Resolucijsko pravilo

+ A1 ali A2 ali ... ali An
+ ne A1 ali B1 ali B2 ali ... ali Bm
+ -----------------------------
+ sledi: A2 ali A3 ali ... ali An ali B1 ali B2 ali ... ali Bm

Temu rezultatu pravimo **resolventa**.

Primer:
(A ali B) in (ne A ali C) --> (B ali C)

Rezultat se lahko preveri tudi z *resničnostno tabelo*.

![Resolucija](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-2023-05-14-184547.png)

### Predikatna logika prvega reda

#### Simboli

+ **Konstante** - A, B, Franc, Maribor, ... - dejanski objekti
+ **Simboli spremenljivk** - x, y, z, ... - splošni objekti
+ **Predikatni simboli** - P, Q, R, Rdeč, Sin ... - lastnosti/relacije med objekti
+ **Funkcijski simboli** - f, g, h, ... - preslikave med objekti

Primeri:

- Napadalec(Messi)
- Velikost(Maribor, 95.000)

#### Atomarni stavek

Atomarni stavek je sestavljen iz **predikata** in **argumentov**. Argumenti so lahko
konstante, spremenljivke ali funkcije - **termi**.

Tudi atomarne stavke lahko povezujemo z logičnimi povezavami.

Vsak atomarni stavek pa še ni izjava. Za izjavo mora veljati:

- Vsi argumenti so **vezani** oz. **kvantificirani**, sicer so **proste spremenljivke**
- stavki z vezanimi spremenljivkami so **zaprti**

Da so kvantificirane pomeni, da se vezane na enega izmed kvantifikatorjev.

#### Kvantifikatorja

+ **Univerzalni kvantifikator** - za vse x velja P(x) - P(x) je resničen za vse x
+ **Egzistenčni kvantifikator** - obstaja x, da velja P(x) - P(x) je resničen za vsaj en x

#### Ostalo

* Pravilno oblikovani stavki - zapisani v sintaksi predikatne logike prvega reda
* Predikatna logika drugega reda - spremenljivke lahko predstavljajo predikate - to je v bistvu samo bolj napredno

PAZI NA VRSTI RED KVANTIFIKATORJEV!

ARGUMENT PREDIKATA NE SME BITI PREDIKAT!

![Nepravilno tvorjeni stavki](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-18-17-49-27.png)

#### Substitucija

+ **Substitucija** je zamenjava spremenljivk v stavku z termi
+ Primer: P(x) --> P(f(x)), kjer x/f(x) - substitucija s1

#### Kompozicija

+ **Kompozicija** samo pomeni, da imamo več substitucij zaporedoma
+ Najprej s2 uporabiš na s1, nato pa prišteješ s1 pare iz s2, ki jih še ni
+ Primer:

![Kompozicija](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-18-17-57-13.png)

#### Unifikacija

+ **Unifikacija** je postopek, ki nam omogoča, da stavke naredimo identične
+ Primer: P(x, y) in P(f(z), g(z)) --> P(f(z), g(z)) in P(f(z), g(z))
+ Skratka ideja je, da poiščemo takšne substitucije, da bosta stavka identična

+ Najsplošnejši unifikator - unifikator z najmanj zamenjavami
+ Množica izrazov je unifikabilna, če obstaja unifikator, ki to množico naredi enočlensko - torej, da so si vsi
  med sabo enaki

#### Pretvorba v klavzulsko obliko

Potrebno zato, da lahko uporabimo algoritem sklepanja. Pri tem nekaj informacije izgubimo.

Za zgled glej prosojnico stran 35.

##### Korak 1

Izločimo simbole implikacije in ekvivalence.

![Korak 1](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-18-18-08-48.png)

![Korak 1](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-18-18-08-59.png)

##### Korak 2

Premaknemo negacije k atomarnim izrazom - De Morganov zakon + kvantifikatorji.

##### Korak 3

Standardizacija ali preimenovanje spremenljivk.
Skratka poskrbimo, da ne pride do kolizije spremenljivk.

##### Korak 4

Izločitev eksistenčnih kvantifikatorjev.

1. Če eksistenčni kvantifikator ni znotraj območja univerzalnega kvantifikatorja, ga zamenjamo s Skolemovo konstanto.
2. Če je eksistenčni kvantifikator znotraj območja univerzalnega kvantifikatorja, ga zamenjamo s Skolemovo funkcijo.

##### Korak 5

Pretvorba v prefiksno obliko. Vse univerzalne kvantifikatorje postavimo na začetek stavka.

##### Korak 6

Postavitev matrike v konjuktivno normalno obliko.
Torej gre za zapis, kjer je matrika zapisana kot konjunkcija končne množice disjunkcij literalov.
Torej nekaj takega:

![Konjuktivna normalna oblika](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-18-18-17-47.png)

Uporabimo pravilo distributivnosti in podobno.

##### Korak 7

Izločitev univerzalnih kvantifikatorjev.

##### Korak 8

Izločitev simbolov konjunkcije. Dobimo množico klavzul.

##### Korak 9

Standardizacija spremenljivk narazen.
Ideja je, da poskrbimo, da se nobena spremenljivka v različnih klavzulah ne pojavi večkrat.

### Splošna resolucija

+ Gre za pravilo sklepanja nad stavki s spremenljivkami.
