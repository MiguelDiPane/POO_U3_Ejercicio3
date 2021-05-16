from claseTallerCapacitacion import TallerCapacitacion

class ManejadorTalleres:
    __talleres = []

    def __init__(self):
        self.__talleres = []

    def addTaller(self,idT,nom,vac,monto):
        try:
            idT = int(idT)
            vac = int(vac)
            monto = int(monto)
            newTaller = TallerCapacitacion(idT,nom,vac,monto)
            self.__talleres.append(newTaller)
        except ValueError:
            print('Error: No se pudo cargar el taller')
     
    def getIdTalleres(self):
        ids = []
        for taller in self.__talleres:
            ids.append(taller.getId())
        return ids

    def validarNum(self,num):
        valido = None
        try: 
            num = int(num)
            ids = self.getIdTalleres()
            if num in ids:
                valido = num - 1 #Retorno indice del curso
            else:
                print('Error: El ID no corresponde a un curso existente')    
        except ValueError:
            print('Error: El ID no corresponde a un curso existente') 
        return valido

    def getTaller(self,num):
        taller = None
        valido = self.validarNum(num)
        if valido != None:
            taller = self.__talleres[valido]
        return taller
    
    def getVacantes(self,num):
        vacantes = 0
        valido = self.validarNum(num)
        if valido != None:
            vacantes = self.__talleres[valido].getVacantes()
            if vacantes == 0:
                print('No hay vacantes disponibles.')
        return vacantes        

    def restVacante(self,num):
        valido = self.validarNum(num)
        if valido != None:
            #Resta uno a las vacantes
            self.__talleres[valido].restVacante(1) 

    def showTalleres(self):
        #----Encabezado de la lista de talleres----#
        header ='+' + '-'*88 + '+'
        print(header)
        print('|{0:^88}|'.format('Talleres disponibles'))
        print(header)
        print('|{0:^12}{1:^45}{2:^9}{3:^22}|'.format('ID Taller','Nombre','Vacantes','Monto Inscripcion [$]'))
        print(header)
        #---Muestro talleres---#
        for taller in self.__talleres:
            print('|{0}|'.format(taller))
        print(header)