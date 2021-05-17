class Inscripcion:
    __fechaInscripcion = None
    __pago = False
    __persona = None
    __taller = None

    def __init__(self,fecha=None,pago=False,persona=None,taller=None):
        self.__fechaInscripcion = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def __str__(self):
        if self.__pago:
            pago = 'Si'
        else:
            pago = 'NO'
        cadena = '{0!s:11}{1:3}{2} {3}'.format(self.__fechaInscripcion,pago,self.__persona,self.__taller)
        return cadena
    
    def getPersona(self):
        return self.__persona
    def getTaller(self):
        return self.__taller
    def getPago(self):
        return self.__pago
    def setPago(self):
        self.__pago = True
    def getFecha(self):
        return self.__fechaInscripcion