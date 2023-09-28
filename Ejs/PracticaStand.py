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
import random
wordlist=["agua", "variable", "programa", "arbol"]
keyword=wordlist[random.randrange(0, len(wordlist))]
shown="_"*len(keyword)
shownlist=shown.split()
counter=0
while True:
    print("".join(shownlist))
    print(keyword)
    letter=input("Ingrese una letra\n")
    for elem in range(len(keyword)):
        if keyword[elem]==letter.lower():
            shownlist[elem]=letter
    while len(shownlist)>len(keyword):
        shownlist.pop
    while len(shownlist)<len(keyword):
        shownlist.append("_")
    print(shownlist)