#Ejercicio 1
base=6
altura=4
area=base*altura
perimetro=base*2+altura*2
#Ejercicio 2
catetoop=6
catetoad=4
hipo=(catetoop**2+catetoad**2)**1/2
#Ejercicio 3
np=4
ns=2
suma=np+ns
resta=np-ns
mult=np*ns
div=np/ns
#Ejercicio 4
f=60.0
c=(f-32)*(5/9)
#Ejercicio 5
#a) No es posible nombrar una variable empezando o conteniendo mayuscula (Es mala practica), ni tampoco inicializarla
#dentro de la funcion input(), asi estaria correcta:
nombre=input("Cual es tu nombre\n")
a=input(nombre, "¿Cuál es tu canción favorita?\n")
#b) No es posible hacer operaciones aritmeticas con un string, aun si es un numero el que fue ingresado, antes hay que
#convertirlo a un valor numerico con int() o float(), asi estaria correcto:
precio =int(input("Precio: "))
total = precio + (precio * 0.1)
#c) No es posible imprimir texto con print() sin el uso de las comillas, asi estaria correcto:
edad = int(input("Edad: "))
print("tu edad es", edad)
#d) No es posible reasignar o asignar valores a variables dentro de la funcion print(), deben hacerse previamente, asi
#estaria correcto:
edad=int(input("Edad: "))
edad=18
print("Veamos si tu edad es 18…", edad)
#Ejercicio 6
pn=int(input("Ingrese el primer numero\n"))
sn=int(input("Ingrese el segundo numero\n"))
tn=int(input("Ingrese el tercer numero\n"))
media=(pn+sn+tn)/3
#Ejercicio 7
minutos= int(input(print("Ingrese los minutos")))
horas= int(minutos/60)
min_restantes= minutos- horas*60
print(f"Minutos ingresados {minutos}, son {horas} horas y {min_restantes} min")
#Ejercicio 8
suel=70000
suelcom=suel*1.10
com=suelcom-suel
print(f"Sueldo: {suel}\n"
    f"Comision: {com}\n"
    f"Total: {suelcom}")
#Ejercicio 9
compra=9000
desc=9000*0.15
comprtotal=compra-desc
print(f"Bruto: {compra}"
    f"Neto: {comprtotal}")
#Ejercicio 10
parcone=7.0
parctwo=8.0
parcthree=5.0
primpart=((parcone+parctwo+parcthree)/3)*0.55
exfinal=9.0
segpart=exfinal*0.30
trabfinal=8.0
tercpart=trabfinal*0.15
calfinal=primpart+segpart+tercpart
print(f"Su calificacion final es {calfinal}")
#Ejercicio 11
np=int(input("Ingrese el primer numero\n"))
ns=int(input("Ingrese el segundo numero\n"))
cont=0
dif=abs(np)-abs(ns)
print(f"La diferencia es de {dif}")
#Ejercicio 12
x=int(input("Ingrese un numero para saber su raiz cubica y su raiz cuadrada\n"))
xcuad=x**1/2
xcub=x**1/3
print(f"Su raiz cuadrada es {xcuad}\n"
    f"Su raiz cubica es {xcub}")
#Ejercicio 13
x=int(input("Ingrese un numero de dos cifras\n"))
xinvone=(x/10)//1
x=str(x)
x=x.replace(x[0], x[1])
x=int(x)
xinvtwo=(x/10)//1
print("Su forma invertida es", str(int(xinvtwo))+str(int(xinvone)))
#Ejercicio 14
a=int(input("Ingrese A\n"))
b=int(input("Ingrese B\n"))
c=a
d=b
a=d
b=c
print(f"Intecambiadas! B={b}, A={a}")
#Ejercicio 15
asal="08:40:21"
print(f"La hora de salida es {asal}")
tlleg=7800
ss=int(asal[6:])
mm=int(asal[3:5])
hh=int(asal[0:2])
print(f"El tiempo de llegada es de {tlleg} segundos")
hlleg=(int(tlleg/3600)//1)+hh
mlleg=(int(tlleg/3600)+mm+hh)
slleg=(int(tlleg/3600)+ss)
print(f"La hora de llegada es {hlleg}:{mlleg}:{slleg}")
#Ejercicio 16
primnom=input("Ingrese su primer nombre\n")
segnom=input("Ingrese su segundo nombre\n")
primapel=input("Ingrese su primer apellido\n")
segapel=input("Ingrese su segundo apellido\n")
print(f"Sus inciales son {primnom[0]}{segnom[0]}{primapel[0]}{segapel[0]}")
#Ejercicio 17
usuario=input("Ingrese su nombre\n")
print(f"Ahora estas en la matrix [{usuario}]")
#Ejercicio 18
cena=int(input("Cuanto costo la cena?\n"))
serv=cena*0.062
prop=cena*0.1
montfinal=cena+serv+prop
print(f"Le costara {montfinal}")
#Ejercicio 19
day=input("Ingrese su dia de nacimiento\n")
mon=input("Ingrese su mes de nacimiento\n")
yea=input("Ingrese su año de nacimiento\n")
print(f"{day}/{mon}/{yea}")
#Ejercicio 20
birthdate=input("Ingrese su fecha de nacimiento\n")
print(f"{birthdate[0:2]}/{birthdate[3:5]}/{birthdate[6:]}")
#Ejercicio 21
rendporlitro=int(input("Ingrese el rendimiento en km por litro de su moto\n"))
tanquecap=int(input("Ingrese la capacidad del tanque de su moto\n"))
recor=int(input("Ingrese el recorrido a hacer en km\n"))
combnec=(recor/rendporlitro)
print(f"Para viajar {recor} km necesitaran {combnec} litros de combustible")







