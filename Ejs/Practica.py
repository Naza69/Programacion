class Naza:
    #AKSJDBAKJSBDAHSBDJANSBDUAHSDUA
    species="Humano"
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.__getName=name
    @property
    def getName(self):
        return self.__getName
    #AISJGBAKSJDBAJSHBDJASBDJANSBD
    @getName.setter
    def setName(self, new_name):
        return self.__getName==new_name
    #IAJSDKAJSBDIAHSDJASHDIAJSD
    def hello(self):
        return f"Hola {self.name}"
lapersona=Naza("Nazareno", 18)
print(lapersona.getName)

