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

