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

Pomembno:

- impulzni odziv == časovna domena
- frekvenčni odziv == frekvenčna domena

## Snov

### Uporaba FFT

FFT se v osnovi uporablja za prikaz (povprečne) frekvenčne vsebine signalov in slik.
Pokaže, kako "močno" je neka frekvenca prisotna v signalu. To lahko pomeni ali
kako dolgo je prisotna ali s kakšno amplitudo je prisotna.

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

Pridobimo na hitrosti a obstaja nevarnost nestabilnosti. Lepo se vidi regresija.**

Splošna oblika MA zapisa (diferenčna enačba filtra):

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

### Zakaj pa tako je [ChatGPT]

The use of both autoregressive (AR) and moving average (MA) components in an ARMA filter is based on the idea
that many real-world processes can be modeled as a combination of these two types of behavior.

Autoregressive behavior suggests that the current value of a variable is dependent on its own past values.
For example, in a time series, the current value may be influenced by its recent history. By including the
AR component in an ARMA filter, it takes into account this autoregressive behavior and models the relationship
between the current output and its own past values.

Moving average behavior, on the other hand, suggests that the current value of a variable is influenced by past
values of another variable (often the input variable). It assumes that there is a short-term memory effect in
the system, where the current output depends on the recent past inputs. Including the MA component in an ARMA
filter captures this moving average behavior and models the relationship between the current output and past
input values.

By combining both AR and MA components in an ARMA filter, it becomes more flexible and capable of capturing
different types of dependencies in a system. This allows the model to better represent and predict the behavior
of various processes, making it a widely used tool in time series analysis and forecasting.

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
transformacija ponuja še dodatne informacije. DFT dela z realnimi števili, Z transformacija
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

Filter nam ponavadi vrne A in B koeficiente, ki jih lahko uporabimo za implementacijo filtra.
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
enakomerna. Na sliki se to vidi kot izenačitev svetlosti, nam pa pomaga pri segmentaciji. Značilna
območja histograma predstavljajo podobne lastnosti v signalu.

Pri segmentaciji nato kot že omenjeno izberemo dva praga, ki določata, katere vrednosti bomo
sprejeli in katere ne.

#### Pragovna segmentacija

Pragovna segmentacija temelji na histogramu. Različne segmente ločimo s pragovi. Lahko si določimo
globalne pragove ali pa lokalne pragove. En prag ali več pragov. Ideja je, da če je vrednost
nad pragom, da rečemo, da gre za ospredje, da pa če je manjša, da gre za ozadje. Kot prag
bi lahko preprosto vzelo kar povprečje ospredja in ozadja kot:

```math
T = (Tb + Tf) / 2
```

Globalni prag ponavadi določimo z uporabo naslednjih dveh formul:

```math
Aj = sum[n=0, j] Hist(n)
Bj = sum[n=0, j] n Hist(n)

j = 0, ..., R-1 (ponavadi 255)
```

S pomočjo A in B nato določimo izbrani prag. Problem pa je, da ker gre tu za globalni prag, da
rezultati morda ne bodo najboljši. Zato lahko uporabimo lokalne prage, kjer za vsak piksel
določimo svoj prag. Tako dobimo boljše rezultate, vendar pa je to tudi bolj računsko zahtevno.

##### Vrste pragov

Prag določen z mediano:

```math
T = At / Ar
```

Dela precej slabo, če imamo veliko šuma.

Povprečni prag:

```math
T = Br / Ar
```

Se dobro obnaša pri šumih SNR >= 20.

Optimalni prag - ga iterativno spreminjamo, dokler spremembe niso več opazne:

```math
Tk+1 = (uTk + vTk) / 2

uTk = BTK / ATk
vTk = (Br - BTK) / (Ar - ATk)
```

Dela dobro pri šumih s SNR >= 10.

Iskanje optimalnega pragu je načeloma poskušanje, dokler ne dobimo dobrih rezultatov.

##### Čemu segmentacija

Namen segmentacije je izločitev objekta iz ozadja. To nam omogoča, da lahko izločimo značilnice
objekta, ki jih nato uporabimo za klasifikacijo. Značilnice so lahko oblike, barve, teksture,
robovi, itd. Potlej lahko bolj uspešno izvedemo klasifikacijo. Po tem principu tudi delujejo
konvolucijske nevronske mreže.

