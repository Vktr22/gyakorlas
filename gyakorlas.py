import random
import math
"""
véletlen számok generálása
"""
def veletlen():
    """[10,30] közötti véletlen szamokat generáljunk"""
    i:int = 0
    while i < 10:
        szam: int = math.floor(random.random()*21 +10)
        print(szam, end=" ")
        i+=1

"""
1. Generálj 5 véletlen lottószámot
[1,90]

2. Generálj 1 véletlen kétjegyű egész számot
    döntsd el róla, hogy páros, v páratlan
    
3. Generálj 15db egész számot [0,1] között
hány egyest generáltál?

4. Generálj egy véletlen számot 1 és 10 között
szorozd meg 3-al
vonj ki belőle 15-öt
oszd el 6-tal
szorozd be 2-vel
vond ki belőle az eredeti számot
a program írja ki, h az eredmény egyenlő e 5-el

5. Írj metódust, mely a paraméterében kapott szövegnek kiírja a hosszát.
Az ötödik karakterét nagybetűvel
"""

def lottoszam():
    i:int = 0
    while i < 5:
        szam: int = math.floor(random.random()*21)
        print(szam, end=" ")
        i+=1
    print(" ")

def ketjegyu():
    i:int = 0
    while i < 1:
        szam: int = math.floor(random.random()*90+10)
        """if szam<10:
            szam*10
        elif szam==0:
            i:int = 0"""
        print(szam, end=" ")
        i+=1
    if szam % 2 == 0:
        print("a szám páros")
    else:
        print("A szám páratlan")

def tizenotegesz():
    i:int = 0
    while i < 15:
        szam: int = math.floor(random.random()*)
        print(szam, end=" ")
        i+=1