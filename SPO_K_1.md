# Kolokvij 1

## Pred vprašanji

Simbol '*' za številko vprašanja namiguje na to, da vprašanje načeloma ni del predmeta, ampak koristi za boljše
razumevanje
ostalih vprašanj.

Vprašanja bolj ali manj zajemajo vso snov predavanj.

Priporočam tudi ogled videov in povezav podanih ob vprašanjih, saj ponujajo dobro razlago snovi in dodatno razumevanje.

Kratice:

* OS - operacijski sistem
* HW - strojna oprema
* GP - glavni pomnilnik
* VPJ - višji programski jezik

## Vprašanja

1 Statične vs dinamične knjižnice.

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
Big-endian is an order in which the "big end" (most significant value in the sequence) is stored first, at the lowest storage address. Little-endian is an order in which the "little end" (least significant value in the sequence) is stored first.
```

6 2 komplement

```
* 2 komplement - negativno število predstavimo tako, da ga zamenjamo z njegovim 2 komplementom
```

7 Plavajoča vejica

```
V glavnem imamo mantisto in eksponent
Mantisa nam pove decimalno število, eksponent pa pove, za koliko je potrebno to število pomnožiti z 10 - torej stopnja 10, ki jo potrebujemo za pomnožitev
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

Zato je takšna struktura 24 bytov

```C
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
Poleg tega ima objekt shrajeno samo vsebine - spremenljivke - in samo kazalec na funkcijo. Tokaj, ko imamo več kot en objekt,
smo verjetno že prihranili veliko prostora.
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

Poleg vektorskega formata rabimo še rasterizator, ki pa nam omogoča prikaz vektorske slike na zaslonu. Ampak prednost
je pa ravno v tem, da ohranimo kakovost slike s tem vektorskim formatom.
```

17 Vloga gonilnikov

```
Gonilniki skrbijo za rasterizacijo, da se nam programerjem s tem ni treba ukvarjati. Mi samo ustvarimo vektorsko ali 
rastesko sliko, gonilniki pa poskrbijo za rasterizacijo, antialiasing in druge stvari.
```

18 TrueType

```
TrueType je vektorski format, ki se uporablja za pisave (fonte) brez izgube kakovosti pri skaliranju.
S tem omogoča prikaz znakov (črk) v maksimalni kvaliteti pri poljubni resoluciji.
```

19 Rasterizacija

```
Problem rasterizacije je, da je treba vektorsko sliko pretvoriti v rastersko sliko. Tu pogosto pride do tega problema, da slika ne izgleda dobro.
Rešitev, ki jo pogosto uporabimo, je, da programu za rasterizacijo damo namig, kako simbol izrisati. Lahko bi npr. rekli,
da naj se potrudi znake narediti simetrične. Za ta namen pa se uporablja tudi tehnika ClearType (anti-aliasing + smoothing).
Slika s pomočjo ClearType izgleda bolj gladko in čisto - ni tistih kvadratnih robov.

To je v bistvu sistemska podpora obliki, kar pomeni, da mi ne rabimo skrbeti za izgled znakov, ampak le za vsebino, kateri
font, barvo uporabimo ipd.
```

20 PostScript

```
PostScript je (programski) jezik, ki pove, kako se nekaj nariše: izris grafičnih elementov (uporabljeno pri tiskanju) v dokumentih.
Doda podporo fontom, kompresiji slik, tekstu ipd. - je kot nek programski jezik za tisk.
Podprt je (bil) v raznih aplikacijah in tiskalnikih.
```

21 PDF

```
PDF je tako neka nadgradna verzija PostScripta. Je bolj optimiziran za digitalno/elektronsko distribucijo.
Omogoča platformno neodvisno prikazovanje dokumentov.
Ravno tako podpira razne grafične elemente: tekst, slike, ostale grafične objekte, povezave, oblike, fonte itd.
Še bolj v smeri programskega jezika z dodanimi objekti.

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
problem polnjenja nahrbtnika, optimizacija prostora.
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
   Povezovanje (povezovalnik) - tu povezujemo zato, da nebi že na izvornem nivoju imeli napak - tako lahko vsak modul posebej preverimo za napake.
3. Izvedljivi modul (.exe)
   Nalaganje (nalagalnik)
4. Naložen program (v glavnem pomnilniku)
   Izvajanje
   
Lokalne spremenljivke gredo ponavadi v registre, globalne pa v glavni pomnilnik.
```

25 Zakaj zbirnik?

```
Morebiti hitrost, direkten dostop do strojne opreme (registri, gonilniki), optimizacija, ...
Sicer ni razloga, ker so današnji prevajalniki zelo močni: koda je hitra, zanesljiva, krajša, prenosljiva.
```

