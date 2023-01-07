def returning_message(id_article,id_market):
    '''
    Esta función de acuerdo a los parametros, debe retornar un mensaje (message), ya que por ejemplo, id_article
    representará la identificación de un articulo y el id_market la de un mercado en especifico, y si esque 
    id_article fuera igual a '1' y id_market fuese igual a '3' significaría que el usario intenta comprar una 
    pierna de jamon y la funcion finalmente retornará un mensaje que diría Piernas de jamon.
    '''
    message = ''
    if id_article == '1' and id_market == '1':
        message = 'Bolsas de papas'
    elif id_article == '2' and id_market == '1':
        message = 'Chocolates'
    elif id_article == '3' and id_market == '1':
        message = 'Refrescos'
    elif id_article == '1' and id_market == '2':
        message = 'Pasteles'
    elif id_article == '2' and id_market == '2':
        message = 'PCs'
    elif id_article == '3' and id_market == '2':
        message = 'Mochilas'
    elif id_article == '1' and id_market == '3':
        message = 'Pares de lentes'
    elif id_article == '2' and id_market == '3':
        message = 'Envases de yogurt'
    elif id_article == '3' and id_market == '3':
        message = 'Piernas de jamon'
    return message
            

def printing_articles(shooping_cart,id_market):
    'Esta función al final lo que retornará será '
    ticket_list = []
    cont = -1
    for article in shooping_cart:
        cont += 1
        if '1' == article[0]:
            ticket_list.append([])
            ticket_list[cont].append(returning_message('1',id_market))
            ticket_list[cont].append(article[1])
        elif '2' == article[0]:
            ticket_list.append([])
            ticket_list[cont].append(returning_message('2',id_market))
            ticket_list[cont].append(article[1])
        elif '3' == article[0]:
            ticket_list.append([])
            ticket_list[cont].append(returning_message('3',id_market))
            ticket_list[cont].append(article[1])
    return ticket_list

# actividad para em modulo -> 13:

super_market = {
  '1.- Bolsa de papas': 10,
  '2.- Chocolate': 6,
  '3.- Refresco': 8
}

super_market_two = {
  '1.- Pastel': 20,
  '2.- PC': 100,
  '3.- Mochila': 30
}

super_market_three = {
  '1.- Par de Lentes': 22,
  '2.- Envase de yogurt': 12,
  '3.- Pierna de jamon': 18
}

class user:
    number_users = 0
    # aqui declaramos una clase con los atributos name para el nombre de un nuevo usario, id para la 
    # identificación personal de un usario y card_num para el numero de tarjeta de credito del usario
    def __init__(self,name,id,card_num):
        user.number_users += 1
        self.name = name
        self.id = id
        self.card_num = card_num
    
    def __str__(self):
        'Funcion que expondrá toda la información basica de nuestro usario: '
        
        print(f'''El usuario se llama {self.name}
El usuario {self.name} esta actualmente identificado como {self.id}
El usuario {self.name} esta sujeto a la tarjeta con la identificacion: {self.card_num['num']}''')
    
    def print_balance(self):
        'Función para mostrar la cantidad de saldo con la que cuenta un usuario: '
        
        print(f'''El usuario {self.name} cuenta con un saldo de {self.card_num['balance']}''')
    
    def print_count(self):
        'Función para mostrar la cantidad de saldo que debe pagar actualmente un usario: '
        
        print(f'''El usuario {self.name} actualmente debe {self.card_num['count']}''')

################################################################
class buyer(user):  
    # aqui declaramos una clase que desde luego que va aheredar los atributos de la 1er clase user, sin embargo 
    # también tendrá incluidos sus propios atributos como son el shooping_cart donde se esperará como parametro 
    # una lista de listas, cada una con dos elementos, el 1ro que representará el índice del producto y el 2do
    # el numero de veces que viene contenido el producto, como por ejemplo:
    # si tomamos de referencia el mercado numero 2, la siguiente lista significaría lo siguiente:
    # [[1,3],[2,4],[3,5]]
    # 3 pasteles, 4 PC y 5 mochilas
    def __init__(self,name,id,card_num,shooping_cart):
        super().__init__(name,id,card_num)
        self.shooping_cart = shooping_cart
    
    # def print_articles(self):
        