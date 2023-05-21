# Kolokvij 2

## Pred vprašanji in snovjo

Simbol '*' za številko vprašanja namiguje na to, da vprašanje načeloma ni del predmeta, ampak koristi za boljše
razumevanje
ostalih vprašanj.

Vprašanja bolj ali manj zajemajo vso snov predavanj.

Priporočam tudi ogled videov in povezav podanih ob vprašanjih, saj ponujajo dobro razlago snovi in dodatno razumevanje.

Kratice:

* FT – Fourierjeva transformacija
* DFT – diskretna Fourierjeva transformacija
* FFT – hitra Fourierjeva transformacija

## Snov

### Uporaba FFT

FFT se v osnovi uporablja za prikaz (povprečne) frekvenčne vsebine signalov in slik.

Opozorilo: FFT pokaže frekvence z vidika, kako se najbolje prilagajajo signalu.
Poleg tega je potrebno paziti na to, da pri tem zaradi diskretne razdelitve frekvenčnega
prostora pride do razlivanja frekvenc.

Do problema pa pride, če je signal stacionaren - za posamezne trenutke ocena napačna.
Izboljšava: kratkočasovna DFT (STFT). Signal razrežemo na **okna**. Če vzorcev pri
izrezu ne spreminjamo, takemu oknu rečemo **kvadratno okno**. Imamo še razne druge tipe oken,
ki ublažijo efekt odrezanega signala. Rezultat STFT je **spektrogram** - je dvodimenzionalen,
medtem ko je običajen FFT enodimenzionalen. Druga dimenzija je čas.

### Kratkočasovna DFT

Za razliko od DFT ta metoda vpelje še čas. Kdaj je katera frekvenca prisotna. Za vsak odsek
signala posebej izračunamo DFT. Seveda tu nastane problemček ali dva, saj signal pogosto
odsekamo tako, da so v njem prisotne frekvence nad Nyquistovo frekvenco ali pa signala
zmanjka ipd.

### STFT

Celotni signal razrežemo na okna.
Pri tem pazimo na:

- MOŽNOSTI: okna se lahko stikajo ali celo prekrivajo
- IZRAČUN: za vsako okno posebej izračunamo FFT in rezultat zapišemo vzdolž osi y
- PAZITI: širina okna in vzorčevalna frekvenca odrejata frekvenčno ločljivost in ta
  je za celotno predstavitev STFT enaka

Primer:
glasba z vzorčevalno frekvenco 44.1 kHz in oknom širine 0.1 s ima frekvenčno ločljivost
10 Hz.

Vizualizacija STFT je spektrogram. Imamo os x (čas) in os y (frekvenca). Barva prikazuje
moč signala pri določeni frekvenci in času, torej amplitudo.

### Frekvenčno filtriranje signalov in slik

Ideja je samo, da naredimo s FFT prehod v frekvenčno domeno in nato tam v transformiranki
vrednosti (frekvence), ki jih ne želimo, postavimo na 0. Nato naredimo inverzno FFT in
dobimo filtriran signal.

Preprosta ideja in tudi dobra v teoriji, a ne deluje najbolje v praksi zaradi razlivanja
frekvenc, kar pa je posledica diskretizacije.

Pristop deluje paketno - FFT obdela signal določene dolžine naenkrat.

### Digitalno filtriranje

Želimo si realno-časovno filtriranje, torej, da se filtriranje izvaja med vzorčenjem.
FFT tu ni uporaben. Nov pristop: digitalno filtriranje.

IDEJA: uporabimo linearne sisteme MA, AR, ARMA. Problem: nestabilnost sistemov AR in
ARMA. Catch je v tem, da ker ponovno uporabljamo prejšnje izhode, da lahko amplituda
signalov eksplodira.

### MA in ARMA zapis sistema

