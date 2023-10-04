choice=bool(True)
summatoryalldigitslist=[]
summatoryalllist=[]
def ciclingdigits(summatoryalldigitslistlocal):
    sumall=0
    for char in summatoryalldigitslistlocal:
        sumall+=int(char)
    return sumall
def ciclingsummatory(summatorynumberslist):
    sumallnumbers=0
    for number in summatorynumberslist:
        sumallnumbers+=int(number)
    return sumallnumbers
def cicling(numberlocal, choicelocal):
    if numberlocal!=0:
        summatorylocal=0
        for char in str(numberlocal):
            summatorylocal+=int(char)
        print(f"La sumatoria de los digitos del numero ingresado es {summatorylocal}")
    else:
        print("Finalizando...")
        choicelocal=False
        return choicelocal
while choice==True:
    summatory=0
    number=input("Ingrese un numero para saber la suma de sus digitos (Ingrese 0 para salir)\n")
    if number.isdigit():
        number=int(number)
        summatory+=number
        summatoryalllist.append(number)
        for character in str(number):
            summatoryalldigitslist.append(character)
        if cicling(number, choice)==False:
            break
        else:
            continue
    else:
        print("Ingrese un numero entero porfavor")
        continue
print(f"La suma de los numeros ingresados es {ciclingsummatory(summatoryalllist)}\n"
    f"La suma de los digitos de todos los numeros ingresados es {ciclingdigits(summatoryalldigitslist)}")
#Ahorcado
def graphiclives(liveslocal):
    if liveslocal==9:
        print(
            "||||||\n"
            "||||||\n"
            "||||||"
            )
    if liveslocal==8:
        print(
            "||||||\n"
            "||||||\n"
            "||||||\n"
            "  ||\n"
            "  ||\n"
        )
    if liveslocal==7:
        print(
            "||||||\n"
            "||||||\n"
            "||||||\n"
            "  ||\n"
            "  ||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
        )
    if liveslocal==6:
        print(
            "||||||\n"
            "||||||\n"
            "||||||\n"
            "  ||\n"
            "  ||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            "||||||\n"
            "|    \n"
            "|    \n"
            "|    \n"
            "|    \n"
            "|    \n"
        )
    if liveslocal==5:
        print(
            "||||||\n"
            "||||||\n"
            "||||||\n"
            "  ||\n"
            "  ||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            " ||||\n"
            "||||||\n"
            "|    |\n"
            "|    |\n"
            "|    |\n"
            "|    |\n"
            "|    |\n"
        )
    if liveslocal==4:
        print(
        "    ||||||\n"
        "    ||||||\n"
        "    ||||||\n"
        "      ||  \n"
        "      ||  \n"
        "    /|||| \n"
        "   / |||| \n"
        "  /  |||| \n"
        " /   |||| \n"
        "     |||| \n"
        "    ||||||\n"
        "    |    |\n"
        "    |    |\n"
        "    |    |\n"
        "    |    |\n"
        "    |    |\n"
        )
    if liveslocal==3:
        print(
        "    ||||||    \n"
        "    ||||||    \n"
        "    ||||||    \n"
        "      ||      \n"
        "      ||      \n"
        "    /||||\    \n"
        "   / |||| \   \n"
        "  /  ||||  \  \n"
        " /   ||||   \ \n"
        "     ||||     \n"
        "    ||||||    \n"
        "    |    |    \n"
        "    |    |    \n"
        "    |    |    \n"
        "    |    |    \n"
        "    |    |    \n"
        )
    if liveslocal==2:
        print(
    "        ||||||          \n"
    "        ||||||          \n"
    "        ||||||          \n"
    "          ||            \n"
    "          ||            \n"
    "        /||||\          \n"
    "       / |||| \         \n"
    "      /  ||||  \        \n"
    "     /   ||||   \       \n"
    "         ||||           \n"
    "        ||||||          \n"
    "        |    |          \n"
    "        |    |          \n"
    "        |    |          \n"
    "        |    |          \n"
    "        |    |          \n"
    "||||||||||||||||||||||||\n"
    "||||||||||||||||||||||||\n"
    "||||||||||||||||||||||||\n"
    "||||||||||||||||||||||||\n"
        )
    if liveslocal==1:
        print(
"|||||||||||||||||||||||||||||||||\n"
"|||||||||||||||||||||||||||||||||\n"
"                             ||||\n"
"            ||||||           ||||\n"
"            ||||||           ||||\n"
"            ||||||           ||||\n"
"              ||             ||||\n"
"              ||             ||||\n"
"            /||||\           ||||\n"
"           / |||| \          ||||\n"
"          /  ||||  \         ||||\n"
"         /   ||||   \        ||||\n"
"             ||||            ||||\n"
"            ||||||           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"    |||||||||||||||||||||||||||||\n"
"    |||||||||||||||||||||||||||||\n"
"    |||||||||||||||||||||||||||||\n"
"    |||||||||||||||||||||||||||||\n"
        )
    if liveslocal==0:
        print(
"|||||||||||||||||||||||||||||||||\n"
"|||||||||||||||||||||||||||||||||\n"
"              ||             ||||\n"
"            ||||||           ||||\n"
"            ||||||           ||||\n"
"            ||||||           ||||\n"
"             ||||            ||||\n"
"              ||             ||||\n"
"            /||||\           ||||\n"
"           / |||| \          ||||\n"
"          /  ||||  \         ||||\n"
"         /   ||||   \        ||||\n"
"             ||||            ||||\n"
"            ||||||           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"            |    |           ||||\n"
"    |||||||||||||||||||||||||||||\n"
"    |||||||||||||||||||||||||||||\n"
"    |||||||||||||||||||||||||||||\n"
"    |||||||||||||||||||||||||||||\n"
        )
