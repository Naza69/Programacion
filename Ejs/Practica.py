def start():
    while True:
        try:
            choice=int(input("1) LLenar un diccionario con los socios\n"
                        "2) Ver cuantos socios tiene el club\n"
                        "3) Ver si un socio ha pagado lo que corresponde\n"
                        "4) Corregir fechas de ingreso al 14/03/2018\n"
                        "5) Dar de baja a un socio\n"
                        "6) Ver el listado de socios completo\n"
                        "7) Salir\n"))
            if choice!=7:
                opchoice(choice)
            else:
                break
        except ValueError:
            print("Valor ingresado no numerico, vuelva a intentarlo")
            continue
def opchoice(choicelocal):
    allascociate={}
    if choicelocal==1:
        allascociate=dict(firstchoice())
    elif choicelocal==2 and len(allascociate)>0:
        howmanyasociate=secondchoice(allascociate)
        print("El numero de asociados es de "+howmanyasociate)
    elif choicelocal==3 and len(allascociate)>0:
        numberasoc=int(input("Ingrese el numero del asociado que quiere verificar si pago o no la cuota\n"))
        if thirdchoice(allascociate, numberasoc)==True:
            print(f"El socio {numberasoc} esta al dia")
        else:
            print(f"El socio {numberasoc} todavia adeuda")
    elif choicelocal==4 and len(allascociate)>0:
        allascociate=fourthchoice(allascociate)
        print("Problema de la fecha solucionado")
    elif choicelocal==5 and len(allascociate)>0:
        asocname=input("Ingrese el nombre del socio que quiere eliminar\n")
        allascociate=fifthchoice(allascociate, asocname)
    elif choicelocal==6 and len(allascociate)>0:
        sixthchoice(allascociate)
    else:
        print("El valor ingresado no corresponde con ninguna opcion o\nprimero tiene que crear un diccionario para elegir las demas opciones")
def choicevealidation(choicelocal):
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
def firstchoice():
    asociatedic={}
    while True:
        sizelocal=int(input("Ingrese la cantidad de socios a registrar\n"))
        counter=0
        while counter<=sizelocal:
            asociate=input(f"Ingrese los datos del socio {counter} a cargar con esta estructura: nrosocio, nombre, fechaingreso, pagoonolacuota\n")
            counter+=1
            if len(asociate.split(", "))>4:
                print("Datos ingresados no correspondientes con la estructura dada, intentelo de nuevo")
                continue
            else:
                asociatedic[counter]=asociate
        choice=input("Quiere volver a repetir el procedimiento\n")
        if choicevealidation(choice)==True:
            continue
        else:
            break
    return asociatedic
def secondchoice(dicofasociates):
    return len(dicofasociates)
def thirdchoice(allasoclocal, asociate):
    validbill=list(allasoclocal[asociate].split(", "))
    if validbill[3].lower()=="cuota al dia":
        return True
    else:
        return False
def fourthchoice(dicofallasoc):
    for everyasoc in dicofallasoc.keys():
        if list(everyasoc.split(", "))[2]=="13/03/2018":
            correctdate=list(everyasoc.split(", "))
            correctdate[2]="14/03/2018"
            dicofallasoc[everyasoc]="".join(correctdate)
    return dicofallasoc
def fifthchoice(allasoc, namelocal):
    for asoc in allasoc.values():
        if asoc[0].lower()==namelocal.lower():
            del allasoc[asoc]
            print("Socio eliminado")
    return allasoc
def sixthchoice(allasociates):
    print("Listado completo de los socios:")
    for asociate in allasociates.items():
        print(asociate)
start()