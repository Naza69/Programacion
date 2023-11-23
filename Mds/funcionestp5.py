def repeat(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=input("Respuesta invalida, intente nuevamente (Si o no)\n")
        if choicelocal.lower()=="si":
            break
        if choicelocal.lower()=="no":
            break
    if choicelocal.lower()=="si":
        return True
    else: 
        return False

def booldni(dnilocal):
    if len(str(dnilocal))==7 or len(str(dnilocal))==8:
        return True
    else:
        return False

def longstring(stringlocal):
    liststrings=stringlocal.split(" ")
    for word in liststrings:
        if word==liststrings[len(liststrings)-1]:
            return len(word)

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

def avrtemp(tempminlocal, tempmaxlocal):
    avrtemplocal=(tempmaxlocal+tempminlocal)/2
    return avrtemplocal

def stringspacey(stringlocal):
    stringwithspace=[]
    for char in stringlocal:
        stringwithspace.append(char+" ")
    return "".join(stringwithspace)

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
from math import pi
def areaandperimeter(radlocal):
    arealocal=pi*radlocal**2
    perimeterlocal=pi*(radlocal*2)
    return arealocal, perimeterlocal
def discount(productslocal):
    dis=0.10
    totallocal=0
    for productl in productslocal:
        totallocal+=int(productl)-(int(productl)*dis)
        print(productl)
    return totallocal
def metafunction(listlocal):
    counter=0
    for elem in range(5):
        listlocal.append("Hola"+str(counter))
        counter+=1
    return listlocal
def centerfunction(listlocal, funcion):
    return funcion(listlocal)
def converdic(phraselocal):
    phraselocalsic={}
    for wordlocal in phraselocal.split(" "):
        phraselocalsic[wordlocal]=len(wordlocal)
    return phraselocalsic
def calcvectormodul(componelocal, complocaltwo, complocalthree):
    vectormodulocal=(componelocal**2+complocaltwo**2+complocalthree**2)**(1/2)
    return vectormodulocal
def primenumberlocal(primelocal):
    divscounterlocal=0
    for number in range(1, primelocal*10):
        if primelocal%number==0:
            divscounterlocal+=1
    if divscounterlocal>2:
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