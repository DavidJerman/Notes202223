# Kolokvij 1

## Vprašanja

1 Statične vs. dinamične knjižnice.

| Statične                                                                                                                  | Dinamične                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - Vse obdelave in podatki so lokalni, na istem mestu - program/sistem je zato večji, težje ga je vzdrževati               | + Obdelave in podatki so lahko porazdeljeni (po omrežju) - lažje vzdrževanje, možnost deljenja knjižnic (Linux ima to zelo dobro)                            |
| - Omejena prenosljivost, ker je potrebno program prilagoditi za ciljno platformo - treba ga je v celoti ponovno prevajati | + Sistemska neodvisnost, ker so knjižnice ločene od programa - prilagodimo samo knjižnico (to lahko prepustim tudi nekemu zunanjemu razvijalcu te knjižnice) |
|                                                                                                                           | + Java je npr. še korak naprej - virtualizacija, kjer namesto programa prilagajamo samo virtualno izvajalno okolje                                           |
| + Optimalna hitrost, ker nimamo povezovanja knjižnic med nalaganjem in zagonom                                            | - Zaradi dodatne režije (povezovanje knjižnic med zagonom/izvajanjem) je program nekaj počasnejši                                                            |
| + Bolj varno, ker imamo manjši, bolj preprost mehanizem za zaščito programa                                               | - Bolj zahtevni sistemi za zaščito, ker lahko npr. nekdo spremeni delovanje knjižnice, medtem ko naš program ostaja isti, mi pa tega ne opazimo              |

2 Naloge OS

```
* Skrbi za platformno neodvisnost sistema - naši programi delujejo na poljubni strojni opremi.
* Skrbi za varnost sistema - ni direktnega dostopa do HW (sistemski klici), preprečuje poseg programa v nedevoljene dele pomnilnika, ...
* Povečanje uporabnosti sistema --> upravljanje z viri (razvščevalniki programov, upravljanje z datotekami, pomnilnikom, ...) - pravično deljenje virov
* Virtualizacija - večje število programov na enem stroju
```

3 Statično ali dinamično – varnost

```
* Statično - manjši, bolj preprost mehanizem za zaščito programa
* Dinamično - bolj zahtevni sistemi za zaščito, ker lahko npr. nekdo spremeni delovanje knjižnice, medtem ko naš program ostaja isti, mi pa tega ne opazimo
```

4 Predstavitev števil

```
0x5A = 0101 1010 = 5*16^1 + 10*16^0 = 90 (decimalno)
```

5 Big Endian vs. Little Endian

```
* Big Endian - prvi byte na prvem naslovu
* Little Endian - prvi byte na zadnjem naslovu
```

6 2 komplement

```
* 2 komplement - negativno število predstavimo tako, da ga zamenjamo z njegovim 2 komplementom
```

7 Plavajoča vejica

```
V glavnem imamo mantisto in eksponent
Mantisa nam pove decimalno število, eksponent pa pove, za koliko je potrebno to število pomnožiti z 2 - torej stopnja 2, ki jo potrebujemo za pomnožitev
```

8 Slabosti in prednosti ASCII

```
- ASCII je 7-bitni kodni sistem, kar pomeni, da lahko predstavi samo 128 znakov

+ ASCII je enostaven za uporabo, ker je vse kar potrebujemo v eni tabeli
+ Je preprost za implementacijo in načeloma podprt na vseh platformah
```

9 Unicode

```
Podpira praktično vse abecede in znake, ki so v uporabi: 1.1 milijona znakov
To implementira z variablino dolžino znaka, ki je lahko od 1 do 4 bajtov.
Kodira se s pomočjo UTF-8, ki pa podpira variablino dolžino in hkrati ohranja ASCII kompatibilnost.
To pomeni, da ohranjami prostorsko učinkovitost ASCII, kjer je to potrebno, a hkrati podpira tudi ostale znake.
Potlej imamo še UTF-16 in UTF-32, ki pa so nekompatibilni z ASCII (2 do 4 bytov, ASCII pa samo 1).
```

10 Zakaj še vedno ASCII?

```
ASCII je še vedno v uporabi, ker je enostaven za implementacijo in je podprt na vseh platformah.
Poleg tega ni garantirano, da bo naš program deloval na vseh platformah, če uporabimo Unicode, saj nekatere
starejše platforme ne podpirajo Unicode, samo ASCII - čeprav načeloma bi UTF-8 moral biti podprt na večini platform.
```

11 Primer UNICODE – število znakov v besedi

```C
int main() {
    char  s[] = "Število znakov v besedi";
    int     i = 0;
    while (s[i] != '\0') i++;
    printf("Število znakov v besedi: %d\n", i);
    printf("Število znakov v besedi strlen: %d\n", strlen(s));
    printf("Število znakov v besedi sizeof: %d\n", sizeof(s));
}
```

Izhod:

