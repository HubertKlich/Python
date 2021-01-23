import requests
from bs4 import BeautifulSoup

class Rodzic:
    def __init__(self, imie,nazwisko):
        self.imieRodzica=imie
        self.nazwiskoRodzica=nazwisko
    def rodzicdziecka(self):
        print("Imię rodzica:", self.imieRodzica)
        print("Nazwisko rodzica:", self.nazwiskoRodzica)
class Dziecko(Rodzic):
    def __init__(self, imieDziecko):
        super().__init__(imieRodzica,nazwiskoRodzica)
        self.imieDziecka = imieDziecko
    def dziecko(self):
        print("Imie dziecka:", self.imieDziecka)
        print("Nazwisko dziecka:", self.nazwiskoRodzica)

class Wyszukiwarka:
    def __init__(self, adres, slowo):
        self.url=adres
        self.slowo=slowo
        self.html_text = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_text, 'html.parser')
    def wyszukaj(self):
        for link in self.soup.find_all('html'):
            if(link.get('lang')=="pl"):
                print("Znaleziono jezyk polski")
            else:
                print("Nieznaleziono jezyka polskiego")
    def szukanie_slowa(self):
        powtorzenie=False
        print("Na stronie wystepuje tyle slow \""+self.slowo+"\":"+str(self.soup.text.count(self.slowo))+"\nCzy chcesz ponowic szukanie innego slowa?[T/N]")
        if input() == "T":
            print("Podaj jakiego slowa szukasz:")
            slowoDoWyszukania = input()
            Wyszukiwarka(adresStrony, slowoDoWyszukania).szukanie_slowa()
    def calytekst(self):
        print("Czy chcesz zobaczyc caly tekst strony?[T/N]:")
        if input() == "T":
            print(self.soup.text)

print("Podaj adres strony internetowej:")
adresStrony=input()
if not adresStrony.startswith("www."):
    adresStrony = "http://www." + adresStrony
if not adresStrony.startswith("http://" or "https://"):
    adresStrony = "http://" + adresStrony
print("Trwa laczenie z adresem: "+adresStrony)

print("Podaj jakiego slowa szukasz:")
slowoDoWyszukania=input()
Wyszukiwarka(adresStrony,slowoDoWyszukania).wyszukaj()
Wyszukiwarka(adresStrony,slowoDoWyszukania).szukanie_slowa()
Wyszukiwarka(adresStrony,slowoDoWyszukania).calytekst()



print("Podaj imie rodzica:")
imieRodzica=input()
print("Podaj nazwisko rodzica:")
nazwiskoRodzica=input()
print("Podaj imie dziecka:")
imieDziecka=input()
Rodzic(imieRodzica,nazwiskoRodzica).rodzicdziecka()
Dziecko(imieDziecka).dziecko()