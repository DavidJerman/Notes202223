# Priprava na kolokvij 2

V naslednjem dokumentu je povzetek vseh potrebnih algoritmov. Primere algortimov
lahko najdete v zapiskih ali pa v knjigi.

## 6. Ravninska triangulacija

Triangulacijo izvajamo nad množico točk S. 

Želimo si, da bi bile triangulacije dobrem zato uvedemo neke kriterije.
Npr. dolžino robov, velikost kotov ipd. Pri tem število robov ostaja 
**enako** ne glede na izbiro kriterija.

Pojmi:

- normalno povezan ravninski graf - vsi robovi se stikajo v S,

### 6.1 MWT - Minimalna utežena triangulacija

Iščemo vsoto dolžin robov, ki je najmanjša. 

1. Tvorimo vse daljice, katerih je m = (n nad 2), O(n^2*log(n)) in razvrstimo 
   po dolžini
2. Nato jemlemo daljice in jih sprejmemo, če le-te ne sekajo katere od
   obstoječih daljic. Če sekajo, jih zavržemo. O(n^4)

Lastnosti:

- požrešna strategija, **ni globalne optimalnosti**

### 6.2 Hamiltonova triangulacija

Tu na vrsto pridejo **trikotniški traki**. Zakaj? Najenostavnejše stiskanje
podatkov triangulacije, poleg tega pa z njimi delajo tudi grafični procesorji.
Tako imamo le **n + 2** oglišč namesto **3n** v optimalnem primeru.
**Posplošen** trikotniški trak omogoča še tvorbo **degeneriranih trikotnikov** -
ploščina je enaka 0. Pri tvorjenju se menja orientacija. V tem primeru dodajamo
posamezne točke.

Drugi problem pa je, da triangulacijo rabimo izvesti nad množico S.

1. Tvorimo spiralo - začnemo z ekstremno točko lupine, nato lahko uporabimo
   prilagojen algoritem za iskanje konveksne lupine. O(n^2)

   Alternativno lahko tvorimo izbočene lupine in jih nato povežemo.
2. Znotraj spirale tvorimo posplošen trikotniški trak. O(n) Tu se izmenjuje
   orientacija, poleg tega pa sta dve točki vedno na zunanji ali notranji 
   lupini in ena na obratno. Če pride do sekanja (vsebnosti ene izmed točk)
   v tvorjenem trikotniku, tvorimo degenerani trikotnik.

Lastnosti:

- hitrejše od MWT

### 6.3 Delaunayeva triangulacija

Optimiziramo minimalni notranji kot. Skratka, če imamo dva trikotnika
z različnima triangulacijama, najprej njune kote damo v neko vrsto in
jih nato uredimo po velikost. Trikotnik, ki ima večji minimalni kot, 
predstavlja boljšo triangulacijo.

#### 6.3.1 Kriterij praznega kroga

Tu je v glavnem ideja, da če naredimo krožnico skozi tri točke, da ne
sme ta krog vsebovati še druge točke. Če točke ne vsebuje, je triangulacija
optimalna. Dokaz je s pomočjo **Talesovega izreka**.

1. Naredimo krožnico in pogledamo, če je veljaven
2. Če ni veljaven, naredimo zamenjavo robov oz **legalizacijo**
3. **Legalizacijo** rabimo preveriti rekurzivno

### 6.4 Algoritmi za tvorbo DT

