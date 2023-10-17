def seepoints(sporteamslocaltwo):
    counterwins=0
    counterdraws=0
    counterallpoints=[]
    for rows in range(len(sporteamslocaltwo)):
        for columns in range(len(sporteamslocaltwo)):
            if sporteamslocaltwo[rows][columns]>sporteamslocaltwo[columns][rows]:
                counterwins+=3
            elif sporteamslocaltwo[rows][columns]==sporteamslocaltwo[columns][rows]:
                counterdraws+=1
        counterallpoints.append(counterdraws+counterwins)
        counterwins=0
        counterdraws=0
    counteraux=0
    for rows in sporteams:
        print(f"El equipo {counteraux+1} quedo con {counterallpoints[counteraux]} puntos")
        counteraux+=1
def diff(sportteamslocaltwo):
    counteraux=0
    counterauxtwo=0
    for rows in range(len(sportteamslocaltwo)):
        for columns in range(len(sportteamslocaltwo)):
            if rows!=columns:
                print(f"Diferencia entre goles marcados y recibidos para el equipo {counteraux+1} con el equipo {counterauxtwo+1}: : {abs(sportteamslocaltwo[rows][columns]-sportteamslocaltwo[columns][rows])}")
            counterauxtwo+=1
        counteraux+=1
        counterauxtwo=0
    print("---------------------------------------------------")
def showingvictsdefeatsanddraws(counterallgoalslocaltwo):
    counteraux=0
    for rows in counterallgoalslocaltwo:
        for columns in range(len(rows)):
            if columns==0:
                print(Fore.GREEN+f"O"*rows[columns]+Style.RESET_ALL+f" {rows[columns]} victoria/s para el equipo {counteraux+1}")
            if columns==1:
                print(Fore.RED+f"O"*rows[columns]+Style.RESET_ALL+f" {rows[columns]} derrota/s para el equipo {counteraux+1}")
            if columns==2:
                print(Fore.YELLOW+f"O"*rows[columns]+Style.RESET_ALL+f" {rows[columns]} empate/s para el equipo {counteraux+1}")
        counteraux+=1
        print("-----------------------------------------------------")
def choose(choicelocal, counterallgoalslocal, sporteamslocal):
    if choicelocal=="1":
        showingvictsdefeatsanddraws(counterallgoalslocal)
    elif choicelocal=="2":
        diff(sporteamslocal)
    elif choicelocal=="3":
        seepoints(sporteamslocal)
while True:
    import random as ran
    from colorama import Fore, Style 
    countergreens=0
    counterreds=0
    counteryellows=0
    counter=[]
    counterallgoals=[]
    sporteams=[[0 for elem in range(10)] for elem in range(10)]
    for visitant in range(len(sporteams)):
        for local in range(len(sporteams)):
            if visitant==local:
                sporteams[visitant][local]=0
            else:
                sporteams[visitant][local]=ran.randrange(0, 6)
    for elem in range(len(sporteams)):
        counter=[]
        for elemtwo in range(len(sporteams)):
            if sporteams[elem][elemtwo]>sporteams[elemtwo][elem]:
                print(Fore.GREEN+"["+str(sporteams[elem][elemtwo]), end="]"+Style.RESET_ALL)
                countergreens+=1
            elif sporteams[elem][elemtwo]<sporteams[elemtwo][elem]:
                print(Fore.RED+"["+str(sporteams[elem][elemtwo]), end="]"+Style.RESET_ALL)
                counterreds+=1
            elif sporteams[elem][elemtwo]==sporteams[elemtwo][elem]:
                print(Fore.YELLOW+"["+str(sporteams[elem][elemtwo]), end="]"+Style.RESET_ALL)
                counteryellows+=1
            elif sporteams[elem][elemtwo]==sporteams[elem][elem]:
                print("["+str(sporteams[elem][elemtwo]), end="]")
        print("")
        counter.append(countergreens)
        counter.append(counterreds)
        counter.append(counteryellows)
        counterallgoals.append(counter)
        countergreens=0
        counterreds=0
        counteryellows=0
    counteraux=0
    print("Dado esta tabla de goles y equipos, elija una opcion\n"
        "1) Ver victorias, derrotas y empates de cada equipo\n"
        "2) Ver diferencia entre goles marcados y recibidos de cada equipo\n"
        "3) Ver los puntos que cada equipo obtuvo")
    choice=input()
    choose(choice, counterallgoals, sporteams)