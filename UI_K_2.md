# Umetna inteligenca kolokvij 2

## 4. Predstavitev znanja

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

![Splošna resolucija](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-20-10-49-48.png)

![Splošna resolucija](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-20-10-54-05.png)

Glej prosojnico stran 44+ za primer.

### Uporaba predikatne logike

+ Dokazovanje teoremov (avtomatsko sklepanje)
+ Planiranje

Aksiom --(sklepanje z resolucijo)--> ciljni stavek / ciljna formula / teorem

Neustrezna resolucija lahko zakasni sklepanje, ne pa ga nujno ustavi.

#### Zgled

Prosojnica stran 56 in 57.

#### Slabosti

+ Veliko časa - eksponentni časovni potek
+ Opis znanja zahteva veliko truda
+ Če se informacij ne da predstaviti v obliki stavkov, potem ne moremo uporabiti predikatne logike

#### Uporaba predikatne logike

+ Planiranje - recimo kako bo robot nekaj naredil - potrebno spreminjanje stanja

## 5. Sklepanje v predikatni logiki

### Resolucijska ovržba

+ Enako **dokazu s protislovjem**.
+ Če W sledi iz S, torej velja, da če je S resničen, W ne more biti neresničen. Želimo priti do protislovja.

#### Dokaz z resolucijsko ovržbo

Imamo stavek S => W, kjer je W ciljni stavek, ki ga želimo dokazati.
Tako postopek sledi:

+ Predpostavimo, da je W neresničen.
+ Pokažemo, da S unija negacija W vodi v protislovje.
+ Ker so S resnični, sklepamo, da je W resničen.

Pred izvedbo stavke pretvorimo v klavzulsko obliko. Tej množici rečemo **temeljna množica**.
Izbiro dveh klavzul, s katerima lahko izračunamo resolvento, imenujemo **kontrolna strategija**.

#### Primer

Imamo sledečo množico stavkov:

+ Ob nekaterih dnevih je sončno in ni toplo.
+ Ob dnevih, ko dežuje, ni sončno.
+ Če ni toplo, je hladno.

In dokazujemo:

+ Ob nekaterih hladnih dnevih ne dežuje.

1. Pretvorimo stavke v klavzulsko obliko (glej prejšnje poglavje).
2. Dobimo temeljno množico klavzul.
3. Izvajamo unifikacijo, dokler ne pridemo do protislovja.

#### Kontrolna strategija

Namen le-te je **iskanje protislovja** - določa, katere klavzule izbiramo za izvedbo resolucijskih korakov.

+ Strategija je **polna**, če vedno najde klavzulo NIL, ko ta obstaja.
+ Delovanje lahko opišemo z **grafom izvajanja**.

![Graf izvajanja](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-20-12-31-59.png)

S pomočjo tega drevesa lahko nato uporabimo razne iskalne algoritme:

+ **iskanje v širino** - polna, a neefektivna
+ **strategija s podporno množico** (klavzule, ki izhajajo iz negacije ciljnega stavka ali naslednikov) - strategija
  pri tvorbi klavzule vzame najmanj enega očeta iz podporne množice - polna in bolj efektivna
+ **strategija s prednostjo enote** - poskušamo najprej izbrati klavzule z enim literalom - dopolnitev
  strategije s podporno množico - polna in bolj efektivna
+ **strategija z obliko linearnega vhoda** - vsaka resolventa ima najmanj enega očeta iz temeljne množice - ni polna,
  enostavna za implementacijo
+ **sestavljene strategije** - kombinacija zgornjih strategij (ponavadi sestavljene iz strategije s podporno množico in
  strategije z obliko linearnega vhoda)

### Poizvedbe

Glej prosojnice stran 41 do 45. Franc in Janez.

### Slabosti resolucije

+ Pri pretvorbi v klavzulsko obliko izgubimo nekaj informacij.
+ Pretvorba v klavzule lahko privede do neučinkovitega reševanja - podvajanje resolucijskih korakov.
+ Ni naravno za človeka razmišljati na tak način, zato imamo alternative avtomatskega sklepanja:
    + veriženje naprej oz. podatkovno vodeno sklepanje
    + veriženje nazaj oz. ciljno vodeno sklepanje

### Veriženje naprej

**Hornova klavzula** je klavzula, ki ima največ en pozitiven literal. Vsako tako klavzulo lahko
zapišemo kot implikacijo. Npr. klavzula !P or !L or B lahko zapišemo kot implikacijo (P in L) => B.

Algoritem veriženja naprej določa, ali ciljna formula W sledi iz baze znanja v obliki Hornovih klavzul

