import random

def elso():
    korrekt:bool=False
    szam:int
    while(korrekt==False):
        szam=int(input("Adjon meg egy páratlan számot: "))
        if(szam%2==1): korrekt=True

def elso2():
    szam=int(input("Adjon meg egy páratlan számot: "))
    while(szam%2==0):
        szam=int(input("Adjon meg egy páratlan számot: "))

def masodik():
    i:int=1
    ottel_oszthato:int=0
    while(i<=7):
        szam:int=int(random.random()*96+5)
        print(szam)
        if(szam%5==0): ottel_oszthato+=1
        i+=1
    print(f"A számok között {ottel_oszthato} db 5-el osztható van!")

def harmadik(text:str, betu:str):
    hany:int=0
    i:int=1
    while(i<=len(text)):
        if(text[i-1]==betu): hany+=1
        i+=1
    print(hany)

#def negyedik():
    



    


