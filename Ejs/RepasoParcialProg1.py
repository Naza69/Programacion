#Ejercicio 1
phrase=[]
while True:
    word=input("Ingrese su frase o palabra\n")
    if len(word)==4:
        word+="!"
    else:
        word+="?"
    phrase.append(word)
    choice=input("Quiere seguir?\n")
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
print("Su frase "+"".join(phrase))
#Ejercicio 2
import random
wordlist=["Naza", "Ruth", "Rodri", "Pablo", "Lucho", "Paula", "Tomas"]
lives=5
while lives>0:
    randomword=wordlist[random.randrange(0, 7)]
    print(wordlist)
    print(f"Tiene {lives} vidas...")
    word=input("Adivine una palabra de esta lista: \n")
    if word.capitalize()==randomword:
        print(f"Enhorabuena! Ha adivinado con {lives} vidas")
        break
    elif lives>0:
        lives-=1
        print(f"Eleccion incorrecta, le quedan {lives} vidas")
        continue
    else:
        lives-=1
        print("Ha perdido! Se ha quedado sin vidas!")
#Ejercicio 3
while True:
    word=input("Ingrese un texto para saber la cantidad de palabras que contiene\n")
    wordlist=word.split(" ")
    print(f"Su texto tiene {len(wordlist)} palabras")
    choice=input("Quiere seguir?\n")
    while choice.lower()!="si" and choice.lower()!="no":
        choice=input("Respuesta invalida, ingrese su eleccion de nuevo (Si o no)\n")
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            break
        else:
            continue
    if choice.lower()=="no":
        break
    elif choice.lower()=="si":
        continue
