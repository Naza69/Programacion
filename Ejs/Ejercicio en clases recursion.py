#Ejercicio 1
import random
def path():
    time=0
    define_path=random.randint(1, 3)
    if define_path==1:
        time+=3
        return time+path()
    elif define_path==2:
        time+=5
        return time+path()
    elif define_path==3:
        time+=7
        return time
print(f"La rata estuvo {path()} minutos para salir de la jaula")
#Ejercicio 2
#Desarrollar un programa que usando una funcion recursiva devuelva la version inversa de un numero entero 

