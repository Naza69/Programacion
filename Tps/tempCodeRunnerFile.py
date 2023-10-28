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
    