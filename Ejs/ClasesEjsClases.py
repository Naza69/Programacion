class Motorcycle:
    state="nuevo"
    engine=False
    def __init__(self, color='', plate='', fuel_in_litters=0, wheels=2, brand='', model='', fabrication_date='', top_speed=100, weight=100):
        self.color=color
        self.plate=plate
        self.fuel_in_litters=fuel_in_litters
        self.wheels=wheels
        self.brand=brand
        self.model=model
        self.fabrication_date=fabrication_date
        self.top_speed=top_speed
        self.weight=weight
    def state_engine(self):
        if self.engine:
            return "El motor esta prendido"
        else:
            return "El motor esta apagado"
    
    @property
    def engine(self):
        return self.engine
    
    @engine.setter
    def engine(self, new_state_engine):
        self.engine = new_state_engine

    def stop(self):
        if self.engine:
            self.engine(False)
            return "Motor apagado"
        else:
            return "El motor ya esta apagado"

    def start_up(self):
        if self.engine==False:
            self.engine(True)
            return "Motor encendido"
        else:
            return "El motor ya esta encendido"