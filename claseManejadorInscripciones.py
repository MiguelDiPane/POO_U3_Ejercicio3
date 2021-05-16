from datetime import date
from claseInscripcion import Inscripcion
from clasePersona import Persona
from claseTallerCapacitacion import TallerCapacitacion

class ManejadorInscripciones:
    __inscripciones = []


    def __init__(self):
        self.__inscripciones = []
    
    def addInscripcion(self,pago,persona,taller):
        if type(pago) == bool and type(persona) == Persona and type(taller) == TallerCapacitacion:
            #Coloco la fecha del momento en que se realiza la inscripcion
            hoy = date.today()
            newInscripcion = Inscripcion(hoy,pago,persona,taller)
            self.__inscripciones.append(newInscripcion)
            print('Inscripcion creada correctamente')
        else:
            print('No se pudo crear la inscripcion')
    
    def consultarInsc(self,miPersona):
        #----Encabezado de la ficha de inscripcion----#
        header ='+' + '-'*74 + '+'
        print(header)
        print('|{0:^74}|'.format('Ficha inscripciones'))
        print(header)
        print('| DNI: {0:68}|'.format(miPersona.getDni()))
        print(header)
        print('|{0:^5}{1:50}{2:19}|'.format('ID','Nombre taller','Monto adeudado [$]'))
        print(header)
        #---Busco inscripciones---#
        hay = False
        for inscripcion in self.__inscripciones:
            persona = inscripcion.getPersona()
            if miPersona == persona:
                hay = True
                taller = inscripcion.getTaller()
                idTaller = taller.getId()
                nombre = taller.getNom()
                if inscripcion.getPago():
                    deuda = 0
                else:
                    deuda = taller.getMonto()
                print('|{0!s:^5}{1:50}{2:^19}|'.format(idTaller,nombre,deuda))
        if not hay:
            print('|{0:74}|'.format('La persona no tiene inscripciones'))
        print(header)
     
    #Busco si la persona ya esta inscripta en el taller
    def buscarInsc(self,miPersona,miTaller):
        i = 0
        esta = False
        while i < len(self.__inscripciones) and not esta:
            taller = self.__inscripciones[i].getTaller()
            persona = self.__inscripciones[i].getPersona()
            if miPersona == persona and miTaller == taller:
                esta = True
            else:
                i +=1
        if esta:
            print('La persona ya se encuentra inscripta en el taller!')
        return esta
    
    def consultarInscTaller(self,miTaller):
        #----Encabezado de la ficha de inscripcion----#
        header ='+' + '-'*100 + '+'
        print(header)
        print('|{0:^100}|'.format('Ficha inscriptos taller'))
        print(header)
        print('|Nombre: {0:92}|'.format(miTaller.getNom()))
        print(header)
        print('|{0:^40}{1:^10}{2:^50}|'.format('Nombre','DNI','Direccion'))
        print(header)
        #---Busco inscripciones---#
        hay = False
        for inscripcion in self.__inscripciones:
            taller = inscripcion.getTaller()
            if miTaller == taller:
                persona = inscripcion.getPersona()
                print('|{0}|'.format(persona))
                hay = True
        if not hay:
            print('|{0:100}|'.format('No hay inscriptos en este taller'))
        print(header)

    def registrarPago(self,miPersona,miTaller):
        i = 0
        fin = False
        while i < len(self.__inscripciones) and not fin:
            persona = self.__inscripciones[i].getPersona()
            taller = self.__inscripciones[i].getTaller()
            if miPersona == persona and miTaller == taller:
                pago = self.__inscripciones[i].getPago()
                if pago:
                    print('Ya ha abonado el taller!')
                else:
                    self.__inscripciones[i].setPago()
                    print('Taller abonado correctamente!')
                fin = True
            else:
                i+=1
        if i == len(self.__inscripciones):
            print('{} no esta inscrito en el taller {}'.format(miPersona.getNom(),miTaller.getId()))
    
    #Obtengo todos los datos necesarios para guardar en archivo
    def getAllData(self):
        data = []      
        for inscripcion in self.__inscripciones:
            fecha = inscripcion.getFecha()
            pago = inscripcion.getPago()
            persona = inscripcion.getPersona()
            dni = persona.getDni()
            taller = inscripcion.getTaller()
            idTaller = taller.getId()
            if pago:
               pago = 'SI'
            else:
                pago = 'NO'
            fila = [fecha,pago,dni,idTaller]
            data.append(fila)
        return data