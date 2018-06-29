print("Hello, World!")

zmienna = 5
#int float

rzeczywista = 7.5
y= float(38)

x= 4.3
print(x)
print( '%.20f' % x, y)
print(x)


#string
napis1 = 'witaj'
napis2 = "witaj"
print(napis1 == napis2) #True

napis = "Nie martw sie o 'pojedyncze' cudzyslowy."

witaj = "witaj"
swiecie = "swiecie"
witajswiecie = witaj + " " + swiecie
print(witajswiecie)

z= isinstance(napis1, int) 
x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(z,x)

#==================================
class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj) 

#issubclass()

#=================================
tablica = []
tablica.append(1)
tablica.append(2)
tablica.append(3)
print(tablica[0]) # wypisze 1
print(tablica[1]) # wypisze 2
print(tablica[2]) # wypisze 3

# wypisze kolejno 1, 2, 3
for x in tablica:
    print(x)


liczby = []
napisy = []
imiona = ["Jan", "Edward", "Joanna"]
#https://www.learnpython.org/pl/Tablice

suma = 1 + 2 * 3 / 4.0
reszta = 11 % 3
kwadrat = 7 ** 2
szescian = 2 ** 3
witajswiecie = "witaj" + " " + "swiecie"
wielewitaj = "witaj" * 10

print("*"*20)


parzyste_dodatnie = [2,4,6,8]
nieparzyste_dodatnie = [1,3,5,7]
naturalne = parzyste_dodatnie + nieparzyste_dodatnie

print([1,2,3] * 3)


#object
#.count()
x = object()
y = object()

# zmien ten kod
x_tab = [x]
y_tab = [y]
duza_tab = []

print("x_tab zawiera %d obiektow" % len(x_tab))
print("y_tab zawiera %d obiektow" % len(y_tab))
print("duza_tab zawiera %d obiektow" % len(duza_tab))

# sprawdzenie poprawnosci
if x_tab.count(x) == 10 and y_tab.count(y) == 10:
    print("Prawie zrobione...")
if duza_tab.count(x) == 10 and duza_tab.count(y) == 10:
    print("Doskonale!")


#=====================================
imie = "Dorota"
print("Witaj, %s!" % imie)

imie = "Marek"
wiek = 23
print("%s ma %d lata." % (imie, wiek))

# To wypisze: Tablica: [1, 2, 3]
MojaTab = [1,2,3]
print("Tablica: %s" % MojaTab)
#na obiekcie automatycznie wywołana metoda repr

#===================================
# tak tworzymy krotke
dane = ("Dorota", 5, 32)

print("%s mieszka w bloku nr %d w mieszkaniu %d" % dane)

# %s
#%d
#%f
#%.ilosccyfr liczba float
#%x/%X  całkowite szestnastkowe małe duże litery

print("Nigdy nie czytalem 'Potopu'.")   # Nigdy nie czytalem 'Potopu'.
print('Nigdy nie czytalem \'Potopu\'.') # Nigdy nie czytalem 'Potopu'.
# Ponizej jak umiescic " w tekscie
print("Nigdy nie czytalem \"Potopu\".") # Nigdy nie czytalem "Potopu".

napis = "AAA BBB ..."
print(len(napis)) # 11
#len długość


napis = "abcdeabcde"
print(napis.index("a")) # 0
print(napis.index("d")) # 3
#pierwszy znak


napis = "abrakadabra"
print(napis.count("a"))  # 5
print(napis.count("ab")) # 2


napis = "abcdefghijk"
print(napis[2]) # c

napis = "abcdefghijklmnop"
print(napis[3:7]) # defg
#wycinanie znaków

'''
napis = "abcdefg"

print napis[0:4] # abcd
print napis[:4]  # abcd


komentarz wieloliniowy !!!!!!!!!!!!!!
print napis[::] # Wypisze caly napis

# zamiast liczby mozemy podac wyrazenie,
# ktorego wynikiem jest liczba
print napis[4:len(napis)] # efg
print napis[4:]           # efg

napis = "abcdef"
print napis[-1]    # f
print napis[-4:-2] # cd
print napis[-4:]   # cdef
print napis[:-2]   # abcd

napis = "Witaj"
print napis.upper() # WITAJ
print napis.lower() # witaj


napis = "Witaj Alu"
print napis.startswith("Witaj") # True
print napis.startswith("Czesc") # False
print napis.endswith("Alu")     # True
print napis.endswith("swiecie") # False

napis = "Ala ma kota."
tablica_slow = napis.split(" ")
print tablica_slow # ['Ala', 'ma', 'kota']


# Rozdziela napis na trzy czesci,
# z ktorych kazda zawiera tylko jedno slowo
print "Napis rozdzielony na slowa: %s" % s.split(" ")

'''

