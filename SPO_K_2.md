# Zapiski za SPO kolokvij 2

# Kazalo

* [Kazalo](#kazalo)
* [Snov](#snov)
* [Vprašanja](#vprašanja)

# Snov

## Sekcije glede na način naslavljanja

Glede na način naslavljanja imamo:

1. Aboslutne sekcije. Te dobimo, če v kodi pri skoku ali vejitvi skočimo direktno na
   nek absoluten naslov.
2. Prenaslovljive sekcije. Tu pri skoku uporabimo register in odmik.
3. Pozicijsko neodvisna. Tu pri skoku uporabimo programski števec. Ideja je, da ne glede
   nato, kje se ukaz za skok nahaja, se vedno premaknemo za nek odmik + EIP. Pri tem
   vemo, da EIP kaže na ukaz za skok. Na ta način je vseeno, kje se ta sekcija nahaja.
   Dobimo jo z ukazom gcc ... -fPIC. Takšna sekcija je tudi prenaslovljiva.

## Prenaslovitvena tabela

Tu pa nastane manjši problem. Relativni odnosi znotraj sekcij se lepo ohranijo, odnosi
med različnimi sekicijami pa se ne. Zato rabimo prenaslovitveno tabelo, ki poskrbi za to,
da se ob spremembi lokacije sekcij v pomnilniku naslovi ažurirajo. Dinamično povezovanje
ni mačji kašelj!

## Globalna simbolična imena

Kadar med sabo povezujemo več knjižnic in podobno pridejo na vrsto import in export tabele.
Import tabela je tabela simbolov, ki vsebuje simbole, katere smo dobili od drugih. Export
pa simbole, katere ponujamo drugim. Te tabele se kot že omenjeno uporabljajo za
nadomestitev simbolov z dejanskimi naslovi ali vrednostmi. Skratka te table vsebujejo
in pa kazalce na mesta, kjer so bili ti simboli uporabljeni.
S pomočjo teh tabel lahko iščemo varnostne lunkje, poleg tega pa otežujejo varovanje
avtorskih pravic.

## Lokacijski števec

...

## Zasnova objektnega modula

Objektni module sestoi iz sledečih delov:

* dolžina tabele globalnih simbolov,
* dolžina vstopne tabele,
* vstopna tabela,
* zunanja tabela,
* dolžina prenaslovitvene tabele,
* prenaslovitvena tabela,
* programska koda.
  Primer:
  ![Zasnova objektnega modula](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-2023-05-13-151020.png)

## ELF format

Sestava ELF formata je slednja:

* ELF glava (magic, class, data, version, OS/ABI, ABI Version, Type, Machine, Version...)
* Tabela z glavo programa [opcijsko]
* Segmenti in znotraj njih sekcije

Primer ELF glave s podatki:

```
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x431850
  Start of program headers:          64 (bytes into file)
  Start of section headers:          860800 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         14
  Size of section headers:           64 (bytes)
  Number of section headers:         34
  Section header string table index: 33
```

## Pomen sekcij v ELF

.text - koda programa
.data - inicializirane globalne spremenljivke
.rodata - read only data
.bss - neinicializicane globalne spremenljivke
.interp - ACSII niz z imenom dinamičnega povezovalnika
.shstrtab - seckija z imeni sekcij
.symtab - simbolna tabela za statično povezovanje
.strtab - tabela nizov znakov

## Čemu služu magično število

Namen magičnega števila je, da identificira tip datoteke - torej da gre za ELF datoteko in
ne kaj drugega. Namreč če vrednosti magičnega števila preko ASCII tabele pretvorimo, dobimo
izpis ELF!

## Primer izvedljivega module (s segmenti)

```
Elf file type is EXEC (Executable file)
Entry point 0x431850
There are 14 program headers, starting at offset 64

Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  PHDR           0x000040 0x0000000000400040 0x0000000000400040 0x000310 0x000310 R   0x8
  INTERP         0x000350 0x0000000000400350 0x0000000000400350 0x00001c 0x00001c R   0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x000000 0x0000000000400000 0x0000000000400000 0x002360 0x002360 R   0x1000
  LOAD           0x003000 0x0000000000403000 0x0000000000403000 0x04d331 0x04d331 R E 0x1000
  LOAD           0x051000 0x0000000000451000 0x0000000000451000 0x07e5f8 0x07e5f8 R   0x1000
  LOAD           0x0cfe00 0x00000000004d0e00 0x00000000004d0e00 0x002208 0x0059a0 RW  0x1000
  DYNAMIC        0x0d0df8 0x00000000004d1df8 0x00000000004d1df8 0x0001e0 0x0001e0 RW  0x8
  NOTE           0x000370 0x0000000000400370 0x0000000000400370 0x000030 0x000030 R   0x8
  NOTE           0x0003a0 0x00000000004003a0 0x00000000004003a0 0x000044 0x000044 R   0x4
  TLS            0x0cfe00 0x00000000004d0e00 0x00000000004d0e00 0x000000 0x000010 R   0x8
  GNU_PROPERTY   0x000370 0x0000000000400370 0x0000000000400370 0x000030 0x000030 R   0x8
  GNU_EH_FRAME   0x0c37d4 0x00000000004c37d4 0x00000000004c37d4 0x001db4 0x001db4 R   0x4
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0x10
  GNU_RELRO      0x0cfe00 0x00000000004d0e00 0x00000000004d0e00 0x001200 0x001200 R   0x1

 Section to Segment mapping:
  Segment Sections...
   00
   01     .interp
   02     .interp .note.gnu.property .note.gnu.build-id .note.ABI-tag .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt
   03     .init .plt .plt.sec .text .fini
   04     .rodata .stapsdt.base .eh_frame_hdr .eh_frame .gcc_except_table
   05     .init_array .fini_array .data.rel.ro .dynamic .got .got.plt .data .bss
   06     .dynamic
   07     .note.gnu.property
   08     .note.gnu.build-id .note.ABI-tag
   09     .tbss
   10     .note.gnu.property
   11     .eh_frame_hdr
   12
   13     .init_array .fini_array .data.rel.ro .dynamic .got
```

### Kam se preslika .text? Kakšne so zastavice?

.text se preslika v tretji segment, torej na naslov 0x003000. Zastavice pa so kot pričakovano
R in E - namreč gre za kodo in le-ta je izvedljiva.

### Kam se preslika .data? Kakšne so zastavice?

.data se preslika v šesti segment, torej na naslov 0x0cfe00. Zastavice pa so kot pričakovano
RW - namreč gre za podatkovni segment, ki je berljiv in zapisljiv.

### Kam se preslika .bss? Kakšne so zastavice?

.bss se preslika v šesti segment, torej na naslov 0x0cfe00. Zastavice pa so kot pričakovano
RW - namreč gre za neicinilarizirane podatke, ki so berljivi in zapisljivi.

## Povezovanje vs. nalaganje

Glavna razlika, ki izda, ali je program pripravljen za povezovanje ali že za nalaganje, je da
pri nalaganju najdemo segmente, pri povezovanju pa seckije.

## Še nekaj o objektnih modulih

Vstopna točka (preamble) se začne v sekciji .init. Treba je tudi doumeti, da v programih najdemo
tako pojem fizičnih kot virtualnih naslovov. Catch je v tem, da ko program še ni naložen v
v pomnilnik, da so naslovi uporabljeni v bistvu virtualni, torej relativni na začetek programa in
ko se program naloži se ti naslovi (odvisno od OS) zamenjajo z pravimi fizičnimi naslovi. Tako
stvari rad dela Windows, Linux pa raje za to uporablja registre in posredno naslavljanje.
Poleg tega program pred vstopom v pomnilnik še nima kopice in stacka. Knjićnice se lahko naložijo
tudi dinamično naknadno.

## VDSO

VDSO je pohitritev na Linuxu, ki deluje tako, da del pomnilnika jedra preslika v pomnilniški
prostor uporabnika. Tako lahko se lahko določeni sistemski klici opravijo brez preklopa v
kernel način.

## PE format - Windows

V bistvu gre za zelo podobnjo zadevo. Samo malce so spremenili stvari od ELF. Primeri takšnih
datotek so .cpl, .exem .dll, ... Izhaja pa iz formata COFF. PE se nato še razširi za .NET z
dodano sekcijo za metapodatke in kodo CRL. .NET koda se zažene v virtualnem stroju. Compila
se delno z JIT compilerjem.
Zgradba tega formata pa je sledeča:

* glava zbirke (MS-DOS)
* opcijska glava
* glavna sekcija
* ostale sekcije
* navodila za prenaslavljanje
* simbolna tabela, export in import tabela
* tabela nizov
  Tudi ta format ravno ne ščiti avtorskih pravic. Ali si pred konkurenco, ali pa produkt
  patentiraj. Edino kar ti je skrito, je simbolna tabela. Format uporablja **relativne virtualne
  naslove**. Vnnaprej se tudi določi izvajalni naslov. Če je ta naslov zaseden, mora nalagalnik
  opraviti prenaslavljanje.

## Sekcije PE formata

![Sekcije PR formata](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-2023-05-13-160347.png)

## Statično povezovanje

Po tem, ko dobimo objektne module, je čas za povezovanje.
Ideja je, da imamo na vhodu več objektnih modulov, ki pa jih moramo povezati v en izvedljiv
modul. Modulu dodelimo pomnilniški prostor, povežemo posamezne objekte simbole, prenaslovimo
vse potrebno in dopolnimo izvedljiv program s sistemskimi klici. Zatem je program pripravljen
za nalaganje.

Ker vse to storimo pred zagonom, ima program zelo dober response time.

Na izhodu pa tudi lahko dobimo različne vrste programov: prenaslovljiv in absolutno izvedljiv
modul ali pa izhodni objektni modul.

Za podrobnosti glej še enkrat prosojnice na strani 35 do 37.

## Programske knjižnice

Tu gre ponavadi za zbirko programskih modulov istega tipa, ki imajo dogovorjen dostop do
posameznih modulov oz. vsebin. Knjižnice so lahko ali statično ali dinamično povezane s
programi. Če so dinamično, ne rabijo biti del programa in se naložijo v pomnilnik ob
nalaganju v program ali ob klicu te knjižnice. Če pa si statične, pa se vsebina celotne
knjižnice doda kar k vsebini modula programa. Če so knjižnice dinamične, potlej so ponavadi
tudi deljene med programi. Zato morajo biti dostopne preko nekega sistemskega direktorija.
Zato tudi rabimo verzioniranje, ki je na Linuxu dobro urejeno, na Windows pa ravno ne.
.NET je to nekako izboljšal z uporabo globalnih repozitorijev knjižnic. Ponavadi imamo več
knjižnic za različne funkcionalnosti, zato da lahko v programu uporabimo samo tiste, ki jih
dejansko rabimo.

Java ima te knjižnice urejene zelo dobro, pa tudi na Linuxu je to kar dobro urejeno, sploh
z vidika verzioniranja. Na Windowsu je to že večji problem. Če si kaj več programiral v C++,
ti je to verjetno že jasno.

### Dinamično povezljive knjižnice

Pri takšnih knjižnicah pogosto tudi najdemo razne ukaze za predprocesor? Poleg tega kot
že omenjeno, se dinamične knjižnice lahko naložijo ali zgodaj ali pozno. Torej takoj ob
nalaganju programa ali šele, ko so klicane oz. rabljene. V win se lahko na funkcije
zglasuješ kar preko indeksov. Hash-vrednosti?

Dinamično povezovanje omogoča večjo prilagodljivost. Recimo imamo aplikacijo strojnega učenja,
ki backend naloži šele naknadno. Npr., da zazna, da je na našem računalniku prisotna grafična
kartica. Namesto basckenda za CPU lahko nato naknadno naloži backend za GPU.

Kar pa se tiče verzioniranja na Linuxu:
deljene knjižnice (shared library)
• naložijo se ob prvem klicu, nato dostopni za vse programe
• fizično in logično ime (knjižnica “primer”, različica 3.1):
• /usr/lib/libprimer.so.3.1 – fizično ime
• /usr/lib/libprimer.so.3 – logično ime (“so”-ime; “shared object”)
• /usr/lib/libprimer.so – ime za povezovanje

Za primere glej PP stran 6, 7...

## Dinamične knjižnjice na Linux-u

Za delo z dinamičnimi knjižnicami na Linuxu imamo knjižnico dlfcn.h. Ta poskrbi za dinamično
nalaganje knjižnice v programu. Za ta namen obstaja funkcija dlopen(), dlclose(), dlsym()...
Te knjižnice se na Linuxu končajo s .so.

## Dinamične knjižnjice na Windows-u

Zgodba tu je podobna v smislu deljenja knjižnic. Tudi povezovanje je lahko tako implicitno
kot eksplicitno. Po povezovanju dobimo import tabelo. V času izvajanja se ta tabela polni z
naslovi te DLL knjižnice. Vsako funkcijo, ki jo DLL izvaža lahko identificiramo po zaporedni
številki (numeric ordinal) ali pa po imenu. Zaporedna številka predstavlja vstop kazalca na
funkcijo v DLL-ovi vstopni tabeli (Export Address Table – EAT). Vstopne tabele EAT imajo
vstope urejene po abecednem vrstnem redu imen funkcij in omogočajo binarno iskanje po
imenu funkcij.

Primer dll knjižnice (implicitno):

```c
#include <windows.h>
#include <stdio.h>

extern  "C" __declspec(dllimport) double AddNumbers(double a, double b);

int main(int argc, char *argv[]) {
   double result = AddNumbers(1, 2);
   printf("The result was: %f\n", result);
   return 0;
}
```

## Nalagalnik

Gre za izvedljiv program v pomnilniku, katerega namen je nalaganje programov, da so ti
pripravljeni za izvajanje. **Inicializira** izvajanje programa tako da dodeli pomnilniški
prostor programu in prenaslovi izvedljiv modul (torej pripredi naslove iz virtualnih na
fizične po potrebi, ter priredi naslove, če ti kažejo na druge sekcije). Tak program je nato
naložen v glavni pomnilnik in je pripravljen za izvajanje.

### Vrste nalagalnikov

* TURBO prevajalnik - prevedi in poženi
* absolutni nalagalnik - kaj takega najdemo na embedded napravah ali pa MBR
* nalagalnik s prenaslavljanjem - to pa najdemo na modernih OS

### Absolutni nalagalnik

Takšen nalagalnik najdemo v BIOSu. Izvedljiv modul se naloži z zunanje pomnilniške enote v
delovni pomnilnik. Namen tega programa v BIOSu je samopreizkušanje komponent. Danes se nalagalnik
takšne vrste v modernih računalnikih ne uporablja več. MBR pa je del pomnilnika na boot napravi,
kjer so zapisani podatki o particijah in ostalo.

Narava absolutnega nalagalnika je taka, da programi namesto virtualnih naslovov uporabljajo že
kar direktno fiizične naslove - zato se to danes tudi več ne uporablja.

Zgradba absolutnega nalagalnika je sledeča:

* dolžina modula
* nalagalni naslov
* absolutna sekcija (programska koda)
* začetni izvajalni naslov
* kontrolni znaki

### Začetni nalagalnik

Gre za kodo oz. nalagalnik (tudi bootloader), ki se zažene ob prižigu naprave - torej računalnika.
Nahaja se v MBR (to je ponavadi na začetku diska, ki se uporablja za boot). Njegovo delovanje je
sledeče:

* BIOS se požene in opravi samopreverjanje strojne opreme,
* BIOS prebere prvi sektor za zagon diska imenovan MBR. Tu se tudi nahaja začetni nalagalnik,
* začetni nalagalnik izvede nadaljnje nalaganje diskov, gonilnikov itd.

Njegova naloga je tako poiskati bootloader, ki nato požene operacijski sistem, ki se nahaja na eni
izmed particij. Ta bootloader je npr. GRUB, ki ga ponavadi najdemo pri Linuxu. GRUB omogoča tudi
multi-boot.

Vredno je še dodati, da BIOS potrebuje naložiti svoje gonilnike, preden se uporabijo tisti od OS.

#### Zgradba začetnega nalagalnika – MBR

To kodo najdemo na začetku diska v MBR.

* Koda nalagalnika,
* podpis diska,
* 2 zloga?,
* particijska tabela (do 4 particije),
* podpis MBR.

MBRju sledijo ponavadi sektorji diska. Velikost sektorjev in MBR je 512 B.

Če imamo več kot 4 particije, lahko uporabimo večnivojsko particijsko tabelo.

#### Particijski nalagalni sektor

Kot omenjeno lahko posamezne primarne particije nadomestimo z razširjenimi particijami. Te v bistvu
kažejo na novo tabelo particij - gre kot omenjeno za večstopenjsko tabelo.

Potlej imamo notranje razširjene particije in logične particije - te so notranje particije, ki pa
niso razširjene.

Potlej pa imamo še particijski nalagalni sektor (ang. partition boot sector). To je poseben sektor,
ki se nahaja na začetku vsake particije na shranjevalni napravi, kot je trdi disk. Tu so vsi podatki
potrebni za zagon OS na tej particiji. Deluje kot mini-bootloader za posamezno particijo.

Postopek:

Preberi particijski nalagalni sektor: BIOS prebere prvi sektor na aktivni particiji, ki vsebuje particijski nalagalni
sektor.

Izvedi nalaganje: Programska koda v particijskem nalagalnem sektorju se izvede in nadaljuje z nalaganjem nadaljnjih
komponent operacijskega sistema.

Prevedi nadzor zagona: Nalagalnik (bootloader), ki je del particijskega nalagalnega sektorja, prenese nadzor nad
nadaljnjim zagonom na glavni zaganjalnik operacijskega sistema.

#### Začetni nalagalnik v osebnem računalniku - postopek nalaganja

* Naloži se BIOS ukaz na naslovu CS:IP
* Skok na kodo za samopreizkušanje
* BIOS gre čez seznam zagonskih enot, da najde pravo
* Iz posamezne zagonske naprave prebere kodo iz MBR
* Koda MBR v particijski tabeli poišče aktivno particijo in naloži kodo iz njenega glavnega sektorja - ponavadi to
  že zadeva od OS
* Ta koda iz glavnega sektorja aktivne particije nalaga OS - **jedro OS gre iz realnega načina v zaščiten način
  delovanja**

### GRUB

Naloga GRUB je nalaganje jedra OS. Tako je pri linuxu, in po nalaganju GRUB preda nadzor OS. Pri Windows-u pa ni
tako. Pri Windows-u kliče GRUB začetni nalagalnik od Windows-a. Ta se nahaja ne preddoločeni lokaciji na disku,
podobno, kot da bi se zadeva zaganjala iz MBR.

### BIOS alternative

* Slabost BIOSa je, da deluje b 16-bitnem načinu in smo omejeni na 1MB naslovnega prostora. To je kar malo, glede
  na to, da BIOS rabi tudi svoje gonilnike.

Nadgradnja BIOSa je potlej UEFI. Uporablja jezik EFI Byte Code in GUID partition table. Podpira pa tudi recimo
Secure Boot.

#### UEFI

Imamo več sistemskih razredov UEFI:

* BIOS,
* UEFI CMS,
* UEFI and CSM,
* UEFI only.

Ostale načine rabimo večinoma še zaradi kompatibilnosti z določenimi operacijskimi sistemi. Linux zna včasih
delati problema tu, oz. nasploh nalaganje večih operacijskih sistemov na eno napravo.

Omogoča nalaganje iz velikih particij s pomočjo GUID tabele. Je neodvisen od CPE - tudi njegovi gonilniki
so neodvisni od CPE. Definirajo se samo komunikacijski protokoli v jeziku UEFI Byte Code, ki pa jo interpreetira
procesor.

![UEFI structure](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Efi_flowchart_extended.svg/1024px-Efi_flowchart_extended.svg.png)

#### Lastnosti UEFI

* Podpira tako 32 kot 64-bitni način delovanja,
* interakcija nalagalnika strojne opreme (firmware loader) in nalagalnika OS (OS loader),
* podpira GUID tabelo,
* nudi storitve (aplikacije UEFI - nalagalniki SO) in tudi med delovanjem OS (čas, datum, NVRAM - trajni pomnilnik),
* EFI Byte Code / Executable - procesorsko neodvisne aplikacije - interpreter je v sistemskem firmware,
* varno nalaganje - preverja podpis nalagalnika OS - če ta ni veljaven, ga ne požene (to uporablja Windows),
* CMS (emulacija BIOS),
* GOP (neodvisnost od standarda VGA),
* uporabniški vmesnika mora razviti proizvajalec.

#### Ostale alternative

Ostale alternative so še Coreboot in pa OpenBIOS.

### Microsoft gonilniki

Ena izmed prednoti gonilnikov Windowsa je ta, da so vsi podpisani. Npr.:

1. Naredimo gonilnik za Windows,
2. Gonilnik pošljemo Microsoftu, da ga potrdi in certificira - torej podpiše,
3. Tako vsakič, ko se ta gonilnik naloži v Windowsu, se najprej preveri, če je podpisan preko MS strežnikov, kjer
   dobi hash kode od veljavnih gonilnikov.

Podobno funkcionalnost najdemo tudi pri Linuxu, le da je na Windowsu vse vodeno s strani MS.

### Secure Boot

Secure Boot deluje zelo podobno tako, da preverja podpis nalagalnika. Za ta namen na današnjih matičnih ploščah
najdemo TPM modul. NAmen njega he shranjevanje RSA ključev za gonilnike, strojno opremo, gesla in podobno. Ideja
je, da bi se TPM modul uporabljal tudi za ščitenje programske opreme. Nekaj podobnega skuša narediti Apple.

### GUID tabela

Kot omenjeno gre za večjo particijsko tabelo. Več o njej na strani 12 do 13 na prosojnicah.

### UEFI boot manager

Ta je naložen v NVRAM (trajni pomnilnik). Zunanja pomnilna enota UEFI pa ima standardno tabelo GPT
in vsaj eno formatirano particijo FAT na začetku le-te. Znotraj te particije najdemo BOOT datoteke,
ki služijo za zagon OS. Te datoteke so zapisane v izvedljivem formatu EFI Byte Code.

### UEFI: nalaganje OS

Imamo več vrst nalaganja: PXE, IPv4, IPv6, UDP, DHCP, HTTP, ...
Secure Boot - preveri podpis datoteke (nalagalnika OS) in če je ta veljaven, ga požene.
Nalagalnik se podpiše s ključem platforme PK, ki je shranjen v firmware. Imamo lahko še bazo
KEK, ki vsebuje dodatne ključe.

## Dinamično povezovanje in Java

### Porazdeljene računalniške aplikacije

To je najvišji nivo dinamičnega izvajanja. Aplikacije in podatki so lahko shranjeni in se izvajajo
na oddaljenih računalniških sistemih in nato komunicirajo med sabo. Prenos modulov kar med
izvajanjem in podobno. Je pa res, da to pomeni, da objekti ne smejo vsebovati sistemsko odvisne
kode. Java npr. bi že lahko delovala na tak način.

### Dinamično izvajanje programa

Največji približek tega je Java, kjer je vsaka koda, knjižnica in tako naprej svoj razred.
Programski jezik je platformno neodvisen, saj se izvaja na virtualnem stroju (JVM). Tako moramo
ke prilagoditi JVM za posamezno platformo in to je to. Cilj je bil celo izvajanje v oblaku.

### Java

Java kot omenjeno uporablja razrede - vse je razred. Izvorna koda .java se prevede v datoteko
.class, ki pa je v bistvu strojno neodvisna koda - vmesna/zložna koda. Ta se nato izvaja na JVM.
Ker ne gre za direktno strojno kodo, simbolna tabela ostaja. Microsoft je naredil svojo
implementacijo JVM, ki pa je bila zelo počasna. Zato so se odločili, da bodo naredili svoj
jezik C#, ki pa bo deloval na .NET platformi. Tako je C# v bistvu Microsoftova Java.

#### JVM

JVM je torej virtualni stroj, ki izvaja vmesno kodo. Njegove naloge so poleg izvajanja kode še
garbage collection, varnost, optimizacija kode, ... Zaradi njegovega načina delovanje - torej
da se vsa koda programa, ki se izvaja nahaja na kopici, je izvajanje počasnejše, ampak
lahko pa kodo spreminjamo on the fly.

#### Javanska zložna koda

Vmesna koda se pri Javi imenuje zložna koda. Le-to interpretira javanski navidezni stroj JVM.
Skrbi za varnost, sistemsko neodvisnost in pa omrežno prenosljivost.

### Kako narediti sistemsko neodvisno programsko kodo

1. Pristop Jave/.NET, kjer imamo samo drugačen virtualni stroj za vsako platformo, pred tem
   pa samo prevedemo v vmesno/zložno kodo,
2. Pristop Google-a, kjer na ciljni platformi prevedemo v strojno kodo.

### Interpretiranje kode

Poznamo naslednje načine interpretiranja kode:

* interpretiranje (ukaz za ukazom) - enostavno, a počasno,
* JIT (just in time) - prevajanje v strojno kodo med izvajanjem,
* AOT (ahead of time) - prevajanje v strojno kodo pred izvajanjem ob namestitvi,
* prilagodljivo optimiranje - optimizacija med izvajanjem.

### Delovanje JVM

Javanski stroj zelo spominja na stack. Imamo OS in znotraj OS imamo nato lahko več
JVM - načeloma enega za vsak thread. Vsak JVM ima svoj pomnilniški prostor. Podobno
kot pri OS imamo tudi tukaj virtualni pomnilniški prostor, ki je razdeljen na
več delov: stack, heap, .data, .text. NA heap dajemo kodo, ki se izvaja, na stack
pa podatke, ki jih potrebujemo za izvajanje - vključno s spremenljivkami, ki bi
jih ponavadi dajali v registre. JVM je namreč skladovno orientiran stroj.

Vsak javanski program tako teče znotraj svojega JVM. Imamo razredne zbirke, iz katerih
lahko naložimo objekte - te nato damo v omenjeni heap. Iz heap pa podatke nato jemujemo
za izvajanje. Vsak JVM ima tudi svoj programski števec.

#### Sklad JVM

Zgradba je zelo podobna zgradbi skladov procesorjev.

Sklad JVM sestoji iz:

* lokalnih spremenljivk,
* režijske informacije za delo s skladom,
* operandnega sklada.

#### Ostale lastnosti

Enako kot pri običajnih nitih, si vse niti javanskega programa delijo isti pomnilniški
prostor. Tako lahko niti med seboj komunicirajo.

Podatkovni tipi so v Javi malce drugačni - recimo bool je velik 4 byte.

### Interpretacija javanske kode

* sprotno prevajanje v strojno kodo,
* JIT (just in time) prevajanje v strojno kodo - ob klicu nekih delov kode,
* prilagodljivo optimiranje - na strojni nivo prevedemo samo najbolj pogosto
  izvajan del kode.

### Zložna koda

Glavna razlika v tej kodi je, da ni platformno odvisna kot recimo strojna koda.
Poleg tega večino ukazov ne dela z registri, ampak z operandnim skladom (skladovno
orientiran stroj), skladom in kopico.

Pri tej zložni kodi je zanimivo tudi to, da najdemo if stavke, ki jih pri običajnem
zbirniku ne najdemo. Ukazi so tudi hitri, saj so zelo preprosti.

### Razredna zbirka

Razredna zbirka je zbirka razredov, ki so na voljo za uporabo. Med njih spadajo:

* razredi,
* niti,
* vsi podatkovni tipi - tudi int, float, double je razred,
* metode,
* ...

Ta razred izgleda tako, da vsebuje tag, ki pove, za kateri razred gre, in pa podatke
o razredu - metode, spremenljivke, ... Te tagi (značke) pridejo iz nabora konstant.

![Zapis metode v naboru konstant](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-2023-05-14-171506.png)

Primer Math.random()

![Primer Math.random()](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-2023-05-14-171855.png)

Za več primerov glej prosojnice stran 25-29.

### Groverjev algoritem (samo malo me je firbec matral)

[Groverjev algoritem](https://www.youtube.com/watch?v=0RPFWZj7Jm0)

### Kako je z interpretacijo kode v Javi

Java najprej prevede izvorno kodo .java v zložno kodo .class - v razredne objekte.
Ti objekti se nato med seboj povezujejo in se izvajajo v virtualnih strojih JVM.
Pri tem se sproti interpretirajo, možno pa je da se koda tudi sproti optimira.
A vprašanje je, če je optimizacija mogoče celo slabša od interpretacije - smo morda
zapravili še več ciklov za optimizacijo kot bi sicer?

### Kaj so metainformacije v kontekstu Jave in programskih jezikov [ChatGPT]

Metainformacije v kontekstu Jave in programskih jezikov so dodatni podatki, ki
opisujejo druge podatke v programski kodi. To lahko vključuje metapodatke, označbe,
informacije o tipu, dokumentacijo in konfiguracijske datoteke. Metainformacije
pomagajo razvijalcem bolje razumeti, interpretirati in uporabljati podatke v
programih.

Primer Java:

En primer metainformacije v programskem jeziku Java je uporaba označb (annotations).
Označbe omogočajo programerjem, da dodajo dodatne informacije ali navodila kodi. Na
primer, v Javi obstaja označba @Deprecated, ki označuje, da je neka metoda, razred
ali spremenljivka zastarela in se ne priporoča več za uporabo. S to označbo
razvijalci prejmejo opozorilo, da bi morali namesto zastarelega elementa uporabiti
alternativne pristope ali funkcionalnosti. Ta metainformacija pomaga razvijalcem
razumeti, kako naj pravilno uporabljajo določene dele kode in zagotavlja smernice
za vzdrževanje in nadgradnjo programske opreme.

Primer C++:

En primer metainformacije v programskem jeziku C++ je uporaba predloženih (template)
razredov. Predloženi razredi omogočajo programerjem, da parametrizirajo tip podatkov,
ki jih razred manipulira ali uporablja. Na primer, lahko ustvarimo predložen razred
`ArrayList`, ki omogoča shranjevanje elementov poljubnega tipa. Pri ustvarjanju
instance tega razreda lahko programer poda želeni tip podatkov, na primer
`ArrayList<int>` za shranjevanje celih števil ali `ArrayList<string>` za
shranjevanje nizov. To omogoča prilagodljivost in ponovno uporabo kode, saj se
razred prilagodi glede na podani tip podatkov. Predloženi razredi v C++
predstavljajo metainformacijo, ki opisuje, kako se bo določen razred uporabljal in
prilagajal glede na podane parametre.

Pojasnilo:

TL;DR: V kontekstu C++ je uporaba predloženih razredov (template classes)
metainformacija. Predloženi razredi omogočajo programerjem ustvarjanje razredov,
ki so parametrizirani glede na tip, kar omogoča prilagodljivost in ponovno uporabo
kode. Metainformacija opisuje, kako se bo razred uporabljal in prilagajal glede na
podane parametre, kar omogoča prilagodljivo obnašanje razreda.

### Kazalci kot metainformacije

Še en primer metainformacij je uporaba kazalcev na funkcije. Kazalci na funkcije
omogočajo programerjem, da funkcije uporabljajo kot parametre drugih funkcij. Na
primer, lahko ustvarimo funkcijo `sort`, ki kot parameter sprejme kazalec na funkcijo
`compare`. Ta funkcija `compare` primerja dva elementa in vrne rezultat, ki določi
vrstni red elementov. Skratka, ne rabimo pisati nove funkcije `sort` za vsak tip.
Je pa res, da to do neke mere **preprečuje standardizacijo in otežuje razumevanje**.

Tako da je izziv najti razmerje med količino metainformacij in razumljivostjo kode.

### Skladovno vs registersko usmerjen stroj

Skladovno usmerjen stroj je stroj, ki uporablja sklad za shranjevanje podatkov.
Primer je Java. Registersko usmerjen stroj pa uporablja registre za shranjevanje
podatkov. Primer je Dalvik. Dalvik da na voljo 65k registrskih mest, čeprav
jih v resnici računalnik nima toliko - pač gredo podatki v pomnilnik.

### Okvirni na skladu

Posamezen okvir kot omenjeno vsebuje lokalne spremenljivke, režijske informacije
in sklad operandov. Vsak okvir je posamezno izvajalno okolje, ki vsebuje vse
potrebne informacije za izvajanje posamezne metode. Imamo pa tudi predel z
virtualnimi registri - PC, vars (kazalec na lokalne spremenljivke), frame (kazalec
na režijske informacije), optop (kazalec na sklad operandov).

Vsi te skladi, ki so sicer ločeni med sabo gredo na koncu na skupni sklad.
Samo pač imamo segmente na skladu.

### Razredne zbirke

Pomembno je poudariti, da tu v Javi simboli iz simbolne tabele ostanejo v
programu, medtem ko v C++ se vse to izbriše. Java jih obravnava kot konstante.

Na vrhu razredne hierarhije je Object, iz katerega izhajajo vsi ostali razredi.

### Izjeme

V glavnem tu je pomembna ideja: če se zgodi izjema, se izvajanje programa
prekine in se začne iskanje bloka, ki bi lahko obravnaval izjemo - tabela
vektorjev z ISR (interrupt service routine).

Izjeme delujejo tako, da zajemajo nek del programa. Povemo, od kje do kje
naj se izjema nahaja. Kar pa to povzroči je, da je izvajanje programa
počasnejše.

### Dinamično povezovanje

Pri Javi gre za **pozno** (ali zgodnje) dinamično povezovanje, kar pa nas stane
tako performanse kot varnosti. Catch je v tem, da se knjižnice naložijo naknadno,
torej med izvajanjem programa. Pri tem se knjižnice pogosto naložijo rekurzivno,
torej potrebujemo celo drevo knjižnic zaradi odvisnosti. To pomeni ŠE več časa.
Takšno nalaganje tako NI realno časovno, ker se izvaja med izvajanjem programa.

Takšno nalaganje tudi pomeni rekurzivno iskanje knjižnic. Za nalaganje poskrbi
JVM. Ukazi s sklicom na objekt obdržijo zaporedno številko vstopa v nabor
konstant, dokler sklic ni razrešen – torej se povežemo s knjižnico.

Takšno nalaganje knjižnic je lahko tudi nevarno, saj lahko napadalec zlahka
zamenja knjižnico z drugo, ki ima isti vmesni vmesnik, vendar pa ima drugačno
implementacijo. Primer take zlorabe je DLL hijacking. Če se spomnimo, so DLL
knjižnice dinamične knjižnice v Windows okolju.

Postopek povezovanja:

+ Preverjanje - verifikacija - ali je binarna koda vmesnika/objekta pravilna,
+ Priprava - priprava pomnilnika - razporejanje pomnilnika (statična inicializacija
  polj ipd.),
+ Razreševanje - razreševanje simbolov,

#### Razreševanje simbolov**

1. Nalaganje - nalaganje podatkovnih tipov,
2. Preverjanje tipa - preveri se sintaksa,
3. Priprava tipa - rezervacija pomnilnika,
4. Razrešitev tipa - razrešitev referenc (rekurzivno),
5. Inicializacija tipa - najprej incializirajo vsi nadrejeni tipi,
6. Preverjanje dostopnih pravic - ali klicoči tip lahko dostopa do klicanega.

### Razredni nalagalniki

Začetni razredni nalagalnik - nalaga lokalne razredne zbirke - isti jezik kot JVM.

Uporabniški razredni nalagalnik - nalaga uporabniške razredne zbirke - napisan v Javi.

Java ti tudi omogoča imeti svoj nalagalnik, ki pa deduje iz starševskega nalagalnika -
torej iz razreda `ClassLoader`.*

### Dalvik

Dalvik je **registersko usmerjen stroj**, ki je bil razvit za Android. Več .class datotek
združi v eno .dex datoteko. Uporablja tudi drugačen nabor ukazov. Poleg tega pa
uporablja tudi sprotno prilagodljivo optimiranje.

ART format - Android Runtime: uporablja ahead-of-time kompilacijo in ob času namestitve
se koda prevede v .dex datoteko, ki je hranjena v ELF formatu.

APK - ZIP + jar, CERT.RSA, AndroidManifest.xml, direktorij lib z domorodno kodo, MANIFEST.MF,
classes.dex, Resources.arsc, ...

## .NET

.NET je platforma, ki je bila razvita za Windows. Lahko bi rekli, da posnema Javo. Preko
skupnega vmesnega jezika CIL (Common Intermediate Language) podpira več deset programskih
jezikov. CIL se hrani v PE formatu (podoben ELF formatu).

CIL teče znotraj platforme CLI (Common Language Infrastructure), kjer najdemo JIT in
AOT (generator strojne kode). To zelo spominja na JVM.

### CIL

Gre za nivo skupka objektov, ki so neodvisni od jezika (.NET assembly).

Podpira obdelavo izjem, garbage collection, varnost, itd.

Microsoft: CLR (Common Language Runtime) - to je izvajalno okolje na Windows, ki vključuje:

- CTS (Common Type System) - skupni tipovni sistem,
- Metadata - opis podatkov,
- CLS (Common Language Specification) - skupni jezikovni standard,
- VES (Virtual Execution System) - virtualni izvajalni sistem,
- BCL (Base Class Library) - knjižnice.

Pazi na drugačne tipe kot v Javi ali C++.

### PE objektni format

PE (Portable Executable) je objektni format, ki ga uporablja Windows. To so moduli tipa
EXE, DLL, SYS, OCX, CPL, SCR, DRV, FON, itd.

Ceč na strani 6+, PP 7.

### Ostalo

Tu je še nekaj glede hash kod, ki se verjetno uporabljajo za preverjanje pristnosti, kot
neke vrste verzioniranje.

## Sistemski klici in gonilniki

### Sistemski klici

Le-te se izvajajo ves čas. Recimo na linuxu lahko to preveriš z `strace` ukazom.

Primer:

![Sistemski klici](https://davidblog.si/wp-content/uploads/2023/05/Screenshot-from-2023-05-23-20-21-26.png)

Ti klici tudi pomenijo stalen prehod iz uporabniškega načina v jedrni način in nazaj. To
pa stane veliko časa.

Aplikacija in OS imata oba svoj podatkovni vmesnik.

#### Pot sistemskega klica

1. Uporabnik pokliče sistemski klic,
2. Aplikacija kliče OS in podatki o klicu se shranijo kot glava zahteve - glava zahteve
   je kot nakupovalni listek,
3. Podatki se prenesejo v jedro,
4. Jedro preveri pravice in preveri, če je klic veljaven,*
5. Jedro aktivira gonilnik,
6. Gonilnik kliče napravo,
7. Aktivira se prekinitvena rutina,
8. Prekinitvena rutina prebere podatke,
9. Prekinitvena rutina prenese podatke v jedro,
10. Jedro prenese podatke v aplikacijo.
11. Aplikacija nadaljuje z delom.

Za prenos podatkov skrbi DMA (Direct Memory Access).

V glavnem pomembno si je zapomniti, da gre vse preko jedra, tudi podatki, ki gredo najprej
v buffer. Ta buffer ni tako velik in moramo ga sproti sprazniti, sicer se nam povozijo
podatki. Ukaza: **copy from/to user space**.

Gonilnikov si NE želimo v jedru, da nam ne povzročijo blue screena. Zato jih imamo v
uporabniškem načinu, če je le mogoče.

Bolj, ko gremo navzdol, bolj specifični smo, kaj od naprave želimo.

### Vrste jeder

#### Monolitno jedro

Vse je v jedru. To je najhitrejša rešitev, vendar je tudi najbolj nestabilna. Še vedno pa
imamo module, ki jih lahko nalagamo ali odložimo. Primer je Linux. Vse funkcionalnosti so
v kernel načinu, zato je veliko preklopov. Moduli so objektno orientiran pristop.

#### Mikrojedro

V jedru imamo le najnujnejše funkcionalnosti. Vse ostalo je v uporabniškem načinu.
Vse storitve/servise imamo v uporabniškem načinu. Primer je NT jedro. Tako je malo
preklopov, vendar je tudi počasnejše in jedro se težje sesuje. Jedro je tudi
majhno in lažje za vzdrževanje. Večja varnost.

Primeri teh storitev so: datotečni sistem, gonilniki, omrežje, itd.

#### Hibridno jedro

Imamo nekaj funkcionalnosti v jedru, nekaj pa v uporabniškem načinu. Primer je Windows 7 in
pa načeloma tudi novi Windows-i.

### Kontekstni preklop

Kontekstni preklop stane čas. Tu pride do vprašanja, ali pri preklopu želimo shraniti vse
registre ali ne. Strojni (HW) preklop si shrani vse, ampak razvijalci OS pa lahko shranimo
samo tisto, kar vemo, da rabimo - to tudi zakomplicira prevajalnike. Večina OS tako sama
izvaja kontekstne preklope.

Jedro ima svoj sklad in se ter tako poskrbi za te kontekstne preklope. Pri tem uporablja
tudi tabelo GDT - Global Descriptor Table.

Za več podrobnosti glej stran 7 do 11.

### Prehodi med obročem 3 in 0

#### Prekinitve

Sprva so se ti prehodi izvajali s pomočjo prekinitvenih rutin. To je bilo zelo počasno,
saj je potreben dostop do pomnilnika (GDT in TSS).
CPU se privzeto nahaja v ringu 0. Nato pa v programu naletimo na programsko prekinitev.
Ta učinkuje kot sistemski klic. Gremo iz user mode v kernel mode.

Prekinitve najdemo v obliki ukazov **int 3**, **int 0x80** na Linuxu in **int 0x2E** na
Windows. Na novejših sistemih lahko v prekinitev tudi vstavimo parametre.

Do preklopa pa seveda pride, ker lahko do V/I naprav dostopamo le iz jedra.

#### LDT

...

### Sistemski klici na novejših procesorjih

Intel: SYSENTER, SYSEXIT

AMD: SYSCALL, SYSRET

Ta način je dosti hitrejši! Uporablja posebne registre, ki nam iz asm niso dostopni kot
uporabniku. Se pa s pomočjo njih implementira ta kontekstni preklop in je, zato tudi
hitrejši. So pa ti registri modelno specifični.

#### Prenos parametrov v sistemske klice

Podatke lahko v sistemske klice prenašamo preko:

- registrov - hitro, manjša količina podatkov, omejeno št. parametrov,
- v bloku pomnilnika - naslov je v registru, veliko podatkov, večji overhead,
- v skladu - isti princip kot pri bloku pomnilnika.

Jedro vedno kopira vse parametre sistemskih klicev iz uporabniškega naslovnega prostora
v naslovni prostor jedra.

## Gonilniki

### Postopek klica gonilnika

1. Opravilo OS kliče gonilnik - zahteva lahko pride iz jedra ali iz neke aplikacije,
2. Glava zahteve [nakupovalni listič] se shrani v vhodno vrsto gonilnika,
    1. Glava zahteve se postavi v vrsto,
    2. Strategijska rutina izbira zahteve po nekem vrstnem redu,
    3. Ponavadi je določena neka prioriteta,
3. Ko gonilnik obdela zahtevo, sproži prekinitev,
4. Sproži se prekinitvena rutina:
    1. To rutino kliče CPU, ko dobi prekinitev od gonilnika,
    2. Gonilnik določa, kaj se zgodi, ko se zgodi prekinitev,
    3. Glede na pomembnost prekinitve imamo dve možni rutini. Ideja je, da če se rutina
       ne izvede v zgornji polovici, se izvede v spodnji polovici:
        1. Zgornja polovica - hitra rutina,
        2. Spodnja polovica - počasna rutina,
5. Ta čas se podatki iz V/I naprave preko gonilnika, preko DMA prenesejo v sistemski vmesnik.

### Model prekinitev

Spodaj opisano model še vedno uporablja ARM, je pa precej počasen. Je pa njegova prednost,
da zlahka registriramo nove rutine.

# Vprašanja

## Sekcija vs. segment

Sekcije predstavljajo različne dele programa in jih najdemo v objektnih modulih - .o
datotekah. Segmente pa najdemo v izvršljivih datotečnih formatih - npr. .exe. Sekcije se
tako združujejo v segmente. Namen segmentov je bolj ali manj organizacija pomnilnika -
kako se program naloži v pomnilnik.

Primeri sekcij so:

- **.text** - koda programa,
- **.data** - inicializirani podatki,
- **.rodata**/.rdata - read only podatki,
- **.bss** - neinicializirani podatki,
- .interp - dinamični linker,
- .shstrtab - imena sekcij,
- .symtab - tabela simbolov,
- .strtab - tabela nizov znakov.

Kar se tiče zastavic, pa samo logičen pomislek: ali se ta koda izvaja, rabimo pravice
za pisanje? Branje je vedno ena izmed zastavic.

Konstante so lahko v .rodata/.rdata ali pa v .text. Ker te dve sekciji padeta v isti
segment, je tudi potrebno paziti na zastavice in na to, da ponesreči ne začnemo
izvajati konstant kot kodo.

## Izvedljivi vs. objektni modul

Izvedljivi modul je končna datoteka, ki je pripravljena za nalaganje in izvajanje. Vsebuje
segmente in vstopno točko. Sekcije so tu že združene v segmente, da se lahko program
direktno naloži v pomnilnik. Objektni modul je predhodnik te datoteke pri prevajanju in
zato še ni izvedljiv, vsebuje samo sekcije in nima vstopne točke.

## VDSO

VDSO je pohitritev na Linuxu, ki deluje tako, da del pomnilnika jedra preslika v pomnilniški
prostor uporabnika. Tako lahko se lahko določeni sistemski klici opravijo brez preklopa v
kernel način.

## Statično povezovanje

Po tem, ko dobimo objektne module, je čas za povezovanje.
Ideja je, da imamo na vhodu več objektnih modulov, ki pa jih moramo povezati v en izvedljiv
modul. Modulu dodelimo pomnilniški prostor, povežemo posamezne objekte simbole, prenaslovimo
vse potrebno in dopolnimo izvedljiv program s sistemskimi klici. Zatem je program pripravljen
za nalaganje.

Ker vse to storimo pred zagonom, ima program zelo dober response time.

Na izhodu pa tudi lahko dobimo različne vrste programov: prenaslovljiv in absolutno izvedljiv
modul ali pa izhodni objektni modul.

Želimo si, da povezovalnik naredi čim več stvari, da je program čim bolj pripravljen za zagon.

Glavna stvar tu pa je, da sekcije, ki pašejo skupaj damo skupaj v dotične segmente.

### V zvezi s sekcijami...*

Ko se povezujejo objektni moduli, se sekcije združujejo v segmente. Segmenti so pa tisti,
ki se naložijo v pomnilnik.

### Sekcije

Nekaj več o sekcijah glede na način naslavljanja: [Sekcije](#sekcije-glede-na-način-naslavljanja).

Imamo več vrst sekcij:

- absolutna sekcija,
- nepoimenovana sekcija,
- poimenovana sekcija.

Kdaj se absolutne sekcije zlivajo? Kadar se sekciji prekrivata – njun pomnilniški prostor sovpada.
Takrat se sekciji združita v eno absolutno sekcijo.

### Prenaslovitvena tabela

Glej [Prenaslovitvena tabela](#prenaslovitvena-tabela).

## PE vs. ELF

Glavna razlika je v tem, da so viri vključeni v izvedljivi modul, medtem ko so pri ELF
ti viri zunanje reference. Recimo primer je ikona aplikacije, ki jo moramo pri PR formatu
priložiti k programu, ki ga prevajamo.

## Povezovanje knjižnic in verzioniranje

Knjižnice lahko povežemo na sledeče načine:

1. Statistično povezovanje,
2. Dinamično povezovanje:
    1. Dinamično povezovanje ob zagonu - zgodnje povezovanje,
    2. Dinamično povezovanje ob prvem klicu knjižnice - pozno povezovanje.

Težavice, ki nastanejo, so sledeče:

- **Kako zagotoviti, da se bo program izvajal tudi v prihodnosti?** - verzioniranje - major in minor version,
  kjer major version spremeni tudi vmesnik, minor version pa ponavadi samo notranje delovanje knjižnice.
- **Problem varnosti** - ker gre za dinamične knjižnice, so te lažje nadomeščene z zlonamernimi
  programi oz. knjižnicami. Pa tudi posodabljanje je problem, ker se lahko zgodi, da se knjižnica
  posodobi, program pa ne. Tako lahko pride do težav.
- **Klic po imenu vs. klic po številki** - Slednje je sicer hitrejše, ampak problem je, kaj če
  se številka funkcije spremeni? Tako je bolje klicati po imenu, ker se to ne spremeni - imamo tabelo
  funkcij z imeni in naslovi. Takšna zgodba je tudi pri DLL-ih, kjer se funkcije zato kličejo po imenu.

Več o tem najdeš v [Programske knjižnice](#programske-knjižnice).

## MBR in BIOS

Kaj je MBR? MBR je Master Boot Record, ki je prvi sektor na disku. Vsebuje pa:

* Koda nalagalnika,
* podpis diska,
* 2 zloga?,
* particijska tabela (do 4 particije),
* podpis MBR.

V MBR najdemo particijsko tabelo, ki vsebuje podatke o particijah.

_Kaj je BIOS? BIOS je Basic Input Output System, ki je firmware, ki se nahaja na matični plošči.
Njegov namen je samopreverjanje in zagon računalnika - torej inicializacija V/I naprav, pregled
predpripravljenega seznama zagonskih enot, dokler ne najde ustrezne. BIOS nato prebere
kodo iz sektorja MBR in jo preda v izvajanje. MBR poišče aktivno particijo in prebere
kodo iz njenega glavnega sektorja. Sledi nalaganje jedra OS._

Več o tem najdeš v [Nalagalnik](#nalagalnik).

### GRUB Multiboot

Glej [GRUB](#grub).

Postopek nalaganja GRUB je sledeč:

1. BIOS poišče zagonsko enoto v seznamu,
2. BIOS prebere MBR kodo in začne izvajanje,
3. MBR koda vsebuje prvo stopnjo nalagalnika GRUB, ki naloži še drugi del GRUB,
4. GRUB na zaslon izpiše seznam operacijskih sistemov in njihovih jeder,
5. Uporabnik izbere jedro, ki ga želi zagnati,
6. Po izbiri se začne nalaganje jedra OS. Pri Windows se kliče Windows-ov nalagalnik.

#### Varnost

[//]: # (TODO: Finish this)

Ker je nalagalnik prvi program, ki se izvede, je pomembno, da je ta program zaupanja vreden...

## Java

Kaj je Java: [Java](#java).

### Virtualizacija

Kaj je virtualizacija: [JVM](#jvm) in [Delovanje JVM](#delovanje-jvm).

### Prednosti

Glavne prednosti so:

- platformna neodvisnost - ker se programi izvajajo na JVM, so ti programi neodvisni od platforme,
- varnost - ker se programi izvajajo na JVM, so ti programi varni v smislu:
  - memory management - imamo garbage collector, ki skrbi za čiščenje pomnilnika,
  - uporaba sandboxa - recimo Java web appleti rečejo v sandbox, ki je varno okolje,
- možnost spreminjanja kode on the fly in nasploh večji nadzor nad izvajanjem programa.

### Slabosti

Glavne slabosti so:

- počasnost - ker se programi izvajajo na JVM, so ti programi počasnejši od programov, ki se izvajajo na strojni opremi,
- kodo težje optimiziramo za ciljno platformo, saj smo odvisni od izvajanega okolja,
- težje je delati z nizkimi nivoji, saj je vse skrito za JVM-om.

