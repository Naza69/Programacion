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
def test_choice():
    assert ifchoicenotok("asjba")==False