```
Število znakov v besedi: 24
Število znakov v besedi strlen: 24
Število znakov v besedi sizeof: 25
```

12 Predstavitev struktur v pomnilniku

```C
struct {
    int a;     // 4 bajti
    char b;    // 1 bajt
    double c;  // 8 bajtov
} x;
```

```
Vprašanje, ki si ga moramo postaviti je, koliko prostora takšna struktura zasede v pomnilniku.
Poglejmo C:
```

```C
int main() {
    struct {
        int a;     // 4 bajti
        char b;    // 1 bajt
        double c;  // 8 bajtov
    } x;
    printf("Velikost strukture: %d\n", sizeof(x));
}
```

Izhod:

```
Velikost strukture: 16
```

```
Velikost strukture je 16 bytov. Hmm, kako to če pa imamo 4 + 1 + 8 = 13 bytov?
Do tega fenomena pride, ker C oz. prevajalnik optimizira hitrost programa in pri tem 
poravna podatke na širino vodila - v tem primeru na 8 bytov, kjer gre 4 byte in 1 byte v prvo vrstico.
To kako se polni struktura je načeloma odvisno od optimizacije, ki jo vklopimo.
Skratka vedno bo šlo za poravnavao. Nikoli neka spremenljivka ne bo "gledala čez rob".
```

```
// Zato je takšna struktura 24 bytov
struct {
char e;    // 1 bajt
int a;     // 4 bajti
char b;    // 1 bajt
double c;  // 8 bajtov
} x;
```

```
| 1 byte | 4 byte | 
| 1 byte |        |
| 8 byte          |
```

13 Posredno naslavljanje

```
Ideja je, da imamo kazalec na kazalec. To nam pride prav, ko imamo neko tabalo kazalcev na funkcije. Ali pa tabelo kazalcev na spremenljivke.
Na ta način, si objekti/razredi lahko delijo funkcije/spremenljivke in ne rabi vsak razred implementirati svoje funkcije.
Tako lahko implementiramo:
* Statične funkcije, ki so deljenje med razredi
* Deodovanje funkcij, kar pomeni, da otrok ne rabi ponovno implemtirati funkcije
* Virtualne metode
* Statična polja (ponovno, deljena med objetki)
* Castanje
* Gonilniki
```

14 Urejanje in oblikovanje

```
Eden izmed glavnih problemov je ločevanje oblikovanja (oblike) od urejevanja (podatkov).
Pri spletnem razvoju je to rešeno z delitvijo na HTML in CSS.
LaTeX to ne ločuje tako učinkovito, ampak podobno imamo delitev na vsebino - torej tekst -
in oblikovanje - v obliki nekih predlog (templatov). Ti določajo obliko oz. izgled dokumenta.
Mi se tako osredotočamo na vsebino, ne pa na oblikovanje.
Word po drugi strani ima to še bolj pomešano.

Glavna ideja je tako, da imamo najprej vhodno besedilo in nato oblikovalnik (kjer določimo font, velikost, barvo ipd.).
Ko to združimo, dobimo izhodno besedilo.

Prednost vsega tega ločevanja je, da lahko vsebino enostavno spremenimo, ne da bi morali spremeniti obliko.
To je lahko pri LaTeXu sicer bolj zahtevno, saj je treba dokumenta znova prevesti, medtem ko se v Word spremembe prikažejo takoj.
```

15 Interaktivno vs statično oblikovanje/urejanje

```
+ Glavna prednost interaktivnega oblikovanja je, da se spremembe prikažejo takoj.
+ Takoj je tudi vidna oblika oz. izgled dokumenta, kar nam omogoča lažje urejanje oblike.
- Slabost je, da je treba dokument stalno posodabljati, kar pa je računsko zahtevno.
- Poleg tega sta vsebina in oblika pri takšnem oblikovanju pogosto pomešani, kar pomeni, da vsebino
  včasih težko spremenimo brez oblike.
```

```
+ Glavna prednost statičnega oblikovanja je, da je vsebina ločena od oblike. Tako se lahko osredotočimo na samo vsebino
  brez spreminjanja oblike in se oblike lotimo šele na koncu. Pri bolj obsežnih dokumentih je to morda še lažje.
+ Ker ni sprotnega posodabljanje, je oblikovanje/urejanje hitrejše.
- Slabost je, da se spremembe prikažejo šele, ko dokument prevedemo.
```

16 Vektorski format

```
Prednost vektorskega formata je ta, da bolje ohranja informacije. To pomeni, da npr. če povečamo velikost prikaza slike
na zaslonu, bo ta ohranila kakovost (rasterska slika pa le-te nebi). Vektorski format to doseže z uporabo matematičnih
formul, ki opisujejo geometrijo slik. to omogoča spremembo velikosti brez izgube informacij.
```

17 Vloga gonilnikov

```
```

18 TrueType