Glej prosojnice 60+.

#### Veriženje naprej v predikatni logiki

Glej prosojnice 72+.

## 6. Verjetnostno sklepanje

**Negotovost** je pomanjkanje informacij, ki bi omogočile sklepanje in planiranje z zanesljivostjo.
Viri negotovosti so:

+ preveč informacij, neobvladljiva količina podatkov
+ nepopolne informacije, teoretično neznanje
+ praktično neznanje - manjka testov ipd.

Dogodki tako dobijo **stopnjo zaupanja** glede na zaznane pokazatelje.

### Teorija verjetnosti

Pojmi:

+ **dogodek** - nekaj, kar se lahko zgodi ali ne
+ **verjetnost** - stopnja zaupanja, da se bo dogodek zgodil
+ **verjetnostno sklepanje** - sklepanje, ki upošteva verjetnost dogodkov
+ prisotnost določenega dogodka opisujemo z **naključno/slučajno spremenljivko**
+ **zaloga vrednosti/domena** - množica vseh možnih vrednosti naključne spremenljivke
+ binarne, diskretne in zvezne naključne spremenljivke
+ **atomarni dogodki** - popolna specifikacija okolja
+ **apriorna/nepogojena verjetnost** - verjetnost dogodka samega po sebi

### Naključne spremenljivke

+ **Boolova** - vrednosti true in false
+ **Diskretna** - vrednosti so iz končne množice - kot verjetnost, da nekaj spada v nek razred
+ **Zvezna** - vrednosti so iz neskončne množice - **funkcija gostote verjetnosti**

### Preglednica verjetnosti

Z njo lahko prikažemo skupno verjetnostno porazdelitev.

Primer:

Vreme = {sončno, oblačno, deževno, nevihtno}
Vročina = {da, ne}
Gripa = {da, ne}

Tabela: 4 x 2 x 2 = 16 možnih kombinacij

### Pogojna verjetnost

Verjetnost dogodka A, če se je zgodil dogodek B.

Pravilo produkta:

![Pravilo produkta](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-20-13-27-03.png)

### Aksiomi verjetnosti

Za vsako izjavo velja, da je v razponu 0 do 1.
Velja tudi:

* P(a ∨ b) = P(a) + P(b) − P(a ∧ b)
* P(a) = 1 − P(¬a)

### Sklepanje s skupno verjetnostno porazdelitvijo

Seštevek atomarnih dogodkov je 1.

Primer:
![Skupna verjetnostna porazdelitev primer](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-20-13-34-22.png)

**Marginalizacija** je izločitev podmnožice naključnih spremenljivk z izračunom vsote
verjetnosti pri vseh možnih vrednostih teh spremenljivk.
**Robna verjetnost** je verjetnost, ki jo dobimo z marginalizacijo.

V bistvu si rečeš, ok zanimajo me spremenljivke A in B. Potlej pa izračunaš verjetnost za vse možne kombinacije
glede na ostale spremenljivke.

Za primere glej prosojnico stran 15.

V tabeli se te različne kombinacije spremenljivk zelo dobro vidijo.

**Normalizacijska konstanta** je vrednost 1/P, ki poskrbi za to, da je seštevek verjetnosti vedno 1.

Primer je na prosojnici stran 23 in 24 ter naprej.

### Sklepanje s polno skupno verjetnostno porazdelitvijo

Postopek je sledeč, kjer so X spremenljivka vprašanja (ali imamo bolezen), E so spremenljivke evidence
(simptomi) in Y neopazovana spremenljivka - neugotovljena prisotnost drugega simptoma.

```
P(X|e) = [P(x1|e), P(x2|e), ---, P(xn|e)] = alfa * P(X, e) = alfa * sum(P(X, e, Y))
```

Glej primere od prej za boljše razumevanje.

### Neodvisnost

Spremenljivki sta neodvisni, če velja:

- P (X | Y) = P(X)
- P (Y | X) = P(Y)
- P (X , Y) = P(X) P(Y)

Neodvisnost zmanjša količino informacij potrebnih za določitev polne skupne porazdelitve.

### Bayesovo pravilo

```
P(Y | X) = P(X | Y) * P(Y) / P(X)
```

+ diagnostično stanje
+ vzročno stanje
+ vzrok
+ normalizacijska konstanta

Glej primer prosojnica stran 31.

Več ko imamo spremenljivk, bolj neučinkovit postopek postaja.

#### Pogojna neodvisnost

Če sta dve spremenljivki pogojno neodvisni, potem velja:

```
P(X, Y | Z) = P (X | Z) * P(Y | Z)
```

