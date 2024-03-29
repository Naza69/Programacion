#Ejercicio 1
city_list = ['Buenos Aires', 'Nueva York']
lista_pasajeros = []
def add_passenger():
    nombre = input('Ingrese el nombre del pasajero:\n')
    dni = input('Ingrese el DNI del pasajero:\n')
    ciudad_destino = input('Ingrese la ciudad de destino del pasajero:\n')
    pais_destino = input('Ingrese el país de destino del pasajero:\n')
    lista_pasajeros.append((nombre, dni, ciudad_destino, pais_destino))
    city_list.append((ciudad_destino, pais_destino))
def add_city():
    print(city_list)
    ciudad = input('Ingrese la ciudad que desea agregar:\n')
    city_list.append(ciudad)
def find_city_by_dni():
    dni_busqueda = input('Ingrese el DNI que desea buscar para saber a qué ciudad viajará el pasajero:\n')
    for pasajero in lista_pasajeros:
        if dni_busqueda == pasajero[1]:
            print(f'El pasajero viajará a la ciudad de {pasajero[2]}.')
            return
    print('Pasajero no encontrado.')
def count_passengers_by_city():
    count = 0
    ciudad_busqueda = input('Ingrese la ciudad que desea buscar para saber cuántos pasajeros viajarán a ella:\n')
    for pasajero in lista_pasajeros:
        if pasajero[2] == ciudad_busqueda:
            count += 1
    print(f'{count} pasajeros viajarán a {ciudad_busqueda}')
def find_country_by_dni():
    dni_busqueda = input('Ingrese el DNI del pasajero para saber a qué país viajará:\n')
    for pasajero in lista_pasajeros:
        if dni_busqueda == pasajero[1]:
            print(f'El pasajero viajará al país de {pasajero[3]}.')
            return
    print('Pasajero no encontrado.')
def count_passengers_by_country():
    count = 0
    pais_busqueda = input('Ingrese el país que desea buscar para saber cuántos pasajeros viajarán a él:\n')
    for pasajero in lista_pasajeros:
        if pasajero[3] == pais_busqueda:
            count += 1
    print(f'{count} pasajeros viajarán a {pais_busqueda}')
while True:
    print("Bienvenido al menú de Agencias de Turismo Fioretti:")
    print("Opciones:")
    print("[1] Agregar pasajeros a la lista de viajeros")
    print("[2] Agregar ciudades a la lista de ciudades")
    print("[3] Dado el DNI de un pasajero, ver a qué ciudad viaja")
    print("[4] Dada una ciudad, mostrar la cantidad de pasajeros que viajan a ella")
    print("[5] Dado el DNI de un pasajero, ver a qué país viaja")
    print("[6] Dado un país, mostrar cuántos pasajeros viajan a ese país")
    print("[7] Salir del programa")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        add_passenger()
    elif opcion == '2':
        add_city()
    elif opcion == '3':
        find_city_by_dni()
    elif opcion == '4':
        count_passengers_by_city()
    elif opcion == '5':
        find_country_by_dni()
    elif opcion == '6':
        count_passengers_by_country()
    elif opcion == '7':
        print("¡Hasta luego!")
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción válida.')
#Ejercicio 2
def listdomains(billlist):
    domdic={}
    for tuple in billlist:
        domlocal=tuple[3]
        namelocal=tuple[0]
        domdic[namelocal]=domlocal
    return domdic
listcualquiera=[("Naza", 5, 700.50, "Oscarguiñazu 311")]
alldic=listdomains(listcualquiera)
for pasiv in alldic.items():
    print(f"Hay que pagarle a {pasiv}")
#Ejercicio 3
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

