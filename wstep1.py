//1
x = """Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz
w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez 
nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków 
później zaczął być używany przemyśle elektronicznym, pozostając praktycznie 
niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy 
Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne 
wersje Lorem Ipsum oprogramowaniem 
przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"""

//2
print("W tekscie jest {0} liter r oraz {1} liter i".format(x.count('r'), x.count('i')))

//4
print(dir(x))
help(x.isspace)

//5
print("Patryk Piotrowski"[::-1])

//6
lista_cyfry=list(range(1,11))
print(lista)
index = lista_cyfry.index(6)
lista_stara=lista_cyfry[:index]
lista_nowa=lista_cyfry[index:]
print(lista_stara)
print(lista_nowa)

//7
lista=lista_stara+lista_nowa
print(lista_cyfry)
lista.insert(0,0)
print(lista)
kopia=lista[:]
kopia.sort(reverse=True);
print(lista_cyfry)
print(kopia)

//8
krotka=((136099, 'Patryk Piotrowski'),(123456,'Kubus Puchatek'))
print(krotka)

//9
slownik=dict(krotka)
print(slownik)
slownik={
	136099:{
		"imie": "Patryk",
		"nazwisko" : "Piotrowski",
		"wiek": 24,
		"mail": "mail@mail.com",
		"rok": 1996,
		"adres":"Olsztyn"},

	123456:{
		"imie": "Kubus",
		"nazwisko" : "Puchatek",
		"wiek": 7,
		"mail": "mail2@mail.com",
		"rok": 2013,
		"adres":"Stumilowy Las"}
	}

//10
numer_telefonu=[
	"123456789","123456789", "123456789",
	"123456789", "123456789", "123456789"]
print(numer_telefonu)
numer_telefonu=set(numer_telefonu)
print(numer_telefonu)

//11
print("1 -> 10")
for y in range(1,11):
	print(y)




