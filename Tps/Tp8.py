#Ejercicio 1
def lenght(number_local):
    try:
        if number_local<10:
            return 1
        else:
            return 1+lenght(number_local//10)
    except ValueError:
        return "El valor ingresado a la funcion no es entero o no es numerico"

number=int(input("Ingrese un numero\n"))
print(f"La cantidad de digitos del numero ingresado es de: {lenght(number)}")

#Ejercicio 2
def is_power(number_local, exponent):
    if number_local == exponent:
        return True
    elif exponent<number_local:
        return False
    else:
        return is_power(number_local, exponent/number_local)

number=int(input("Ingrese el numero que esta elevando\n"))
number_exponent=int(input("Ingrese el numero que sea saber si es potencia del anterior ingresado\n"))
print("Es potencia" if is_power(number, number_exponent) else "No es potencia")

#Ejercicio 3
def how_many_string_in(string_local, sub_string_local, start=0, positions=None):
    if positions is None:
        positions=[]
    index=string_local.find(sub_string_local, start)
    if index !=-1:
        positions.append(index)
        start=index+1
        return how_many_string_in(string_local, sub_string_local, start, positions)
    else:
        return positions

string=input("Ingrese una cadena\n")
sub_string=input("Ingrese una subcadena\n")
print(how_many_string_in(string, sub_string))

#Ejercicio 4
def even(number_local):
    if number_local % 2 == 0:
        return "Es par"
    else:
        return odd(number_local)
def odd(number_local):
    if number_local % 2 != 0:
        return "Es impar"
    else:
        return even(number_local)

number=int(input("Ingrese un numero entero\n"))
print(odd(number))

#Ejercicio 5
def greatest_in_list(number_list_local, counter=0, greatest=0):
    counter=len(number_list_local)-1
    if number_list_local[counter] > greatest and counter != 0:
        greatest=number_list_local[counter]
        counter-=1
        return greatest_in_list(number_list_local, counter, greatest)
    else:
        return greatest

number_list=[1, 4, 6, 8, 11]
print("El mayor de la lista es", greatest_in_list(number_list))

#Ejercicio 6
def replicate_elems_in_list(list_local, times_to_replicate):
    if not list_local:
        return []
    element = list_local[0] 
    replicated_elements = [element] * times_to_replicate  
    return replicated_elements + replicate_elems_in_list(list_local[1:], times_to_replicate)

list_any = [1, 2, 3]
result = replicate_elems_in_list(list_any, 2)
print(result)

#Ejercicio 7
def calculate_sum(n, p):
    if n == 1:
        return p
    else:
        return n * p + calculate_sum(n - 1, p)

#Ejercicio 8
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

#Ejercicio 9
def combinations(lst, k, current=""):
    if k == 0:
        print(current)
        return
    for char in lst:
        combinations(lst, k - 1, current + char)

#Ejercicio 10
def paper_sizes_A(N):
    if N == 0:
        return (841, 1189)  # Measurements of A0 paper
    else:
        previous_width, previous_length = paper_sizes_A(N - 1)
        new_width = previous_length // 2
        new_length = previous_width
        return (new_width, new_length)