#Programa de reclutamiento de mutantes de Magneto
#Parcial 2 Programacion

def is_mutant(dna):                                                 #Funcion booleana para verificar 4 nucleotidos consecutivos en filas, columnas o diagonales
    counter_mutations=0                                             #Y por tanto para saber si la secuencia de adn es de un mutante o no
    for row in range(len(dna)):
        for column in range(6):
            if column<3 and dna[row][column]==dna[row][column+1] and dna[row][column+1]==dna[row][column+2] and dna[row][column+2]==dna[row][column+3]:
                counter_mutations+=1
    for row in range(len(dna)):
        for column in range(6):
            if row<3 and dna[row][column]==dna[row+1][column] and dna[row+1][column]==dna[row+2][column] and dna[row+2][column]==dna[row+3][column]:
                counter_mutations+=1
    for row in range(len(dna)):
        for column in range(6):
            if row<3 and column<3 and dna[row][column]==dna[row+1][column+1] and dna[row+1][column+1]==dna[row+2][column+2] and dna[row+2][column+2]==dna[row+3][column+3]:
                counter_mutations+=1
    for row in range(len(dna)):
        for column in range(6):
            if row<=3 and column>=3 and dna[row][column]==dna[row+1][column-1] and dna[row+1][column-1]==dna[row+2][column-2] and dna[row+2][column-2]==dna[row+3][column-3]:
                counter_mutations+=1
    if counter_mutations>1:
        return True
    else:
        return False

#Caso de prueba mutante
"""dna_for_testing=[
    "AAAACT",
    "CATACT",
    "GTTTTA",
    "TATTGT",
    "GCTGTA",
    "CGTACA"
]
print(is_mutant(dna_for_testing))"""
#Caso de prueba no mutante
"""dna_for_testing=[
    "AACACT",
    "CGTATC",
    "GTAGCA",
    "TATAGT",
    "GCAGTA",
    "CGTACA"
]
print(is_mutant(dna_for_testing))"""

def menu():
    while True:                                                     #Funcion booleana para imprimir un menu
        print(
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░Bienvenido al sistema de        \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░reclutamiento de mutantes!      \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░█░░░░░░░░░░░░Porfavor, ingrese una opcion!   \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█░░█░░█░░░░░░░░░░1) Verificar ADN                \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░█░░█░█░▓░░░░░░░2) Salir                        \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████████░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░█░░█░██░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█░░█░░█░░██░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░█░░█░░██░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒█░░█░░███░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░██░░█░░▓██░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░░░░██████████▓█████░░░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░░██░▓░░█░░███░░░░░░░░░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░░█▓░█░░█░░█░█░░░░░░░░░░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░██░█░░█░░█░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░░░███░░█░░█░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░▒█▓▒██░░█░▒███░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                \n"
        "░░░░░░░░░░░██▒█░▓░░██░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                \n"
        "░░░░░░░░░░░░░█░█░░███░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                \n"
        "░░░░░░░░░░░░░░█░░█░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░█░▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                \n"
        "░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                \n"
            )
        choice_local=input()
        if choice_local!="1" and choice_local!="2":
            print("Su eleccion no corresponde con ninguna opcion expresada, intente de nuevo")
            continue
        else:
            break
    return choice_local

def print_sequence(dna_sequence_local):                     #Funcion para imprimir la secuencia
    for row in dna_sequence_local:
        for column in row:
            print(f"[ {column} ]", end="")
        print()

def is_sequence_full(dna_sequence_local):                    #Funcion booleana que verifica que la secuencia no tenga mas de 36 nucleotidos
    nucleotide_summatory=0
    for row in dna_sequence_local:
        for column in row:
            nucleotide_summatory+=1
    if nucleotide_summatory>=36:
        return False
    else:
        return True

def dna_sequence_creator():                                     #Funcion creadora de la matriz de la secuencia de adn
    sequence_blanck=[]
    return sequence_blanck

def dna_fill_valid(nucleotide_local, nucleotides_list_local):
    nucleotide_input_list=nucleotide_local.split()
    nucleotides_summatory_bool=0
    for nitro_base in range(len(nucleotide_input_list)):                                                      
        for iterable_nucleotide in range(len(nucleotide_input_list[nitro_base])):
            if nucleotide_input_list[nitro_base][iterable_nucleotide] in nucleotides_list_local:
                nucleotides_summatory_bool+=1
    if len(nucleotide_local)!=6:
        return False
    if nucleotides_summatory_bool!=6:
        return False
    else:
        return True

