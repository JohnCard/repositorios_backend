# Introducción

class car:
    make = 'Tesla'
    model = 'Model_3'
    year = '2022'
    
    def turn_off():
        pass
    
    def turn_on():
        pass
    
################################################################

car_1 = car()
car_2 = car()
car_3 = car()

dir(car_1)

################################################################

# Creando clases
class car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        print('Una instancia de la clase se ha creado exitosamente')
        
    def print_attributes(self):
        print(f'Marca: {self.make}')
        print(f'Modelo: {self.model}')
        print(f'Año: {self.year}')
        
####
car_1 = car('tesla','modelo_3','2022')
####
car_1.print_attributes()