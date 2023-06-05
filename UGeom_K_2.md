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

- ovijanje paketov
- deli in vladaj
- inkrementalni algoritmi
- prebirna premica
- metoda z izbočeno lupino

#### 6.4.1 Fang in Piegl*

1. Razdelimo v polrobove. Prvi polrob je najkrajši. Uvrstimo polrob v seznam, ki se obnaša kot sklad
2. Iščemo naslednji točko, ki bi tvorila veljavno DT
   1. Vzamemo polrob iz seznama in poiščemo najbližjo točko temu polrobu
   2. Če se zgodi, da nastane komplementaren rob že obstoječemu, oba odstranimo iz sklada
...

#### 6.4.2 Deli in vladaj

1. Razdelimo točke v več kosov tolikokrat, dokler ne dobimo dovolj majhen problem - recimo dokler ni
   število točk tri ali manj


#### 6.4.3 Metoda s 3D izbočeno lupino

1. Množico S projeciramo na paraboloid. z = x^2 + y^2
2. Točke povežemo v trikotnike
3. Odstrnimo trikotnike, ki kažejo navznoter, torej v smeri osi z
4. Preslikamo nazaj v 2D

#### 6.4.4 Inkrementalni algoritem

Ideja tu je, da točke dobivamo postopoma in ne vse naenkrat.

1. Začnemo z nekaj že trianguliranimi točkami
2. Vstavimo novo točko in ugotovimo, v kateri trikotnik spada - najzahtevnejši del
3. Naredimo povezave med točko in oglišči trikotnika - dobimo 3 nove trikotnike
4. Legaliziramo te trikotnike

Zgornji algoritem ponavljamo, dokler ne zmanjka točk.

Število trikotnikov je enako 2n - 2 - k, kjer je k število točk na robu.

Algoritem je časovno kar učinkovit, ampak **težek za implementacijo**.

Pri točki 2 lahko uporabimo različne algoritme za preverjanje vsebnosti. 
Recimo _strategija s prehodom_. Ta metoda je preprosta in ne potrebuje veliko 
pomnilnika.

Drugi algoritmi so še **GICS**, iskanje najbližje točke.

##### 6.4.4.1 Korakanje

Ideja pri korakanju je, da se premikamo po trikotnikih, dokler ne najdemo
tistega, ki vsebuje točko. Lahko pride do robnih pogojev, kjer je točka 
v oglišču ali na robu. Če je v oglišču, jo spustimo, če pa je na robu, pa
se trikotniki tvorijo malce drugače.

#### 6.4.5 Algoritem Guibasa, Knutha in Sharirja (GKS) - O(n*logn)

Ta algoritem ravno tako uporablja inkrementalno vstavljanje.

Glavna ideja tu je, da naredimo to, da točke nikoli ne padejo izven 
**konveksne lupine**. Na ta način poenostavimo in zmanjšamo kodo.
Generator točk **omejimo** na neko minimalno in maksimalno število x in y.

1. Tvorimo **veliki trikotnik**, ki zajema vse točke
   1. Točke premaknemo tako, da je njihovo težišče v koordinatnem izhodišču
   2. max = max(abs(Xmax, Xmin, Ymax, Ymin))
   3. p1 = (3*max, 0), p2 = (0, 3*max), p3 = (-3*max, -3*max)
2. Generiramo točko po točko in jih dodajamo v triangulacijo
   1. Najdemo trikotnik, ki vsebuje točko
   2. Naredimo tri nove trikotnike
   3. Legaliziramo trikotnike

Psevdokod:

```
1  Inicializacija
2     Randomizacija točk
3     Določčitev BT (velikega trikotnika)
4     Inicializacija PS (podatkovne strukture, ki je drevo)
5  Tvorba DT do terminalnega simbola (ko zmanjka točk)
6     Izberemo točko p
7     Najdemo trikotnik(a), ki vsebuje točko p - t1, t2
8     if t2 == NULL:                                             // 3je trikotniki
9        Razdeli (t1, t11, t12, t13)
10       Legaliziraj (t11, t12, t13)
11    else:                                                      // 4je trikotniki
12       Razdeli (t1, t2, t11, t12, t21, t22)
13       Legaliziraj (t11, t12, t21, t22)
14    goto 5
15 Finalizacija - odstranimo BT
```

**Podatkovna struktura**

Podatkovna struktura uporabljena tu je **DAG** (usmerjen acikličen graf). V njem delamo
vse povezave - ko ustvarjamo trikotnike in ko jih legaliziramo.

