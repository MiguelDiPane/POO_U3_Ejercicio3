class Persona:
    __nombre = ''
    __direccion = ''
    __dni = ''

    def __init__(self,nom='',dir='',dni=''):
        self.__nombre = nom
        self.__direccion = dir
        self.__dni = dni
    
    def getDni(self):
        return self.__dni
    def getNom(self):
        return self.__nombre
    
    def __str__(self):
        cadena = ' {0:^39}{1:^10}{2:^50}'.format(self.__nombre,self.__dni,self.__direccion)
        return cadena