'''
x = 2
print x == 2 # wypisze True
print x != 2 # wypisze False
print x == 3 # wypisze False
print x < 3  # wypisze True

imie = "Jan"
wiek = 23
if imie == "Jan" and wiek == 23:
    print "Nazywasz sie Jan i masz 23 lata."

if imie == "Jan" or imie == "Robert":
    print "Nazywasz sie Jan lub Robert"

imie = "Robert"
if imie in ["Jan", "Robert"]:
    print "Nazywasz sie Jan lub Robert"

bloki kodu wcięcia zamiast nawiasów
WCIĘCIA 4spacje


if <wyrażenie jest prawdziwe>:
    <rób coś>
    ....
    ....
elif <poprzednie wyrazenie jest falszywe, ale to prawdziwe>:
    <rób coś innego>
    ....
    ....
else: # jesli zadne z powyzszych nie jest prawdziwe
    <rób jeszcze coś innego>
    ....
    ....

x = 2
if x == 2:
    print "x wynosi dwa!"
else:
    print "x jest rozne od dwoch."

PUSTE OBIEKTY

    Pusty napis: ""
    Pusta tablica (lista): []
    Liczba zero: 0
    Zmienna logiczna zawierająca False: False

OPERATOR is
x = [1,2,3]
y = [1,2,3]
print x == y # Wypisze True
print x is y # Wypisze False

tablica = [1, 2, 3]
tablica2 = ['a', 'b', tablica]
print tablica == tablica2[2] # True
print tablica is tablica2[2] # True

# Ponizej dowod na to, ze is mowi prawde

tablica.append(4) # Dodajemy do tablicy liczbe 4
print tablica2[2] # [1, 2, 3, 4]

TA SAMA komórka pamięci
tablica = [1, 2, 3]
tablica2 = ['a', 'b', tablica]
print tablica == tablica2[2] # True
print tablica is tablica2[2] # True

tablica2[2] = tablica + [4]
print tablica is tablica2[2] # False
print "tablica2 = ", tablica2[2]
print "tablica = ", tablica
'''


'''
NOT
print not False              # Wypisze True
print (not False) == (False) # Wypisze False

'''
#===========================================================
pierwsze = [2,3,5,7]
for pierwsza in pierwsze:
    print(pierwsza)

'''
# Wypisze liczby 0 1 2 3 4
for x in xrange(5):
    print x,

print

# Wypisze 3 4 5
for x in xrange(3,6):
    print x,

RANGE - nowa tablica
XRANGE - pojedyncza liczba




licznik = 0
while licznik < 5:
    print licznik,
    licznik += 1  # Ma to taki sam efekt jak licznik = licznik + 1




# Wypisze 0 1 2 3 4

licznik = 0
while True:
    print licznik,
    licznik += 1
    if licznik >= 5:
        break

print

# Wypisze tylko liczby nieparzyste - 1 3 5 7 9
for x in xrange(10):
    # Sprawdz, czy x jest parzyste
    if x % 2 == 0:
        continue
    print x,
    
'''

'''
funkcja
naglowek_bloku: 
    1. linia bloku 
    2. linia bloku 
    ...

slowo_koluczowe_bloku nazwa_bloku(argument1, argument2, ...)

def
!!!!!!!!

def przywitanie():
    print "Pozdrowienia z mojej funckji!"

def przywitanie_imienne(imie, zyczenia):
    print "Witaj" + imie + ". Zycze Tobie " + zyczenia

przywitanie() # Wypisze "Pozdrowienia z mojej funckji!"
przywitanie_imienne("Jacek", "zdrowia") # Wypisze immienne zyczenia




def dzielenie(dzielna, dzielnik):
    if(dzielnik == 0):
        return # zakoncz funkcje nic nie zwracajac
    else:
        return dzielna / dzielnik

print dzielenie(5, 0)
print "#########################"
print dzielenie(10, 2)








def dzielenie(dzielna, dzielnik):
    if(dzielnik == 0):
        return # zakoncz funkcje nic nie zwracajac
    else:
        return dzielna / dzielnik

def przywitanie():
    print "Pozdrowienia z mojej funckji!"

def przywitanie_imienne(imie, zyczenia):
    print "Witaj", imie, ". Zycze ci", zyczenia

# brak argumentow i zwracanej wartosci
przywitanie()

# brak zwracanej wartosci, ale sa juz argumenty
przywitanie_imienne("Jacek", "zdrowia")

# jak przypisac zmiennej wartosc zwrocona przez funkcje
x = dzielenie(9, 3)
print x


'''

