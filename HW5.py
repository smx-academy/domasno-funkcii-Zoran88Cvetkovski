"""1. Da se kreira funkcija so ime pecati_zdravo koja ke prima parametar ime 
i da se pecati poraka so pozdrav zaedno so imeto koe e isprateno kako parametar. Imeto da go vnese korisnikot.
"""

def pecati_zdravo (ime):
    print ("Pozdrav {}".format (ime))

print ("Vnesete go Vaseto ime")
ime=str (input ())
pecati_zdravo (ime)

"""2. Da se kreira funkcija so ime zbir koja ke prima dva broevi kako parametar, 
da se presmeta zbirot i da se ispecati dali zbirot e paren ili ne paren. Broevite da gi vnese korisnikot.
"""
def zbir (x,y):
    sobiranje = x+y
    print ("Zbirot na {} i {} iznesuva {}".format (x,y,sobiranje))
    if sobiranje%2==0:
        print ("Zbirot e paren broj")
    else:
        print ("Zbirot e neparen broj")
print ("Vnesete go prviot broj")
brojce1= int (input ())
print ("Vnesete go vtoriot broj")
brojce2 =int (input ())

zbir (brojce1,brojce2)

"""3. Da se kreira funkcija so ime najgolem_broj koja ke prima 3 parametri, 
da se najde najgolemiot broj i da se ispecati. Broevite da gi vnese korisnikot
"""

def najgolem_broj (lisa):
    maks= max (lisa)
    print ("Najoglem broj e {}".format(maks))

lisa=[]
print ("Potrebno e da vnesete tri broja.")
print("Vnesete go prviot broj")
z=int (input())
lisa.append (z)
print("Vnesete go vtoriot broj")
c=int (input())
lisa.append (c)
print("Vnesete go tretiot broj")
v=int (input())
lisa.append (v)

najgolem_broj(lisa)

"""4. Da se kreira funkcija plostina i funkcija perimetar koi ke primaat dva paremtri, 
da presmetuvaat plostinata i perimetarot na pravoagolnik. 
Korisnikot da gi vnesuva broevite i korisnikot da izbere koja presmetka da se izvrsi. DA NE SE IZVRSUVAAT DVETE
"""

def plostina (a,b):
    kalplostina = a*b
    print ("Plostina na pravoagolnikot so strani {} i {} iznesuva {}".format(a,b,kalplostina))
def perimetar (a,b):
    kalperimetar = 2*a+2*b
    print ("Perimetar na pravoagolnik so strani {} i {} iznesuva {}".format (a,b,kalperimetar))


print ("Potrebno e da gi vnesete dvete strani na pravoagolnikot")
print ("vnesete ja prvata strana na pravoagolnikot ")
x=int (input ())
print ("Vnesete ja vtorata stana na pravoagolnikot")
y=int (input ())


izbor = input("Izberete dali sakate da vi bide presmetana plostina ili perimetarot na pravoagolnikot\n")
if (izbor == "plostina"):
    plostina (x,y)
elif (izbor == "perimetar"):
    perimetar(x,y)


"""5. Da se kreira funkcija koja ke prima eden parametar lista i da moze da presmeta prosek na listata"""

def prosek_na_list (broevi):
    prosek = zbir /vkupno
    print ("Prosek na broevite vo lista iznesuva {}".format(prosek))

idemo = "da"
vkupno = 0
broevi= []
print ("Potrebno e da vnesete broevi vo vasata lista")
while idemo=="da":
    print ("vnesete broj")
    broj= int(input())
    broevi.append (broj)
    vkupno +=1
    idemo =input ("da prodolzime? 'da' ili 'ne'\n")
print ("Vie gi imate Vneseno slednive broevi: ",broevi)
#zbir =sum (broevi)

#print (zbir)
#print (vkupno)
prosek_na_list (broevi)


"""6. Da se kreira funkcija so ime najdolgo ime koja ke prima lista kako parametar, 
da go njade najdolgoto ime od lista, da go ispecati i da kaze od kolku parametri e sostaveno. Korisnikot da gi vnesuva iminjata
"""
def Najdolgo_ime (lista):
    print ("Najdolgo ime e {}".format (lista))

def baranje_na_najdolgo_ime (dolzina):
    print ("Najdolgo ime se sostoi od {} karakteri".format(dolzina))

lista = []
dolzina = []
da="da"

print ("Treba da vnesete iminja koi bi sakale da gi imate vo Vasata lista")
while da == "da":
    print ("Vnesete ime koe ke bide zapisano vo Vasata lista")
    ime = str (input ())
    lista.append (ime)
    dolzina.append (len (ime))
    da =input ("Dali sakate da vnesete novo ime? 'da' ili 'ne'\n")
print ("Vie gi imate Vneseno slednive iminja: ",lista)

najdolgo = max (dolzina)
brisi=dolzina.index (najdolgo)
final = lista [dolzina.index (najdolgo)]

Najdolgo_ime (final)
baranje_na_najdolgo_ime (najdolgo)

"""7. Da se napravi funkcija koja ke presmetuva prosek na ucenik, otcenite da gi prima kako parametar vo lista. 
Da ima druga funkcija koja kako parametri ke gi prima prosekot i imeto na ucenikot, 
ke presmetuva uspeh na ucenik spored prosekot i da ispecati so kakov uspeh e toj ucenik"""

def ime_na_ucenik (x):
    print ("Ucenikot so ime {}".format (x))

def prosek_na_oceni (prosek):
    print ("se zdobi so prosek {}".format (prosek))

def uspeh_na_ucenik (uspeh):
    if uspeh <1.5:
        print ("Ucenikot postigna Nezadovolitel uspeh")
    elif uspeh >=1.5 and uspeh <2.5:
        print ("Ucenikot postigna Zadovolitel uspeh")
    elif uspeh >=2.5 and uspeh <3.5:
        print ("Ucenikot postigna Dobar uspeh")
    elif uspeh >=3.5 and uspeh <4.5:
        print ("Ucenikot postigna Mnogu Dobar uspeh")
    else:
        print ("Ucenikot postigna Odlicen uspeh")


print ("Vnesete go imeto na ucenikot")
ime = str (input())

da="da"
brojac = 0
lista_na_ocenki =[]

while da =="da":
    print ("Vnesete predmet ")
    predmet = str (input ())
    brojac +=1
    print ("Vnesete ja ocenkata za predmetot {}".format (predmet))
    ocena = int (input ())
    while True:
        if ocena>5:
            print("Ocenkata ne e evidentirana. Vnesete ja ocenkata za predmetot {}".format (predmet))
            ocena= int (input())
        else:
            break
    lista_na_ocenki.append (ocena)
    da  =input ("da prodolzime? 'da' ili 'ne'\n")

prosek = sum (lista_na_ocenki)/brojac
uspeh=prosek


ime_na_ucenik (ime)
prosek_na_oceni (prosek)
uspeh_na_ucenik (uspeh)

"""8. Da se napravi funkcija koja kako parametar ke prima nekoj string i da proveri dali toj string e palindrom 
t.e. dali toj string se cita od dvete strani
Primer: ana, kalabalak"""

def Proverka (x):
    if (x == x[::-1]):
        print ("Zborot {} e palindrom".format (x))
    else:
        print ("Zborot {} ne e palindrom".format (x))

print ("Vnesete nekoj zbor za da se proveri dali e palindrom")
zbor = str (input ())

Proverka(zbor)