26.1 Simboli, funkcije

```
V debug načinu si želimo program videti z vidika višjega programskega jezika, čeprav se ta izvaja po korakih na nizkem nivoju - na nivoju strojne kode.
Zato tudi 1 korak v višjem programskem jeziku predstavlja več korakov v  nižjem strojnem jeziku. To prevajanje deluje kot
neko kopiranje assembly kode za specifične ukaze višjega strojnega jezika.

Zato rabimo simbole, ki nam povejo, kje se kateri ukaz začne in konča. Tudi za funkcije rabimo simbole, ki nam povejo
naslove funkcij. Simboli so v bistvu tako bolj prijazna imena za naslove, ki jih lahko dodamo ukazom in funkcijam -
na strojnem nivoju so funkcije tako ali tako nič drugega kot nek odsek kode na nekem naslovu in klic fukcij je samo 
skok na ta naslov in shranitev trenutnega stanja.
```

26.2 Klicanje funkcij

```
Ko kličemo funkcijo A, se lokalne spremenljivke funkcije A shranijo v registre. Ko nato kličemo funkcijo B, se lokalne
spremenljivke funkcije A najprej shranijo na sklad, doda se še naslov za vrnitev in kazalec na prejšnji okvir, in lokalne
spremenljivke funkcije B gredo v registre. Ker je sklad struktura tipa LIFO, funkcija A konča z izvajanjem zadnja.
```

26.3 Kratka zgodovina procesorjev

```
Procesorji na začetku niso imeli DMA krmilnika in za ta namen registre za shranjevanje naslovov DI, SI, SP, BP, PC, ... To je bilo počasno.
```

27 Slika pomnilnika

```
Pomnilnik programa v glavnem sestoji iz štirih segmentov (od višjega proti nižjemu naslovu):
* Sklad - dinamičen segment za shranjevanje lokalnih podatkov - pri menjavi konteksta se tja shranijo lokalne spremenljivke (registri) - širi se navzdol
* Kopica - dinamičen segment za dinamično alokacijo pomnilnika (malloc, new, free, delete)
* Podatkovni segment - statični segment (fiksne velikosti) za shranjevanje globalnih spremenljivk - statično alocirane spremenljivke
* Tekst segment (koda) - statični segment (fiksne velikosti) za shranjevanje kode
```

28 Efektivni naslov

```
Efektivni naslov je naslov, ki ga uporablja procesor za dostop do nekega dela pomnilnika. Najdemo ga v zbirnih ukazih, ko
dostopamo do GP in ga je potrebno pred uporabu izračunati. Formula se glasi: 
Bazni_register + Faktor*Indeksni_register + odmik
Le-ta se nato združi z segmentnim registrom, da dobimo fizični naslov pri recimo realnem načinu delovanja.
Efektivni naslov je namreč relativen glede na začetek programa (ta se začne z naslovom nič).
Za ta namen imamo tudi AGU enoto.
```

29 Kaj je sklad?

```
Gre za dinamičen del (segment) pomnilnika, ki služi kot prostor za začasno shranjevanje lokalnih spremenljivk (registrov).
To nam pride prav pri npr. zamenjavi konteksta. Za ta namen imamo tudi kazalec na začetek (vrh) sklada (RSP) in kazalec na
okvir sklada (RBP) - ta predstavlja začetek trenutnega dela sklada, ki ga uporabljamo.
Z vsako zamenjavo konteksta tako nastane nov okvir in se doda na sklad (push, ovijanje sklada) oz. vzame iz sklada (pop, 
odvijanje sklada), ko se vračamo iz funkcije.

Na vrhu sklada (za RSP) imamo še 128 bajtov rdeče cone (Linux/MacOS, x64). Gre za zavarovan del pomnilnika pred RSP, do katerega
naj signali in interrupt handlerji ne bi dostopali. Omogoča shranjevanje podatkov na stack brez spreminjanja RSP - omogoča
funkcijam začasno shranjevanje podatkov.

Vrstni red nalaganja spremenljivk na stack je sledeč:
* RBP (v začetni funkciji ga ne shranimo)
* argumenti funkcije
* naslov za vrnitev
* lokalne spremenljivke

Torej:

high-address

---------------  1
| args for 2  |
| ret         |
| locals      |
---------------  2
| RBP         |
| args for 3  |
| ret         |
| locals      |
---------------  3
...
red zone

low-address

```

30 Sklad vsebina – 32 vs 64 bit

