# Umetna inteligenca kolokvij 2

## Predstavitev znanja

+ Znanje predstavimo z **izjavami (dejstva)**, iz njih tvorimo **sklepe**.
+ V računalništvu jim rečemo **stavki**. **Baza znanja** pa je množica vseh teh stavkov.
+ **Logika** je formala predstavitev znanja.
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
+ Stavek je **izpolnjiv** če obstaja interpretacija, ki ga naredi resničnega

### Pravila sklepanja

+ **Modus ponens** - A če potem B, A, torej B
+ **Modus tollens** - A če potem B, ne B, torej ne A
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