#klasy
#obiekty  


class MojaKlasa:
      zmienna = "blah"
      def funkcja(self):
           print("To jest wiadomość wewnątrz klasy.")

mojobiekt = MojaKlasa()
mojobiekt.zmienna = "ple"
print(mojobiekt.zmienna)

mojobiekt.funkcja()

#===========================================
#gotowa klasa Pojazd

class Pojazd:
    nazwa = ""
    rodzaj = "auto"
    kolor = ""
    wartosc = 100.00
    def opis(self):
        napis_opisu = "%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return napis_opisu

# Ponizej umiesc swoj kod
Auto1 = Pojazd()
Auto1.nazwa = "VW"
Auto1.kolor = "czerwony"
Auto2 = Pojazd()

# sprawdzenie kodu
print(Auto1.opis())
print(Auto2.opis())


#=============================================================
#słowniki
kontakty = {}
kontakty["Jan"] = 938477566
kontakty["Jacek"] = 938377264
kontakty["Janusz"] = 947662781

#ala tablice asocjacyjne

kontakty = {
    "Jan" : 938477566,
    "Jacek" : 938377264,
    "Janusz" : 947662781
}

#for imie, numer in kontakty.iteritems():
#    print("%s ma numer telefonu: %d" % (imie, numer))

for imie in kontakty:
    print("%s ma numer telefonu: %d" % (imie, kontakty[imie]))
    
'''
del ksiazkatelef["Jan"]
#usuwanie elementu
ksiazkatelef.pop("Jan")
'''

kontakty = {
    "Bartek" : 938477566,
    "Monika" : 938377264,
    "Kamila" : 947662781
}

# miejsce na twoj kod
kontakty["Jakub"]=938273443
kontakty.pop("Kamila")


# sprawdzenie poprawnosci koadu
if "Jakub" in kontakty and kontakty["Jakub" ] == 938273443:
    print("Jakub jest w kontaktach.")
    print("Jego numer to ", kontakty["Jakub"], ".")
if "Kamila" not in kontakty:
    print("Kamili nie ma w kontaktach.")


#======================================================
# moduły i pakiety
# moduły - pliki .py z zestawem funkcji
# import
'''
wbudowane moduły
http://docs.python.org/2/library/
wczytuje tylko raz moduł

moduł urllib - czyta dane URL

import urllib
uzycie
urllib.urlopen(...)

przeglądanie zawartości modułów
dir
help

import urllib
dir(urllib)

jak znajdziemy funkcję to info

help(urllib.urlopen)

===================================
własne moduły

plik z .py i nazwa jaką chcemy

---------------------------------------------
pakiety to przestrzenie nazw - moga zawierać wiele modułów i innych pakietów
foldery ze znakiem szczególnym

kazdy pakiet musi nmieć plik __init__.py   niepusty 

folder foo - jak nazwa pakietu
i tam moduł bar.py 
dodajmy plik __init__.py wewnątrz foo

import goo.bar - i możemy używać moduł goo.bar
(tutaj odwołanie foo.bar)
albo 
from foo import bar
(a tutaj tylko bar)


w pliku __init__.py
aby moduł był niewidoczny z zewnątrz
nadpisać zmienną __all__

__init__.py:

__all__ = ["bar"]

posortowana alfabetycznie lista wszystkich funkcji modułu re
która zawiera słowo find

'''

import re
for funkcja in dir(re):
    if funkcja.count("find")>0:
        print(funkcja)



import re
tablica = []
for funkcja in dir(re):
    if funkcja.count("find"):
        tablica.append(funkcja)
print(tablica)




'''
Listy skladane

nowa tablica na podstawie innej

'''

napis = 'Odwazny rudy lis przeskoczyl nad spiacym wilczurem'
slowa = napis.split() # tworzymy tablice ze slowami zawartymi w napisie
dlugosc_slow = []
for slowo in slowa:
    if slowo != 'nad':
        dlugosc_slow.append(len(slowo))

