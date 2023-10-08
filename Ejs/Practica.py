def choicefuckingok(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, ingrese si o no\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def capicuanumberbool(capicualocal):
    invcapicualocallist=list(reversed(str(capicualocal)))
    if str(capicualocal)=="".join(invcapicualocallist):
        return True
    else:
        return False
while True:
    try:
        capicua=int(input("Ingrese el numero que quiere saber si es capicua\n"))
        if capicuanumberbool(capicua)==True:
            print("El numero introducido es capicua!")
        else:
            print("El numero introducido no es capicua...")
        choice=input("Quiere volver a hacer el procedimiento?\n")
        if choicefuckingok(choice)==True:
            continue
        else:
            break
    except ValueError:
        print("El valor introducido no es entero, o no es numerico, intentelo de nuevo")
        continue