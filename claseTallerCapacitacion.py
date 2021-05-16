class TallerCapacitacion:
    __idTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0

    def __init__(self,idT=0,nom='',vac=0,monto=0):
        self.__idTaller = idT
        self.__nombre =  nom
        self.__vacantes = vac
        self.__montoInscripcion = monto
    
    def __str__(self):
        cadena ='{0!s:^12}{1:45}{2!s:^9}{3!s:^22}'.format(self.__idTaller, self.__nombre,self.__vacantes,self.__montoInscripcion)
        return cadena
    def getId(self):
        return self.__idTaller
    def getNom(self):
        return self.__nombre
    def getMonto(self):
        return self.__montoInscripcion
    def getVacantes(self):
        return self.__vacantes
    def restVacante(self,cant):
        self.__vacantes -= cant