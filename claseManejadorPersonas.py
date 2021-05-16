from clasePersona import Persona

class ManejadorPersonas:
    __personas = []

    def __init__(self):
        self.__personas = []
    
    def addPersona(self):
        dni = input('Ingrese dni: ')
        pos = self.buscarDNI(dni)
        if dni.isdigit():
            if pos == None:
                print('Datos personales requeridos:')
                nombre = input('Ingrese nombre: ')
                direccion = input('Ingrese direccion: ')
                persona = Persona(nombre,direccion,dni)
                self.__personas.append(persona)
            else:
                print('La persona ya se encuentra en el sistema')
                persona = self.__personas[pos]
        else:
            persona = None
        return persona
    
    #Busca el DNI y retorna la posicion en lista personas, None si no esta o es invalido
    def buscarDNI(self,dni):
        if dni.isdigit():
            i = 0
            esta = False
            while i < len(self.__personas) and not esta:
                if dni == self.__personas[i].getDni():
                    esta = True
                else:
                    i +=1
            if not esta:
                print('La persona NO se encuentra en el sistema.\n')
                i = None
        else:
            print('El dni no es valido\n')
            i = None
        return i #Retorno el indice de la persona o None si no esta

    #Obtiene persona segun indice
    def getPersona(self,indice):
        persona = self.__personas[indice]
        return persona

