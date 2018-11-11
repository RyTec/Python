#-------------------------------------------------------------------------------
# Name:        KartyaJatek.py
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
            rand_item = self.items[random.randrange(len(self.items))]
            self.lapid = self.items.index(rand_item)
            self.lap.remove(rand_item)
            print("ennyi lap maradt: ", len(self.lap))
            if len(self.lap) == 0:
                print("---------------------------------")
            else:
                return self.lapid
        else:
            return None

jatek = KartyaJatek()
jatek.kever()
ii = 52
for n in range(ii):
    c = jatek.huz()
    if c == None:
        print("Vége a játéknak")
    else:
        ii -= 1
        print (n+1,". húzás ", jatek.kartya_neve(c))
        print("---------------------------------")
