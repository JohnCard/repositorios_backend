class car:
    super_attribute = 'Atributo de la super/ clase padre'
    
    def __init__(self):
        print('Una instancia de la super clase padre exitosamente')
    
    def super_method(self):
        print('Método de la super clase padre')
        
class collection_car(car):
    sub_attribute = 'Atributo de la sub clase hija'
    
    def __init__(self):
        print('Una instancia de la sub clase hija exitosamente')
    
    def sub_method(self):
        print('Método de la sub clase hija')
        
################################################################
sub_car = collection_car()

################################################################
sub_car.super_method()
sub_car.sub_method()
print(sub_car.super_attribute)
print(sub_car.sub_attribute)

################################################################
class sub_collection_car(collection_car):
    sub_sub_attribute = 'Atributo de la sub clase sub'
    
    def __init__(self):
        print('Una instancia de la sub_sub clase nieta')
    
    def sub_sub_method(self):
        print('Método de la sub_sub clase nieta')
        
################################################################
sub_sub_car = sub_collection_car()

################################################################
sub_sub_car.super_method()
sub_sub_car.sub_method()
sub_sub_car.sub_sub_method()
print(sub_sub_car.super_attribute)
print(sub_sub_car.sub_sub_attribute)