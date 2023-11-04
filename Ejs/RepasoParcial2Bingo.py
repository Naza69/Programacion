#Bingo

import random as ran
import time as t
def print_card(card_local):
    aux_letter_bingo=["B", "I", "N", "G", "O"]
    aux_letter_counter=0
    for rows in card_local:
        for column in rows:
            print("[ ", column, " ]", end="")
        """print(f"{aux_letter_bingo[aux_letter_counter]}\n")"""
        aux_letter_counter+=1
        print()

def card_creator():        #Funcion main de matriz del carton
    card_main=bingo_card()
    print("A continuacion, llene su carton con 25 numeros unicos!")
    rows_aux=0           
    while True:
        try:
            number_local=int(input("Ingrese un numero entero comprendido entre 1 y 75\n"))
            if number_local<1 or number_local>75:
                print("El numero no esta comprendido entre el rango especificado")
                continue
            aux_number_in_card=0
            for row in range(len(card_main)):
                if number_local in card_main[row]:
                    aux_number_in_card+=1
                    break
            if aux_number_in_card>0:
                aux_number_in_card=0
                print("El valor ingresado ya se encuentra en el carton")
                continue
            if is_full_every_row(card_main, rows_aux):
                card_main[rows_aux].append(number_local)
            else:
                rows_aux+=1
                card_main[rows_aux].append(number_local)
            if is_card_main_full(card_main):
                print_card(card_main)
                continue
            else:
                print_card(card_main)
                break
        except ValueError:
            print("El valor ingresado no es numerico o no es entero, vuelva a intentarlo")
            continue
    return card_main

def bool_bingo_card():              #Funcion creadora del carton bool
    card_main_bool_local=[[False for metaelem in range(5)] for elem in range(5)]
    return card_main_bool_local

def is_full_every_row(card_main_local, row_local):    #Funcion bool para ver si cada fila del carton esta llena
    if len(card_main_local[row_local])==5:
        return False
    else:
        return True

def bingo_card():                         #Funcion creadora de la matriz del carton
    card_local=[[] for elem in range(5)]
    return card_local

"""def input_card_fill(number_meta_local, card_main_local):     #Funcion para llenar una posicion del carton
    for row in range(card_main_local):
        for column in range(card_main_local):
            card_main_local[row][column]=number_meta_local
    return number_meta_local"""

def is_card_main_full(card_main_local):        #Funcion bool para ver si el carton esta lleno
    summatory=0
    for row in card_main_local:
        for column in row:
            summatory+=1
    print(summatory)
    if summatory>=25:
        return False
    else:
        return True

def bingo_hype():                              #Funcion para aleatorizar la bola salida del bombo
    random_ball=ran.randint(1, 75)
    t.sleep(0.5)
    print("Mezclando", end="")
    t.sleep(0.5)
    print(".", end="")
    t.sleep(0.5)
    print(".", end="")
    t.sleep(0.5)
    print(".", end="")
    print(f"Salio {random_ball}!\r", end="")
    t.sleep(0.5)
    return random_ball


def menu():                                 #Funcion de menu basico para seleccionar 
    while True:
        print(
    ".,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n"     
    ".,,,///////////,,,,,,,,/////,,,,,,/////,,,,,/////,,,,,,*/((((((/,,,,,,,,,**/////*,,,,,,,\n"      
    ".,,,(############*,,,,,#####,,,,,,######*,,,(###(,,,,((((((/((((((*,,,*/////////////,,,,\n"      
    ".,,,(####,,,,####*,,,,,#####,,,,,,########,,(###(,,,((((/,,,,,,,,,,,,*////*,,,,,/////,,,\n"      
    ".,,,(###########*,,,,,,#####,,,,,,####/####((###(,,*((((,,,,(((((((,,*////,,,,,,*////,,,\n"      
    ".,,,(####,,,,/####,,,,,#####,,,,,,####/,*#######(,,,((((/,,,,,,((((,,,////*,,,,,/////,,,\n"      
    ".,,,(#############,,,,,#####,,,,,,####/,,,/#####(,,,,((((((((((((((,,,,/////////////,,,,\n"      
    ".,,,//////////*,,,,,,,,/((((,,,,,,/(((/,,,,,((((/,,,,,,,**////*,,,,,,,,,,,,**/**,,,,,,,,\n"      
    " __                      __    __   __   __     \n"
    "|__) .  _   _   _  |©     _)  /  \   _)   _)    \n"
    "|__) | | ) (_) (_) .     /__  \__/  /__  __)    \n"
    "           _/                                   \n"         
    "                                                \n"
    "|_       |\ |  _  _   _   _  _  _   _           \n"
    "|_) \/   | \| (_| /_ (_| |  (- | ) (_)          \n"
    "    /                                           \n"
    "__                                              \n"
    "|_  .  _   _  _ |_ |_ .                         \n"
    "|   | (_) |  (- |_ |_ |                         \n")
        print(
                "1) Jugar\n"
                "2) Salir"
                )
        choice=input("Ingrese una opcion!\n")
        if choice!="1" and choice!="2":
            print("Su eleccion no corresponde con ninguna opcion expresada, intente de nuevo")
            continue
        else:
            break
    return choice

