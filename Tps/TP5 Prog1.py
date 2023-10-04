#Ejercicio 1
def booldni(dnilocal):
    if len(str(dnilocal))==7 or len(str(dnilocal))==8:
        return True
    else:
        return False
def repeat(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=("Respuesta invalida, intente nuevamente (Si o no)")
        if choicelocal.lower()=="si":
            break
        if choicelocal.lower()=="no":
            break
    if choicelocal.lower()=="si":
        return True
    else: 
        return False
while True:
    try:
        dni=int(input("Ingrese su DNI\n"))
        if booldni(dni)==True:
            print("Su Dni es correcto")
            choice=input("Quiere repetir el proceso?\n")
            if choice.lower()!="si" and choice.lower()!="no":
                repeat(choice)
            elif choice.lower()=="si":
                continue
            elif choice.lower()=="no":
                break
        else:
            print("Valor ingresado invalido, intente de nuevo")
            continue
    except ValueError:
        print("Valor ingresado invalido, intente de nuevo")
        continue
#Ejercicio 2
def choicenotok(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, intente de nuevo (Si o no)\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def longstring(stringlocal):
    liststrings=stringlocal.split(" ")
    for word in liststrings:
        if word==liststrings[len(liststrings)-1]:
            return len(word)
while True:
    string=input("Ingrese una frase\n")
    print(f"La longitud de la ultima palabra del string ingresado es {longstring(string)}")
    choice=input("Quiere repetir el proceso?\n")
    if choicenotok(choice)==True:
        continue
    else:
        break
#Ejercicio 3
def idenmember(namelocal, dnilocal):
    idlocal=namelocal.split(" ")[0]+str(len(namelocal.split()[1]))+str(dnilocal)[0]+str(dnilocal)[1]+str(dnilocal)[2]
    return idlocal
def addingcounter(counterlocal):
    counterlocal+=1
    return counterlocal
def dniok(dnilocal):
    if len(str(dnilocal))==7 or len(str(dnilocal))==8:
        return True
    else:
        return False
def nameok(namelocal):
    if len(namelocal.split(" "))==3:
        return True
    elif len(namelocal.split(" "))==2:
        return True
    else:
        return False
def choiceok(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta ingresada invalida, solo se acepta si o no\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def register(regislocal):
    counter=0
    while True:
        try:
            name=input("Ingrese el nombre del socio\n(Nombre Apellido o Nombre1 Nombre2 Apellido)\n")
            dni=int(input("Ingrese su DNI\n"))
            if nameok(name)==True and dniok(dni)==True:
                regislocal[name]=dni
                counter=addingcounter(counter)
                print(f"Su identificador es {idenmember(name, dni)}")
            elif nameok(name)==True and dniok(dni)==False:
                print("Dni ingresado incorrecto, intente de nuevo")
                continue
            elif nameok(name)==False and dniok(dni)==True:
                print("Nombre ingresado invalido, intente de nuevo")
                continue
            else:
                print("Los valores no corresponden con los requisitos para el registro, intente de nuevo")
                continue
            choice=input("Quiere seguir?\n")
            if choiceok(choice)==True:
                continue
            else:
                break
        except ValueError:
            print("El valor ingresado para el DNI no es numerico, intentelo de nuevo")
            continue
print("Bienvenido al The Bar, a continuacion ingresara el nombre y el DNI del socio a registrar")
regis={}
register(regis)
#Ejercicio 4
def choiceokey(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta ingresada invalido, solo se acepta si o no\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def inputs():
    while True:
        try:
            number=int(input("Ingrese el primer numero\n"))
            numbertwo=int(input("Ingrese el segundo numero\n"))
            if number%numbertwo==0:
                print(f"{number} es multiplo de {numbertwo}")
            elif numbertwo%number==0:
                print(f"{numbertwo} es multiplo de {number}")
            else:
                print("Los dos numeros ingresados no son multiplos entre si")
            choice=input("Quiere volver a repetir el procedimiento?\n")
            if choiceokey(choice)==True:
                continue
            else:
                break
        except ValueError:
            print("Alguno de los valores ingresados no es numerico, intente de nuevo")
            continue
inputs()
#Ejercicio 5
def avrtemp(tempminlocal, tempmaxlocal):
    avrtemplocal=(tempmaxlocal+tempminlocal)/2
    return avrtemplocal
def choiceifnotok(choicelocal):
    while choicelocal.lower()!="no" and choicelocal.lower()!="si":
        choicelocal=input("Respuesta invalida, solo se permite si o no")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def daysdegrees():
    while True:
        try:
            days=int(input("Ingrese la cantidad de dias de los que quiere calcular su media termica\n"))
            for every in range(days):
                tempmin=int(input(f"Ingrese la minima del dia {every}\n"))
                tempmax=int(input(f"Ingrese la maxima del dia {every}\n"))
                print(f"La media termica del dia {every} es {avrtemp(tempmin, tempmax)}")
            choice=input("Quiere volver a repetir el procedimiento?\n")
            if choiceifnotok(choice)==True:
                continue
            else:
                break
        except ValueError:
            print("Valor ingresado no valido o no numerico, intentelo de nuevo")
            continue
daysdegrees()
#Ejercicio 6
def choicehavetobeok(choicelocal):
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
def stringspacey(stringlocal):
    stringwithspace=[]
    for char in stringlocal:
        stringwithspace.append(char+" ")
    return "".join(stringwithspace)
while True:
    string=input("Ingrese la cadena de caracteres que quiere convertir a espaciado\n")
    print(f"La version espaciada de la cadena ingresada es <{stringspacey(string)}>")   
    choice=input("Quiere volver a repetir el procedimiento?\n")
    if choicehavetobeok(choice)==True:
        continue
    else:
        break
#Ejercicio 7
def choiceyeahok(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, solo se acepta si o no, intente de nuevo\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def greatest(numberlistlocal):
    greatestlocal=0
    for number in numberlistlocal:
        if number>greatestlocal:
            greatestlocal=number
    return greatestlocal
def leatest(leatestlocal, greatestlocal, numberlistlocal):
    leatestlocal=greatestlocal
    for number in numberlistlocal:
        if number<leatestlocal:
            leatestlocal=number
    return leatestlocal
while True:
    try:
        numberlist=[]
        size=int(input("Ingrese la cantidad de numeros que quiere ingresar en la lista\n"))
        for number in range(size):
            number=int(input(f"Ingrese el numero de la casilla {number}"))
            numberlist.append(number)
        leat=0
        greater=greatest(numberlist)
        leat=leatest(leat, greater, numberlist)
        print(f"El mayor de los numeros ingresados a la lista es {greater}")
        print(f"El menor de los ingresados a la lista es {leat}")
        choice=input("Quiere repetir todo el procedimiento?\n")
        if choiceyeahok(choice)==True:
            continue
        else:
            break
    except ValueError:
        print("Valor ingresado no valido o no numerico, intente de nuevo")
        continue
#Ejercicio 8
def choiceoblok(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, solo se acepta si o no, intente de nuevo\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
from math import pi
def areaandperimeter(radlocal):
    arealocal=pi*radlocal**2
    perimeterlocal=pi*(radlocal*2)
    return arealocal, perimeterlocal
while True:
    try:
        rad=float(input("Ingrese el valor del radio de su circunferencia para calcular su area y perimetro\n"))
        print(f"El area y perimetro de su circunferencia es {areaandperimeter(rad)} respectivamente")
        choice=input("Quiere volver a repetir el procedimiento?\n")
        if choiceoblok(choice)==True:
            continue
        else:
            break
    except ValueError:
        print("Valor ingresado no valido o no numerico, intente de nuevo")
        continue
#Ejercicio 9
def choiceokis(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, solo se acepta si o no, intente de nuevo\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def login(loginslocal):
    counterlogin=0
    while True:
        userlocal=input("Ingrese su nombre de usuario\n")
        passlocal=input("Ingrese su contraseña\n")
        if userlocal=="usuario1":
            if passlocal=="asdasd":
                break
            else:
                print("Contraseña incorrecta")
                continue
        elif loginslocal==0 and counterlogin==0:
            counterlogin+=1
            print("Limite de intentos alcanzado, se le dara otro intento")
            continue
        elif loginslocal==0:
            break
        elif userlocal=="usuario1" and passlocal!="asdasd":
            print("Contraseña incorrecta")
            loginslocal-=1
            continue
        else:
            print("Contraseña incorrecta")
            loginslocal-=1
            continue
    return loginslocal
while True:
    while True:
        print("Bienvenido a logingenerico.com! A continuacion inicie sesion con su cuenta registrada")
        logins=3
        logins=login(logins)
        if logins==0:
            print("Limite de intentos alcanzado, intente de nuevo o mas tarde")
            break
        elif logins>0:
            print("Bienvenido Usuario 1, iniciando sesion")
            break
    choice=input("Quiere volver a hacer el procedimiento?\n")
    if choiceokis(choice)==True:
        continue
    else:
        break
#Ejercicio 10
def choicevalid(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, solo se acepta si o no, intente de nuevo\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def discount(productslocal):
    dis=0.10
    totallocal=0
    for productl in productslocal:
        totallocal+=int(productl)-(int(productl)*dis)
        print(productl)
    return totallocal
products={}
productsprices=[]
while True:
    porcent=0
    size=int(input("Cuantos productos agregara al carrito?\n"))
    for prod in range(size):
        product=input("Ingrese el precio del producto\n")
        porcent=int(input(f"Ingrese el porcentaje que ocupa el producto en el carro\n"))
        products[product]=porcent
        productsprices.append(product)
    print(f"El total con un descuento del 10 porciento es de {discount(productsprices)}")
    choice=input("Quiere volver a repetir el procedimiento?\n")
    if choicevalid(choice)==True:
        continue
    else:
        break
#Ejercicio 11
def metafunction(listlocal):
    counter=0
    for elem in range(5):
        listlocal.append("Hola"+str(counter))
        counter+=1
    return listlocal
def centerfunction(listlocal, funcion):
    return funcion(listlocal)
centerlist=[]
meta=centerfunction(centerlist, metafunction)
print(meta)
#Ejercicio 12
def choiceyesok(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, solo se acepta si o no, intente de nuevo\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def converdic(phraselocal):
    phraselocalsic={}
    for wordlocal in phraselocal.split(" "):
        phraselocalsic[wordlocal]=len(wordlocal)
    return phraselocalsic
while True:
    phrase=input("Ingrese una frase para obtener un diccionario con cada palabra de la frase y sus longitudes como valor\n")
    phrasedic=converdic(phrase)
    for word in phrasedic.items():
        print(word)
    choice=input("Quiere repetir todo el procedimiento otra vez?\n")
    if choiceyesok(choice)==True:
        continue
    else:
        break
#Ejercicio 13
def choicecomeon(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, solo se acepta si o no, intente de nuevo\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
def calcvectormodul(componelocal, complocaltwo, complocalthree):
    vectormodulocal=(componelocal**2+complocaltwo**2+complocalthree**2)**(1/2)
    return vectormodulocal
while True:
    try:
        print("A continuacion, ingrese el valor de las tres componentes de su vector")
        compone=float(input("Ingrese el valor de la primera componente\n"))
        comptwo=float(input("Ingrese el valor de la segunda componente\n"))
        compthree=float(input("Ingrese el valor de la tercera componente\n"))
        print(f"El modulo de su vector es {calcvectormodul(compone, comptwo, compthree)}")
        choice=input("Quiere volver a hacerlo de nuevo?\n")
        if choicecomeon(choice)==True:
            continue
        else:
            break
    except ValueError:
        print("Alguno de los valores introducidos no es numerico, intentelo de vuelta")
        continue
#Ejercicio 14
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
def primenumberlocal(primelocal):
    divscounterlocal=0
    for number in range(1, 10):
        if primelocal%number==0:
            divscounterlocal+=1
    if divscounterlocal>2:
        return True
    else:
        return False
while True:
    try:
        prime=int(input("Ingrese el numero que quiere saber si es primo\n"))
        if primenumberlocal(prime)==True:
            print("El numero no es primo")
        else:
            print("El numero es primo")
        choice=input("Quiere hacer el procedimiento de vuelta?\n")
        if choicefuckingok(choice)==True:
            continue
        else:
            break
    except ValueError:
        print("El valor ingresado no es entero o no es numerico, intente de nuevo")
        continue
#Ejercicio 15
def choiceokilive(choicelocal):
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
def numbercounter(counterlocal):
    counterlocal+=1
    return counterlocal
def factorial(numberlocal):
    factoriallocal=1
    for values in range(1, numberlocal+1):
        factoriallocal*=values
    return factoriallocal
while True:
    counter=0
    while True:
        try:
            number=int(input("Ingrese un numero para saber su factorial\n(Ingrese 0 para salir)\n"))
            if number==0:
                break
            print(f"El factorial de {number} es {factorial(number)}")
            counter=numbercounter(counter) 
        except ValueError:
            print("El valor ingresado no es entero, o no es numerico, intente de vuelta")
            continue
    print(f"El total de numeros ingresados fue de {counter}")
    choice=input("Quiere repetir?\n")
    if choiceokilive(choice)==True:
        continue
    else:
        break
#Ejercicio 16
def choicenotokamdeath(choicelocal):
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
def digitinnumber(digitlocal, numberlocal):
    counterlocal=0
    for elem in str(numberlocal):
        if str(digitlocal)==elem:
            counterlocal+=1
    return counterlocal
while True:
    number=int(input("Ingrese un numero\n"))
    digit=int(input("Ingrese el digito que desea saber si esta en el numero ingresado\n"))
    print(f"La/s ocurrencia/s del digito en el numero ingresado son de/es de {digitinnumber(digit, number)}")
    choice=input("Quiere repetir el proceso?\n")
    if choicenotokamdeath(choice)==True:
        continue
    else:
        break
#Ejercicio 17
def primenumberlocaltwo(primelocal):
    divscounterlocal=0
    for number in range(1, 10):
        if primelocal%number==0:
            divscounterlocal+=1
    if divscounterlocal>2:
        return True
    else:
        return False
def factorialtwo(numberlocal):
    factoriallocal=1
    for values in range(1, numberlocal+1):
        factoriallocal*=values
    return factoriallocal
def digitinnumbertwo(digitlocal, numberlocal):
    counterlocal=0
    for elem in str(numberlocal):
        if str(digitlocal)==elem:
            counterlocal+=1
    return counterlocal
def digitssum(numberlocal):
    sumlocal=0
    for number in str(numberlocal):
        sumlocal+=int(number)
    return sumlocal
while True:
    try:
        number=int(input("Ingrese un numero primo\n"))
        digit=int(input("Ingrese un digito para saber la cantidad de sus ocurrencias en el numero ingresado\n"))
        if primenumberlocaltwo(number)==True:
            break
        print(f"La suma de los digitos del numero ingresado son {digitssum(number)}")
        print(f"El digito ingresado tiene {digitinnumbertwo(digit, number)} ocurrencia/s en el numero ingresado")
        print(f"El factorial de {number} ingresado es {factorialtwo(number)}")
        print("El numero ingresado es primo!")
    except ValueError:
        print("Alguno de los valores ingresados no son enteros, o no son numericos, intente de nuevo")
        continue
print(f"La suma de los digitos del numero ingresado son {digitssum(number)}")
print(f"El digito ingresado tiene {digitinnumbertwo(digit, number)} ocurrencia/s en el numero ingresado")
print(f"El factorial de {number} ingresado es {factorialtwo(number)}")
print("El numero ingresado no era primo!")
print("Finalizando...")
