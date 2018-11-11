#-------------------------------------------------------------------------------
# Name:        KartyaJatek2.py
# Author:      RyTec
#
# Created:     03.11.2018
# Copyright:   (c) RyTec 2018
# Licence:     GPL
#-------------------------------------------------------------------------------
import random


class KartyaJatek:
    def __init__(self):
        self.lapok = []
        for i in range(4):
            for n in range(2,15,1):
                self.lapok.append([n, i],)

    def kartya_neve(self, lapszam):
        szam = [2,3,4,5,6,7,8,9,10,'Junge', 'Dáma', 'Király', 'Ász']
        szin = ['Kör', 'Káró', 'Treff', 'Pik']
        self.lapszam = lapszam-1
        if self.lapszam < 0:
            self.lapszam = 0
        self.llap = self.lapok[self.lapszam]
        return (szin[self.llap[1]], szam[self.llap[0]-2])

    def kever(self):
        self.lap = self.lapok
        random.shuffle(self.lap)


    def huz(self):
        self.items = self.lap
        if len(self.items) > 0 :
            laphuzas = self.items[0]
            self.lapid = self.items.index(laphuzas)
            self.lap.remove(laphuzas)
            if len(self.lap) == 0:
                print("---------------------------------")
            else:
                return self.lapid
        else:
            return None

jatek1 = KartyaJatek()
jatek2 = KartyaJatek()
jatek1.kever()
jatek2.kever()
ii = 52
a = 0
b = 0
for n in range(ii):
    c = jatek1.huz()
    cc = jatek2.huz()
    if c or cc == None:
        print("Vége a játéknak")
        if a > b:
            nyertes = "'a' játékos nyert"
        if b > a:
            nyertes = "'b' játékos nyert "
        print("A(z) ", nyertes, "!")
        print('Az "A" játkékos pontszáma:', a)
        print('Az "B" játkékos pontszáma:', b)
    else:
        ii -= 1
        print ("A játékos", n+1,". húzás ", jatek1.kartya_neve(c))
        print ("B játékos",n+1,". húzás ", jatek2.kartya_neve(cc))
        if jatek1.kartya_neve(c)[1] == 'Junge':
            kartya_ertek1 = 11
        elif jatek1.kartya_neve(c)[1] == 'Dáma':
            kartya_ertek1 = 12
        elif jatek1.kartya_neve(c)[1] == 'Király':
            kartya_ertek1 = 13
        elif jatek1.kartya_neve(c)[1] == 'Ász':
            kartya_ertek1 = 14
        else:
            kartya_ertek1 = jatek1.kartya_neve(c)[1]
            print(kartya_ertek1)

        if jatek2.kartya_neve(cc)[1] == 'Junge':
            kartya_ertek2 = 11
        elif jatek2.kartya_neve(cc)[1] == 'Dáma':
            kartya_ertek2 = 12
        elif jatek2.kartya_neve(cc)[1] == 'Király':
            kartya_ertek2 = 13
        elif jatek2.kartya_neve(cc)[1] == 'Ász':
            kartya_ertek2 = 14
        else:
            kartya_ertek2 = jatek2.kartya_neve(cc)[1]
            print(kartya_ertek2)

        if kartya_ertek1 < kartya_ertek2:
            b += 1
            nyertes = "-t a B játékos nyerte!"
            print('pontszáma:', b)
        elif kartya_ertek1 > kartya_ertek2:
            a += 1
            nyertes = "-t az A játékos nyerte!"
            print('pontszáma:', a)
        else:
            nyertes = ": döntetlen !"
        print("A kör", nyertes)
        print("---------------------------------")