Pri tem je vredno še dodati, da načeloma težko rečemo, ali je nek prag slab ali dober in da
je to dosti lažje reči šele ko dobimo rezultate klasifikacije. Bolj uspešen kot naš model
je pri dajanju napovedi, boljša je naša segmentacija.

##### Lokalni prag

Lokalni optimalni prag lahko izračunamo na sledeč način:

```math
T = Topt(1 - x)
```

kjer je x korekcijska vrednost piksla izračunana kot:

```math
x = 1/3R(|a - b - c + d| + |a - b + c - d| + |a + b - c - d|)
```

kjer so a, b, c in d sosednji piksli.

Iz formule zgoraj je mogoče tudi opaziti, da gre v bistvu za detektorje robov! Prvi je
sicer malce čuden, ampak zaznava diagonalne robove. Drugi je za zaznavanje navpičnih robov,
tretji pa za zaznavanje vodoravnih robov.

Uporaba te metode najbrž ne bo prikazala ogromnih vizulanih rezultatov, a se bo zelo dobro
poznalo na klasifikaciji.

#### Klasifikacija

Pri linearni klasifikaciji je najlažji način klasifkacije uporaba linearnega klasifikatorja.
Točke lahko razdelimo na množice točk z uporabo klasifikatorjev. Klasifikacijo izvajamo
v prostoru značilnic. Recimo primer:

![Klasifikacija](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-2023-05-25-201540.png)