**Lastnosti:**

- velika poraba pomnilnika
- naporno sprogramirati
- graf se lahko izrodi - rešitev za to je randomizacija točk (v liniji 2 pseudokoda)
- hranimo celotno zgodovino DT

#### 6.4.6 Algoritem z iskanjem najbližje točke

Ponovno, gre za _inkrementalni algoritem_, zato imamo generator točk.

Ideja tu je podobna kot pri iskanju najbližje točke. Imamo podatkovno strukturo, ki
hrani točke in njihove sosede. Ko vstavimo novo točko, namesto da gledamo vse trikotnike,
ki vsebujejo točko, gledamo samo tiste, ki so v bližini - torej sosede. Večino časa 
sosed tudi je trikotnik, ki vsebuje točko. Če imamo v celici več točk, potem moramo
uporabiti seznam za vsako celico.

Postopek:

1. Inicializacija
   1. Inicializacija iskalne strukture
   2. Določitev BT
   3. Vstavitev prve točke
2. Triangulacija
   1. Izberemo točko p
   2. Najdemo trikotnik, ki vsebuje točko p
   3. Delitev trikotnika in legalizacija
3. Finalizacija
   1. Odstranitev BT
   2. Shranjevanje trikotnik*

#### 6.4.7 Algoritem s preiskovalno premico in napredujočo fronto - Fortune

Tu se ravno tako premikamo točko po točko. 

Začnemo z neko triangulacijo, nato pa pride nova točka. Če točke pogledamo od zgoraj,
potem zgornjemu delu lupine rečemo **fronta**. Ob dodajanju nove točke, naredimo
projekcijo na rob spodaj, da vemo, kam točka pade. Nato naredimo povezavo med tema dvema
ogliščema. Za tem pa sledi sprehod levo in desno, kjer opazujemo, če se da iz nove točke tvoriti
še kakšne trikotnike s fronto.

1. Nov trikotnik s pomočjo projekcije
2. Legalizacija
3. Fronta se poveča
4. Razširimo v levo in v desno
5. Fronta se poveča

Robni primer: točka pade izven fronte - rešitev je lahko uporaba BT,
kjer na začetku na fronto dodamo točki (Xmin - E, Ymin - E) in (Xmax + E, Ymin - E).
E = 0.0001

Psevdokod:

```
1  Inicializacija
2     Urejanje točk glede na smer premikanja
3     Določitev BT
4     Inicializacija fronte (AF)
5  Triangulacija
6     Izberemo točko p
7     Naredimo projekcijo točke p na rob spodaj
8     Tvorimo trikotnik
9     Legaliziramo trikotnik
10    Razširi fronto v levo in desno
11    goto 5
12 Finalizacija
13    Odstranimo BT
```

Robni primer: točka pade pri projekciji na neko točko. Razširimo ali levo ali desno - 
poljubno.

Pri tvorjenju trikotnikov lahko tudi dodamo pogoj, da mora biti kot dovolj majhen.
Če ni ju pač ne naredimo. Ampak je pa na račun tega potrebno na koncu te trikotnike 
spet dodati. Glej učbenik 92.

**Problem, ko preveč trikotnikov nismo naredili in nastane "kotanja"**

Glej urg.pdf stran 9.

TODO

## 7. Voronoijevi diagrami

### 7.1 Definicija - preprost diagram

Gre za graf, ki je dualen Delaunayevemu triagulacijskemu grafu. To v bistvu pomeni,
da so povezave na tem grafu pravokotne na povezave na Delaunayevem grafu. Tvori pa
se ga tako, da za vsaki dve poljubni točki tvorimo premico med njima, ki je enako
oddaljena od obeh točk. Te premice nato kombiniramo, kjer se sekajo.

Primer uporabe je ugotavljanje, kateri točki je nova točka najbližje. To zlahka
določimo s tem, v katero celico točka pade v Voronoijevem diagramu.

Pojmi:

- V. točka
- V. celica
- V. rob
- V. središče

Glej stran 107 za zapis definicije.

Lastnosti:

- natančno določena izbočena lupina
- Voroinojev diagram določa neposredne sosede
- Voronoijev diagram je dualen Delaunayevemu diagramu
- minimalno vpeto drevo v minimalnem času - Evklidovo vpeto drevo v linearnem času (skupna
  dolžina vseh povezav v drevesu je minimalna)
- max. število točk: 2n - 5
- max. število robov: 3n - 6
- če pa so kolinearne pa 0 točk, n - 1 robov

Dualnost pomeni, da lahko gremo iz enega grafa v drug graf v linearnem času.

