# Zapiski za SPO koolokvij 2

## Sekcije glede na način naslavljanja.
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
pri nalaganju najdemo segmente, pri povezovanju pa še seckije. 

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
vse potrebno in dopolnimo izvedljiv program s ssitemskimi klici. Zatem je program pripravljen
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
