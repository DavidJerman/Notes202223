# Umetna inteligenca

## Pred snovjo

Sekcije s pojmi imajo na voljo check-marke. Le-te lahko označiš tako, da v oglate oklepaje namesto presledka vstaviš
`x`. Na primer: `[x]` označi tole. Tako si lahko daš zaznamke, kaj si že prebral.

## Snov

### Uvod

#### Kaj je umetna inteligenca?

Strojno oprema z inteligentnim vedenjem. Sistemu, ki pa odraža inteligenco pa rečemo agent.
Ko neki AI zna rešiti problem rečemo učinek AI - problem je rešljiv z algoritmom, torej ni več AI.

Pojmi:

- [ ] Ozka (šibka) vs splošna (močna) AI
- [ ] Točka singularnosti, superinteligenca
- [ ] Turingov test

### Reševanje problemov z iskanjem

Reševanje problema je v bistvu iskanje poti od začetnega stanja do cilja, če ustvarimo prostor stanj.
Tako lahko za reševanje takih problemov uporabimo iskalne algoritme: DFS, BFS, A*...
Hevristika nam poda neko znanje, oceno o okolju v katerem smo, tako da lahko
bolj učinkovito preiskujemo prostor stanj.

Prostor stanj <N, A, S, G>:

- N - množica vseh stanj
- A - množica vseh akcij
- S - začetno stanje
- G - ciljno stanje

Opis stanja je lahko popolni ali delni. Če je delen samo pomeni, da nimamo vseh
informacij o trenutnem stanju.

Cilj iskanja je lahko **najti pot do cilja** ali **najti ciljno stanje**.
Prvo je npr. iskanje poti do doma, drugo pa rešitev sudokuja.

Prostor stanj lahko vizualiziramo z grafom - stanja so vozlišča, povezave pa akcije.
Imamo cikličen, acikličen graf in drevo. Globina d je oddaljenost od začetnega vozliššča
do končnega vozlišča. Vejitveni faktor b je število povezav, ki vodijo iz enega
vozlišča. Ponavadi vzamemo povprečje.

#### Iskalno drevo

Načini iskanja:

- Iskanje z veriženjem naprej,
- Iskanje z veriženjem nazaj,
- Iskanje z veriženjem naprej in nazaj (dvosmerno).

Potek iskanja lahko ponazorimo z iskalnim drevesom. Razvoj vozlišča pomeni, da tvorimo
vse naslednike.

<img src="https://davidblog.si/wp-content/uploads/2023/04/Screenshot-2023-04-01-144356.png" width="700" alt="Drevo stanj">

#### Implementacija iskanja

Uporabimo seznama open in closed, ter iskanje naprej.
V open imamo obiskana vozlišča. V closed pa razvita vozlišča.

Poznamo dve vrsti strategij:

- [ ] Informirana - uporabljamo hevristiko
- [ ] Neinformirana - ne uporabljamo hevristike

Algoritem je poln, če rešitev vedno najde in optimalen, če najde najboljšo rešitev.

#### Neinformirane strategije

- [ ] BFS - iskanje v širino, _open_ je FIFO vrsta, optimalen, poln, O(b^d+1)
- [ ] BFS z uniformnih stroškom - _open_ urejen po strošku poti, poln, optimalen, če povezave vse +
- [ ] DFS - iskanje v globino, _open_ je LIFO vrsta, ni optimalen, je poln, O(b^m), m je max. razdalja med dvema
  vozliščema v grafu prostora stanj
- [ ] DFS z omejitvijo globine - se omejimo do globine l, ni nujno poln, če ne gremo dovolj globoko, O(b^l)
- [ ] DFS z omejitvijo globine (postopno povečevanje globine) - še najbolj primerno kot neinformirana strategija
- [ ] Dvosmerno iskanje - iskanje naprej in nazaj, O(b^(d/2)) - stik preverjamo s presekom open

#### Informirane strategije

