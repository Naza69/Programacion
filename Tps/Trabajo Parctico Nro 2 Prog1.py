#Ejercicio 1
pced=int(input("Ingrese los años de su computadora\n"))
if pced<=2:
    print("Es nuevo")
else:
    print("Es viejo")
#Ejercicio 2
pced=int(input("Ingrese los años de su computadora\n"))
if pced<=2:
    print("Es nuevo")
elif pced<0:
    print("ERROR (Ingreso un numero negativo)")
else:
    print("Es viejo")
#Ejercicio 3
persone=input("Ingrese el nombre de la primera persona\n")
perstwo=input("Ingrese el nombre de la segunda persona\n")
if persone.lower()[0]==perstwo.lower()[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
#Ejercicio 4
inter=("Ingrese su intencion de voto!\n"
"1)Candidato A por el partido rojo\n"
"2)Candidato B por el partido verde\n"
"3)Candidato C por el partido azul\n")
print(inter)
intvot=input()
if intvot=="1":
    print(f"Usted ha votado por el partido {inter[59:63]}")
elif intvot=="2":
    print(f"Usted ha votado por el partido {inter[93:98]}")
elif intvot=="3":
    print(f"Usted ha votado por el partido {inter[128:]}")
else:
    print("Opcion erronea")
#Ejercicio 5
letter=input("Ingrese una letra\n")
if len(letter)>1:
    print("No se puede procesar el dato")
elif letter.lower()=="a" or letter.lower()=="e" or letter.lower()=="i" or letter.lower()=="o" or letter.lower()=="u":
    print("Es vocal")
#Ejercicio 6
year=int(input("Ingrese el año"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
#Ejercicio 7
np=int(input("Ingrese el primer numero\n"))
ns=int(input("Ingrese el segundo numero\n"))
nt=int(input("Ingrese el tercer numero\n"))
nmayor=0
if np>nmayor:
    nmayor=np
    if ns>nmayor or nt>nmayor:
        if nt>nmayor:
            nmayor=nt
        else:
            nmayor=ns
nmenor=0
if np<nmayor:
    nmenor=np
    if ns<nmenor or nt<nmenor:
        if nt<nmenor:
            nmenor=nt
        else:
            nmenor=ns
print(f"El menor es {nmenor}")
#Ejercicio 8
usuario=input("Ingrese su nombre de usuario\n")
key=input("Ingrese la contraseña\n")
inusuario="Gwenevere"
inkey="excalibur"
if usuario==inusuario:
    if usuario==inusuario and key==inkey:
        print("Usuario y contraseña correctos")
    else:
        print("Acceso denegado")
else:
    print("Acceso denegado")
#Ejercicio 9
groupa={}
groupb={}
usernom=input("Ingrese su nombre\n")
usersex=input("Ingrese su sexo\n")
refabec=["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m"]
refabecseg=["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if usernom[0].lower() in refabec and usersex[0].lower()=="m":
    groupa[usernom]=usersex
    print(f"Usted ha sido añadido a la primera parte del grupo A")
elif usernom[0].lower() in refabecseg and usersex[0].lower()=="h":
    groupa[usernom]=usersex
    print(f"Usted ha sido añadido a la segunda parte del grupo A")
else:
    groupb[usernom]=usersex
    print(f"Usted ha sido añadido al grupo B")
#Ejercicio 10
print("El valor de la entrada es $1000")
edad=int(input("Ingrese su edad\n"))
if edad<4 and edad>=0:
    print("Usted o su hijo entra gratis!")
elif edad>4 and edad<18:
    print("Usted o su hijo paga $500")
elif edad>18:
    print("Usted paga $1000")
else:
    print("Edad ingresada invalida")
#Ejercicio 11
ingveg=[" Pimiento", " Tofu"]
ingnoveg=[" Pepperoni", " Jamon", " Salmon"]
despiz=input("Quiere su pizza vegetariana?\n")
piz="pizza"
if despiz.lower()=="si":
    piz=piz+" muzzarella vegetariana"
    print(f"1){ingveg[0]}\n"
    f"2){ingveg[1]}")
    despiz=int(input("Eliga entre los ingredientes vegetarianos\n"))
    piz=piz+" con"+ingveg[despiz-1].lower()
    print(f"Usted ha pedido una {piz}")
elif despiz.lower()=="no":
    piz=piz+" muzzarella no vegetariana"
    print(f"1){ingnoveg[0]}\n"
        f"2){ingnoveg[1]}\n"
        f"3){ingnoveg[2]}")
    despiz=int(input("Eliga un ingrediente no vegetariano\n"))
    piz=piz+" con"+ingnoveg[despiz-1].lower()
    print(f"Usted ha pedido una {piz}")
#Ejercicio 12
currdate=input("Ingrese la fecha actual\n"
        "DD/MM/YY\n")
randate=input("Ingrese una fecha cualquiera\n"
        "DD/MM/YY\n")
curryear=currdate[6:]
currmon=currdate[3:5]
currday=currdate[0:2]
ranyear=randate[6:]
ranmon=randate[3:5]
randay=randate[0:2]
if int(ranyear)>int(curryear) or int(ranmon)>int(currmon) or int(randay)>int(currday):
    diffyear=abs(int(curryear)-int(ranyear))
    diffmon=abs(int(currmon)-int(ranmon))
    diffday=abs(int(currday)-int(randay))
    print(f"Faltan {diffyear} año/s, {diffmon} mes/es y {diffday} dia/s para la fecha cualquiera ingresada")
elif int(ranyear)<int(curryear) or int(ranmon)<int(currmon) or int(randay)<int(currday):
    diffyear=abs(int(curryear)-int(ranyear))
    diffmon=abs(int(currmon)-int(ranmon))
    diffday=abs(int(currday)-int(randay))
    print(f"Han pasado {diffyear} año/s, {diffmon} mes/es y {diffday} dia/s desde la fecha cualquiera ingresada")
else:
    print("Cualquiera de las dos fechas ingresadas tienen un formato invalido")
#Ejercicio 13
numone=int(input("Ingrese el primer numero\n"))
numsec=int(input("Ingrese el segundo numero\n"))
nummayor=0
if numone>nummayor:
    nummayor=numone
    if nummayor % numsec == 0:
        print(f"{nummayor} es multiplo de {numsec}")
    elif numsec==0 or numone==0:
        print("Se han ingresado valores nulos")
    elif numsec<0 or numone<0:
        print("Se han ingresado valores negativos")
    else:
        print(f"{nummayor} no es multiplo de {numsec}")
else:
    nummayor=numsec
    if nummayor % numone == 0:
        print(f"{nummayor} es multiplo de {numone}")
    elif numsec==0 or numone==0:
        print("Se han ingresado valores nulos")
    elif numsec<0 or numone<0:
        print("Se han ingresado valores negativos")
    else:
        print(f"{nummayor} no es multiplo de {numone}")
#Ejercicio 14
print("Ingrese los valores de los coeficientes de esta ecuacion para darle solucion\n"
    "ax + b = 0")
a=int(input("Ingrese el valor de a\n"))
b=int(input("Ingrese el valor de b\n"))
x=-b/a
print(f"El valor de x es {x}, es decir, es de solucion unica")
#Ejercicio 15
des=input("El area de que figura quiere calcular?\n"
        "Ingrese c o C para calcular el area de un circulo\n"
        "Ingrese t o T para calcular el area de un triangulo\n")
if des.lower()=="c":
    rad=float(input("Ingrese el radio del circulo\n"))
    from math import pi
    area=pi*rad**2
    print(f"El area de su circulo es {area}")
elif des.lower()=="t":
    base=float(input("Ingrese el valor de la base de su triangulo\n"))
    altura=float(input("Ingrese el valor de la altura de su triangulo\n"))
    area=(base*altura)/2
    print(f"El area de su triangulo es {area}")
else:
    print("Solo se puede calcular el area de un circulo o un triangulo, cualquier otro valor ingresado es invalido")
#Ejercicio 16
a=int(input("Ingrese el primer numero\n"))
b=int(input("Ingrese el segundo numero\n"))
des=input("Vamos a usar una calculadora!\n"
        "Eliga una operacion aritmetica\n"
        "1)Suma\n"
        "2)Multiplicacion\n"
        "3)Resta\n"
        "4)Division\n")
if des=="1":
    print(f"{a}+{b}={a+b}")
elif des=="2":
    print(f"{a}x{b}={a*b}")
elif des=="3":
    print(f"{a}-{b}={a-b}")
elif des=="4":
    print(f"{a}÷{b}={a/b}")
else:
    print("El valor ingresado no corresponde con ninguna opcion")
#Ejercicio 17
dia=input("Ingrese un dia de la semana\n")
if dia.lower()=="lunes":
    print("Odio los lunes... -Garfield")
elif dia.lower()=="viernes":
    print("Vamos locoooooo que es viernessssss!!")
elif dia.lower()=="sabado":
    print("Hoy es sabado loco, hace lo que quieras")
elif dia.lower()=="domingo":
    print("Hoy es domingo, espero que no te hayas levantado temprano")
else:
    print("Estamos entre semana entonces... Dia habil, cobras el aguinaldo, trabajas, etc.")
#Ejercicio 18
trabhors=int(input("Cuantas horas ha trabajado este mes?\n"))
salporhors=int(input("Cuanto es su salario por hora?\n"))
salporhorsex=salporhors*1.10
if trabhors>48:
    trabhorsex=trabhors-48
    print("Usted ha trabajado una/s hora/s extra/s\n"
        f"Ha trabajado {trabhorsex} hora/s extra")
    saltotal=((trabhors-trabhorsex)*salporhors)+(trabhorsex*salporhorsex)
    print(f"Su salario total es {saltotal}")
else:
    print("Usted no ha trabajado horas extras\n"
    f"Su salario total es {trabhors*salporhors}")
#Ejercicio 19
canlap=int(input("Ingrese la cantidad de lapices que se quiere llevar\n"))
valporlap=60
desc=(canlap*valporlap)*0.07
if canlap>=1000:
    valbrut=canlap*valporlap
    valtotal=valbrut-desc
    print("Usted quiere comprar 1000 o mas de 1000 lapices, se la aplicara un descuento al valor total a pagar\n"
        f"Valor total a pagar con descuento del 7%: ${valtotal}")
else:
    print(f"Valor a pagar total sin descuento: ${canlap*valporlap}")
#Ejercicio 20
print("Hola alumno! Ingrese sus 4 notas")
np=int(input("Primer nota: "))
ns=int(input("Segunda nota: "))
nt=int(input("Tercer nota: "))
nc=int(input("Cuarta nota: "))
prom=(np+ns+nt+nc)/4
if prom>=6:
    print("Usted ha aprobado!")
elif prom<6:
    print("Usted ha desaprobado...")
else:
    print("Una o mas de las notas ingresadas son negativas o mayores a 10")