def mark_number_register(blanck_register_local, random_ball_local):
    if random_ball_local in blanck_register_local:
        blanck_register_local.remove(random_ball_local)
        return blanck_register_local
    else:
        return blanck_register_local

def random_ball_in_card(card_local, random_ball_local, card_bool_local, row_local, column_local):
    if card_local[row_local][column_local]==random_ball_local:
        card_bool_local[row_local][column_local]==True
        print("                                                                                  \r", end="")
        print("Lo tiene en su carton!\r", end="")
        return True

def replace_random_ball_in_card_bool(card_bool_local, row_local, column_local):
    card_bool_local[row_local][column_local]==True
    return card_bool_local

def is_any_card_row_complete(card_bool_local):
    summatory_local=0
    for row in range(1):
        for column in range(5):
            if card_bool_local[row][column]==True:
                summatory_local+=1
    if summatory_local==5:
        return True
    else:
        return False

"""def is_any_card_column_complete(card_local):"""


def main():                                                 #Funcion main para ejecutar el juego en su totalidad
    print("Bienvenido al bingo!")
    if menu()=="1":
        card=card_creator()
        card_bool=bool_bingo_card()
        blanck_register=[]
        for row in range(75):
            blanck_register.append(row)
        print(
"            █▓                       ▒▒▒▒█     \n"
"█▓  █▒                               █▒▒▒▒▓    \n"
"       ▓▒▒██       ███░█░░█░███            ███ \n"  
"   █▒▒█  █      █░░█░░░░░░░░░░█░░█         █▒█ \n"   
"              █░░░░░░░██████░░░░░░░█       █▒█ \n"   
"             ▒░░█▒░░░░░░░░░░░░░░▒█░░▒      █▒█ \n"   
"            ▒▒░░█░░░░█░░░░░░█░░░░█░░▒▒     █▒█ \n"   
"           █▓░░░░░░░░█▒▒▒▒▒▒█░░░░░░░░▓█    █▒█ \n"   
"           ▓░█░█░░░░░█░░░░░░█░░░░░█░█░▓    █▒█ \n"   
"         ▒▒░░░░█░░░░░██▒▒▒▒▒█░░░░░█░░░░▒▒▒▒▒▒█ \n"   
"         ▒▒░█░░█▒▒▒█░█▒▒▒▒▒▒██░░░██▒██░▒▒      \n"   
"         ▒▒█░░█▒▒▒▓████████████▓▒▒▒▒▒▒█▒▒      \n"   
"         ▒▒ ░█░▒▓▒▒▒▒█▒▒▒▒█▒█▒▒▒▒▓▒▒█▒ ▒▒      \n"   
"         ▒▒ █░░▓█▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▓▓██ ▒▒      \n"   
"         ▒▒   █░▓▓▒▒███▒▒▒▒███▒▒▓▓░█   ▒▒      \n"   
"         ▒▒     █▒▒▒▒█▓▒▒▒▒▓▒▒▒▒▒█     ▒▒      \n"   
"         ▒▒       ██▒▓▓█▒▒██▓▒██       ▒▒      \n"   
"         ▒▒                            ▒▒      \n"   
"         ▒▒                            ▒▒      \n"   
"         ▒▒                            ▒▒      \n"   
"      █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█   \n"   
"    █▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█ \n"   
"   ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓\n")
        while True:
            random_ball=bingo_hype()
            blanck_register=mark_number_register(blanck_register, random_ball)
            if len(blanck_register)==0:
                break
            for row in range(len(card)):
                for column in range(5):
                    if random_ball_in_card(card, random_ball, card_bool, row, column):
                        card_bool=replace_random_ball_in_card_bool(card_bool, row, column)
                        break
            if is_any_card_row_complete(card):
                break
    else:
        return None

main()
