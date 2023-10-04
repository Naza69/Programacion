def primenumberlocaltwo(primelocal):
    divscounterlocal=0
    for number in range(1, 10):
        if primelocal%number==0:
            divscounterlocal+=1
    if divscounterlocal>2:
        return True
    else:
        return False
def factorialtwo(numberlocal):
    factoriallocal=1
    for values in range(1, numberlocal+1):
        factoriallocal*=values
    return factoriallocal
def digitinnumbertwo(digitlocal, numberlocal):
    counterlocal=0
    for elem in str(numberlocal):
        if str(digitlocal)==elem:
            counterlocal+=1
    return counterlocal
def digitssum(numberlocal):
    sumlocal=0
    for number in str(numberlocal):
        sumlocal+=int(number)
    return sumlocal
while True:
    try:
        number=int(input("Ingrese un numero primo\n"))
        digit=int(input("Ingrese un digito para saber la cantidad de sus ocurrencias en el numero ingresado\n"))
        if primenumberlocaltwo(number)==True:
            break
        print(f"La suma de los digitos del numero ingresado son {digitssum(number)}")
        print(f"El digito ingresado tiene {digitinnumbertwo(digit, number)} ocurrencia/s en el numero ingresado")
        print(f"El factorial de {number} ingresado es {factorialtwo(number)}")
        print("El numero ingresado es primo!")
    except ValueError:
        print("Alguno de los valores ingresados no son enteros, o no son numericos, intente de nuevo")
        continue
print(f"La suma de los digitos del numero ingresado son {digitssum(number)}")
print(f"El digito ingresado tiene {digitinnumbertwo(digit, number)} ocurrencia/s en el numero ingresado")
print(f"El factorial de {number} ingresado es {factorialtwo(number)}")
print("El numero ingresado no era primo!")
print("Finalizando...")