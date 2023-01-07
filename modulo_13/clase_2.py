# Accediendo a los atributos de los objetos:
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
        
car_2 = car('tesla','model_Y','2019')
car_2.print_attributes()

####
dir(car_2)

####
print(car_2.make)

####
print(car_2.model)

####
print(car_2.year)

################################################################
class car:
    opus = 0
    
    def __init__(self,make,model,year):
        car.opus += 1
        self.make = make
        self.model = model
        self.year = year
        print('Una instancia de la clase se ha creado exitosamente')
        
    def print_attributes(self):
        print(f'Marca: {self.make}')
        print(f'Modelo: {self.model}')
        print(f'Año: {self.year}')

####
car_1 = car('tesla','model_G','2018')
car_2 = car('tesla','model_Y','2019')

####
print('Hay',car.opus,'opus creados')

####
car_3 = car('tesla','model_H','2017')

####
print('Hay',car.opus,'opus creados')

################################################################
class car:
    total = 0
    
    def __init__(self,make,model,year):
        car.total += 1
        self.make = make
        self.model = model
        self.year = year
        print('Una instancia de la clase se ha creado exitosamente')
    
    def __del__(self):
        car.total -= 1
        
    def print_attributes(self):
        print(f'Marca: {self.make}')
        print(f'Modelo: {self.model}')
        print(f'Año: {self.year}')
        
####
car_1 = car('tesla','model_G','2018')
car_2 = car('tesla','model_Y','2019')
car_3 = car('tesla','model_H','2017')
car_4 = car('tesla','model_F','2016')

####
print('Hay',car.total,'opus creados')

####
del car_4

####
print('Hay',car.total,'opus creados')

####
car.__del__()