print(dlugosc_slow)

#--------------------------------
#prościej przez listy składane
napis = 'Odwazny rudy lis przeskoczyl nad spiacym wilczurem'
slowa = napis.split()
dlugosc_slow = [len(slowo) for slowo in slowa if slowo != 'nad']
#dlugosc_slow = [len(slowo) for slowo in slowa] #dla wszystkich

print(dlugosc_slow)

#mapowanie elementów na inne !!!!!!!!

'''
Z pomocą listy składanej stwórz nową tablicę nowa 
na podstawie tablicy liczby. nowa ma się składać 
z całkowitych części nieujemnych liczb tablicy liczby. 
Wskazówka: liczbę rzeczywistą możemy zaokrąglić do całkowitej 
za pomocą int(), np.: int(4.3) da nam 4.
'''
liczby = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

nowa = [ int(liczba) for liczba in liczby if liczba>=0]

print(nowa)

'''
funkcje o zmiennej liczbie argumentów


def funkcja(pierwszy, drugi, trzeci):
    # robi cos z trzema argumentami
    ...


def foo(pierwszy, drugi, trzeci, *reszta):
    print "Pierwszy: %s" % pierwszy
    print "Drugi: %s" % drugi
    print "Trzeci: %s" % trzeci
    print "I cala reszta... %s" % list(reszta)

zmianna liczba argumentów!!!!!!!!!!!
'''
def foo(pierwszy, drugi, trzeci, *reszta):
    print("Pierwszy: %s" % pierwszy)
    print("Drugi: %s" % drugi)
    print("Trzeci: %s" % trzeci)
    print("I cala reszta... %s" % list(reszta))
foo("a","b","c","d","e","f","g","h","i","j")


'''
przekazywanie przez słowa kluczowe - nie ma znaczenia kolejność argumentów
'''

def funkcja(pierwszy, drugi, trzeci, **opcje):
    if opcje.get("akcja") == "dodaj":
        print("Suma to: %d" % (pierwszy + drugi + trzeci))

    if opcje.get("zwroc") == "pierwszy":
        return pierwszy

wynik = funkcja(1, 2, 3, akcja = "dodaj", zwroc = "pierwszy")
print("Wynik: %d" % wynik)

print("*"*20)
#====================================================
'''
Napisz funkcje "foo" i "bar" tak, aby mogły otrzymywać zmienną liczbę 
argumentów (3 lub więcej). Funkcja foo musi zwracać liczbę 
dodatkowych argumentów jakie otrzymała. Funkcja bar musi zwracać 
True, jeśli argument przypisany słowu kluczowemu magiczna_liczba 
jest równy 7, oraz False w przeciwnym razie.
'''
# zmien funkcje ponizej
def foo(a, b, c, *opcje):
    return list(opcje)

def bar(a, b, c, **opcje):
    return opcje.get("magiczna_liczba") == 7


# test kodu
if foo(1,2,3,4) == 1:
    print("Dobrze.")
if foo(1,2,3,4,5) == 2:
    print("Lepiej.")
if bar(1,2,3,magiczna_liczba = 6) == False:
    print("Bardzo dobrze.")
if bar(1,2,3,magiczna_liczba = 7) == True:
    print("Doskonale!")

'''
regularne wyrażenia

moduł re


'''
import re

tekst = """Wyobraz sobie, ze ten tekst zawiera numer
PIN 9434 twojej karty do bankomatu, a ty wlasnie go
zapomniales. 8888 Jak szybko go odnalezc?"""

#4cyfry
#r przed ciągiem wyłącza normalne dormatowanie znaku \ escape
sciezka = r'\d\d\d\d'
dopasowanie = re.search(sciezka, tekst)
#zwraca specjalny obiekt Match

if dopasowanie: #Sprawdzamy czy udalo sie cos znalezc
    numer = dopasowanie.group()
    print(numer)

