from Practica import randomizeword
def fillandanalize(liveslocal, letterlocal, shownlistlocal, keywordlocal):
    while len(shownlistlocal)>len(keywordlocal):
        shownlistlocal.pop
    while len(shownlistlocal)<len(keywordlocal):
        shownlistlocal.append("_")
    for elem in range(len(keywordlocal)):
        if keywordlocal[elem]==letterlocal.lower():
            shownlistlocal[elem]=letterlocal.lower()
    if letterlocal.lower() not in keywordlocal:
        lives=ciclinglives(liveslocal)
        print(f"No ha acertado en ninguna letra, intente nuevamente, le quedan {lives} intentos")
    if "".join(shownlistlocal)==keywordlocal:
        print(f''.join(shownlistlocal))
        print(f"Enhorabuena, ha adivinado la palabra! Era <{''.join(shownlistlocal)}>")
        return False
    elif lives==0:
        print(f"Se ha quedado sin intentos! La palabra era <{''.join(shownlistlocal)}>")
        return False
    while len(shownlistlocal)>len(keywordlocal):
        shownlistlocal.pop
    while len(shownlistlocal)<len(keywordlocal):
        shownlistlocal.append("_")
wordlist=["agua", "variable", "programa", "arbol"]
keyword=randomizeword(wordlist)
shown="_"*len(keyword)
shownlist=list(shown)
counter=0
lives=10
letter=input("Ingrese una letra\n")
while fillandanalize(lives, letter, shownlist, keyword)!=False:
    from Practica import ifchoicenotok
    choice=input("Desea jugar de vuelta?\n")
    if ifchoicenotok(choice)==True:
        continue
    else:
        break
def ciclinglives(liveslocal):
    liveslocal-=1
    return liveslocal