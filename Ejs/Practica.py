#Ahorcado
import random
def ciclinglives(liveslocal):
    liveslocal-=1
    return liveslocal
def randomizeword(wordlistlocal):
    keywordlocal=wordlistlocal[random.randrange(0, len(wordlistlocal))]
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
    wordlist=["agua", "variable", "programa", "arbol", "computadora", "facultad", "edificio", "funcion", "parcial", "python", "java"]
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
            print(f"No ha acertado en ninguna letra, intente nuevamente, le quedan {lives} intentos")
        if "".join(shownlist)==keyword:
            print(f''.join(shownlist))
            print(f"Enhorabuena, ha adivinado la palabra! Era <{''.join(shownlist)}>")
            break
        elif lives==0:
            print(f"Se ha quedado sin intentos! La palabra era <{''.join(shownlist)}>")
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


