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

[Monte Carlo Tree Search](https://www.youtube.com/watch?v=onBYsen2_eA)