```
https://eli.thegreenplace.net/2011/02/04/where-the-top-of-the-stack-is-on-x86/
TL;DR: Pri obeh najdemo lokalne spremenljivke in naslov za vračanje ob klicu funkcije. Po klicu funkcije pa še kazalec 
       na prejšnji okvir sklada (RBP oz. EBP). Tudi vrednosti funkcije se vračajo preko sklada.
       Pri 64-bit pa pogosto najdemo še prej omenjeno rdečo cono (128 bajtov).
```

31 Zakaj lokalne spremenljivke na skladu, ko pa bi bile lahko v registrih?

```
Razlog tiči v tem, da je registrov pogosto premalo (recimo imaš samo 8 splošno namenskih registrov).
Nato izbiraš med pomnilnikom, ki ti ga dodeli OS ali skladom, ki ga že imaš. Sklad je seveda hitrejši in zato so
lokalne spremenljivke shranjene tam, četudi morda nova funkcija znotraj trenutne ne bo klicana.
Mogoče izgubimo malce na hitrosti (zanemarljivo malo ponavadi), a če nas to skrbi, je na voljo zbirnik.
```

32 Kaj so okvirji na skladu

```
Okvir na skladu je del sklada, ki služijo za shranjevanje lokalnih spremenljivk (registrov) trenutne funkcije.
V njem ponavadi najdemo še kazalec na prejšnji okvir sklada (RBP oz. EBP) in naslov za vračanje ob klicu funkcije.
```

33 Kaj pa kopica?

```
Kot omenjeno že prej, gre za dinamičen segment pomnilnika, ki služi za dinamično alokacijo pomnilnika (malloc, new, free, delete).
```

34 Ostranjevanje (paging)

```
Ostranjevanje (paging) je razdelitev glavnega pomnilnika na enako velike enote (strani) - ponavadi velikosti 4kB (12-bit).
Tako namesto da naslvljamo direktne lokacije v pomnilniku, naslovimo stran in povemo še odmik znotraj strani.
Ostranjevanje prepreči zunanjo razdrobljenost, omili notranjo razdrobljenost, poenostavi delo OS in omogoča virtualni
pomnilnik - če zmanjka prostora v GP, lahko strani "odložimo" na disk.
OSu tudi omogoča lažjo zaščito pomnilnika in manj režije.

2⁵² strani nam je na voljo.
Poleg tega uvedemo **večstopenjsko tabelo** strani, kjer shranjujemo informacije o straneh - kje se nahajajo, ali so 
veljavne (v glavnem pomnilniku) in nekatere druge zastavice. Večstopenjsko pa zato, ker vseh strani v eno samo
tabelo nebi mogli shraniti (premajhen pomnilnik).

Rabimo uvesti preslikavo virtualnih naslovov v fizične (ker strani niso nujno v pomnilniku, jih celo lahko celo več, kot
pa je velikost pomnilnika in ni nujno da so na lokaciji v pomnilniku, ki je enaka fizični lokaciji strani) - uvedemo
preslikovalne tabele.
```

35 Little magic box - Intel allocator - preimenovanje registrov

```
Ideja je, da imamo za vsak logični register več fizičnih registrov v ozadju. To omogoča izvajanje več ukazov hkrati brez 
premikanja spremenljivk v pomnilnik. Imamo namreč več ALU enot in tako lahko npr. izračunamo več stvari hkrati 
(out of order execution), če so deli kode med sabo neodvisni.
```

36 AGU

```
AGU (address generating unit) je enota v procesorju, ki služi za izračun efektivnega naslova. S tem pohtri računanje
naslovov za dostop do pomnilnika in zmanjša število ciklov, ki bi jih sicer procesor porabil za ta izračun.
```

37 ALU

```
Aritmetično logična enota - služi za izvajanje aritmetičnih in logičnih operacij (+, -, *, /, &, |, ^, ~, <<, >>, ...)
```

38 FPU

```
Floating point unit - služi za izvajanje operacij z realnimi števili (float, double).
```

39 MMX in SSE

```
MultiMedia eXtensions - služi za izvajanje operacij z 64-bitnimi celoštevilskimi števili ali grupami manjših števil.
Nekako ostanek iz preteklosti.

Streaming SIMD Extensions - služi za izvajanje operacij z 128-bitnimi celoštevilskimi števili ali grupami manjših števil.
Uvede 8 novih XMM registrov in več ukazov za računanje z njimi. So širine 128 bitov in omogočajo računanje z več
števili hkrati (2x64, 4x32...). Njihov namen je pohitritev takšnih računskih operacij.
```

40 Cache - predpomnilnik

```
Cache je majhen ampak zelo hiter pomnilnik, ki ga najdemo v procesorju. Njegov namen je pohitritev dostopa do podatkov
na ta način, da se najpogosteje uporabljeni podatki iz GP shranijo v cache.
```

41 Out of order execution

