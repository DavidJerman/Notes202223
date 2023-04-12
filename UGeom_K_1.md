# Uvod v računalniško geometrijo

## Snov

### Izbočena lupina

Izbočeni lupini rečemo tudi konveksna lupina. Ponavadi je naša naloga iskanje izbočene lupine
v neki množici točk – za ta namen imamo različne algoritme, ki jih bomo spoznali v nadaljevanju.

### Naivni algoritem/pristop

Ta algoritem je prepost, ampak zelo počasen.

Ideja je, da za vsako točko potegnem premice iz nje do vseh ostalih točk, ki še niso na lupini.
Nato izberemo premico, katera na eni strani nima nobenih točk. To najlažje naredimo z vektorskim 
produktom. Točke na tej premici bodo gotovo del izbočene lupine.

Časovna zahtevnost:
O(n^3)

### Jarvishev obhod/marš

Ta algoritem temelji na tem, da začnemo z neko ekstremno točko (npr. z največjo x koordinato).
Iz te točke nato potegnemo daljice do vseh ostalih točk in pri tem izračunamo polarni kot.
Premica z najmanjšim polarnim kotom nam pove, katera je naslednja točka na izbočeni lupini.
Postopek ponavljamo, dokler ne tvorimo celotne lupine, le da kote računamo glede na prejšnjo
premico.

Časovna zahtevnost:
O(h*n), kjer je h število točk na izbočeni lupini

### Grahamov algoritem/preiskovanje

Najprej izberemo poljubno točko o, ki je lahko npr. povprečje treh naključno izbranih točk.
Ta točka bo izhodišče polarnega koordinatnega sistema. Vse točke nato uredimo glede na polarni
kot - točke, ki imajo enak kot, pa glede na razdaljo od o (bližje središču je prej). Točke
nato vstavimo v dvojno povezan seznam. Nato po vrsti izbiramo točke: p1, p2, p3 in tvorimo
trikotnike. Če je trikotnik p1p2p3 pozitivno orientiran, točko p2 dodamo na lupino, sicer 
odstranimo točko p2 iz seznama in gremo po seznamu za eno mesto nazaj.

Časovna zahtevnost:
O(n*log(n))

### Inkrementalna metoda

Osnovna ideja:
- delno rešitev že imamo – torej imamo že izbočeno lupino
- dodamo novo točko, ki morda ni del izbočene lupine
- preverimo, ali je nova točka del izbočene lupine, če ni, jo odstranimo
- ponavljamo postopek, dokler ne zmanjka novih točk

Implementacija:
- izberemo tri nekolinearne točke, ki tvorijo trikotnik
- za preostale točke preverimo, ali so vsebovane v trikotniku
- če so, jih odstranimo, sicer dodamo v izbočeno lupino in popravimo izbočeno lupino
- ponavljamo postopek, dokler ne zmanjka točk

To, ali je nova točka del lupine ali ne, preverimo tako, da pogledamo, ali se obe sosednji
točki nahajata na isti strani poltraka. [slika 12] To preverimo s pomočjo vektorskega produkta.

Časovna zahtevnost:
O(n^2)

### Algoritem s preiskovalno premico

Imamo preiskovalno premico, ki se premika skozi prostor – ponavadi od leve proti desni
po osi x. Medtem naleti na dogodke – na naše točke. Glede na vrsto dogodka lahko osveži
podatkovno strukturo ali ne. To preiskovanje lahko implementiramo tako, da točke razvrstimo
glede na os vrednosti x koordinate.

Implementacija:
- točke uredimo glede na x koordinato
- z vsako novo točko nato samo popravimo lupino

Časovna zahtevnost:
O(n^2)

### Strategija deli in vladaj – Quickhull

Tu je glavna ideja, da uporabimo strategijo deli in vladaj. Problem ves čas delimo na dva dela.

Implementacija:
- najprej izberemo dve nasprotni ekstremni točki in potegnemo daljico skozi njiju
- dobimo dve množici
- znotraj te množice poiščemo točko, ki tvori maksimalno ploščino trikotnika z daljico (če jih
  je več, vzamemo tistega z največjim kotom)
- točke, ki padejo znotraj trikotnika, odstranimo, za ostale pa ponavljamo zgornji postopek

Implementacija je pogosto rekurzivna.

Psevdokod:

```
Quickhull(S):
    if velikost(S) <= 3:
        return S
    else:
        izberemo dve nasprotni ekstremni točki
        potegnemo daljico skozi njiju
        dobimo dve množici
        izloči točke v S1
        izloči točke v S2
        return Quickhull(S1) + Quickhull(S2)
```

Časovna zahtevnost:
O(n*log(n))

### Aproksimacijski algoritem

Ta metoda izgubi nekaj natančnosti, ampak je dosti hitrejša. Področje s točkami razdelimo na
trakove vzporedne z osjo y. V vsakem traku poiščemo točki z max in min y. Te točke so 
verjetno del izbočene lupine. Nad temi točkami nato uporabimo algoritem kot je Grahamov
algoritem.
