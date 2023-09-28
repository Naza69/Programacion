#Ejercicio 1
x=0
while x<=30:
    x+=1
    if x==15:
        print(f"The value of the loop is {x}")
        print(f"The execution of the loop was broken when x was {x}")
        break
    if x==4 or x==6 or x==10:
        print(f"The value of {x} was skipped")
        continue
    print(f"The value of the loop is {x}")
#Ejercicio 1.1
phrase="hola"
while phrase!="":
    phrase=input("Ingrese una cadena")
    print(phrase.upper())
#Ejercicio 2
binnacle=[]
bankaccount=5000
choice="0"
while choice!="":
    choice=input("1)Deposito\n"
                        "2)Retiro\n"
                        "Ingrese el numero de operacion que quiere realizar\n")
    if choice=="1":
        downpayment=int(input("Ingrese el valor a depositar\n"))
        bankaccount+=downpayment
        paymentaux="D "+str(downpayment)
        binnacle.append(paymentaux)
    elif choice=="2":
        withdraw=int(input("Ingrese el dinero a retirar\n"))
        bankaccount-=withdraw
        withdrawaux="R "+str(withdraw)
        binnacle.append(withdrawaux)
    elif (choice!="1" or choice!="2") and choice!="":
        print("El valor ingresado no corresponde con ninguna operacion disponible")
print("\n".join(binnacle), f"\nTotal en cuenta: {bankaccount}")
#Ejercicio 3
number=1
primenumbers=[]
while number!=0:
    number=int(input("Ingrese un numero\n"))
    dividerscounter=0
    for z in range(number, 0, -1):
        if number%z==0:
            dividerscounter+=1
    if dividerscounter<=2 and number!=0:
        primenumbers.append(str(number))
print("Los numeros primos ingresados fueron", ", ".join(primenumbers))
#Ejercicio 4
while True:
    firstyear=int(input("Ingrese el primer año\n"))
    secondyear=int(input("Ingrese el segundo año\n"))
    if(isinstance(firstyear, int) and isinstance(secondyear, int)):
        if firstyear<secondyear:
            for year in range(firstyear, secondyear, 1):
                if (year%4==0 and year%100!=0) or year%400==0:
                    print(year, "es bisiesto")
                elif year%10==0:
                    print(year, "es multiplo de 10")
        elif firstyear>secondyear:
            for year in range(secondyear, firstyear, 1):
                if (year%4==0 and year%100!=0) or year%400==0:
                    print(year, "es bisiesto")
                elif year%10==0:
                    print(year, "es multiplo de 10")
        elif firstyear==secondyear:
            print("ERROR, los años son iguales\n"
                "Vuelva a ingresar los años")
            continue
        else:
            print("ERROR, alguno de los valores ingresados no es un numero entero,\n"
                "y por tanto no coincide con un/los año/s del calendario gregoriano\n"
                "Vuelva a ingresar los años")
            continue
        choice=input("Quiere hacerlo de vuelta?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            print("Respuesta invalida, vuelva a ingresar su eleccion, (Si o No)")
            choice=input()
            if choice.lower()=="si":
                break
            elif choice.lower()=="no":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    else:
        print("ERROR, alguno de los valores ingresados no es un numero entero,\n"
            "y por tanto no coincide con un/los año/s del calendario gregoriano\n"
            "Vuelva a ingresar los años")
        continue
#Ejercicio 5
for number in range(1, 20+1, 1):
    if number%2!=0:
        continue
    else:
        print(number)
#Ejercicio 6
numberlist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
especificnumber=7
for found in numberlist:
    if found==especificnumber:
        print("Numero encontrado!")
        break
#Ejercicio 7
while True:
    choice=input("1) Revivir a Rosas\n"
                "2) Reconsquistar Constantinopla y revivir el imperio bizantino\n"
                "3) Impedir el surgimiento de FUCA\n"
                "4) Ponerle unipox a las costuras de Pangea\n"
                "5) Robar los documentos mas secretos de la CIA y publicarlos\n"
                "Eliga una de las opciones!\n")
    if choice=="1":
        print("Usted ha elegido:\n"
            "1) Revivir a Rosas\n"
            "La confederacion Argentina ha vuelto y ha entrado en una cruenta guerra con las naciones del pacifico sur.")
        choice=input("Quiere elegir de nuevo?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            print("Respuesta invalida, vuelva a ingresar su eleccion, (Si o No)")
            choice=input()
            if choice.lower()=="si":
                break
            elif choice.lower()=="no":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    elif choice=="2":
        print("Usted ha elegido:\n"
            "2) Reconsquistar Constantinopla y revivir el imperio bizantino\n"
            "Tiene en sus manos a Constantinopla de nuevo, y con ella casi toda Europa tambien.")
        choice=input("Quiere elegir de nuevo?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            print("Respuesta invalida, vuelva a ingresar su eleccion, (Si o No)")
            choice=input()
            if choice.lower()=="si":
                break
            elif choice.lower()=="no":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    elif choice=="3":
        print("Usted ha elegido\n"
            "3) Impedir el surgimiento de FUCA\n"
            "Es el año 2023, la tierra es una roca mas del universo, vacia, sin vida.")
        choice=input("Quiere elegir de nuevo?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            print("Respuesta invalida, vuelva a ingresar su eleccion, (Si o No)")
            choice=input()
            if choice.lower()=="si":
                break
            elif choice.lower()=="no":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    elif choice=="4":
        print("Usted ha elegido:\n"
            "4) Ponerle unipox a las costuras de Pangea\n"
            "Es el año 2023, la tierra esta unida bajo la tutela de un unico gobierno, no hay guerras, todo es utopico.")
        choice=input("Quiere elegir de nuevo?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            print("Respuesta invalida, vuelva a ingresar su eleccion, (Si o No)")
            choice=input()
            if choice.lower()=="si":
                break
            elif choice.lower()=="no":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    elif choice=="5":
        print("Usted ha elegido:\n"
            "5) Robar los documentos mas secretos de la CIA y publicarlos\n"
            "Eres la persona mas buscada por el gobierno norteamericano hasta el momento, hay conmociones mundiales,\n"
            "protestas, manfiestaciones, revoluciones, miles de inovaciones tecnologicas; EEUU se sume en una guerra civil\n"
            "sin precedentes.")
        choice=input("Quiere elegir de nuevo?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            print("Respuesta invalida, vuelva a ingresar su eleccion, (Si o No)")
            choice=input()
            if choice.lower()=="si":
                break
            elif choice.lower()=="no":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    else:
        print("Respuesta no correspondiente con las opciones dadas,\n"
            "ingrese su eleccion de nuevo porfavor")
        continue

