#1_

class Persona:
    def _init_(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        
        if nombre.strip() != "":
            self.nombre = nombre
        else:
            print("Error: El nombre no puede estar vacío.")

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        # Valida que la edad sea un número positivo
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("Error: La edad debe ser un número positivo.")

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):

        if isinstance(dni, int) and dni >= 0:
            self.dni = dni
        else:
            print("Error: El DNI debe ser un número positivo.")

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad >= 18

# MAIN
persona1 = Persona()
persona1.set_nombre("Juan Pérez")
persona1.set_edad(25)
persona1.set_dni(12345678)

persona1.mostrar()
if persona1.esMayorDeEdad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")

#---------------------------------------------------------------------
#2_

class Cuenta:
    def _init_(self, titular=None, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        
        if isinstance(titular, Persona):
            self.titular = titular
        else:
            print("Error: El titular debe ser una instancia de la clase Persona.")

    def get_titular(self):
        return self.titular

    def set_cantidad(self, cantidad):

        if isinstance(cantidad, (int, float)):
            self.cantidad = cantidad
        else:
            print("Error: La cantidad debe ser un número decimal.")

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print("Datos de la cuenta:")
        print(f"Titular: {self.titular.get_nombre()}")
        print(f"Cantidad: ${self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se ha ingresado ${cantidad:.2f} a la cuenta.")
        else:
            print("Error: La cantidad a ingresar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
            print(f"Se ha retirado ${cantidad:.2f} de la cuenta.")
        else:
            print("Error: La cantidad a retirar debe ser mayor que cero.")

class Persona:
    def _init_(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

persona1 = Persona("Juan Pérez", 30, "12345678")
cuenta1 = Cuenta(persona1, 1000.0)

cuenta1.mostrar()
cuenta1.ingresar(500.5)
cuenta1.retirar(300.75)

cuenta1.mostrar()

#---------------------------------------------------------------------
#3_

class Triangulo:
    def _init_(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtener_lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

def ingresar_datos_triangulo():
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    lado3 = float(input("Ingrese la longitud del tercer lado: "))
    return lado1, lado2, lado3


print("Ingrese los datos del triángulo:")
lado1, lado2, lado3 = ingresar_datos_triangulo()

triangulo = Triangulo(lado1, lado2, lado3)

print(f"El lado con mayor longitud es {triangulo.obtener_lado_mayor()}")
print(f"El triángulo es de tipo {triangulo.determinar_tipo()}")

#---------------------------------------------------------------------
#4_

class Contacto:
    def _init_(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def _init_(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto añadido exitosamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Email: {contacto.email}")
                print("")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Contacto encontrado:")
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Email: {contacto.email}")
                return
        print("Contacto no encontrado.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print("Contacto editado exitosamente.")
                return
        print("Contacto no encontrado.")


agenda = Agenda()

while True:
    print("\nMenú de Agenda:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        agenda.añadir_contacto(nombre, telefono, email)
    elif opcion == "2":
        agenda.listar_contactos()
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto a editar: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")
        nuevo_email = input("Ingrese el nuevo email: ")
        agenda.editar_contacto(nombre, nuevo_telefono, nuevo_email)
    elif opcion == "5":
        print("Agenda cerrada.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")