def choice_valid(choice_local):                                 #Funcion booleana para validar la eleccion de reinicio al final
    while choice_local.lower()!="si" and choice_local.lower()!="no":
        print("Solo se acepta si o no, intente de nuevo")
        choice_local=input()
        if choice_local.lower()!="si" and choice_local.lower()!="no":
            continue
        else:
            break
    if choice_local=="si":
        return True
    else:
        return False

import time as t

def main():                                                       #Funcion main para ejecutar el programa en su conjunto
    while True:
        if menu()=="1":
            dna_sequence=dna_sequence_creator()
            nucleotides=["A", "T", "G", "C"]
            while True:
                new_nucleotide=input("Ingrese sus nucleotidos\n(Recuerde que la estructura genetica\ndel ser humano se basa en\nlas bases nitrogenadas: A, T, C, G)\n")
                if dna_fill_valid(new_nucleotide.upper(), nucleotides)==False:
                    print("Nucleotidos no valido, o no perteneciente a la genetica humana, intente de nuevo")
                    continue
                else:
                    dna_sequence.append(new_nucleotide.upper())
                    print_sequence(dna_sequence)
                if is_sequence_full(dna_sequence)==False:
                    print("Llenado de la secuencia terminado")
                    break
            print("Veamos si es mutante", end="")
            t.sleep(0.5)
            print(".", end="")
            t.sleep(0.5)
            print(".", end="")
            t.sleep(0.5)
            print(".")
            if is_mutant(dna_sequence):
                print(
    "   Es mutante!                  ▓▓         \n"
    "                                ▓▓▓        \n"
    "                              ▓▓▓ ▓▓       \n"
    "                             ▓▓▓   ▓▓      \n"
    "                            ▓▓ ▓▓▓  ▓▓▓    \n"
    "               ░  ░░      ▓▓▓▓▓▓▓▓▓▓▓      \n"
    "               ░  ░░  ▓▓▓▓▓▓▓              \n"
    "             ░  ░   ▓▓▓ ▓▓ ▓▓              \n"
    "            ░░░    ▓ ▓▓  ▓▓▓▓              \n"
    "                ▓     ▓▓  ▓▓               \n"
    "               ▓▓      ▓▓▓▓▓               \n"
    "              ▓▓▓▓▓     ▓▓▓                \n"
    "             ▓▓   ▓▓▓▓▓▓▓                  \n"
    "             ▓▓▓▓   ▓▓▓                    \n"
    "             ▓▓ ▓▓▓▓▓                      \n"
    "           ▓▓▓▓▓▓                          \n"
    "       ▓▓▓▓  ▓▓                            \n"
    "    ▓▓▓  ▓▓▓ ▓▓                            \n"
    "  ▓▓▓▓▓▓▓   ▓▓                             \n"
    " ▓▓▓     ▓▓▓▓                              \n"
    " ▓▓▓▓▓▓▓▓▓▓▓                               \n"
    "▓      ▓▓▓                                 \n"                                      
                    )
                choice=input("Quiere volver a repetir el proceso?\n")
                if choice_valid(choice):
                    continue
                else:
                    break
            else:
                print(
    "              █          █                           \n"   
    "              █          █       ░                   \n"  
    "               ██████████                            \n"   
    "          ░     ████████    No es mutante...         \n"   
    "                  ████                               \n"   
    "                 ██  ██                              \n"   
    "                █      █                             \n"   
    "              █          █                           \n"   
    "              █          █                           \n"   
    "              █          █                           \n"   
    "              █          █                           \n"   
    "    ░           █      █                             \n"  
    "                 ██  ██                              \n"   
    "                  ████                               \n"   
    "          ░     ████████                             \n"   
    "               ██████████                            \n"   
    "              █          █                           \n"   
    "              █          █                           \n"   
                )    
                choice=input("Quiere volver a repetir el proceso?\n")
                if choice_valid(choice):
                    continue
                else:
                    break
        else:
            return None

main()