Tako dobimo novo tabelo verjetnosti - stran 35.
Tako lahko tabelo zapišemo z manj spremenljivkami in prihranimo nekaj prostora in časa.

### Naivni Bayesov model ali Bayesov klasifikator

Gre za model verjetnostnega sklepanja, ki prepostavlja pogojno neodvisnost spremenljivk
evidence.
Model deluje zelo dobro.

### Bayesova mreža

Predstavitev polne skupne verjetnostne porazdelitve v obliki acikličnega grafa.

+ naključne spremenljivke so vozlišča mreže
+ povezava od vozlišča X do Y predstavlja odvisnost Y od X
+ vsako vozlišče dobi pogojno verjetnostno porazdelitev P(X | Parent(X))

Za primer glej prosojnico stran 38.

[//]: # (TODO: Finish this)

## 7. Mehka logika

Gre za razširitev klasične logike. Omogoča obdelavo negotovih, nepopolnih informacij.
Uporabljeno v krmilnih napravah, nevronskih mrežah, sklepanje na podlagi pravil...

### Mehke množice

Ideja je, da elementi le delno pripadajo neki množici. Kot da bi bili robovi množice
zamegljeni. Pretvorba numerične lastnosti objekta v pripadnost mehki množici se imenuje
**fuzifikacija** in je opisana z **pripadnostno funkcijo**. Recimo, ko mi poskušamo
oceniti kako star je nekdo - srednje star, mlad, star? Recimo si 60% da je mlad, 40%
da je srednje star.

### Predstavitev mehkih množic

Najpogosteje pripadnost mehkim množicam prikažemo s pomočjo trapezoidnih grafov.
Prehod med posameznimi množicami je ponavadi postopen in zato se sosednji trapezoidi sekajo,
lahko pa je prehod tudi takšen, da trapezoidi postanejo štirikotniki. Velja pa ponavadi,
da je seštevek 1, ni pa to nujno.

### Mehka spremenljivka

Mehka spremenljivka je spremenljivka, katere vrednosti so izrazi v naravnem jeziku. Npr.
kot zgoraj omenjeno različne starostne skupine.

### Operacije nad mehkimi množicami

+ negacija (1 - verjetnost)
+ disjunkcija (max ali Pa + Pb - Pa * Pb)
+ konjunkcija (min ali Pa * Pb)

Zgoraj naštete operacije lahko med sabo tudi kombiniramo.

### Sklepanje v mehki logiki

Bazo znanja v mehki logiki izrazimo v obliki mehkih pravil tipa če-potem. Primer: primernost
osebe za smučarskega skakalca.

Baza:

+ IF starost=mlad in teža=lahek THEN primernost=zelo_primeren
+ IF starost=mlad in teža!=lahek THEN primernost=primeren
+ IF starost=srednje_mlad and teža!=lahek THEN primernost=primeren
+ ...

Izpolnjenost pogojev se prenese na sklep?

### Sistem mehkega sklepanja

Mehka domena - definicije vhodnih in izhodnih mehkih spremenljivk. Baza znanja v obliki
množice mehkih pravil.
Postopek sklepanja:

- fuzifikacija ali zmehčanje - pretvorba numeričnih vrednosti v pripadnost mehkim množicam
- sklepanje - izpeljava sklepov iz mehkih pravil - prenos aktivacije pogojev na sklepe mehkih pravil
- defuzifikacija ali odmehčanje - pretvorba mehkih sklepov v numerične vrednosti

Zgornje si lahko predstavljamo tudi kot nevronsko mrežo.

### Defuzifikacija

Postopek:

- grafe pripadnostnih funkcij za izhodne mehke vrednosti obrežemo in skaliramo na višino dosežene aktivacije
- površine pod skaliranimi grafi združimo v en likin izračunamo njegovo **karakteristično točko** (npr. težišče)

Glej stran 22 do 26.

### Mehki krmilnik

Primer: tempomat. Prejema podatke o varnostni razdalji, hitrost približevanja in razliko od željene
hitrosti.

Vhodne spremenljivke:

- razdalja (majhna, srednja, velika)
- približevanje (počasno, srednje, hitro)
- hitrost (nizka, ustrezna, visoka)

Izhodne spremenljivke:

- pospešek (zaviraj, vzdržuj, pospešuj)

Baza znanja:

- IF razdalja=majhna AND približevanje!=počasno THEN signal=zaviraj
- IF razdalja=srednja AND približevanje=hitro THEN signal=zaviraj
- ...

Za slike glej prosojnice stran 30+.

Rešitev primera:

- Varnostna razdalja: 1.8s
- Hitrost približevanja: 15km/h
- Trenutna hitrost: 8km/h nižja od željene

Postopek reševanja:

- fuzifikacija:
    - razdalja je 0.2 majhna, 0.8 srednja, 0.0 velika
    - približevanje je 0.5 počasno, 0.5 srednje, 0.0 hitro
    - ...
- mehko sklepanje:
    - gremo čez vsa pravila:
        - min(0.2, 0.5) = 0.2 -> zaviraj
        - min(0.8, 0) = 0 -> zaviraj
        - ...
- skupne aktivacije sklepov so 0.2 zaviraj, 0.8 vzdržuj in 0 pospešuj.
- defuzifikacija:
    - y = (0.2 * -3.24 + 0.8 * 0 + 0 * 3.24) / (0.2 + 0.8 + 0.0) = -0.648

## 9. Uvod v nevronske mreže

### Nevronska mreža

Gre za matematični model, katerega namen je posnemanje delovanja bioloških nevronskih mrež.
Nevronske mreže so sestavljene iz nevronov, ki so med seboj povezani z utežmi. Možgani so
zelo kompleksni in paralelno delujoči.

### Umetni nevron

Struktura:

- numerični vhodi
- vsak vhod ima utež w
- vsak vhod ima pristranskost/bias b ali prag (threshold) za aktivacijo, -1 ali +1
- vhodi se seštejejo in se glede na aktivacijsko funkcijo pretvorijo v izhod

Danes se večinoma uporablja bias +1. Nevron se imenuje tudi **enota**. V literaturi se
**aktivacija** včasih imenuje tudi izhod sam. Vrednost **v** pa imenujemo uteženi vhod za
aktivacijsko funkcijo.

Vhod: [x1, x2, x3, ..., xn]^T

Uteži: [w1, w2, w3, ..., wn]^T

Aktivacija: v = **w**^T * **x** + b ali v = **w**^T * **x** - prag

Izhod: y = f(v)

Vrste aktivacijskih funkcij:

- pragovna/stopničasta - y = 0 ali 1
- linearna - y = v
- Popravljena linearna ReLU - y = max(0, v)
- leaky ReLU - y = max(0.01 * v, v)
- softplus - y = ln(1 + e^v)
- ELU (exponential linear unit) - y = v, če v >= 0, y = a * (e^v - 1), če v < 0
- sigmoidna - y = 1 / (1 + e^-v)
- hiperbolični tangens - y = (1 - e^-2v) / (1 + e^-2v)

### Ciljna aplikacija

- regresija - izhod je realno število na podlagi vhodnih podatkov
- klasifikacija - izhod je razred na podlagi vhodnih podatkov

### Pragovna logična enota - TLU

Uporablja stopničasto aktivacijsko funkcijo. Delovanje TLU določeno z uteženim vektorjem
w = [w0, w1, w2, ..., wn]^T in pragom, ki je utež w0. y = 1, če v >= 0, y = 0, če v < 0.

x = [x0, x1, x2, ..., xn]^T je vhodni vzorec, ki je opisan z množico **numeričnih atributov**
ali **značilk**.

Prednost TLU: **pohlevna degredacija** oz. odpornost na šum ter strojne napake.

Primer:

Glej prosojnico stran 20 do 27.

Delovanje TLU lahko razumemo kot **linearni klasifikator** - torej ločitev vhodnih vzorcev v
dva razreda. Razred 0, ki ima na izhodu 0 in razred 1, ki ima na izhodu 1. Meja med razredoma je
določena z **hiper-ravnino** - bodisi premica v 2D ali ravnina v 3D.

Delitvena premica: w1 * x1 + w2 * x2 = w0

Zadevo lahko izrišemo v 2D ravnino.

#### Učenje TLU

Učenje TLU je postopek, pri katerem se določijo uteži w. Učenje TLU je **nadzorovano** in
**iterativno**. Za učenje uporabljamo **učno množico**. Učna množica je množica vhodnih
vzorcev, ki so opisani z značilkami in pripadajočimi razredi. Vzorez označimo z (x, d),
x^(p) in d^(p) pa sta p-ti vzorec in p-ti razred. Število učnih vzorcev je v praksi
dosti manjše od števila vseh možnih razredov.

Cilj je, da se TLU nauči posploševati.

Ker gre za iterativen postopek, učenje poteka v **epohah**. Ko TLU naredi napako pri učenju,
uteži popravimo s pomočjo **učnega pravila**. Osnovno pravilo je **učno pravilo perceptrona**.

### Učno pravilo perceptrona