```
Procesor kodo razbije na več delov in določene dele kode izvede paralelno, če so med sabo neodvisni.
Na koncu seveda poskrbi za vzpostavitev originalenga vrstnega reda kode.
Primer je računanje dveh neodvisnih spremenljivk.
```

42 Cevovodi in branch prediction (predikcija vejitev)

```
Cevovodi omogočajo nek nivo paralelizacije s tem, da izvajajo več ukazov hkrat s tega vidika, da ko je en ukaz
pridobljen in gre v dekodiranje, da se začne pridobivati že naslednji ukaz.
Cevovod sestoji iz več faz/nivojev: fetch, decode, execute, writeback.
Potlej ko je specifičen ukaz v eni izmed faz, gre naslednji ukaz v prejšnjo fazo.

Fetch - pridobivanje ukazov iz pomnilnika
Decode - dekodiranje ukaza
Execute - izvajanje ukaza
Writeback - zapis rezultata v pomnilnik

Tu pa pride na vrsto predikcija vejitev. Predikcija vejitev je predvidevanje, katera pot bo izbrana pri veji (if, while, for...).
Če pot uganemo, super, jo upoštevamo, sicer je treba celoten cevovod zavreči in začeti znova.
Imamo več načinov predikcije vejitev, ki pa so danes že zelo učinkoviti (Intel kar 97%).

Primeri predikcije vejitev:
- Statistična predikcija,
- Predikcija na podlagi zgodovine...
```

43 Zakasnjene vejitve

```
Ideja tu je, da prevajalnik išče kodo neodvisno od vejitve in jo izvede šele po vejitvi.
Izvede jo šele za vejitvijo - to pride prav, da v primeru da se za vejitev zmoti, ne zavržemo od vejitve 
neodvisne kode v cevovodu. Na ta način vejitev lahko izvaja že, ko se v cevovodu izvaja neodvisna koda.
To pohitri izvajanje kode, saj je manj čakanja na vejitve.

Zakasnitve so omejene z dolžino cevovoda.
```

44 Matična plošča

```
Matična plošča je osnova računalnika. Vsebuje procesor, pomnilnik, različne povezave, napajanje, ...

The southbridge typically implements the slower capabilities of the motherboard in a northbridge/southbridge chipset computer architecture.

The northbridge is a computer chip found on motherboards. It connects the CPU to the memory, peripheral buses, and other components.

Potrebna je tudi sinhronizacija med različnimi komponentami.
```

