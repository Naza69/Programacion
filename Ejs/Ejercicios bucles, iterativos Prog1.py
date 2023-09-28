#Ejercicio 1
men=input("Ingrese el mensaje que quiere enviar Jefe\n")
corr=int(input("Ingrese el corrimiento Jefe\n"))
menlist=men.split(" ")
encpalab=""
abc=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", 
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
p=0
menenlist=[]
for z in menlist:
    palab=z
    encpalab=""
    for y in palab:
        lett=y
        if lett in abc:
            enclett=abc[(abc.index(lett)+corr) % 27]
            encpalab=encpalab+enclett
        else:
            encpalab=encpalab+lett
    menenlist.append(encpalab)
    p+=1
print("Su mensaje encriptado es este Jefe:"," ".join(menenlist))
#Ejercicio 2
x=1
while x != 0:
    x=int(input("Ingrese un numero\n"))
    z=str(x)
    contpar=0
    contimpar=0
    for y in z:
        if int(y) % 2 == 0:
            contpar+=1
        else:
            contimpar+=1
    print(f"El numero ingresado tiene {contpar} digito/s par/es y {contimpar} digito/s impar/es")
