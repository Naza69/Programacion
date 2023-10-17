def repeticiones_not(array1,array2):#MUESTRO LOS ELEMENTOS DEL array1 QUE NO SE REPITEN EN array2
    students_primary = []
    for i in array1: 
        if i not in array2:
            students_primary.append(i)
    return students_primary

def repeticiones_mas_de_una_vez(array): #MUESTRA LOS ELEMENTOS QUE SE REPITEN MAS DE UNA
    new_list = []
    for i in array:
        counter = array.count(i) #CUENTO CUANTAS VECES SE REPITEN LOS ELEMENTOS
        if counter > 1:
            new_tupla = (i,f"Se repite: {counter}")
            new_list.append(new_tupla) #AGREGO LA TUPLA CON EL VALOR DE LA POSICION Y LAS VECES QUE SE REPITE A UNA LISTA
    new_list = set(new_list)
    return new_list

def repeticiones_todos(array): #MUESTRA LOS ELEMENTOS QUE SE REPITEN Y LOS QUE NO SE REPITEN
    new_list = []
    for i in array:
        counter = array.count(i) #CUENTO CUANTAS VECES SE REPITEN LOS ELEMENTOS
        new_tupla = (i,f"Se repite: {counter}")
        new_list.append(new_tupla) #AGREGO LA TUPLA CON EL VALOR DE LA POSICION Y LAS VECES QUE SE REPITE A UNA LISTA
    new_list = set(new_list)
    return new_list


def verificar_nombre(variable): #FUNCION PARA VALIDAR QUE NO HAYA NUMEROS EN EL NOMBRE
    list_numbers = "123456789"
    list_special_characters = "!@#$%^&*()_+}{|?><,./[]"
    for i in range (0,len(variable)):
        if variable[i] not in list_numbers and variable[i] not in list_special_characters:
            check = True
        else:
            check = False
    return check