class Dispositivo:
    def __init__(self, diccionario):
        self.id = 0
        self.marca = ''
        self.tipo = ''       #Los 3 son diccionarios 
        self.nombre = ''
       
    
    def dispositivo1(self):
        self.id = 1
        self.nombre = 'teclado'
        self.marca = 'genius'
    
    def dispostivo2(self):
        self.id = 2
        self.nombre = 'mouse'
        self.marca = 'logitech'

    def dispositivo3(self):
        self.id = 3
        self.nombre = 'memoria'
        self.tipo = 'ram'


#

#valor = diccionario.get(clave, default[es el valor por defecto])  