Za več lastnosti glej učbenik stran 109.

VD -> DT: povežemo središča celic neposrednih sosedov
DT -> VD: razpolovimo povezave in povežemo razpolovišča

### 7.2 Algoritmi za tvorbo Voronoijevih diagramov

1. Naivni algoritem - za vsako točko naredim bisektorje
2. Inkrementalni algoritem
3. Deli in vladaj
4. Prebirna premica

#### 7.2.1 Deli in vladaj - O(n log n)

Deluje s časovno kompleksnostjo O(n log n). Ideja je, da množico S tako dolgo delimo,
dokler ne dobimo trivialnega problema (1 do 3 točke). Največ težav pride pri funkciji 
zlitja. 

Psevdokod:

```
Voronoi(S, V)
begin
   Razdeli S na dve podmnožici S1 in S2
   if not množica S1 dovolj majhna then
      Voronoi(S1, V1)
   if not množica S2 dovolj majhna then
      Voronoi(S2, V2)
   Zlij V1 in V2 v V
end
```

Postopek zlitja:

1. Najdemo ekstremni točki v S1 in S2 in ju povežemo
2. Nato naredimo novo točko na ustvarjenem poltraku ki polzi po poltraku proti povezanima točkama
3. Točka nadaljuje navzdol, dokler ne naleti na enega izmed robov S1 ali S2
4. Takrat se smer točke spremeni tako, da je točka vedno enako oddaljena od obeh točk iz množic S1 in S2

Za sliko glej učbenik stran 116.

#### 7.2.2 Prebirna premica - O(n log n)

- Erfurtov algoritem

Tu pa je ideja, da ustvarimo 3D stožce za vsako točko. Presečišča (**bisekcije**) teh stožcev so
Voronoijevi robovi. Nato uporabimo prebirno premico za premikanje preko ravnine, da ugotovimo,
kje ta presečišča so.

Preiskovalna premica, oz. v 3D prostoru ravnina, je nagnjena pod kotom 45 stopinj glede na preiskovalno os.
Njen presek s stožci tvori parabole, ki pa nam povejo, kje bodo Voronoijevi robovi in točke. 
Voronojev rob se tako gradi z zakasnitvijo glede na prebirno premico.

Imamo dva dogodka preiskovalne premice:

- dogodek točke - ustvari se nov stožec
- dogodek na krožnici - sprememba obstoječega stanja v podatkovnih strukturah

