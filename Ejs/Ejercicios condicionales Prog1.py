ing=input("Ingrese dia, DD/MM\n")
dia_semana=ing[0:ing.find(",")].lower()
dia=int(ing[ing.find(" ")+1:ing.find("/")])
mes=int(ing[ing.find("/")+1:])
semanadays=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
if dia_semana!=semanadays[0] and dia_semana!=semanadays[1] and dia_semana!=semanadays[2] and dia_semana!=semanadays[3] and dia_semana!=semanadays[4]:
    print("ERROR (Dia se la semana ingresado inexistente)")
elif dia>31: 
    print("ERROR (Ningun mes tiene mas de 31 dias)")
elif dia<1:
    print("ERROR (No existe dia cero)")
elif mes>12:
    print("ERROR (El año solo tiene 12 meses)")
elif mes<1:
    print("ERROR (No existe mes cero)")
if dia_semana==semanadays[0] or dia_semana==semanadays[1] or dia_semana==semanadays[2]:
    modiexam=input("Este dia se tomaron examenes?\n").lower()
    if modiexam=="si":
        desaprobs=int(input("Ingrese la cantidad de desaprobados\n"))
        aprobs=int(input("Ingrese el numero de aprobados\n"))
        alumn=aprobs+desaprobs
        porcaprobs=(aprobs*100)/alumn
        print(f"El porcentaje de aprobados es del {porcaprobs}%")
else:
    print("Hoy no se pudo haber tomado examen")
if dia_semana==semanadays[3]:
    print("Hoy es dia de practica hablada")
    asis=input("Ingrese el porcentaje de asistencias\n")
    asis=int(asis[0:asis.find("%")])
    if asis>50.0:
        print("Asitio la mayoria")
    else:
        print("No asistio la mayoria")
if dia_semana==semanadays[4] and dia==1 and (mes==1 or mes==7):
    print("Comienzo de nuevo ciclo")
    alumnew=int(input("Ingrese el numero de alumnos del nuevo ciclo\n"))
    aran=int(input("Ingrese el arancel por cada alumno\n"))
    arantotal=alumnew*aran
    print(f"El total del arancel es ${arantotal}")