[South-bridge](https://en.wikipedia.org/wiki/Southbridge_(computing))

[North-bridge](https://en.wikipedia.org/wiki/Northbridge_(computing))

45 Imena registrov

```
EAX - general purpose register (32-bit)
RAX - general purpose register (64-bit)
AX - general purpose register (16-bit)
AH - general purpose register (8-bit)

RSI - source index (64-bit) - index za branje iz pomnilnika
RDI - destination index (64-bit) - index za pisanje v pomnilnik

RIP - instruction pointer (64-bit) - kazalec na naslov naslednjega ukaza (call, jmp, ret, ...) - eden za vsako nit

Lokacijski števec - iz kje v datoteki beremo - naredi se eden za vsako odprto datoteko

EFALGS - flags register (32-bit) - registri za shranjevanje stanja procesorja (npr. overflow, carry, zero, parity ...)

FPU/MMX registri (80-bit) - FPU in MMX
YMM registri (256-bit) - SSE2
XMM registri (128-bit) - SSE

V legacy 32-bit načinu imamo 8 YMM/XMM registrov, v 64-bit načinu pa 16.
```

46 Računalniške operacije in tipi podatkov

```
Operacije:
- aritmetične (+, -, *, /, %)
- logične (&, |, ^, ~)
- bitne (<<, >>)

Tipi podatkov:
- celoštevilski (int, long, ...)
- realni (float, double, ...)
- znakovni (char, string, ...)
- logični (bool)
- pointerji (int*, ...)
- strukture (struct, class ...)
```

47 Koliko biten je ta ukaz?

```asm
mov eax, 0x12345678  ; 32-bit
mov rax, 0x12345678  ; 64-bit
```

```
V glavnem bodi pozoren na tipe registrov in na podatkovne tipe (BYTE [8], WORD [16], DWORD [32], QWORD [64]...).
```

48.1 Kontekstni preklop in preimenovanje registrov

```
Pri zamenjavi/preklopu konteksta je potrebno shraniti trenutno stanje registrov. To je mogoče pohitriti z uporabo
preimenovanja registrov. Za vsak logičen/navidezen register imamo v ozadju več fizičnih registrov. In procesor poskrbi
za preslikavo med njimi. Tako ob preklopu konteksta samo zamenjamo skupino registrov, ki jo uporabljamo.
To pride prav tudi pri nitenju, kjer ima vsaka nit svoje lokalne spremenljivke (registere).
```

48.2 Programski števec

```
Vsaka nit ima svoj programski števec. Vsak proces oz. nit ima svojo banko registrov (preimenovanje registrov).
Tu pa pride tudi do manjše razlike med nitmi in procesi: niti si delijo pomnilniški prostor, procesi pa ne.

Vsak dostop do sistemskih virov zahteva dovoljenje od OS. Med čakanjem je nit oz. program v kernel načinu, in vmes
lahko drugi procesi izvajajo svoje ukaze. Spet, to se da pohitriti z uporabo preimenovanja registrov.
``` 

49 Zakaj te zamenjave sploh delamo?

```
Zamenjave konteksta izvajajmo, ker želimo, da vmes ko en proces v kernel modu čaka na neke sistemske vire - recimo določene
podatke iz pomnilnika, da se lahko vmes izvaja nek drug proces - samo zamenjamo kontekst, kar pa je z uporabo preslikave
rehistrov storjeno zelo hitro. Point: učinkovitost. Poleg tega je to potrebno za navidezno realno-časovno delovanje OS.
```

50 Kam pa z lokalnimi podatki pri klicu funkcije?

```
Lokalne spremenljivke funkcije so shranjene na stacku. Ob klicu nove funkcije so tako na stacku shranjene
lokalne spremenljivke in pa naslov za vrnitev (in pa ponavadi na začetku še kazalec na prejšnji okvir).
```

50.5 Načini delovanja programov glede na privilegije

```
- realni način - ostaja iz obdobja 16-bitnih procesorjev
- virtualni način - 32-bitni procesorji - emulira realni način
- protected način - 32-bitni procesorji
- long mode - 64-bitni procesorji
   - 64-bitni način - 64-bitni procesorji
   - compatibility mode - 64-bitni procesorji - podpora za 32/16-bitne programe
   
Število SSE registrov je v 32-bit 8, v 64-bit 16.
```

51 Delitev naslovitvenega prostora OS in uporabnika

```
OS ima svoj naslovitveni prostor, ki je ločen od uporabniškega. To zagotavlja nemotenoo in varno delovanje OS, ker 
programom preprečimo dostop do pomnilnika OS, da le-te nebi česa koruptirali.

Ta delitev je s trenutno 48-bitno implementacijo (virtualni prostor je sicer velik 64-bitov, ampak fizično lahko 
naslovimo samo naslove do 48-bitov pri translaciji naslovov) narejena tako, da je prvih 48 bitov pri naslavljanju
za uporabnika, zadnjih 16 bitov pa za kernel. Dobimo uporabniški pomnilniški prostor in pomnilniški prostor jedra.
Na voljo nam je 256 TiB pomnilnika za uporabnika in 64 KiB za jedro.
```

[Virtual address space](https://en.wikipedia.org/wiki/X86-64#Virtual_address_space_details)

```bash
dmesg | grep "Memory"
```

```console
[    0.112886] Memory: 32467112K/33474256K available (16393K kernel code, 4379K rwdata, 10820K rodata, 3240K init, 6556K bss, 1006884K reserved, 0K cma-reserved)
```

52 Glavni pomnilnik – naslavljanje po zlogih

```
Zlog - 1 byte
Beseda - 2 byte
Dvojna beseda - 4 byte
Četverna beseda - 8 byte
```

53 Nekaj o zbirniku

```
Format zbirnika:
Oznaka: OpCode Destinacija, Izvor

OpCode - ukaz, ki ga želimo izvesti
Destinacija - kje želimo shraniti rezultat
Izvor - od kod želimo vzeti podatke

Oznaka ti v bistvu pove naslov ukaza - tako tudi definiramo funkcije - dodamo oznako nekemu delu kode.
V ozadju v bistvu klic funkcije ni nič drugega kot le shranitev trenutnega stanja in skok na nek naslov.

Navodila lahko zbirniku podamo preko globalnih spremenljivk. Te po prevedbi programa v bistvu postanejo naslovi, 
prevajalnik pa te naslove vstavi, kjer smo se na to globalno spremenljivko sklicevali.

Pomnilniški prostor lahko rezerviramo v bss sekciji s pomočjo resb, resw, resd, resq ukazov.
Konstante - torej vrednosti, ki se hard-codajo v ukaz/kodo - zapišemo npr. kot 
KONSTANTA equ 12
```

54 Gajbe in palete – sekcije in segmenti

```
Ideja je, da se različni tipi podatkov zapišejo/shranijo v različne sekcije.
Neicializirani podatki, inicializirani podatki, konstante, funkcije - vsake izmed teh gredo v svojo sekcijo.
Le-te pa se nato združijo v segmente. Recimo konstante in koda gredo v isti segment (.text).
Neicializirani podatki in inicializirani podatki pa gredo v različne segmente (.bss in .data).
Te segmenti tako tvorijo program. In ko program želimo zagnati, potrebne segmente naložimo v pomnilnik.
```

55 Načini naslavljanja

```
- takojšnje naslavljanje (immediate addressing) - v ukazu je vrednost, ki se uporabi (konstanta)
- registrsko naslavljanje (register addressing) - v ukazu je register, ki se uporabi
- neposredno naslavljanje (direct addressing) - v ukazu je naslov, ki se uporabi:

Pri neposrednem naslavljanju lahko naslov izračunamo na več načinov - za to računanje poskrbi AGU enota v procesorju.
Formula za izračun naslova: 
naslov = base + index * scale + displacement

Mimogrede: cilj in izvor ne moreta biti hkrati pomnilniška naslova.
```

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-18-00-06.png" alt="Screenshot from 2023-03-30 18-00-06" width="800"/>

56 Windows proti Linuxu

```
```

57 Kdaj katero naslavljanje uporabimo?

```
Odmik (neposredno naslavljanje): če uporabimo izključno odmik, potlej je ta odmik od naslova 0. To pogosto uporabimo v 
kombinaciji z globalnimi spremenljivkami in neinicializiranimi spremenljivkami.
Primer:
mov ax, [0x1000]

Bazno (registersko posredno naslavljanje): to je zelo uporabno za recimo dostop do podatkov v strukturi, poljih, ker lahko
vrednost poljubnega baznega registra spreminjamo - recimo se premikamo skozi neko polje.
Primer:
mov ax, [ebx]

Baza + odmik (relativno registrsko naslavljanje): uporabno za dostop elementov objekta in polja. Baza predstavlja
začetek objekta ali polja, odmik pa predstavlja odmik.
Primer:
mov ax, [ebx + 0x1000]

Baza + indeks (bazno-indeksno naslavljanje): to je zelo uporabno za dostop do podatkov v tabelah. Bazni register predstavlja
začetek tabele, indeksni pa predstavlja indeks elementa v tabeli. Indeks lahko nato dinamično spreminjamo.
Uporabno kot neka for zanka čez polje.
Primer:
mov ax, [ebx + ecx]
```

58 Segmentiranje pomnilnika

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-18-16-59.png" alt="Screenshot from 2023-03-30 18-16-59" width="800"/>

```
Uvedemo segmente v pomnilniku, da ločimo programe v pomnilniku. Vsakemu programu damo svoj segment.
Ko želimo dostopati do nekih podatkov v segmentu, najprej dobimo efektivni naslov ZNOTRAJ SEGMENTA. Šele nato
procesor izračuna fizični naslov, ki ga dobi preko efektivnega naslova in segmentnega registra.
Segmenti register v descriptor tabeli pogleda, kje se naš segment nahaja in kako velik je.
Če poskušamo dostopati izven segmenta, dobimo napako! Tako je zagotovljena integriteta in varnost podatkov v pomnilniku.

Skratka uvedemo te virtualne naslove, ki pa jih AGU preračuna v fizične naslove.
```

59 Segmentacija in paging skupaj

```
```

60 Windows vs Linux – naslavljanje, AGU, registri, relokacija**

```
Recimo imamo proces A na nekem mestu. Nato tja dodamo še proces B, ampak za C pa zmanjka prostora.
Imamo dve opciji: relocirati enega izmed programov ali pa procesu C dodelimo lokalno kopijo. Nič od tega ni optimalno.

Unix se teh naslovov loti z uporabo registra + odmik - relativno naslavlanje. To je lahko kar PC.
```

** Ta odgovor je škrbina, če ga želite izboljšati, kontaktirajte avtorja.

61 Prenaslovitvena tabela

```
Prenaslovitvena tabela služi za prenaslovitev klicev funkcij iz knjižnic, ko le-te premaknemo v pomnilnik.
Npr. neko knjižnico x smo najprej imeli naloženo takoj za programom, a se kasneje premakne dugam zaradi določenih razlogov.

Uglavnem nam pove, kjer vse je ob spremembah treba naslove popraviti.
```

Zelo dobra razlaga celotnega procesa prevajanja programa in ustvarjanja relokacijske, simbolne tabele.

[Relocation and Symbol Table](https://stevenschmatz.gitbooks.io/eecs-370/content/Lecture_Notes/lecture_7.html)

62 Prevajanje višjih programskih jezikov

```
Višji programski jeziki se prevedejo v več assembly ukazov. Debug si mora tudi shraniti, kateri assemblz ukazi pripadajo
kateremu višjemu programskemu jeziku. Tako se med debugganjem v bistvu premikamo skozi več ukazov hkrati.
Poleg tega si debugger oz. program shrani tabelo simbolov - to je tabela imen vseh funkcij, spremenljivk itd.
```

63 Načini naslavljanja

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-18-36-52.png" alt="Screenshot from 2023-03-30 18-36-52" width="800"/>

```
To registri na levi so vsi segmenti.
Žal pa se takšno naslavljanje ne uporablja več, ker ga je industrija zavrgla.

Glavni takeaway je, da smo uvedli virtualne naslove, kar pomeni da smo omejeni na nek lokalni del pomnilnika. To je na
del pomnilnika, ki ga za naš program dodeli OS. Če želimo več pomnilnika, moramo za to prositi OS (sistemski klici).
Ker pa uporabljamo virtuali pomnilnik, je v ozadju potrebno izračunavati fizične naslove - to pa je naloga AGU enote.
```

[What are the FS and GS registers](https://stackoverflow.com/questions/10810203/what-is-the-fs-gs-register-intended-for)

64 Simbolna in ukazna tabela

```
Simbolna tabela

Vsebuje imena spremenljivk, funkcij, objektov, razredov, vmesnikov, ... in njihove naslove. Se dinamično gradi med zbiranjem.
Zgradi in uporablja jo compiler in pomaga določiti:
 - preslikavo imen v naslove/vrednosti,
 - scope (obseg),
 - ali je spremenljivka že definirana,
 - poda informacije o spremenljivki/objektu,
 - type checking,
 - tip spremenljivke,
 - konstante, keterim pa so določene vrednosti, ne pa naslovi...

Načeloma delamo novo tabelo simbolov za vsak scope (obseg). In le-te so lahko organizirane v drevo.
Tabela se polni med zbiranjem dinamično. Lokalne spremenljivke gredo v registre.

Dinamično povezovanje knjižnic:
Ena izmed pomembnih uporab te tabele je dinamično povezovanje knjižnic. Sklice na knjižnice namreč še ne moremo
zamnjati z dejanskimi naslovi, dokler knjižnice nismo naložili. Šele, ko se knjižnica naloži, lahko zamnjamo simbole
v programu z dejanskimi naslovi iz knjižnice. Torej med prevajanjem se na knjižnic sklicujemo, med povezovanjem
pa se sklicevanja zamenjajo z dejanskimi naslovi.

Ker so imena spremenljivk v simbolni tabeli lahko variabline dolžine, uvedemo kazalce na besede in tako prihranimo nekaj prostora.
Temu rečemo tudi dvostopenjska simbolna tabela.
 

Ukazna tabela

Ukazna tabela pa vsebuje ukaze, ki jih najdemo v naši kodi, ter operacijske kode, ki ji pripadajo.
Ta tabela je fiksna. V njej najdemo podatk o mnemoniku (operandu), pripadajoči operacijski kodi, tipu ukaza in številu 
operandov. S pomočjo tega lahko kasneje tvorimo ukaz.

```

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-18-53-19.png" alt="Screenshot from 2023-03-30 18-53-19" width="800"/>

Some Indian guy on YouTube: [Symbol table](https://www.youtube.com/watch?v=oyG_JfrbTCQ)

65 Zakaj se imena simbolov ne začnejo s števili?

```
Glavni razlog je v tem, da če bi števila uporabili za imena simbolov, nebi mogli razlikovati med simboli in vrednostmi.
```

66 Konstrukcija simbolnih tabel

```
Hash-table!
```

[Hash-table - a solution for everything](https://www.youtube.com/watch?v=5bId3N7QZec)*

```
Simbolna tabela se generira v dveh fazah (generiranje tabele + zamenjava):
 - prva faza - analiza kode in zbiranje informacij o simbolih (polnenje tabele),
 - druga faza - sinteza: zamenjava simbolov z njihovimi naslovi/vrednostmi (prevajanje).
 
Za dostop podatkov v simbolni tabeli lahko uporabimo hash-table. Ta omogoča hitro linearno preiskovanje podatkov O(n)
in še hitrejše binarno preiskovanje podatkov O(log2 n). Do vrednosti simbolnih imen zarade delovanja hash tabele
dostopamo kar preko njihovih imen.

Če je v hash tabeli lokacija zasedena, potem samo gremo za eno naprej (naslov povečamo za 1).

1-prehodno polnenje pa ta dva koraka združi v enega.
```

[Symbol table](https://www.youtube.com/watch?v=Dd3DWRpqI40)

<img src="https://davidblog.si/wp-content/uploads/2023/03/Screenshot-from-2023-03-30-19-25-21.png" alt="Screenshot from 2023-03-30 19-25-21" width="800"/>

67 Še nekaj o simbolnih tabelah

```
Pogosti ukazi in operandi se lahko združijo v nove ukaze. Recimo če imamo na voljo 8-bitov za inštrukcije, imamo pa
samo 206 inštrukcij, lahko preostalih 50 inštrukcij zapolnimo z novimi ukazi, ki združujejo stare ukaze.

Naslovi se lahko dodajo šele naknadno, ko je knjižnica vključena.

V simbolni tabeli tudi najdemo vse simbole iz knjižnic.

Te simbolne tabele ostanejo v kodi, če uporabljamo debug. Zato tudi lahko med debugganjem vidimo imena spremenljivk.

Za odstranjevanje teh ukazov imamo sicer ukaz strip - tega si želimo uporabiti, če želimo zavarovati našo kodo - 
intelektualna lastnina. Zato tudi, če imamo to tabelo, lahko skoraj da dobimo originalno izvorno kodo.

Iz ukazne tabele pa s pomočjo tabele dobimo dejanske ukaze.
```

68* Stopnje prevajanja

```
* Leksikalna analiza
* Sintaktična analiza
* Semantična analiza
* Vmesno generiranje kode
* Optimizacija
* Prevajanje v strojno kodo
```

69 Inline funkcije - makro zbirniki

```
Inline funkcije so funkcije, ki so vključene v kodo, kjer so klicane. To pomeni, da se funkcija ne kliče, ampak se 
dejansko "skopira" v kodo, kjer je klicana. Tako lahko pridobimo na hitrosti in hkrati, ko spreminjamo vsebino funkcije
se ta posodobi tudi vsepovsod, kjer je bila klicana.

Boomerang tu je podvajanje simbolov - ko npr. dvakrat zapored kličemo isto funkcijo. V ozadju za to poskrbi prevajalnik - 
zamenja imena simbolov, ko so uporabljeni drugič.
```

[When to use inline functions](https://www.reddit.com/r/learnprogramming/comments/3h5dbm/c_why_not_inline_every_function/)

70 Dodatne vsebine**

```
Imamo dve vrsti ne definirane vrednosti pri floatu (NaN):
tihi - program se nadaljuje
glasni - fatal error
```

** Ta odgovor je škrbina, če ga želite izboljšati, kontaktirajte avtorja.

71 Pogojno zbiranje

```
Pogojno zbiranje je zbiranje kode, ki se izvede le, če je izpolnjen določen pogoj. Po domače povedano gre za if stavke 
v makrojih - če je pogoj izponjen se nek makro izvede sicer ne. To nam pride prav, če recimo pišemo različno kodo
za dve različni platformi, ampak je samo del kode različen, zato imamo v isti izvorni kodi to ločeno z npr.
```

```c++
#ifdef __linux__
    // linux specific code
#else
    // windows specific code
#endif
```

72 Nadzorne sekcije

```
Nadzorne sekcije najdemo v objektnih modulih - gre za programsko kodo. Te nadzorne sekcije so lahko:
 * aboslutne (niso prenosljive - začnejo se na naslovu 0),
 * nepoimenovane (so prenosljive in jih tvori compiler - glavni program v VPJ),
 * poiemenovane (so prenosljive in jih tvori programer - podprogrami v VPJ).
 
Če v nekem ukazu JMP uporabimo direkten naslov, je ta sekcija abosultna - neprenosljiva.
Če uporabimo register z odmikom, postane prenosljiva - smo znotraj sekcije.
Če pa uporabimo programski števec in odmik pa postane celo prenaslovljiva, pozicijsko neodvisna sekcija.
```

73 Prenaslovitvena tabela

```
The relocation table is used by the linker/loader to adjust the addresses in the object code so that they point to the 
correct memory locations at runtime. When the object code is compiled, it contains references to various symbols, such 
as variables, functions, and other code sections, which are located at different addresses in memory.

The relocation table contains information about the symbols that need to be relocated and their corresponding addresses 
in the object code. When the linker/loader combines multiple object files into an executable program, it uses the 
relocation table to update the addresses of these symbols to their correct values in the final program.

In the context of object modules with control sections, the relocation table contains information about the symbols used
in the control sections and their corresponding addresses in memory. This allows the linker/loader to correctly 
relocate the control sections to their proper locations in memory when the program is loaded and executed.

So, in summary, the relocation table is a crucial component in the process of creating an executable program from object
files. It allows the linker/loader to resolve references to symbols and adjust the addresses in the object code so that
they point to the correct memory locations at runtime.
```