#Ejercicio 4
while True:
    try:
        assists=int(input("Ingrese la cantidad de asistencias que tuvo este mes\n"))
        choice=input("Trabajo los domingos?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            choice=input("Respuesta invalida, ingrese su eleccion de nuevo (Si o no)\n")
            if choice.lower()=="no":
                break
            elif choice.lower()=="si":
                break
            else:
                continue
        if choice.lower()=="si":
            while True:
                try:
                    weekendhours=int(input("Ingrese las horas trabajadas los domingos\n"))
                    if assists>=22 and assists>0 and weekendhours<5 and weekendhours>3:
                        print("Usted ha asistido todo el mes y adicionalmente ha trabajado entre 3 y 5 horas los domingos")
                        monthsalary=150000+(1500000*0.03)
                        print(f"Su salario es ${monthsalary}")
                        break
                    elif assists>=22 and assists>0 and weekendhours>6 and weekendhours<10:
                        print("Usted ha asistido todo el mes y adicionalmente trabajado entre 6 y 10 horas los domingos")
                        monthsalary=150000+(150000*0.10)
                        print(f"Su salario es ${monthsalary}")
                        break
                    elif assists<22 and assists>0 and weekendhours>3 and weekendhours<10:
                        print("Usted no ha asistido todo el mes, pero ha trabajado entre 3 y 10 horas los domingos")
                        monthsalary=100000+(100000*0.02)
                        print(f"Su salario es ${monthsalary}")
                        break
                    else:
                        monthsalary=150000
                        print(f"Usted ha asistido todo el mes, pero no ha alcanzado las horas suficientes para un bono por domingos,\nle correponde ${monthsalary}")
                        break
                except ValueError:
                    print("El valor ingresado no es numero entero, vuelva a intentar")
                    continue
        elif choice.lower()=="no":
            if assists>22 and assists>0:
                monthsalary=150000
                print(f"Usted ha asistido todo el mes y no ha trabajado para el bono de los domingos,\nle corresponde ${monthsalary}")
        if assists<22:
            monthsalary=75000
            print(f"Usted no ha asistido todo el mes, le corresponde ${monthsalary}")
    except ValueError:
        print("El valor ingresado no es un numero entero, vuelva a intentar")
        continue
    choice=input("Quiere volver a hacer el procedimiento?\n")
    while choice.lower()!="si" and choice.lower()!="no":
        choice=input("Respuesta invalida, ingrese su eleccion de nuevo (Si o no)\n")
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            break
        else:
            continue
    if choice.lower()=="no":
        break
    elif choice.lower()=="si":
        continue
#Ejercicio 5
while True:
    try:
        firstnumber=float(input("Ingrese el primer numero\n"))
        secondnumber=float(input("Ingrese el segundo numero\n"))
        if firstnumber==secondnumber:
            print(f"{firstnumber} x {secondnumber} = {firstnumber*secondnumber}")
        elif firstnumber>secondnumber:
            print(f"{firstnumber} - {secondnumber} = {firstnumber-secondnumber}")
        else:
            print(f"{firstnumber} + {secondnumber} = {firstnumber+secondnumber}")
    except ValueError:
        print("El valor ingresado no es numerico, vuelva a intentarlo")
        continue
    choice=input("Quiere volver a hacer el procedimiento?\n")
    while choice.lower()!="si" and choice.lower()!="no":
        choice=input("Respuesta invalida, ingrese su eleccion de nuevo (Si o no)\n")
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            break
        else:
            continue
    if choice.lower()=="no":
        break
    elif choice.lower()=="si":
        continue
#Ejercicio 6
print("Bienvenido al ANSES! Para saber la clasificacion en el regimen jubilatorio de la persona en cuestion,\n"
        "se necesitara saber su edad y sus años de antiguedad en su trabajo\n"
        "A continuacion...")
while True:
    try:
        age=int(input("Ingrese la edad de la persona en cuestion!\n"))
        laboryears=int(input("Genial! Ahora ingrese sus años de antiguedad en su trabajo!\n"))
        if age>=laboryears and age>18:
            if age>=60 and laboryears<25 and age>0:
                print("La persona en cuestion se encuentra dentro del regimen:\n"
                "-Jubilacion por edad")
            elif age<60 and laboryears>=25 and age>0:
                print("La persona en cuestion se encuentra dentro del regimen:\n"
                "-Jubilacion por antiguedad joven")
            elif age>=60 and laboryears>=25 and age>0:
                print("La persona en cuestion se encuentra en el regimen:\n"
                "-Jubilacion por antiguedad adulta")
            elif age<60 and laboryears<25 and age>0 and laboryears>0:
                print("La persona en cuestion no dispone ni de la edad necesaria, ni de los años de trabajo suficientes\npara considerarse jubilado por el regimen")
            elif age>0 and laboryears<0:
                print("Los años trabajados no corresponden con un numero entero positivo\n"
                "Vuelva a ingresar sus datos")
                continue
            elif age<=0 and laboryears>0:
                print("La edad no corresponde con la de un numero entero positivo\n"
                "Vuelva a ingresar sus datos")
                continue
            elif age>0 and laboryears==0:
                print("Los años trabajados son nulos! No le corresponde ninguna clasificacion segun el regimen")
        elif age<laboryears:
            print("Es imposible que la persona en cuestion haya trabajado mas años que años de edad tiene\n"
                "Vuelva a ingresar los datos")
            continue
        else:
            print("La persona en cuestion no es mayor de edad como para contribuir legalmente con sus años de trabajo")
        choice=input("Quiere volver a hacer el procedimiento?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            choice=input("Respuesta invalida, ingrese su eleccion de nuevo (Si o no)\n")
            if choice.lower()=="no":
                break
            elif choice.lower()=="si":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    except ValueError:
        print("El valor ingresado no corresponde con el de un numero entero, vuelva a intentar")
        continue
print("Gracias por usar el programa oficial de evaluacion de regimen jubilatorio de ANSES! Que tenga un buen dia!")
#Ejercicio 7
while True:
    try:
        antiguaty=int(input("Ingrese sus años de antiguedad\n"))
        if antiguaty<1 and not antiguaty<0:
            salary=150000+(150000*0.05)
            print(f"Le corresponde ${salary}")
        elif antiguaty>=1 and antiguaty<2:
            salary=150000+(150000*0.07)
            print(f"Le corresponde ${salary}")
        elif antiguaty>=2 and antiguaty<5:
            salary=150000+(150000*0.10)
            print(f"Le corresponde ${salary}")
        elif antiguaty>=5 and antiguaty<10:
            salary=150000+(150000*0.15)
            print(f"Le corresponde ${salary}")
        elif antiguaty>=10:
            salary=150000+(150000*0.20)
            print(f"Le corresponde {salary}")
        else:
            print("El valor ingresado no corresponde con el de un numero positivo, vuelva a ingresar el valor")
            continue
        choice=input("Quiere volver a hacer el procedimiento?\n")
        while choice.lower()!="si" and choice.lower()!="no":
            choice=input("Respuesta invalida, ingrese su eleccion de nuevo (Si o no)\n")
            if choice.lower()=="no":
                break
            elif choice.lower()=="si":
                break
            else:
                continue
        if choice.lower()=="no":
            break
        elif choice.lower()=="si":
            continue
    except ValueError:
        print("El valor no corresponde con el de un numero entero positivo, vuelva a ingresar los datos")
        continue