listasp=[]

def agg_ele_listasp():
    ne = int(input("quanti elementi vuoi inserire:"))
    for i in range(ne):
        ele = input()
        listasp.append(ele)

def vislistasp():
    print(listasp)

def rimele():
    ele = int(input("indice che vuoi rimuovere:"))
    if 0 <= ele < len(listasp):
        listasp.pop(ele)
    else:
        print("Indice non valido")


def contaelementi():
    for i in (listasp:
        print(i)    

def svuotalistap():
    listasp.clear()
    print("lista svuotata")

while True:
    print("1)aggiungi elemento alla lista")
    print("2)visualizza lista")
    print("3)rimuovi elemento dalla lista")
    print("4)esci")
    scelta = int(input("scegli un opzione:"))
    if scelta == 1:
        agg_ele_listasp()
    elif scelta == 2:
        vislistasp()
    elif scelta == 3:
        rimele()
    elif scelta == 4:
        break
    else:
        print("opzione non valida")