'''
r"^(From|To|Cc).*?python-list@python.org"
^ poczatek
| alternatywa
.*? wiele znaków (z wyjątkiem \n) - dopasowanie niezachłanne do najmniejszej liczby znaków
. kazdy znak
* powtorzenie ? niezachłanne



# przyklad
import re
# Ponizej jest dokonywana lekka optymalizacja naszego wyrazenia
pattern = re.compile(r"\[(on|off)\]")

# Teraz szukamy
re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")
# Zwroci obiekt Match
re.search(pattern, "Nada...:-(")
# Nic nie zwroci
# koniec przykladu

# Cwiczenie: skonstruj wyrazenie odpowiadajace adresowi email

def test_email(twoje_wyrazenie):
    wyrazenie = re.compile(twoje_wyrazenie)
    adresy = ["john@example.com", "python-list@python.org", '"wha.t.`1an?ug{}ly@email.com"']
    for adres in adresy:
        if not re.match(wyrazenie, adres):
            print "Nie udalo ci sie przyporzadkowac %s" % (adres)
        elif not twoje_wyrazenie:
            print "Nie wprowadziles wyrazenia do funkcji test_email"
        else:
            print "Dobrze"

wyrazenie = r"" # Tu wpisz swoje wyrazenie
test_email(wyrazenie)


http://www.ex-parrot.com/pdw/Mail-RFC822-Address.html
Mail::RFC822::Address: regexp-based address validation


'''

'''
wyjątki
błędy
try catch

20 liczb - gdy brak danych to zastap daną jkako 0
obsługa 

for i in range(20):
    try:
        rob_cos_z_tablica(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
        rob_cos_z_tablica(0)




'''



print("="*30)
'''
zbiory
zbiór set tablica bez powtarzajacych elementow
tylko jeden raz

'''
print( set("jego imie to Eryk i Eryk jest jego imieniem".split()) )



A = set(["Jake", "John", "Eric"])
B = set(["John", "Jill"])

#czesc wspolna
print(A.intersection(B)) # set(['John'])
print(B.intersection(A)) # set(['John'])

#osoby ktore brały udział tylko w jednym spotkaniu
print(A.symmetric_difference(B)) # set(['Jill', 'Jake', 'Eric'])
print(B.symmetric_difference(A)) # set(['Jill', 'Jake', 'Eric'])

#Wyodrębnieniu osób, które brały udział w A i nie brały w B, służy różnica zbiorów difference:
print(A.difference(B)) # set(['Jake', 'Eric']
print(B.difference(A)) # set(['Jill'])


#suma zbiorow
print(A.union(B)) # set(['Jill', 'Jake', 'John', 'Eric'])


'''
funckje czesciowe

Czasami w swoim programie wielokrotnie wywołujemy pewną funkcję z tymi samymi argumentami. Aby skrócić zapis w takich sytuacjach, stosujemy funkcje częściowe. Najpierw musimy je zaimportować z odpowiedniej biblioteki.

from functools import partial

def mnozenie(x, y):
    return x * y

podwojenie = partial(mnozenie, 2)

print podwojenie(6)  # 12
print podwojenie(11) # 22
print podwojenie(7)  # 14

'''

print("This line will be printed.")


#wcięcia
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

#numbers:  integer float complex zespolone   
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)


mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)
#łatwiej dodaje się apostrofy przy ""

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)
#przypisywanie do wielu zmiennych

#nie można mixować dodawania liczb i tekstu


'''
# change this code
mystring = None
myfloat = None
myint = None

mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

'''

#listy
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

mylist = [1,2,3]
print(mylist[1])

'''
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
'''

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)


'''
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
'''

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#formatowanie tekstu    
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)
#rzutowanie na tekst

'''
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
'''

astring = "Hello world!"
astring2 = 'Hello world!'



astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

#--------------------
astring = "Hello world!"
print(astring.index("o"))

#gdzie jest o => 4  01234

astring = "Hello world!"
print(astring.count("l"))
#liczba o =>3

astring = "Hello world!"
print(astring[3:7])
#slice string
#-3 trzeci od końca

astring = "Hello world!"
print(astring[3:9:2])
#co 2 litere   [start:stop:step]

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])
# to samo

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

print("*"*20)
astring = "Hello world!"
print(astring[:])
print(astring[::2])  #co 2 litera

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))


astring = "Hello world!"
afewwords = astring.split(" ")

'''
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

'''

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

#=============================================================
#     
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

'''
if <statement is="" true="">:
    <do something="">
    ....
    ....
elif <another statement="" is="" true="">: # else if
    <do something="" else="">
    ....
    ....
else:
    <do another="" thing="">
    ....
    ....
</do></do></another></do></statement>
'''

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

#operator is
#identyczność
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False        

print(not False) # Prints out True
print((not False) == (False)) # Prints out False