```
TrueType je vektorski format, ki se uporablja za pisave (fonte) brez izgube kakovosti pri skaliranju.
S tem omogoča prikaz znakov (črk) v maksimalni kvaliteti pri poljubni resoluciji.
```

19 Rasterizacija

```
Problem rasterizacije je, da je treba vektorsko sliko pretvoriti v rastersko sliko. Tu pogosto pride do izgube kakovosti slike.
Rešitev, ki jo pogosto uporabimo, je, da programu za rasterizacijo damo namig, kako simbol izrisati. LAhko bi npr. rekli,
da naj se potrudi znake narediti simetrične. Za to pa se uporablja tudi tehnika ClearType (anti-aliasing + smoothing).
Slika s pomočjo ClearType izgleda bolj gladko in čisto - ni tistih kvadratnih robov.

To je v bistvu sismska podpora obliki, kar pomeni, da mi ne rabimo skrbeti za izgled znakov, ampak le za vsebino.
```

20 PostScript

```
PostScript je jezik, ki pove, kako se nekaj nariše: izris grafičnih elementov (uporabljeno pri tiskanju) v dokumentih.
Doda podporo fontom, kompresiji slik, tekstu ipd. - je kot nek programski jezik za tisk.
Podprt je (bil) v raznih aplikacijah in tiskalnikih.
```

21 PDF

```
PDF je tako neka nadgradna verzija PostScripta. Je bolj optimiziran za digitalno/elektronsko distribucijo.
Omogoča platformno neodvisno prikazovanje dokumentov.
Ravno tako podpira razne grafične elemente: tekst, slike, ostale grafične objekte, povezave, oblike, fonte itd.

Sestoji iz nekaj delov:
* Glava - struktura dokumenta, verzija, podatki o avtorju, ...
* Telo - vsebina dokumenta - objekti (tekst, slike, povezave, ...)
* Tabela reference - seznam vseh objektov v dokumentu za lažji dostop
* Rep - lokacija tabele prečnih reference, konča se z %%EOF
```

22 LaTeX - princip škatel

```
LaTeX je zasnovan tako, da je vsebina ločena od oblike. Je kot nek programski jezik in sestoji iz jezika in tolmača.
Ima nekaj 100 ukazov za grajenje dokumenta.

Posamezni objekti - simboli, besedila, slike, grafi, ... - so v LaTeXu zapisani v obliki škatel.
Škatle gradijo dokument. Le-tem lahko spreminjamo: velikost, vsebino. Lahko pa jih tudi gnezdimo.
Škatle imajo neko določeno višino in širino in ko ustvarimo vse škatle, je naloga LaTeXa, da jih pravilno postavi - 
problem polnjenja nahrbtnika.
```

23 DOCX

```
DOCX dokumenti uporabljajo XML za shranjevanje vsebine, oblike, podatkov itd.
Imamo tudi več markup jezikov za opis različnih gradnikov: besedilo (Word), razpredelnice (Excel), prosojnice (PP), 
matematični izrazi, vektor grafike (GIMP npr.), ...

Te različne tehnologije lahko potlej tudi kombiniramo - npr. matematični izrazi zniotraj word dokumenta.
Vse skupaj pa nazadnje zazipamo v eno datoteko (npr. .docx). Kompresija je potrebna, ker je XML zelo ponavljujoč, lahko bi
rekli, da je precej "balasta" - kompresija pa vse skupaj zmanjša na primerno velikost.

Skratka več datotek za en dokument.
```

24 Življenjski cikel programa

```
Program gre čez nekaj faz:
1. Izvorni program (C, C++, ...)
   Predprocesiranje (import, makro, ...)
   Zbiranje (zbirnik) / prevajanje (prevajalnik)
2. Objektni moduli (.obj - strojna koda)
   Povezovanje (povezovalnik)
3. Izvedljivi modul (.exe)
   Nalaganje (nalagalnik)
4. Naložen program (v glavnem pomnilniku)
   Izvajanje
```

25 Zakaj zbirnik?

```
Morebiti hitrost, direkten dostop do strojne opreme (registri, gonilniki), optimizacija, ...
Sicer ni razloga, ker so današnji prevajalniki zelo močni: koda je hitra, zanesljiva, krajša, prenosljiva.
```

26 Simboli, funkcije

```
```

27 Slika pomnilnika

```
Pomnilnik v glavnem sestoji iz štirih segmentov (od višjega proti nižjemu naslovu), za ketere pa imamo tudi segmentne registre:
* Sklad - dinamičen segment za shranjevanje lokalnih podatkov - pri menjavi konteksta se tja shranijo lokalne spremenljivke (registri)
* Kopica - dinamičen segment za dinamično alokacijo pomnilnika (malloc, new, free, delete)
* Podatkovni segment - statični segment (fiksne velikosti) za shranjevanje globalnih spremenljivk
* Tekst segment (koda) - statični segment (fiksne velikosti) za shranjevanje kode
```

28 Efektivni naslov

```
```
