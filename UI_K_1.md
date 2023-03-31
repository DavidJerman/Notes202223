# Umetna inteligenca

## Pred vprašanji

Sekcije s pojmi imajo na voljo check-marke. Le-te lahko označiš tako, da v oglate oklepaje namesto presledka vstaviš
`x`. Na primer: `[x]` označi tole. Tako si lahko daš zaznamke, kaj si že prebral.

## Vprašanja

#### Genetski algoritem

[Genetski algoritem](https://www.youtube.com/watch?v=1i8muvzZkPw)

### Iskanje v igrah

Omejili se bomo na igre med dvema igralcema.

Pojmi:

- [ ] Zero sum game
- [ ] Igre s popolno informacijo
- [ ] Kompleksnost prostora stanj
- [ ] Velikost drevesa iger

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
9. Ya G nam je tako vseeno. To vejo obrežemo.

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
Skratka, uvedemo verjetnost. Z vlakom pa bomo npr. prišli v 35min vedno. Skratka prehajamo med stanji in uvedemo verjetnosti.
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
* [ ] **Model okolja** - predstavitev okolja - posnema delovanje okolja - omogoča planiranje - agent model lahko ima ali pa ga nima (trial error)

Ker so akcije zaporedne, je lahko okrepitveno učenje težko - ni nujno, da je neka akcija na dolgi rok dobra: **problem dodelitve zaslug**.

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

Funkcija vrednosti akcije? Določa pričakovano povračilo, če agent začne v stanju s, izvede akcijo a in sledi pravilniku π.

Bellmanova enačba str. 34

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-31-14-44-16.png" alt="Bellmanova enačba" width="600">

#### Optimalni pravilnik