import random
def ciclinglives(liveslocal):
    liveslocal-=1
    return liveslocal
def randomizeword(wordlistlocal):
    keywordlocal=wordlistlocal[random.randrange(0, len(wordlist))]
    return keywordlocal
def ifchoicenotok(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta incorrecta, intente de nuevo\n")
        if choicelocal.lower()!="si" and choicelocal.lower()!="no":
            continue
        else:
            break
    if choicelocal.lower()=="si":
        return True
    else:
        return False
while True:
    wordlist=["agua", "variable", "programa", "arbol"]
    keyword=randomizeword(wordlist)
    shown="_"*len(keyword)
    shownlist=list(shown)
    counter=0
    lives=10
    print("Bienvenido al ahorcado, a continuacion tendra 10 intentos para adivinar las letras de una palabra\n"
            "elegida aleatoriamente!")
    while lives>=1:
        print("".join(shownlist))
        letter=input("Ingrese una letra\n")
        while len(shownlist)>len(keyword):
            shownlist.pop
        while len(shownlist)<len(keyword):
            shownlist.append("_")
        for elem in range(len(keyword)):
            if keyword[elem]==letter.lower():
                shownlist[elem]=letter.lower()
        if letter.lower() not in keyword:
            lives=ciclinglives(lives)
            graphiclives(lives)
            print(f"No ha acertado en ninguna letra, intente nuevamente, le quedan {lives} intentos")
        if "".join(shownlist)==keyword:
            print(f''.join(shownlist))
            print(f"Enhorabuena, ha adivinado la palabra! Era <{keyword}>")
            break
        elif lives==0:
            print(f"Se ha quedado sin intentos! La palabra era <{keyword}>")
            break
        while len(shownlist)>len(keyword):
            shownlist.pop
        while len(shownlist)<len(keyword):
            shownlist.append("_")
    choice=input("Desea jugar de vuelta?\n")
    if ifchoicenotok(choice)==True:
        continue
    else:
        break
print("Gracias por jugar al ahorcado!")
#Comprension de listas dentro de listas
dimensiones=int(input("Ingrese el numero de dimensiones del vector\n"))
valores=int(input("Ingrese los valores de sus arrays\n"))
pointant=[valores for valores in range(valores)]
vector=[pointant for elems in range(dimensiones)]
print(vector)
#########
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
            number=int(input(f"Ingrese el numero de la casilla {number}\n"))
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