[//]: # (Vir: Predavanja)

Pri klasifikaciji se je potrebno seznaniti še z nekaj pojmi:

- **TP** - true positive - pravilno pozitivni
- **TN** - true negative - pravilno negativni
- **FP** - false positive - napačno pozitivni
- **FN** - false negative - napačno negativni

Primer:

Imamo 30 jabolk in 30 hrušk. Zaznali smo 35 jabolk in 25 hrušk. Kaj je TP, TN, FP in FN?

Z vidika jabolk:

- TP: 30
- TN: 25
- FP: 5
- FN: 0

Rezultat: 30/35 = 0.86

Nato imamo še pojma:

- **TPF** - true positive fraction - senzitivnost
    - TPF = TP / (TP + FN)
- **TNR** - true negative fraction - specifičnost
    - TNR = TN / (TN + FP)
- **FNF** - false negative fraction
    - FNF = 1 - TPF
- **FPF** - false positive fraction
    - FPF = 1 - TNF

Za primer zgoraj so rezultati:

- TPF: 1
- TNR: 0.83
- FNF: 0
- FPF: 0.17

##### Natančnost modela

V praksi tako iščemo kompromis med TPF in TNR. To lahko naredimo z uporabo ROC krivulje.
ROC krivulja je krivulja, ki prikazuje odvisnost TPF od FPF. Najboljša je ponavadi tista,
ki se čim bolj približa enemu izmed robov na osi y = x. Najslabša krivulja pa je tista,
ki gre skozi os y = -x.** Čim bližje smo tej diagonali, tem slabši je naš model za
predikcije.

Optimalni prag tako iščemo na ta način, da opazujemo spreminjan ROC krivulje in iščemo
AUC (area under curve), ki je čim večji. AUC je v bistvu ploščina pod krivuljo. Če je
AUC = 1, potem je naš model popolnoma natančen.

ROC - receiver operating characteristic. ROC krivulja ponavadi izgleda nekako takole:

![ROC](https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/ROC_space-2.png/800px-ROC_space-2.png)

[//]: # (Vir: Wikipedia)

Več o tem:

- [ROC krivulja](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
- [AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)
- [Neka spletna stran](http://www.anaesthetist.com/mnm/stats/roc/Findex.htm)

## Vprašanja

### 1. Kratkočasovna Fourierova transformacija - STFT

- [x] Done

Ideja tu je, da namesto, da obdelamo celoten signal, signal razdelimo v okna in v vsakem
oknu izvedemo Fourierovo transformacijo. Tako dobimo še dodatne informacije o času, v katerem
se je pojavila določena frekvenca. Seveda pa se tu pojavi "trade-off". Ker je okno omejeno,
pride do manjše natančnosti pri določanju frekvenc - do manjše resolucije. Večjo frekvenčno
resolucijo/ločljivost kot želimo, manjšo časovno resolucijo bomo imeli.

Kako pa to veš iz slike? Tista slika, kjer je so barve bolj "razpacane" je najverjetneje
uporabljala manjše okno.

### 2. Težave s STFT

- [x] Done

Kot že omenjeno je eden izmed problemov frekvenčna ločljivost vs. časovna ločljivost.

Drugi problem pa je frekvenčno razlivanje, pa tudi to, da določen signal ni prisoten
skozi celotno okno.

### 3. Primer SFTF

- [x] Done

```
Fvz = 44.1k
Dolzina okna: 0.1s

Ugotovitev:
število vzorcev: 44.1k
frekvenčna ločljivost: 1/0.1 = 10Hz
```

STFT lahko prikažemo z uporabo 3D grafa ali pa 2D grafa, kjer je z os barvna lestvica.

### 4. Filtriranje

- [x] Done

Ideja filtriranja je v osnovi to, da se določenih frekvenc v signalu želimo znebiti. Predvsem
gre tu za to, da se znebimo šuma in izboljšamo razmerje SNR (signal to noise ratio).

Prvi način filtriranja je v frekvenčni domeni, kjer samo ustvarimo okno z ničlami in enicami
in to pomnožimo s signalom. Ničle izničijo frekvence, ki jih ne želimo.

### 5. Zakaj NE filtriranje v frekvenčni domeni?

- [x] Done

Razloga sta dva:

- zaradi frekvenčnega razlivanja se lahko zgodi, da izničimo tudi frekvence, ki jih ne bi
  smeli - zgubimo nekaj natančnosti
- takšno filtriranje deluje offline, kar pomeni, da rabimo celoten posnetek preden lahko
  filtriramo, kar pa pomeni, da ne moremo filtrirati real-time

### 6. Filtriranje v časovni domeni

- [x] Done

Prejšnjo idejo lahko prenesemo v časovno domeno. Poznamo frekvenčno karakteristiko filtra,
ki jo lahko prenesemo v časovno domeno, da dobimo impulzni odziv filtra. To storimo s
pomočjo inverzne Fourierove transformacije.

### 7. Frekvenčna transponiranka impulznega odziva

- [x] Done

Izraz "frekvenčna transponiranka impulznega odziva" se nanaša na postopek pretvorbe impulznega
odziva filtra iz časovne domene v frekvenčno domeno. Ta postopek se izvaja s pomočjo diskretne
Fourierove transformacije (DFT) ali hitre Fourierove transformacije (FFT).

Postopek frekvenčne transponiranke impulznega odziva je naslednji:

1. Najprej morate imeti **impulzni odziv** filtra v časovni domeni. Impulzni odziv je odziv filtra
   na enotski impulz.

2. Uporabite diskretno Fourierovo transformacijo (DFT) ali hitro Fourierovo transformacijo (FFT)
   na impulzni odziv filtra v časovni domeni. To pretvori impulzni odziv v frekvenčno domeno.

3. Rezultat je frekvenčna transponiranka impulznega odziva, ki predstavlja spekter filtra v
   frekvenčni domeni. Temu rečemo tudi **frekvenčna karakteristika filtra**.

Frekvenčna transponiranka impulznega odziva se uporablja za analizo frekvenčnih lastnosti filtra.
Na podlagi tega spektra je mogoče določiti, kako filter vpliva na različne frekvence v vhodnem
signalu. Poleg tega se frekvenčna transponiranka impulznega odziva lahko uporabi tudi za oblikovanje
in optimizacijo filtrov.

### 8. MA, AR in ARMA modeli

- [x] Done

Sledeči modeli so filtri tipa **IIR** - infinite impulse response. To pomeni, da imajo lahko neskončen
impulzni odziv.

Pri obeh modelih delamo s preteklimi vzorci. Na ta način dobimo občutek za to, kako se je signal
spreminjal v preteklosti. Namen teh modelov je, da opravijo filtriranje signala.

MA sistem je sistem oblike:

```
y[n] = b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] + ... + bL * x[n-L+1]
```

Sprejema prejšnje **VHODNE** vrednosti. Išče tekoče povprečje prejšnjih vhodnih vrednosti. Zato
se tudi imenuje _Moving Average_. To povprečje pa se nato pomnoži z nekimi koeficienti, ki
dosežejo efekt filtriranja. Problem **MA** je visoka računska zahtevnost. Pri njem najdemo
**koeficiente b**.

AR sistem je sistem oblike:

```
y[n] = a1 * y[n-1] + a2 * y[n-2] + ... + aL * y[n-L+1]
```

Sprejema prejšnje **IZHODNE** vrednosti. Na dolgo mu rečemo _avtorekurzivni_ ali _autoregressive_
sistem. AR sistem je avtorekurzivni, kar pomeni, da izhodni vzorec filtra vpliva na naslednje izhodne
vzorce. Pri njem najdemo **koeficiente a**.

ARMA model pa kombinira oba modela. ARMA model je sistem oblike:

```
y[n] = b0 * x[n] + b1 * x[n-1] + b2 * x[n-2] + ... + bL * x[n-L+1] 
       + a1 * y[n-1] + a2 * y[n-2] + ... + aL * y[n-L+1]
```

**Red filtra** je max(L, M), kjer je L red MA sistema in M red AR sistema oz. število koeficientov
b in a.

Pa še ne pozabi, vse opisano je v bistvu **KONVOLUCIJA**.

[Vloga MA in AR modelov by ChatGPT]

V kontekstu filtriranja signalov ima AR (avtoregresivni) model vlogo modeliranja odvisnosti izhodnega vzorca od
preteklih izhodnih vzorcev. AR model pomaga zaznati vzorce ali trende v signalu ter jih uporabiti za filtriranje ali
napovedovanje prihodnjih vzorcev. Z drugimi besedami, AR model se osredotoča na preteklost izhodnega signala, da bi
razumel njegovo strukturo.

MA (gibanjsko povprečje) model pa ima vlogo zglajevanja signala in odstranjevanja šuma. MA model se osredotoča na
preteklost vhodnega signala in izračuna tekoče povprečje prejšnjih vhodnih vzorcev. To zmanjšuje vpliv naključnih nihanj
in šuma v signalu, kar omogoča bolj gladko in stabilno filtriranje.

ARMA model, ki združuje tako AR kot tudi MA komponento, se uporablja za bolj prilagodljivo filtriranje signalov. AR del
pomaga zajeti odvisnost izhodnega signala od preteklih izhodnih vzorcev, medtem ko MA del prispeva k zglajevanju signala
in odstranjevanju šuma. Združevanje obeh modelov omogoča bolj natančno in učinkovito filtriranje signalov ter
napovedovanje prihodnjih vzorcev.

Torej, AR model pomaga razumeti strukturo in vzorce v izhodnem signalu, medtem ko MA model zgladi signal in odstrani
šum. Skupaj se uporabljata za ustvarjanje učinkovitih in prilagodljivih filtrov za obdelavo signalov.

### 9. Prednosti in slabosti ARMA modela

- [x] Done

Ena izmed slabosti je, da so takšni filtri lahko nestabilni. Do te nestabilnosti lahko pride,
kadar so koeficienti A zelo blizu 0. Poleg tega se je treba zavedati, da ARMA model signal
rekurzivno pošilja samega vase, kar lahko povzroči, da amplituda eksplodira.

Prednosti pa so to, da imamo lahko recimo neskončen impulzni odziv in vseeno zelo dobro
filtriramo želene frekvence.

### 10. Impulzni odziv

- [x] Done

Kadar je vrednost vseh koeficientov A enaka 0, razen prvega 1, je impulzni odziv kar enak B.

Impulzni odziv ARMA modela je v Z ravnini definiran kot:

```
H(z) = B(z) / A(z)
```

MA sistem:

```
H(z) = B(z)
```

AR sistem:

```
H(z) = 1 / A(z)
```

ARMA sistem:

```
H(z) = B(z) / A(z)
```

### 11. Kaj je Z transformacija?

- [x] Done

V bistvu gre za manjšo priredbo Laplaceove transformacije. Z transformacija je namenjena
analizi diskretnih sistemov in signalov, ravno tako kot DFT. Olajša nam določene operacije,
ki bi sicer bile zelo zahtevne v časovni domeni.

Z transformacija je definirana kot:

```
Y(z) = sum(n=0, N-1) y[n] * z^-n

z = e^(jw)

ali

z = e^(-n * 2 * pi / N * k)
```

Kot v Z ravnini določa frekvenco. Poleg tega je vredno omeniti, da je Z **kompleksen**,
zato je potreben tudi prikaz v kompleksni ravnini.

Za Z transformacijo pa je značilna tudi konvolucija in deluje na enak način kot DFT.
Torej, da samo zmnožimo frekvenčni odziv z vhodnim signalom.

### 12. Z transformacije zgledi

- [x] Done

```
y[n] = [1, 2, 3, 4, 5]

Y(z) = 1 * z^0 + 2 * z^-1 + 3 * z^-2 + 4 * z^-3 + 5 * z^-4
```

Kar opazimo je, da gre za polinom.

### 13. Stabilnost ARMA modela

- [x] Done

Stabilnost ARMA sistema lahko zlahka ugotavljamo v Z ravnini. Namreč vemo, da je impulzni
odziv ARMA modela enak:

```
H(z) = B(z) / A(z)
```

In ta odziv je v bistvu polinom. Koeficienti b nam dajo ničle, koeficienti A pa pole.
Pravimo tudi, da gre za **sistemovo prenosno karakteristiko**.

S pomočjo ugotavljanja ničel in polov lahko nato govorimo o stabilnosti sistema. Najprej
je vredno pomniti, da se frekvence na enotski krožnici za nek filter odražajo takole:

![Frekvence na enotski krožnici](https://davidblog.si/wp-content/uploads/2023/06/Screenshot-2023-06-03-195627.png)

Filter je stabilen, če so vsi poli **ZNOTRAJ** enotske krožnice. To pomeni, da impulzni odziv
sistema skozi čas pada in ne narašča, kar si tudi želimo. Namreč, če so poli zunaj enotske
krožnice pomeni, da imajo višjo magnitudo, kar pa vodi v nestabilnost filtra.

Pa dodal bi še, da je red filtra max(ničle, poli).

### 14. Razumevanje filtrov s pomočjo enotske krožnice

- [x] Done

Samo logičen pomislek. Ničle pomeni, da se funkcija v tisti okolici približa ničli.
Frekvence v tistem območju sili k ničli.
Poli pa pomenijo, da se funkcija v tisti okolici približa neskončno. Torej tiste
frekvence ohranja. Od tod sledi,
da tam kje najdemo ničle, da se frekvence filtrirajo, tam pa, kjer najdemo pole, se 
frekvence ojačajo.

Tako bi nizkoprepustni filter imel ničlo na levi, pol pa na desni. Torej, vse frekvence
blizu Fvz/2 bi bile filtrirane, vse frekvence blizu 0 pa bi bile ojačane. Seveda, poli
pri tem NE smejo biti izven enotske krožnice, saj bi to pomenilo nestabilnost filtra.
Poleg tega pa, filtri ne morejo biti popolni, nekaj frekvenc vedno preide skozi filter.

### 15. Lomna frekvenca

- [x] Done

Lomna frekvenca je frekvenca, kjer se začnejo frekvence filtrirati. Bolj konkretno, je
meja pri **0.7** amplitude oz. **-3dB**.

### 16. Ostale lastnosti filtrov

- [x] Done

**Območja filtra**

- prepustno območje - območje, kjer se frekvence prepuščajo
- prehodno območje - območje, kjer prehajamo iz območja prepuščanja v območje filtriranja
- zaporno območje - območje, kjer se frekvence filtrirajo

**Tipi filtrov**

- nizkoprepustni - prepušča frekvence do lomne frekvence
- visokoprepustni - prepušča frekvence nad lomno frekvenco
- pasovni - prepušča frekvence med dvema lomnima frekvencama
- pasovno zaporno - prepušča frekvence izven dveh lomnih frekvenc

### 17. Primer opisa filtra

- [x] Done

Opiši sledeči filter:

![Primer filtra](https://davidblog.si/wp-content/uploads/2023/06/Screenshot-2023-06-03-201757.png)

Če predpostavimo, da frekvence gredo od manjše proti večji, potem gre za nizkoprepustni
filter. Lomna frekvenca je nekje na tretjini. Prehodno območje je precej dolgo. Poleg tega
pa ne filtrira v celoti vseh frekvenc nad lomno frekvenco.

### 18. Primeri filtrov

- [x] Done

- Butterworth,
- Chebyshev,
- Bessel,
- Elliptic
- ...

### 19. Šum v signalih

- [x] Done

Šum je v bistvu vsak signal, ki ga ne želimo. Lahko je posledica okolja, napak v merjenju,
ali pa je posledica samega sistema. Šuma se lahko znebimo s pomočjo filtrov.

Količino šuma v signalu lahko opišemo s pomočjo **SNR** (signal to noise ratio). Ta
nam pove, koliko je signal močnejši od šuma. 

```
SNR = 10 * log10(Es / En)
```

Kjer je Es energija signala, En pa energija šuma.

Primer: če imamo SNR 10dB, to pomeni, da je signal 10x močnejši od šuma, torej, da je šum
10% signala.

SNR zapis s pomočjo apmlitude:

```
SNR = 20 * log10(As / An)
```

### 20. Zakaj si želimo boljši SNR?

- [x] Done

Razlog tiči v tem, da prvo kot prvo nam šum NE koristi. Poleg tega je stiskanje ob odstranitvi
šuma veliko bolj učinkovito. Signal je tudi lažje obdelovati. 

### 21. Kako deluje 2D konvolucija?

- [x] Done

Ideja je popolnoma ista - imamo impulzni odziv 2D filtra (kernel, jedro) in vhodno sliko (signal).
Ta dva nato med sabo množimo kot pri konvoluciji. Tudi tu lahko delamo ali v frekvenčnem ali
časovnem prostoru. Večinoma pa delamo v časovnem.

Primer takega filtra je npr. nizkoprepustni filter, ki ga uporabimo za zmanjšanje šuma. Deluje
tako, da v filter damo samo enice in ta sliko "zamegli" ter tako efektivno odstrani višje
frekvence. Gre za računanje povprečja.

Filtre moramo normalizirati, če želimo, da ne uničimo slike.

### 22. Detekcija robov

- [x] Done

Detekcijo robov lahko izvajamo z izbiro pravih filtrov. V splošnem jih prepoznamo po tem, da je
v njih prisotno odštevanje. V ozadju je ideja, da tam kjer je gradient velik, se bo to tudi
odražalo na filtru in dobili bomo večjo vrednosti. Torej iščemo območja velike spremembe kontrasta.

**Robertsova operatorja**

Omogočata detekcijo diagonalnih robov. Nista najbolj optimalna.

```
C0 = [-1 0]                  C1 = [0 -1]
     [ 0 1]                       [1  0]

Desno diagonalni robovi      Levo diagonalni robovi
```

**Laplaceov operator**

Omogoča detekcijo vseh robov. Načeloma je še vseeno boljše kombinirati prejšnja operatorja.

```
C = [ 0  1  0]
    [ 1 -4  1]
    [ 0  1  0]
    
ta omogoča detekcijo robov v vseh smereh

C = [ 1  1  1]
    [ 1 -8  1]
    [ 1  1  1]
    
    
ta pa tudi
```

**Sobelov operator**

Omogoča detekcijo navpičnih in vodoravnih robov.

```
Cy = [-1 0 1]              Cx = [-1 -2 -1]
     [-2 0 2]                   [ 0  0  0]
     [-1 0 1]                   [ 1  2  1]
     
Navpični robovi            Vodoravni robovi
```

Kombinacija Sobelovih operatorjev je najboljša izbira za detekcijo robov.

Poleg tega kombinacija teh dveh omogoča ugotovitev amplitude in smeri robov.

```
A = sqrt(Cx^2 + Cy^2)
kot = atan(Cy / Cx)
```

### 23. Cannijev detektor robov

- [x] Done

Cannijev detektor robov je najboljši detektor robov. Kombinira razne tehnike zaznave kot so 
Gaussovo sito, Robertsov operator in določanje praga, da zazna robove, tudi če so pretrgani.

### 24. Pojmi v prostoru značilk

- [x] Done

Vsak signal nosi neke informacije in le-te lahko izluščimo. To lahko med drugim storimo
s pomočjo filtrov in segmentacije. Na ta način zberemo kup informacij o signalu, ki jim
rečemo **značilke**. Te značilke tvorijo t.i. **prostor značilk**.

Primer:

_Imamo sliko psa. Iz nje nato lahko izluščimo sledeče značilnice: barva, oblika uljev,
število nog, dolžina repa, ipd._

Postopku izluščevanja značilk rečemo **ekstrakcija značilk**.

Značilke nam lahko služijo za razpoznavo nekih objektov ali pa za **klasifikacijo**.

**Klasifikacija** pomeni razvrščanje objektov v razrede. To lahko naredimo na podlagi
značilk, ki smo jih izluščili.

### 25. Razpoznavalni sistem

- [x] Done

To je sistem, s katerim opravimo **razpoznavanje oblik**. Postopek je sledeč:

1. Pretvorba iz fizikalnega sveta (neskončno dimenzij) v prostor oblik (2D, 3D, ...)
2. Ekstrakcija značilk, da preidemo v prostor značilk (N dimenzionalni prostor)
3. Pravila odločanja za klasifikacijo v razrede (K)

### 26. Določanje praga

- [x] Done

Ko iščemo območje oblike v signalu, moramo poiskati segment slike, kjer je ta objekt prisoten.
Temu postopku pravimo **segmentiranje**. Najpreprostejši pristop je z uporabo pragov. Potlej 
samo gledamo za vsak pixel na sliki, če je njegova vrednost večja od praga. Če je, ga označimo
kot del objekta, če ne, pa ne. Tako dobimo true/false masko, ki nam pove, kje se objekt nahaja.

![Prag](https://davidblog.si/wp-content/uploads/2023/06/Screenshot-2023-06-03-210859.png)

Določanje pragu je lahko kar zahtevna stvar. Najpreprostejši način je, da določimo globalni
prag - torej neko vrednost, ki je enaka za vse piksle na sliki.

Pri določanju pragov si lahko pomagamo s **histogrami**.

### 27. Sivinski histogram

- [x] Done

Sivinski histogram je najlažje določiti tako, da poiščemo minimalno in maksimalno vrednost
na sliki. Nato naredimo histogram, ki ima toliko stolpcev, kot je razlika med minimalno in
maksimalno vrednostjo. Velikost stolpca predstavlja število pikslov, ki imajo to vrednost.
Območja, kjer je koncentracija velika, kažejo na potencialne segmente.

### 28. Izboljšava histograma

- [x] Done

Pri segmentaciji si želimo, da bi bile sivine čim bolj enakomerno porazdeljene, saj lahko tako
bolje določimo prag. To storimo s pomočjo **linearizacije**. S to metodo sivine, ki so bolj na
kupu, razvlečemo, tiste, ki so bolj razpršene, pa stisnemo skupaj. S tem dosežemo, da so sivine
bolj enakomerno porazdeljene.

### 29. Kje je optimalni prag?

- [x] Done

Formule za določitev optimalnega pragu ni. Lahko pa si tu pomagamo z neko hevristiko, kot je
npr. uspešnost klasifikacije. Če sliko bolje klasificiramo pri določenem pragu, potem je ta
prag boljši. To spominja na učenje z vzorci pri nevronskih mrežah.

### 30. Povprečje vs. mediana

- [x] Done

Glavna razlika je v tem, da je mediana dosti bolj odporna na velika odstopanja. Npr. če
imamo vrednosti 1, 2, 3, 1000 v seznamu, potlej bo povprečje 251, mediana pa 2.5. Mediana 
je namreč srednja vrednost, ki jo dobimo, če seznam uredimo po velikosti. V primeru zgoraj je
sredina enaka 2, 3, zatorej je mediana (2 + 3) / 2 = 2.5.

Zato je najbolje, da izračunamo tako mediano kot povprečje, da dobimo občutek o lastnosti
opazovanih podatkov oz. signalov.

### 31. Vrste pragov

- [x] Done

Imamo globalni in lokalni prag. Globalni je enak za celotno sliko, lokalni pa je različen
za vsak piksel slike. Če uporabljamo lokalne pragove, lahko tudi kombiniramo več pragov.

Kar se tiče globalnih pragov, lahko le-te izračunamo s pomočjo mediane (problem je šum),
s pomočjo povprečja (odporen na šum, 20 dB+) ali pa z izračunom optimalnega pragu (odporen na
šum, 10 dB+).

### 32. Lokalni prag

- [x] Done

Prednost lokalnega pragu je, da lahko mejo praga spreminjamo glede na določeno karakteristiko,
kot je npr. prisotnost roba. Če rob v nekem pikslu zaznamo, potlej prag spustimo. To je lahko
dober način za zaznavanje ospredja in ozadja.

Formula:

```
T = Topt(1 - x)

x = 1/3R * (|a - b - c + d| + |a - b + c - d| + |a + b - c - d|)
```

Kjer so a, b, c, d koti v 3x3 operatorju, R pa je število sivinskih nivojev na sliki.

Razlika med lokalnim in globalnim pragom z očesom morda ni vidna, vendar pa kot omenjeno
prek lahko uspešnost segmentacije ocenimo z rezultati klasifikacije.

### 33. Klasifikacija

- [x] Done

Tu bi samo še enkrat poudaril najpomembnejše pojme:

- vektor značilnic - vektor, ki opisuje neko obliko - dimenzija **R**
- linearna klasifikacija določi meje med razredi
- poznamo tudi nelinearna odločitvena pravila (polinomi ipd.)
- število razredov označimo s K
- Število vadbenih vzorcev ali **pralikov** pa označimo z **M**

### 34. Ocenjevanje uspešnosti razpoznavalnih algoritmov

- [x] Done

Pri tem uporabljamo naslednje metrike:

- **TP** - true positive - pravilno pozitivni
- **TN** - true negative - pravilno negativni
- **FP** - false positive - napačno pozitivni
- **FN** - false negative - napačno negativni

Primer:

Imamo 30 jabolk in 30 hrušk. Zaznali smo 35 jabolk in 25 hrušk. Kaj je TP, TN, FP in FN?

Z vidika jabolk:

- TP: 30
- TN: 25
- FP: 5
- FN: 0

Rezultat: 30/35 = 0.86

Nato imamo še pojma:

- **TPF** - true positive fraction - senzitivnost
    - TPF = TP / (TP + FN)
- **TNF** - true negative fraction - specifičnost
    - TNF = TN / (TN + FP)
- **FNF** - false negative fraction
    - FNF = 1 - TPF
- **FPF** - false positive fraction
    - FPF = 1 - TNF

Za primer zgoraj so rezultati:

- TPF: 1
- TNR: 0.83
- FNF: 0
- FPF: 0.17

##### Natančnost modela

V praksi tako iščemo kompromis med TPF in TNF. To lahko naredimo z uporabo ROC krivulje.
ROC krivulja je krivulja, ki prikazuje odvisnost TPF od FPF (senzitivnosti od
specifičnosti). Najboljša je ponavadi tista,
ki se čim bolj približa enemu izmed robov na osi y = x. Najslabša krivulja pa je tista,
ki gre skozi os y = -x.** Čim bližje smo tej diagonali, tem slabši je naš model za
predikcije.

Optimalni prag tako iščemo na ta način, da opazujemo spreminjan ROC krivulje in iščemo
AUC (area under curve), ki je čim večji. AUC je v bistvu ploščina pod krivuljo. Če je
AUC = 1, potem je naš model popolnoma natančen. Obratno, če je AUC 0, je model tudi
popolnoma natančen, ampak rabimo pa obrniti rezultate.

ROC - receiver operating characteristic. ROC krivulja ponavadi izgleda nekako takole:

![ROC](https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/ROC_space-2.png/800px-ROC_space-2.png)

[//]: # (Vir: Wikipedia)

Več o tem:

- [ROC krivulja](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
- [AUC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)
- [Neka spletna stran](http://www.anaesthetist.com/mnm/stats/roc/Findex.htm)

ROC krivuljo lahko vidimo tudi na slednji sliki, kjer enako iščemo kompromis med
senzitivnostjo in specifičnostjo:

![ROC](https://davidblog.si/wp-content/uploads/2023/06/Screenshot-2023-06-04-084800.png)
