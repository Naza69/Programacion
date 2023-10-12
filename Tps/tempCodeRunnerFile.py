def metafunction(listlocal):
    counter=0
    for elem in range(5):
        listlocal.append("Hola"+str(counter))
        counter+=1
    return listlocal
def centerfunction(listlocal, funcion):
    return funcion(listlocal)
list=["Sergio"]
print(metafunction(list))