Povezava: ![Raymond Hill](https://web.archive.org/web/20230328053239/http://www.raymondhill.net/voronoi/rhill-voronoi.html)

TL;DR: Ko najdemo točko, se začne tvorit stožec, drugi dogodek pa je, ko se neki stožec konča - torej
se parabola skrči v točko in izgine. Z drugim dogodkom se ustvari Voronojeva točka in začne se nov
Voronojev rob.

## 8. Mnogokotniki

Mnogokotnike lahko delimo v več skupine glede na njihove lastnosti.

Lahko so konveksni in konkavni oz. vbočeni in izbočeni. Pri konveksnih je triangluacija
lahko v času O(n), pri konkavnih pa v času O(n^3).

Naslednja delitev je na enostavne in ne-enostavne. Enostavni so tisti, ki nimajo presečišč
sami s seboj. Ne-enostavni pa so samosekajoči - spremeni se jim orientabilnost.

Naslednja delitev je še na mnogokotnike z luknjami in brez lukenj. Kadar imamo gnezdene luknje,
se z vsako luknjo usmerjenost zamenja.

Potlej pa imamo še **obočene** mnogokotnike, kjer se izmenjuje izbočenost in vbočenost.

Za točne definicije glej stran 127.

## 9. Vsebnostni algoritmi

Algoritmi se tu delijo v dve grupi:

- brez priprave podatkov - O(n),
  - algoritem enakih predznakov (**izbočeni mnogokotniki**),
  - algoritem s poltrakom,
  - algoritem z vsoto kotov,
  - algoritem s KKS,
- z pripravo podatkov - potencialno še hitrejši.
  - algoritem s trakovi,
  - algoritem s klini,
  - algoritem CBCA,

### 9.1 Algoritem enakih predznakov

Deluje samo za izbočene mnogokotnike. Mnogokotnik mora biti **pravilno orientiran**.
Če je testirana točka na isti strani vseh robov, potem je točka znotraj mnogokotnika.
To, na kateri strani leži, določimo z vektorskim produktom. Če se spremeni **predznak**
vektorskega produkta za katerikoli rob, potlej je točka **zunaj** mnogokotnika.

### 9.2 Algoritem s poltrakom

Ta algoritem deluje tudi z luknjami. Ideja je, da iz točke v poljubno smer potegnemo
poltrak. Nato poiščemo vsa presečišča z mnogokotnikom. Če je število presečišč liho,
potem je točka znotraj mnogokotnika.

Če slučajno poltrak pade na točko, imamo robni primer.
V tem primeru lahko:

1. Spreminjamo kot, dokler poltrak ne pade na nobeno točko - to ni časovno učinkovito.
2. Druga metoda je opisana na strani 133, ampak je nismo opisali.

Drugi mejni primer je, če testirana točka leži na meji mnogokotnika.

### 9.3 Algoritem z vsoto kotov

Tu je ideja, da dodamo točko in to novo točko povežemo z vsemi ostalimi točkami.
Nato opazujemo kote med poltraki. Če je vsota poltrakov enaka 2 pi, potlej je točka
znotraj mnogokotnika, če pa je vsota 0 pa zunaj mnogokotnika.

Zelo potratna metoda, je pa ta algoritem **manj občutljiv na zaokrožitveno napako**.
Deluje pa tudi nad luknjami do neke mere - če vemo, na katerem nivoju te luknje so.

### 9.4 KKS - Algoritem kodiranega koordinatnega sistema

Gre za izboljšavo s poltrakom, tako da je algoritem zelo dober.

1. Dodamo novo točko in te točke ustvarimo koordinatni sistem
2. Nato si izberemo poljubno os - recimo -x
3. ...
4. Profit

TODO: Zakaj se gre tule

### 9.5 Algoritem s trakovi O(n log n)

Najprej za vsako točko potegnemo premice. Za vsak trak ugotovimo, katere robove 
vsebuje, kar storimo v logaritemskem času. It te točke nato potegnemo poltrak in
ugotovimo, katere robove iz tega pasu le-ta seka. Podobno ko pri metodi poltraka,
tudi tu sodo število pomeni, da točka leži zunaj mnogokotnika, liha pa, da znotraj.

Rešitev robnih primerov je lahko rotacija mnogokotnika.

### 9.6 Algoritem s klinom

Deluje samo za **izbočene mnogokotnike**. Iz poljubne točke znotraj mnogokotnika
potegnemo žarke skozi oglišča mnogokotnika - teh je **n**. To nam da kline - torej 
razdelitev mnogokotnika. Nato v času O(log n) ugotovimo, v katerem klinu je točka
s pomočjo dejstva, da gre za polarni koordinatni sistem. Nato za novo točko le
še preverimo, na kateri strani daljice je - to nam pove, ali je zunaj ali znotraj
mnogokotnika.

### 9.7 Algoritem CBCA

Osnovna ideja je, da sliko vstavimo v mrežo neke velikosti. Velikost določimo s pomočjo
sledeče hevristike:

```
Nx = 2 * [ratio * sqrt(n)]

Ny = 2 * [sqrt(n) / ratio]

ration = (Xmax - Xmin) / (Ymax - Ymin)
```

1. Priprava podatkov - ustvarimo mrežo velikosti Nx * Ny
2. Celice nato barvamo glede na to, ali so znotraj, zunaj, ali na robu mnogokotnika
   1. W - celica je zunaj
   2. B - celica je znotraj
   3. G - celica je na robu

Barvanje celic dosežemo s pomočjo rasterizacije. Zadeva deluje v konstantnem času.

Psevdokod:

```
1   Inicializacija
2   Polje celic
3   Vanj vstavimo mnogokotnike
4   Celice dobijo zastavice
5   Ugotavljanje vsebnosti
```

Vsebnost oz. to, na kateri strani roba leži točka, preverjamo s pomočjo vektorskega
produkta. Naredimo vektorski produkt z najbližjim robom.

Ta algoritem je zelo učinkovit.

Za zapolnjevanje zunanjih celic z barvo B lahko uporabimo algoritem poplavljanja.

## 11. Triangulacija mnogokotnika

Delitev glede na kriterij gradnje triangulacije:

- brez kriterija
- DT
- s Steinerjevimi točkami

Steinerjeve točke dosežejo to, da so trikotniki čim bolj enakostranični.

Pri tem je Steinerjev algoritem najpočasnejši izmed teh treh, brez kriterija pa
najhitrejši.

TODO - Tisto nekaj z DT

### 11. 1 Trapezna delitev mnogokotnika - algoritem s preiskovalno premico

