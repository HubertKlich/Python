import re
import subprocess
from subprocess import Popen, PIPE, STDOUT, call
import pytest
import sys
import numpy as np

class pytest:
#pytest
    def f(x):
        return x+1
    def test_mytest(self):
        assert self.f(6)==7
    def sprawdzenie(self):
        pytest.mark.skipif("f(6)>=5",reason="Pominiecie")
        assert self.f(6)==5
    def sprawdzenie2(self):
        pytest.mark.xfail("f(6)>=5",reason="Pominiecie")
        assert self.f(5) == 4
    def sprawdzenie3(self):
        pytest.mark.fail("f(6)>=5",reason="Pominiecie")
        assert self.f(4)== 3
    def sprawdzenie3(self):
        pytest.mark.xpass("f(6)>=5",reason="Pominiecie")
        assert self.f(3)== 2
    def test_mytest2(self):
        assert self.f(6)==9

class zwykle:
#zwykleoperacje
    def __init__(self,nazwa):
        self.nazwa=nazwa
    def tekst(self):
        fh = open('demo.txt', 'w')
        fh.write(self.nazwa)
        fh = open('demo.txt', 'r')
        print(fh.read())
        fh.close()
        if fh.closed:
            print("Do pliku demo.txt zapisano: " + self.nazwa)
        else:
            print("Zapis do pliku nieudany")

    def dzialanie(self):
        a=int(self.nazwa)*int(self.nazwa)
        print("Kwadrat tej liczby to:"+str(a))
class regex:
#regex
    def __init__(self, tekst):
        self.tekst = tekst
    def tekstpodzial(self):
        x=re.sub("\s","\n",self.tekst)
        print(x)
    def liczby(self):
        p=re.compile('\d')
        print(p.findall(self.tekst))
class subprocess:
#subprocess
    from subprocess import Popen, PIPE, STDOUT, call
    def __init__(self, tekst):
        self.tekst = tekst
    def sciezka(self):
        subprocess.call(self.tekst, shell=True)
    def ls(self):
        out=Popen([self.tekst],stderr=STDOUT,stdout=subprocess.PIPE)
        output=out.stdout.read()
        print(output)


class numpy:
#numpy
    def __init__(self, ilosc1, ilosc2, ilosc3):
        self.ilosc1 = ilosc1
        self.ilosc2 = ilosc2
        self.ilosc3 = ilosc3
    def funkcja1(self):
        a=np.array([self.ilosc1])
        print(a)
    def funkcja2(self):
        b=np.arange(int(self.ilosc1),int(self.ilosc2),int(self.ilosc3))
        print(b)
    def funkcja3(self):
        c=np.linspace(int(self.ilosc1),int(self.ilosc2),int(self.ilosc3))
        print(c)
    def funkcja4(self):
        d=np.random.randint(int(self.ilosc1))
        print(d)
class wybieranie:
    def opcja1(self):
        print("Podaj jakis tekst:")
        x = input()
        wartosci = zwykle(x)
        wartosci.tekst()
        menu()
    def opcja2(self):
        print("Podaj jakas liczbe:")
        x = input()
        wartosci = zwykle(x)
        wartosci.dzialanie()
        menu()
    def opcja3(self):
        print("Podaj jakis tekst do podzialu:")
        x = input()
        wartosci = regex(x)
        wartosci.tekstpodzial()
        menu()
    def opcja4(self):
        print("Podaj jakis tekst z liczbami:")
        x = input()
        wartosci = regex(x)
        wartosci.liczby()
        menu()
    def opcja5(self):
        print("Podaj jakas komende np.echo $HOME(Dzialanie call):")
        x = input()
        wartosci = subprocess(x)
        wartosci.sciezka()
        menu()
    def opcja6(self):
        print("Podaj jakas komende np.ls(Dzialanie Popen):")
        x = input()
        wartosci = subprocess(x)
        wartosci.ls()
        menu()
    def opcja7(self):
        print("Podaj jakies liczby po przecinku(ile chcesz):")
        x = input()
        wartosci = numpy(x, None, None)
        wartosci.funkcja1()
        menu()
    def opcja8(self):
        print("Podaj jakies 3 liczby po przecinku(1 to od ilu, 2 do ilu, 3 co ile ma byc przeskok):")
        x = input()
        p = re.split(r'\W+', x)
        wartosci = numpy(p[0], p[1], p[2])
        wartosci.funkcja2()
        menu()
    def opcja9(self):
        print("Podaj jakies 3 liczby po przecinku(1 to od ilu, 2 do ilu, 3 na ile czesci ma byc podzielony przedzial):")
        x = input()
        p = re.split(r'\W+', x)
        wartosci = numpy(p[0], p[1], p[2])
        wartosci.funkcja3()
        menu()
    def opcja10(self):
        print("Podaj do jakiego maksymalnego przedzialu ma zostac wylosowana liczba:")
        x = input()
        wartosci = numpy(x, None, None)
        wartosci.funkcja4()
        menu()
#Funkcja glowna
def numer(argument):
    switcher={
        0: lambda: quit(),
        1: lambda: wybieranie().opcja1(),
        2: lambda: wybieranie().opcja2(),
        3: lambda: wybieranie().opcja3(),
        4: lambda: wybieranie().opcja4(),
        5: lambda: wybieranie().opcja5(),
        6: lambda: wybieranie().opcja6(),
        7: lambda: wybieranie().opcja7(),
        8: lambda: wybieranie().opcja8(),
        9: lambda: wybieranie().opcja9(),
        10: lambda: wybieranie().opcja10()
    }
    return switcher.get(argument,lambda: print("Wybierz inna wartosc"))()
def cls():
    for x in range(80):
        print("\n")
def menu():
    print("\n"+"Wcisnij ENTER")
    p=input()
    if p=="":
        cls()
        print("MENU" + "\n" + "1) Wpisanie wartosci ktora podasz do pliku tekstowego"+ "\n" + "2) Obliczanie kwadratu liczby"+ "\n" + "3) Dzielenie tekstu na osobne linijki"+ "\n" + "4) Wyciaganie z tekstu cyfr"+ "\n" + "5) Wpisanie do konsoli komendy typu echo"+ "\n" + "6) Przedstawienie dzialania Popen"+ "\n" + "7) Wpisywanie liczby do macierzy jednowierszowej"+ "\n" + "8) Wypisywanie liczb z przedzialu co ktoras liczbe"+ "\n" + "9) Dzielenie przedzialu na dana ilosc czesci"+ "\n" + "10) Losowanie jakiejs liczby z danego przedzialu")
        x=input()
        numer(int(x))
menu()