[MA in ARMA zapis sistema](https://www.youtube.com/watch?v=5-2C4eO4cPQ)**

MA - Moving Average

AR - Auto Regressive

ARMA - Auto Regressive Moving Average

```textmate
y[n] = x[n] + x[n - 1] + x[n - 2] + ... + x[n - L + 1]  -->  MA  -->  računsko zahtevno
```

alternativno:

```textmate
y[n] = y[n - 1] + x[n] - x[n - L]  -->  AR(MA)  -->  nestabilnost
```

Pridobimo na hitrosti a obstaja nevarnost nestabilnosti. Lepo se vidi regresija.

Splošna oblika MA zapiska (diferenčna enačba filtra):

```textmate
y[n] = b[0] * x[n] + b[1] * x[n - 1] + ... + b[L] * x[n - L + 1]  -->  MA(L)
```

Splošna oblika ARMA zapisa (diferenčna enačba filtra):

```textmate
y[n] = b[0] * x[n] + b[1] * x[n - 1] + ... + b[L] * x[n - L + 1] + a[1] * y[n - 1] + ... + a[L] * y[n - L + 1]  -->  ARMA(L, M)
```

Pri tem so **a** koeficienti AR, **b** pa koeficienti MA. Število a in b koeficientov
določa red sistema oz. red filtra. Red filtra = max(a, b).

Več o filtrih: [Digitalni filtri](https://en.wikibooks.org/wiki/Signal_Processing/Digital_Filters)

### Delitev filtrov

- Digitalni filtri:
    - **FIR** (Finite Impulse Response) - izhod takšnega filtra je odvisen od **končnega** števila
      vzorcev vhodnega signala. Pri takšnih filtrih ponavadi najdemo **b** koeficiente.

      ![FIR](https://wikimedia.org/api/rest_v1/media/math/render/svg/bfc7e9ab283882ceed75eed09f4d6ec5d5e5cc27)

      Pri sliki zgoraj so **b** koeficienti uteži, **x**-i pa so vzorci vhodnega signala.

      ![FIR](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/FIR_Filter.svg/750px-FIR_Filter.svg.png)

      Računsko zelo zahtevni brez prilagoditve implementacije.

      Izbira takšnega filtra omogoča linearno fazo.

        - **MA** (Moving Average) Filtri - V bistvu gre za FIR filtre, ki za koeficiente uporabljajo
          uteži, ki so skalirane vrednosti 1. Običajen FIR filter pa ima prilagojene koeficiente glede
          na filter. Gre za alternativno prezentacijo FIR filtrov.

          ![MA](https://wikimedia.org/api/rest_v1/media/math/render/svg/d3d0e85a3774b233e985cbf540d050fb86dad1a2)

    - **IIR** (Infinite Impulse Response) - izhod takšnega filtra je odvisen od **neskončnega**
      števila vzorcev vhodnega signala. Pri takšnih filtrih ponavadi najdemo **a** in **b** koeficiente.
      Če imamo neko določeno število koeficientov a in b, je **red filtra** enak max(a, b).

      ![IIR](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Biquad_direct_form_2_transposed.svg/300px-Biquad_direct_form_2_transposed.svg.png)

        - **AR** (Auto Regressive) Filtri - V bistvu gre za IIR filtre, ki za koeficiente uporabljajo
          uteži, ki so skalirane vrednosti 1. Običajen IIR filter pa ima prilagojene koeficiente glede
          na filter. Gre za alternativno prezentacijo IIR filtrov.

          ![AR](https://wikimedia.org/api/rest_v1/media/math/render/svg/437303f4633eb600690c70c746eda47bfd3d73af)

        - **ARMA** (Auto Regressive Moving Average) Filtri - gre za filtre, ki so kombinacija AR in MA
          filtrov. Potemtakem je formula sledeča:

          ![ARMA](https://wikimedia.org/api/rest_v1/media/math/render/svg/ff42a8229f7766a8d774af512a714af896554e6b)

          Pri tem so **a** koeficienti AR, **b** pa koeficienti MA. Število a in b koeficientov določa
          red sistema oz. red filtra. Red filtra = max(a, b). ARMA filtri so digitalni IIR filtri s poli
          in ničlami.

### Z transformacija

Z transformacija je transformacija, ki jo uporabljamo za prehod iz časovne domene v frekvenčno
domeno. Z transformacija je podobna Laplaceovi transformaciji, le da je Z transformacija
diskretna. Razlika med FFT ali DFT v primerjavi z Z transformacijo pa je v glavnem ta, da Z
transformacija ponuja še dodatne informacije. DFTF dela z realnimi števili, Z transformacija
pa s kompleksnimi števili. Z transformacija je definirana kot:

![Z transformacija](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-2023-05-21-084615.png)

Za Z transformacijo velja:

- linearnost,
- premik,
- konvolucija kot množenje,

Rezultat Z transformacije je v bistvu polinom.

[Več o Z transformaciji](https://www.youtube.com/watch?v=mJgVOV9jRZU)

Primeri so na prosojnicah stran 14, 15, 16.

### Z transformacija - ARMA sistem

[//]: # (TODO: Napiši vsebino za to poglavje)

### Frekvenčni odzivi idealnih filtrov

Vrste filtrov/sit:

- nizko sito - low pass filter (**LPF**) - prepušča nizke frekvence, visoke zatre
- visoko sito - high pass filter (**HPF**) - prepušča visoke frekvence, nizke zatre
- pasovno prepustno sito - band pass filter (**BPF**) - prepušča frekvence v določenem pasu, ostale zatre
- pasovno zaporno sito - band stop filter (**BSF**) - zatre frekvence v določenem pasu, ostale prepušča

Pojmi:

- **ojačenje** - gain - ojačenje signala
- **lomna frekvenca** - cutoff frequency - frekvenca, pri kateri se začne zmanjševati ojačenje
- **pasovna širina** - bandwidth - razlika med zgornjo in spodnjo lomno frekvenco
- **središčna frekvenca** - center frequency - središčna frekvenca pasovno prepustnega/zapornega sita

Primeri filtrov:

- **Butterworth**
- **Chebyshev**
- **Bessel**
- **Elliptic**
- **Gaussian**

Filter name ponavadi vrne A in B koeficiente, ki jih lahko uporabimo za implementacijo filtra.
Pri ustvarjanju filtra določimo red filtra, lomne frekvence in tip filtra. Poleg tega pa še
metodo ustvarjanja filtra (npr. Butterworth, Chebyshev, ...).

Filtri s pomočjo teh koeficientov in vhodnega signala izračunajo izhodni signal.

### Šum in motnje

Izhodni signal pa seveda ni popoln. Malce se pokvari zaradi šuma in motenj. Razmerje med šumom
in motnjami opišemo z **SNR** (Signal to Noise Ratio). SNR je razmerje med močjo signala in močjo
šuma. SNR je v decibelih (dB).

```text
SNR = 10 * log10(Es / En)    [dB]
```

#### Odstranjevanje šuma in motenj s filtriranjem

Recimo imamo signal, kjer je SNR=10dB, torej je moč signala 10x večja od moči šuma.
Šum je nad 1.5 kHz.
Tvorimo nizko sito z lomno frekvenco 1 kHz.

```matlab
[B, A] = butter(5, 1000/22050, 'low');
y = filter(B, A, x);
```

### 2D digitalni filtri

Princip delovanja 2D filtrov je enak kot pri 1D filtrih. Razlika je samo v še eni dimenziji in
implementaciji. Enako je 2D filtriranje 2D konvolucija med impulznim odzivom 2D filtra in vhodnim
signalom (sliko).

2D filtrom rečemo tudi **lokalni slikovni operatorji**, **maske** ali **kerneli** (jedra).

Delovanje tega filtra je takšno, da jedro premikamo preko slike, množimo s sliko in seštevamo
rezultate. Rezultat je nov pixel v izhodni sliki.

POZOR: pri tem pogosto pride do ojačenja, zato je potrebno rezultat normalizirati.

#### 2D nizko sito

2D nizko sito je v bistvu uporaba filtra, kjer so vse vrednosti filtra enake 1/N, kjer je N
število vrednosti v jedru filtra. Gre v bistvu za glajenje, blur, smoothing.

Ta metoda iz slike odstrani šum, je pa res da slika s tem izgubi nekaj informacij v smislu
ostrosti.

#### Gradient v sliki

Na sliko lahko gledamo tudi kot na spektrogram, kjer osi x, y predstavljata piksle, os z pa
intenziteto. Potlej vidimo, da razlike v barvah v bistvu predstavljajo gradient - naklon -
slike. Po tem principu tudi deluje iskanje robov.

#### Zaznava robov

Naklon v sliki - torej rob - dobimo kot razliko sosednjih pikslov. Večja kot je razlika, bolj
strm je naklon, bolj strm je naklon, bolj verjetno je da gre za rob.

Če med piksli ni razlike, potem je naklon 0, torej ni roba.

Slikovni operatorji, ki zaznavajo robove:

Robertsov operator:

```text
c0 = [-1  0]   c1 = [ 0 -1]
     [ 0  1]        [ 1  0]
```

c0 zaznava desno diagonalo, c1 pa levo diagonalo.

Laplaceov operator:

```text
c0 = [ 0 -1  0]   c1 = [-1 -1 -1]
     [-1  4 -1]        [-1  8 -1]
     [ 0 -1  0]        [-1 -1 -1]
``` 

c0 zaznava vodoravne in navpične robove, c1 pa vse robove.
Laplaceov operator je bolj občutljiv na šum.**

Sobelov operator:

```text
c0 = [-1  0  1]   c1 = [-1 -2 -1]
     [-2  0  2]        [ 0  0  0]
     [-1  0  1]        [ 1  2  1]
```

c0 zaznava navpične robove, c1 pa vodoravne robove.

Najbolje je, da kombiniramo dva Sobelova operatorja namesto da uporabimo Laplaceov operator.
Dobimo lepšo zaznavo robov, manj šuma.

#### Frekvenčni odziv 2D filtrov

Nizko sito prepušča nizke frekvence, visoke pa duši, kar se na sliki kaže kot to, da se hitre
spremembe sivin izločijo - torej se slika "zamegli" oz zgladi.

Operatorji za odkrivanje robov namreč računajo gradient. Ta operacija pa ustreza Laplaceovemu
ali Sobelovemu situ. Odkrivanje robov duši nizke frekvence in poudarja visoke frekvence - torej
robove, spremembe sivin.

#### Canyev detektor robov

Problem zaznave robov je, da je detekcija pogosto taka, da so robovi natrgani. Canny predlaga
postopek, kako te robove povezati.

Cannyev postopek:

1. Obdelava slike z Gaussian filtrom
2. Določanje slikovnih gradientov z Robertsovim operatorjem
3. Izbira vstopnega in izstopnega praga - basically meja med tem kaj je in ni rob
4. Iskanje dovolj visokih gradientov, ki se dajo povezati v sklenjene robove - definicija
   sosedstev med piksli

### Odkrivanje in razpoznavanje oblik

Posamezne lastnosti slik lahko izločimo s pomočjo filtrov. Tem lastnostim rečemo tudi značilke
(features). Izločanje značil pa imenujem feature extraction.
Te značilke lahko nato posredujemo nevronski mreži. To je v bistvu tudi nadgradnja zaznave.
Recimo vemo, da gre za jabolko, če je okroglo in rdeče.

#### Razpoznavalni sistemi

Pojavom in objektom rečemo **oblike** (patterns). Če lahko izločimo vse značilnice, lahko
te objekte klasificiramo. Razpoznavanje oblik lahko opravi **razpoznavalni sistem**.

Postopek:

1. zaznava objekta v realnem svetu in pretvorba v sliko
2. izločitev značilnic --> prehod v prostor značilnic
3. klasifikacija --> prehod v prostor razredov / odločitveni prostor

#### Zaznavanje oblik

Da lahko dobimo značilke, moramo najprej zaznati objekt. Oblike zaznamo v **času** ali
**prostoru**. Zaznave imajo svojo razsežnost - bodisi dimenzije ali časovno razsežnost.
Skratka naš cilj je zaznava začetka in konca objekta.
Temu postopku rečemo segmentiranje, ker izberemo segment signala, kjer se objekt nahaja.

#### Segmentacija

Segmentiranje lahko opravimo ali v časovnem/slikovnem prostoru ali v frekvenčnem prostoru.

Glede na prag se nato odločimo, ali je objekt prisoten ali ne. To je binarna odločitev.
Rečemo, da signal **binariziramo**. Rečimo, če iščemo rdeče jaboljko, določimo nek
prag za rdečo, modro in zeleno.

#### Določanje pragov

Prag moramo pač dobiti s poskušanjem, dokler le-ta ne izloči vseh neželenih objektov.
V veliko pomoč tu nam je histogram.

#### Histogram

Histogram je grafični prikaz porazdelitve vrednosti v signalu, kjer recimo opazujemo neko
značilko, kot je recimo sivina. Tako bo histogram prikazoval koliko katerega nivoja sivine
je prisotnega v sliki.

Tako najpogosteje tvorimo histogram amplitud. Primeri historgramov so tako: histogram za
elektrodiagram in sivinsko umetno sliko.

Histogram ima tako neko maksimalno in minimalno vrednost, poleg tega pa ima določeno število
razredov. Razred je neka skupina vrednosti. Tako lahko histogram razdelimo na 256 razredov za
sivinsko sliko.

#### Uporabnost histogramov

Z uporabo linearizacije lahko na sliki izboljšamo kontrast, če recimo so vse vrednosti histograma
pod neko vrednostjo - razporedimo vrednosti čez celotno x-os in s tem dobimo boljši kontrast ter
posledično lažjo ekstrakcijo značilnic oz. segmentacijo še pred tem. Še ena podobna izboljšava je
ekvalizacija histograma, kjer razporedimo vrednosti histograma tako, da je porazdelitev čim bolj
enakomerna. Na sliki se to vidi kot izenačitev svetlosti, nam pa pomaga pri segmentaciji.

Pri segmentaciji nato kot že omenjeno izberemo dva praga, ki določata, katere vrednosti bomo 
sprejeli in katere ne.

#### Pragovna segmentacija

