#m
from math import *
from random import *
try:
    päev=int(input("Mis päev ja mitu tundi täna on ?"))
    if  päev==1:
        n="Esmaspäev"
        n="6 tundi"
    elif päev==2:
        n="Teisipäev"
        n="8 tundi"
    elif päev==3:
        n="kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="Nelijapäev"
        n="5 tundi"
    elif päev==5:
        n="Reede"
        n="7 tundi"
    elif päev==6:
        n="Laupäev"
        n="0 tundi"
    elif päev==7:
        n="Pühapäev"
        n="0 tundi"
    else:
        n="vale number"
    print(n)
except:
    print("!!!!!")
#V 13/12/12
print("Sisselogimine tahvel")
try:
    vanus=int(input("kui vana sa oled"))
    if vanus>=18:
        print("Kas te annate vanematele loa oma Tahvelt vaadata?")
        o=(input("Jah või ei. "))
        if o.lower()=="jah":
            print({o})
            print("See on ligipääs teie vanematele.")
            print("Tahvel on kinni.")
        elif o.upper()=="EI":
             print("Sissepääs puudub.")
             print("Tahvel on kinni.")
    if vanus<18:
        print("Juurdepääs vanematele on automaatselt antud.")
except:
    print("Tahvel on kinni.")
print()
print()



#12 (4)
from math import *
from random import *
print("распорядок дня")

try:
    kell=int(input("mis kell "))
    if kell==(0):
        print(f"kodus")
    elif kell==(1):
        print("просыпаюсь")
    elif kell==(2):
        print("чищю зубы")
    elif kell==(3):
        print("дклвю заряду")
    elif kell==(4):
        print("иду гулять")
    elif kell==(5):
        print("пришол домой")
    elif kell==(6):
        print("чищю зубы")
    elif kell==(7):
        print("иду гулять")
    elif kell==(8):
        print("гуляю")
    elif kell==(9):
        print("играю с друзьями")
    elif kell==(10):
        print("иду в магазин")
    elif kell==(11):
        print("купил еды")
    elif kell==(12):
        print("иду домой")
    elif kell==(13):
        print("чищю зубы")
    elif kell==(14):
        print("сплю")
except:
        print("!!!")


#12 (1)
from math import *
from random import *
print("koogi retsept")
try:
    if toiduvalmistamise==(0):

    elif toiduvalmistamise==(1):
        print("koostisosade lisamine")
    elif toiduvalmistamise ==(2):
        print("яйца 4 шт ")
    elif toiduvalmistamise==(3):
        print("мука 120 г ")
    elif toiduvalmistamise==(4):
        print("сахар 120 г ")
    elif toiduvalmistamise==(5):
        print("разрыхлитель 1 ч.л. ")
    elif toiduvalmistamise==(6):
        print("какаопорошок 1,5 ст.л.")
    elif toiduvalmistamise==(7):
        print("банан 3 шт. ")
    elif toiduvalmistamise==(8):
        print("сметана 1 большая банка ")
    elif toiduvalmistamise==(9):
        print("peale koostisosade lisamist segame ja lisame ainele uusi koostisosi")
    elif toiduvalmistamise==(10):
        print("küpsetamine ahjus ")
    elif toiduvalmistamise==(11):
        print("valmis! ") 
    toiduvalmistamise=int(input("mis staadiumis "))
except:
        print("!!!")