Uporaba hevristike - hevristično iskanje! Reševanje optimizacijskih problemov.

- [ ] Best-first search - v vsakem koraku izberemo vozlišče z najboljšo oceno f(n) v seznamu _open_ - seznam urejen po
  f(n)

Osnovna komponenta: hevristična ocena h(n) - ocena stroška do cilja. Npr. zračna razdalja
do cilja.

#### Algoritem A

Za izbiro naslednje poteze uporabimo oceno f(n) = g(n) + h(n), kjer je g(n) pot do trenutnega vozlišča,
h(n) pa ocena stroška do cilja. Ni ravno idealen.

#### Algoritem A*

Algoritem A* je izboljšava algoritma A. Predvsem gre za to, da uporabimo boljšo hevristiko.
Ta mora biti:

- sprejemljiva (moramo podceniti strošek) - h(n) <= h*(n), kjer je h*(n) optimalna hevristika
- za vsako vozlišče open in closed beležimo najkrajšo pot. Če je nova pot krajša, potem
  vozlišče dodamo v open - odstranimo starega oz. posodobimo njegovo oceno. Če je vozlišče
  v closed, ga odstranimo in ga dodamo v open ter popravimo še vsem naslednikom ALI (!!!!!!)
- hevristična ocena je konsistentna oz. monotona: h(n) <= c(n, n') + h(n), torej
  velja trikotniška neenakost

Ta algoritem je poln in optimalen.

Izboljšave: postopno poglabljanje, rekurzivno iskanje z izbiro najboljšega, pomnilniško omejen A*, ...

[A* vs DFS vs BFS](https://github.com/DavidJerman/AStar)

#### Hevristika

Primeri hevristik:

- [ ] Zračna razdalja
- [ ] Število kock na nepravem/pravem mestu

Poglej dodatno: pojmi na strani 71/106.

#### Lokalni iskalni algoritem

Ideja je, da se premikamo iz stanja v stanje, brez da bi poznali okolico. Preko tega spoznamo okolico.
Skratka izvajamo lokalne spremembe in iščemo globalni maksimum (čeprav ponavadi najdemo nek
lokalni maksimum).

Primerno, kadar iščemo stanja z maksimalno ugodnostjo (fitness). To ugodnost dobimo
s pomočjo hevristične ocenitvene funkcije.

<img src="https://www.tutorialandexample.com/wp-content/uploads/2019/07/Working-of-a-Local-search-algorithm.png" width="700" alt="Lokalni iskalni algoritem">

Primer je lahko sudoku, kjer je premik zamenjava dveh nefiksnih polj, cilj pa je najti
končno rešitev - optimalna rešitev ima hevristično oceno 0.

##### Hill climbing

Začnemo iz naključnega stanja, izberemo potezo, ki prinaša največje izboljšanje trenutnega stanja.
Zaključimo, ko najdemo optimalno rešitev (globalni maksimum oz. optimum).
Problem platoja (ravnine) omejimo tako, da omejimo število premikov na ravnini.

Izboljšave: stohastično vzpenjanje glede na hevristiko, s prvim izborom, z naključno
ponovitvijo - nekajkrat začnemo znova iz novega naključnega stanja, ...

##### Simulated annealing

Kombiniramo vzpenjanje na hrib z naključnim iskanjem - polnost iskanja.
Izberemo naključnega naslednika in če je boljši od trenutnega stanja, to sprejmemo.

Ostale metode:

- [ ] Iskanje s spremenljivo sosesko
- [ ] Iskanje tabu
- [ ] Local beam search
- [ ] Genetski algoritem

[Hill climbing](https://www.youtube.com/watch?v=oSdPmxRCWws)

##### Genetski algoritem

Tvorimo populacijo k naključnih začetnih stanj. Stanja so zakodirana v kromosome -
to je lahko npr. nek array vrednosti (recimo barva, pozicija x, pozicija y, ...).

Kodirano predstavitev rešitve imenujemo **genotip**, njeno dejansko interpretacijo
pa **fenotip**. Naslednjo generacijo osebkov tvorimo s pomočjo:

- [ ] Selekcije - izberemo najboljše osebke
- [ ] Križanja - izberemo dva najboljša osebka in jih križamo
- [ ] Mutacije - izberemo naključnega osebka in ga mutiramo - mu naključno spremenimo
  neke lastnosti/vrednosti

Primer:
Genotip pri postavitvi kraljic na šahovnico bi lahko npr. bile številke od 1 do 8 
v arrayu, ki bi za posamezno vrstico predstavljale stolpec, v katerem je kraljica.

Imamo več oblik selekcije:

- naključna selekcija,
- proporcionalna selekcija (verjetnost izbire kromosoma proporiconalna njegovi oceni),
- turnirska selekcija (izberemo naključno m < k osebkov in izberemo najboljšega),
- selekcija po ranku (izberemo naključno proporcionalno indeksu kromosoma v sortiranem
  polju kromosomov),
- elitizem (izberemo najboljše osebke in jih prenesemo v naslednjo generacijo),

Križanje se zgodi z neko verjetnostjo pc. 

Oblike križanja:

- uniformno križanje (vsak par genov starševskih kromosomov
  neodvisno izmenjamo z verjetnostjo pc),
- eno točkovno križanje (izberemo naključno točko in zamenjamo lastnosti na obeh kromosomih
  od te točke naprej),
- dvo točkovno križanje (izberemo dve naključni točki in zamenjamo lastnosti na obeh
  kromosomih med njima),

Mutacija z verjetnostjo pm za cel kromosom ali posamezno lastnost (gen).

[Genetski algoritem](https://www.youtube.com/watch?v=1i8muvzZkPw)

### Iskanje v igrah

Omejili se bomo na igre med dvema igralcema.

Pojmi:

- [x] Zero sum game - seštevek rezultatov enega in drugega nasprotnika je 0
- [x] Igre s popolno informacijo - vemo vse o stanju igre
- [ ] Kompleksnost prostora stanj - število položajev dosegljivih iz začetnega stanja
- [ ] Velikost drevesa iger - število listo v drevesu - število vseh različnih iger

Cilj je iskanje čim boljše naslednje poteze. Uvedemo tudi ocenitveno funkcijo.
Preiskujemo s pomočjo drevesa igre – v praksi se to ponavadi implementira z rekurzijo.

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-21-41-34.png" width="700" alt="Drevo stanj">

Izvajamo iskanje po tem drevesu – tako iščemo rešitev.

#### Minimax

Imamo igralca Min in Max, en maksimizira, drugi minimizira. Igralca se izmenjujeta.
Primer je igra s križci in krožci. V listih dobimo statične ocene položajev – to je v bistvu hevristika. Zmago nagradimo
z zelo visoko oceno.
Te ocene se nato prenašajo navzgor – enkrat izberemo min, drugič max – odvisno, kateri igralec je na vrsti.

Implementacija z rekurzivnim iskanjem v globino.

<img src="https://davidblog.si/wp-content/uploads/2023/02/MIN_MAX1.jpg" alt="Drevesna struktura">

<a href="https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/">Geeks for Geeks</a>

##### Gradivo iz vaj

```
Najprej bomo delali igre za dva igralca.
Na koncu je dobiček enak izgubi poraženca.
Igro s popolnimi (šah, dama - vidimo vse na polju) in nepopolnimi informacijami (karte, ker ne vemo, kaj ima
nasprotnik).
Torej če nimamo popolnih informacij ne moremo vnaprej nečesa računat, pri popolni informaciji
pa to lahko. Lahko planiramo poteze brez potrebe po statistiki.

Pa se najprej osredotočimo na križce in krožce. Igra se zagotovljeno konča po 9-tih potezah.
Zadevo definiramo kot iskalni problem. Skratka struktura z nekimi komponentami in po njej iščemo.
Vse skupaj formaliziramo, omejimo se na določene igralce, poteze in kdaj je konec igre...

Naše komponente:

* **Začetno stanje** (obliko polja, koliko jih je, stanje - je prazno ponavadi) - le-tega rabimo, da vemo, kje začeti.
  Z nekimi potezami delamo nova stanja.
* **Naslednje poteze** - funkcija prehoda med stanji. Torej formaliziramo, kako priti iz enega stanja v drugo.
  Rezultat funkcije je novo stanje. Z naslednjo potezo izberemo novo začetno stanje in nadaljujemo
  z iskanjem naprej in ponavljamo.
* **Zaključni pogoj igre** - kdaj je igre konec. Lahko je je konec, lahko je ni, lahko je neodločeno. -->
  Matematična formulacija funkcije
* **Ocenitvena funkcija - hevristika** - tako razločimo med dobrimi in slabimi potezami. Izberemo si pač eno
  hevristiko - npr. gledamo katera poteza nam da največ zmagovalnih potez.

Ko imamo vse te komponente lahko pričnemo s strateško igro.

### Zakaj je to iskalni problem?

Ker je igranje igre v bistvu iskanje naše najboljše poteze. Naša naloga je namreč iskanje najboljših potez.
Lahko razmišljamo tudi za več potez naprej, ampak se omejimo na neko število potez.

### Naprej...

Za nas so sovražnikove dobre poteze slabe poteze, naše dobre pa za nasprotnika slabe.

### Bistvo algoritma - drevo igre

Gre za vizualizacijo problema, ne rabimo dejanske drevesne strukture.

<img src="https://davidblog.si/wp-content/uploads/2023/02/MIN_MAX1.jpg" alt="Drevesna struktura">

Preprosto povedano, npr., iz začetnega stanja praznega polja, lahko križec postavimo na 9 različnih polj,
nato krožec na preostalih 8 polj, nato... In dobimo drevesno strukturo.
Konkretno za križce in krožce bi potlej skupno imeli 9! potez. To je kar veliko potez.
Na koncu pa pač pridemo do nekega zaključnega stanja - seveda si želimo zmagovalnega stanja.

To je potlej naš iskalni prostor. Z vsako izbiro pa je naš iskalni prostor manjši. Imamo izmenjujoče nivoje, enkrat
izbiramo mi, enkrat pa nasprotnik. Optimalni algoritem bi zgeneriral vsa možna stanja in zatem izbiral
poteze, ki so zanj najbolj ugodne. Vse bi v naprej izračunal. To si pri takšni igri lahko privoščimo, pri kompleksnih
igrah pa to ne gre, ker je računsko prezahtevno.

### Pomembno

Pri rekurziji nikoli ne pozabi na končni pogoj! Rabimo neki if stavek.

Našega igralca simuliramo z maksimizatorjem,
nasprotnika pa minimizatorjem. Namreč mi igrami za zmago, za nasprotnika pa želimo, da izgubi.

Mi bomo gledalo nekaj potez naprej. Minimax izbere eno potezo in gleda še dve potezi naprej. Izbere
najboljšo potezo in pogleda nazaj, katera je naslednja poteza. Na naslednjo potezo vpliva ocenitvena
funkcija in trenutno stanje. Hevristično funkcija najdeš na teams ali v učbeniku.

Vemo, da je najboljša začetna izbira za zmago sredina. Potemtakem to tudi izberemo preko hevristike.
Hevristiko lahko sredi igre tudi menjamo... Tako maksimiziramo možnost zmage.
Potezam dodelimo uteži in hevristična funkcija nam vrne večjo vrednost za boljše poteze.
Z igro zaključimo, ko pridemo do globine 0.

Algoritem je v učbeniku na strani 68. Imaš ga pa tudi na prosojnicah.

Algoritem v bistvu dela od spodaj navzgor. Ravno obratno kot mi govorimo.

## Algoritem Alfa-Beta

To je v bistvu nadgradnja prejšnjega algoritma. Ta algoritem za razliko od prejšnjega ne pregleda vsega.
Npr. na izbiro imamo tri slabe možnosti - teh zato ne bomo preiskali, ker nam nič ne dajo.
Alfa-beta obrezovanje (pruning) - deluje tako, da obreže nekatere veje z dodajanjem neskončnih vrednosti.
Recimo pri kakšni igri kot je šah je tole kar obvezno.
Torej algoritem dopolnimo z alfo in beto, ki sta pa meji, za to ali gremo sploh gledat neko vejo naprej - skratka
odrežemo neko vejo - s pogojem prenehamo rekurzijo, tako da vrnemo.
Če pa ni rekurzije pa break.

<img src="https://davidblog.si/wp-content/uploads/2023/02/alpha-beta-pruning-step7.png" alt="Alpha-Beta Pruning">

Torej potlej damo recimo max na -Inf min pa na Inf. In max in min postavita neko mejo, do kje bomo še
preiskovali. In če se meji križata, pomeni da nimamo boljše rešitve.

Učbenik str. 85.

Sprememba je tako zelo mala. Samo dodamo parametra alfa in beta. Če je val >= beta, zaključimo...
Enačaj imamo zato, ker se lahko pojavi tudi enakost vrednosti in alfe (bete).
Za neskončno daj neko zelo veliko vrednost - neko vrednost, ki jo z hevristiko ne bomo dosegli.

### Note

Skrajno levo vedno pogledamo, ker je algoritem rekurziven.

### Optimalni alfa-beta rez

Če je vse poravnano spodaj, torej so uteži urejene naraščajoče.

### Navodila

Imej zgoraj izbiri težavnosti. Potlej imej izbiro algoritma. Imej še števec za zmage igralca, računalnika,
izenačenje. Pa imej na sredini še polje za križce in krožce.

### Zunanji viri

<a href="https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/">Geeks for Geeks</a>
```

#### Negamaks

Ocene se razlikujejo le v predznaku – hevristična ocena je tako za oba igralca enaka. Zmaga ali izguba.

#### Algoritem Alpha-Beta

Tu pa uvedemo neko mejo in obrezovanje vej.

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-21-53-59.png" alt="Alpha-Beta Pruning">

Recimo v primeru zgoraj:

1. Gremo od A do B do D.
2. Za D vidimo, da je 2, kar pomeni, da je zgornja meja za B (MIN) 2.
3. E ima večjo oceno, ga ne upoštevamo.
4. Beta je tako 2.
5. Za A (MAX) je tako spodnja vrednost 2.
6. Alfa postane 2.
7. V C-ju ugotovimo, da je F = 1, torej beta = 1.
8. Ta poteza nam da vedeti, da bo A (MAX) zagotovo izbral B, ker ima le-ta višjo spodnjo mejo --> alfa >= beta.
9. Za G nam je tako vseeno. To vejo obrežemo.

Če bi bilo drevo urejeno (najbolj levi naslednik v vsakem poddrevesu najugodnejši za igralca na potezi), bi algoritem
ovrednotil pol toliko listov kot običajni minimax.

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-22-01-53.png" alt="Alpha-Beta Pruning" width="800">

Ta algoritem lahko implementiramo tudi z oknom alfa-beta.

#### MCTS

[Monte Carlo Tree Search](https://www.youtube.com/watch?v=UXW2yZndl7U)

Skratka glavna ideja je: izberemo naslednji list v drevesu stanj glede na podano formulo (oz. naključno). Za tisti list
nato izvedemo
simulacijo igre, ki nam doda informacije o tem, kako dober je ta list.

Nadgradnja je selekcija RAVE. Ideja tu je, da pri oceni poteze upoštevamo vse simulacije, ne samo tiste, v keteri
i nastopa – torej simulacije izvedene s to potezo.*

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-31-06-57-10.png" alt="RAVE" width="600">

* [RAVE](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)

### Okrepitveno učenje

Glavna ideja je, da se algoritem uči na podlagi izkušenj. Za dobre akcije dobi nagrado, za slabe kazen.
Ta algoritem oz. model, ki se uči imenujemo **agent**.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Reinforcement_learning_diagram.svg/250px-Reinforcement_learning_diagram.svg.png" alt="Reinforcement Learning">

Ostale oblike strojnega učenja so:

* Nadzorovano učenje
* Ne-nadzorovano učenje
* Semi-nadzorovano učenje

Pojmi:

- [ ] okolje - v njem deluje agent
- [ ] stanje - v njem se nahaja agent
- [ ] akcija - agent lahko izvede akcijo
- [ ] pravilnik/strategija - določa, kakšne akcije lahko izvede agent
- [ ] nagrada - nagrada, ki jo dobi agent za izvedeno akcijo
- [ ] izkušnja - stanje, akcija, nagrada, novo stanje

Cilj na dolgi rok je čim večja nagrada. Stanje - akcija - nagrada.

Naloge agenta so lahko epizodne - to pomeni, da je potrebnih več akcij, da se doseže cilj.

Naloga je zvezna, če ni nekih jasnih meja med akcijami.

#### Markovski odločitveni procesi

[Markov Decision Process](https://www.youtube.com/watch?v=2iF9PRriA7w)

Glavna ideja je, da je naslednje stanje (prehod) odvisno samo od trenutnega stanja.

Primer je recimo, da poskušamo priti do službe. Na voljo so nam avto, kolo in vlak.
Če gremo s kolesom, smo 100%, da bomo prišli v 45min. Če pa gremo z avtom, pa je recimo 10% možnost, da
naletimo na prometno nesrečo, kar pomeni, da bomo prišli v 60min. Je pa tudi 20% možnost, da bomo prišli v 30min.
Skratka, uvedemo verjetnost. Z vlakom pa bomo npr. prišli v 35min vedno. Skratka prehajamo med stanji in uvedemo
verjetnosti.
Pri vlaku pa lahko dodamo še 10% možnost za čakalnico, v katero pa se lahko vračamo in če smo prevečkrat čakali,
gremo lahko tudi nazaj domov in nato recimo z avtom ali kolesom.

Uvedemo negotovost - verjetnost.

Te verjetnosti so predstavljene z **modelom okolja**.

Izračun verjetnosti:

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-31-14-16-07.png" alt="Markovski odločitveni procesi" width="600">

#### Komponente RL

* [ ] **Pravilnik** - obnašanje agenta - katere akcije lahko izvede (npr. look-up tabela)
* [ ] **Signal nagrade** - zaželenost stanja kot korist izvedene akcije
* [ ] **Funkcija vrednosti** - dolgoročna vrednost posameznega stanja
* [ ] **Model okolja** - predstavitev okolja - posnema delovanje okolja - omogoča planiranje - agent model lahko ima ali
  pa ga nima (trial error)

Ker so akcije zaporedne, je lahko okrepitveno učenje težko - ni nujno, da je neka akcija na dolgi rok dobra: **problem
dodelitve zaslug**.

Ker je interakcija z okoljem vzorčena - torej nimamo popolnih informacij o okolju, je potrebno uporabiti
funkcijsko aproksimacijo pravilnika (npr. nevronska mreža).

#### Križci in krožci

Minimaks predpostavi, da nasprotni igralec igra optimalno - najbolje. Ker pa mi nimamo popolnega modela okolja, tega
ne moremo predpostaviti oz. predvideti.

<img src="http://incompleteideas.net/book/ebook/figtmp0.png" alt="Tic-Tac-Toe" width="600">

Med igro izbiramo med najboljšimi potezami (izkoriščanje) in naključnimi potezami (raziskovanje).
Po vsaki požrešni potezi popravimo vrednost stanja s pred nasprotnikovo potezo (ker se korak pred tem o potezi
odločamo mi) tako, da jo približamo vrednosti stanja s’ po odgovoru

Učenje s časovno razliko:

```
V(s) = V(s) + α·(V(s’) – V(s))
```

Alfa predstavlja hitrost učenja. Le-tega lahko sproti zmanjšujemo do 0. Potlej konvergira, ampak preneha z učenjem.

#### Reciklažni robot

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-31-14-37-18.png" alt="Reciklažni robot" width="600">

#### Povračilo

Cilj agenta je maksimizirati povračilo, t.j. nagrado na dolgi rok. Označimo ga z G. Je seštevek vseh prihodnjih nagrad.
Uvedemo pa še zniževalni faktor - tako so akcije, ki so blizu bolj pomembne od tistih v prihodnosti.

#### Pravilnik

Pove nam, kakšna je verjetnost, da bo agent v nekem stanju izvedel neko akcijo.

Funkcija vrednosti akcije? Določa pričakovano povračilo, če agent začne v stanju s, izvede akcijo a in sledi pravilniku
π.

Bellmanova enačba str. 34

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-31-14-44-16.png" alt="Bellmanova enačba" width="600">

#### Optimalni pravilnik

Skozi učenje želimo pravilnik izboljšati. Pravilnik je boljši, če velja

```
vπ1(s) ≥ vπ2(s) za vse s∈𝒮
```

Vedno obstaja optimalni pravilnik. Za ocenitev pravilnika rabimo neko metodo (policy-evaluation).
Da bi izbirali med več pravilniki, ni ravno učinkovito zato obstoječ pravilnik izboljšujemo.

Optimalni pravilnik lahko poiščemo z algoritmom **posplošene iteracije pravilnika**, ki ponavlja: 1) ocenitev pravilnika
(za trenuten pravilnik določimo vrednost stanj in akcij) in 2) izboljšanje pravilnika. Ponavljamo do konvergence
pravilnika
(tj. dokler ne dobimo optimalnega pravilnika).

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-2023-03-31-192732.png" alt="Optimalni pravilnik" width="600">

Po izboljšavi pravilnika izberemo najboljše akcije. Tak pravilnik je determinističen - v vsakem stanju izbere najboljšo
akcijo.
Za izboljšanje uporabljamo greedy metodo. Da pridemo do rešitve, niti ne rabimo čakati do konvergence.

[Policy Iteration](https://www.youtube.com/watch?v=l87rgLg90HI)

#### Raziskovanje okolja

Če poznamo okolje - imamo model okolja - lahko planiramo. V resničnem svetu tega nimamo, zato uvedemo učenje s poskusi
in napakami.
Iteracija pravilnika je primer dinamičnega programiranja.

Raziskovanje vs. izkoriščanje (pozna okolje, ima neke informacije) - kompromis.

Cilj agenta pa je maksimizirati skupno nagrado (povračilo).

#### Strategije raziskovanja

Požrešna (vedno najvišjo), naključna, ε-požrešna (z verjetnostjo ε izberemo naključno akcijo), optimistična
inicializacija
(začetne vrednosti visoke, postopoma znižujemo), softmax (verjetnost izbire akcije je proporcionalna vrednosti akcije),
UCB.
UCB spominja na Monte-Carlo metode.

#### Optimizacija pravilnika RL

Iskanje optimalnega pravilnika -> ni modela okolja -> raziskovanje, izkoriščanje -> nagrada, povračilo -> iskanje
maksimalnega povračila -> ocenitev pravilnika/izboljšanje pravilnika.

Pravilnik lahko stohastičen (naključen) ali determinističen (npr. greedy).

Problem napovedi - izračun vrednosti vseh stanj. Pričakovano povračilo lahko simuliramo z Monte-Carlo metodo.
Vzamemo povprečje več simulacij. Primerno za epizodne probleme: osvežitev stanj, akcij, pravilnika na koncu epizode.

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-2023-03-31-210410.png" alt="Monte-Carlo" width="600">

#### Učenje s časovno razliko

Monte-Carlo metoda je neučinkovita, ker je preveč stohastično. Učenje s časovno razliko kombinira Monte-Carlo in
dinamično programiranje. Monte-Carlo je dodano to, da se pravilnik posodablja z vsako akcijo.
Ocenitev pravilnika TD (ideja: z vsakim korakom t ocenimo pričakovano povračilo do konca epizode):

```
vπ(s) = 𝔼π[Gt:T|St=s]
= 𝔼π[Rt+1 + γ·Gt+1:T|St=s]
= 𝔼π[Rt+1 + γ·vπ(St+1)|St=s]
```

bootstrapping

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-2023-03-31-211018.png" alt="TD" width="600">

// TODO: The rest of the slides

### Predstavitev znanja z logiko

Pojmi:

- [ ] Izjave - dejstva
- [ ] Sklepanje - izpeljevanje novih dejstev
- [ ] Predstavitev znanja - predstavitev znanja v logični obliki - logika
- [ ] Stavki ali formule - dejstva v jeziku logike - baza znanja
- [ ] Sintaksa
- [ ] Semantika
- [ ] Resničen, neresničen stavek
- [ ] Logično sledi
- [ ] Algoritem sklepanja - iz baze znanja izpelje nova dejstva
- [ ] Smiselno sklepanje - ne sme biti nesmiselno - izpelje nekaj smiselnega iz baze znanja
- [ ] Poln - vse stvari, ki jih lahko izpeljemo iz baze znanja
- [ ] Boolova logika - logika, ki ima dve vrednosti: resnična in neresnična
- [ ] Atomarne izjave - nedeljive izjave
- [ ] Ne-atomarni stavki - deljivi na atomarne
- [ ] Konjunkcija, disjunkcija, implikacija, ekvivalenca, predpostavka, posledica, negacija
- [ ] Pravilnostna tabela
- [ ] Komutativnost, asociativnost, involucija (odstranitev negacije)
- [ ] Veljaven stavek - tavtologija
- [ ] Izpolnjiv stavek
- [ ] Dokaz s protislovjem - iz A sledi B
- [ ] Aksiomi -> teoremi = dokaz teorema
- [ ] Modus ponens, modus tollens

#### Resolucija

Uporablja se pri avtomatičnem dokazovanju. Deluje na stavkih, ki so klavzule (konjunkcija atomarnih izjav).
Velja, da lahko stavek P1 or P2 s stavkom ¬P1 or Q1 združimo v stavek P2 or Q1. Temu rečemo resolventa.

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-2023-03-31-212834.png" alt="Resolucija" width="600">

#### Predikatna logika prvega reda

Sladki spomini na diskretne strukture.

Štiri vrste simbolov:

- [ ] Simboli konstant - končni objekti
- [ ] Funkcijski simboli - preslikave med objekti
- [ ] Simboli spremenljivk - splošni objekti
- [ ] Simboli predikatov - relacije med objekti

Primer lastnosti: P(x, y) - x je oče y

Argumenti predikata so lahko zgoraj navedeni simboli. Rečemo jim termi. Predikate povežem z logičnimi operatorji (
konjunkcija, disjunkcija, implikacija, ekvivalenca, predpostavka, posledica, negacija).
vse spremenljivke morajo biti kvantificirane oz. vezane
(bound); nekvantificirane spremenljivke so proste (free)
– stavki z vsemi vezanimi spremenljivkami so zaprti
(closed).

Univerzalnostni kvantifikator: za vse x velja P(x).
Existencialni kvantifikator: za kakšen koli x velja P(x).

Stavki morajo biti pravilno oblikovani.

Imamo še predikatno logiko drugega reda.

#### Substitucija

Gre za zamenjavo spremenljivk, to je vse. Notacija v/t pomeni, da vse pojavitve "t" v stavku zamenjamo z "v".

Kompozicija: TODO
