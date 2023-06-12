import unittest
#Escribir la funcionalidad de lo que tenemos que hacer
from dispositivo import Dispositivo
from database import Database


class MyTest(unittest.TestCase):

    def setUp(self):
        dispositivo_1 = {
            "id": 1,
            "nombre": "teclado",      
            "marca": "genius",
        }
        dispositivo_2 = {
            "id": 2,
            "nombre": "mouse",         #Dicionario de dispositivos
            "marca": "logitech",
        }
        dispositivo_3 = {
            "id": 3,
            "nombre": "memoria",
            "tipo": "ram",
        }

        self.database_template = {"dispositivos": [
            dispositivo_1,                                 #Diccionario que tiene una lista que tiene un diccionario que tiene 3 diccionarios
            dispositivo_2,      #Lista de 3 diccionarios que crea objetos 
            dispositivo_3,
        ]}

        self.dispositivo_1 = Dispositivo(1, "teclado", "genius")  #Crea un objeto
        self.dispositivo_2 = Dispositivo(2, "mouse", "logitech")  
        self.dispositivo_3 = Dispositivo(diccionario=dispositivo_3)  #Manda un diccionario como parametro, constructor que puede recibir un diccionario
        self.dispositivo_4 = Dispositivo(
            4, "placa de red", tipo="wireless", marca="tp-link")   

    def compare_dispositivos(self, dispositivo_1: Dispositivo, dispositivo_2: Dispositivo):  
        if dispositivo_1.id != dispositivo_2.id:
            return False
        if dispositivo_1.nombre != dispositivo_2.nombre:
            return False
        if dispositivo_1.marca != dispositivo_2.marca:     #El diccionario esta para despistar, tiene 4 atributos (ID,nombre,marca,tipo)
            return False                                   
        if dispositivo_1.tipo != dispositivo_2.tipo:
            return False
        return True

    def test_create_database(self):                         #Ver si se crea la base de datos, que tenga un constructor que va a recibir un diccionario que es una lista de diccionarios donde por cada uno de los elementos se generan un objeto dispositivo
        database = Database(self.database_template)
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))          #En el 0 va el 1, etc. Asi se crean las base de datos 
        self.assertTrue(self.compare_dispositivos(              
            self.dispositivo_2, database.database[1]))          #Se sabe que es un diccionario por los corchetes 
        self.assertTrue(self.compare_dispositivos(              
            self.dispositivo_3, database.database[2]))

    def test_delete_by_id(self):                             #Recibir como parametro el id, recorrer los objetos de la lista y eliminarla
        database = Database(self.database_template)
        database.delete_by_id(id=2)
        self.assertEqual(len(database.database), 2)         
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_3, database.database[1]))

    def test_add_dispositivo(self):                         #Mandar como parametro un dispositivo y agregarlo a final
        database = Database(self.database_template)
        database.add_dispositivo(self.dispositivo_4)
        self.assertEqual(len(database.database), 4)
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_2, database.database[1]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_3, database.database[2]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_4, database.database[3]))

    def test_add_diccionario(self):
        diccionario = {
            "id": 5,
            "nombre": "placa de video",
            "tipo": "pci-e",
            "marca": "ati",
        }
        database = Database(self.database_template)
        database.add_dispositivo(diccionario=diccionario)
        self.assertEqual(len(database.database), 4)
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_1, database.database[0]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_2, database.database[1]))
        self.assertTrue(self.compare_dispositivos(
            self.dispositivo_3, database.database[2]))
        self.assertTrue(self.compare_dispositivos(
            Dispositivo(diccionario=diccionario), database.database[3]))


if __name__ == '__main__':
    unittest.main()