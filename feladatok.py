def szam_jegye(szam: int):
    """2. írj metódust, mely a paraméterében kapott számról megmondja,
        h hání 1-es, 10-es, 100-as, 1000-es, stb van benne
        használd hozzá az egész osztás operátorát - //
        pl: 123//10 = 12  123%10=3 """

    print("azám: ", szam)
    """hogy kapjuk meg az utso szamjegyet?"""
    while (szam<9):
        print("következő számjegy", szam%10)
        szam = szam //10
        print("Az aktuális szám ", szam)

    print("az utolsó számjegy ", szam)
def szam_szamjegye2 (szam:int):
    szoveg_szam:str=str