import csv
from claseMenu import Menu
from claseManejadorTalleres import ManejadorTalleres
from claseManejadorInscripciones import ManejadorInscripciones
from claseManejadorPersonas import ManejadorPersonas

if __name__ == '__main__':
    manejadorT = ManejadorTalleres()
    manejadorP = ManejadorPersonas()
    manejadorI = ManejadorInscripciones()
    
    archivo = open('Talleres.csv')
    reader = csv.reader(archivo,delimiter=';')
    bandera = False
    for fila in reader:
        if not bandera:
            bandera = True
            cant = int(fila[0])
        else:
            manejadorT.addTaller(fila[0],fila[1],fila[2],fila[3])           
    archivo.close()

    miMenu = Menu()
    miMenu.define_menu('Menu de opciones',['[1]- Inscribir persona a taller','[2]- Consultar inscripcion','[3]- Consultar Inscriptos','[4]- Registrar pago','[5]- Guardar inscripciones','[0] - Salir'])
    miMenu.showMenu()
    op = miMenu.selectOption()

    while op != 0:
        if op == 1:
            #Agrego una nueva persona
            manejadorT.showTalleres()
            persona = manejadorP.addPersona() #Verifica si ya se encuentra en el sistema
            if persona != None:
                salir = False
                #Ingreso taller
                num = input('\nIngrese ID taller: ')
                taller = manejadorT.getTaller(num)
                while salir == False:
                    if taller != None:
                        #Verifico que el taller tenga vacantes disponibles
                        vacantes = manejadorT.getVacantes(num) 
                        #Verifico que no este ya inscripta en el taller
                        esta = manejadorI.buscarInsc(persona,taller)
                        if not esta and vacantes > 0:
                            manejadorT.restVacante(num)
                            manejadorI.addInscripcion(False,persona,taller)
                    #Consulto si desea inscribirse en otro taller
                    op1 = None
                    while op1 != 's' and op1 != 'n':
                        op1 = input('Desea inscribirse en otro taller? [S][N]: ')
                        if op1.lower() == 's':
                            #Ingreso taller
                            num = input('\nIngrese ID taller: ')
                            taller = manejadorT.getTaller(num)
                        elif op1.lower() == 'n':
                            salir = True               
            input('Presione ENTER para continuar...')
        #Consultar inscripción
        if op == 2:
            dni = input('Ingrese DNI: ')
            esta = manejadorP.buscarDNI(dni)
            if esta != None:
                persona = manejadorP.getPersona(esta)
                manejadorI.consultarInsc(persona)
            input('Presione ENTER para continuar...')
        #Consultar inscriptos
        if op == 3:
            manejadorT.showTalleres()
            num = input('\nIngrese ID taller: ')
            taller = manejadorT.getTaller(num)
            if taller != None:
                esta = manejadorI.consultarInscTaller(taller)
            input('Presione ENTER para continuar...')
        #Registrar pago
        if op == 4:
            dni = input('Ingrese DNI: ')
            esta = manejadorP.buscarDNI(dni)
            if esta != None:
                persona = manejadorP.getPersona(esta)
                manejadorI.consultarInsc(persona)
                num = input('\nIngrese ID taller: ')
                taller = manejadorT.getTaller(num)
                salir = False
                while salir == False:
                    if taller != None:
                        manejadorI.registrarPago(persona,taller)
                    #Consulto si desea abonar otro taller
                    op1 = None
                    while op1 != 's' and op1 != 'n':
                        op1 = input('Desea abonar otro taller? [S][N]: ')
                        if op1.lower() == 's':
                            #Ingreso taller
                            num = input('\nIngrese ID taller: ')
                            taller = manejadorT.getTaller(num)
                        elif op1.lower() == 'n':
                            salir = True  
            input('Presione ENTER para continuar...')
        
        #Guardar inscripciones en archivo
        if op == 5:
            archivo = open('Inscripciones.csv','a',newline='') #Crea el archivo o agrega al final si existe
            writer = csv.writer(archivo)
            #Obtengo la posicion del puntero, si es 0 agrego el header
            pos = archivo.tell()
            if pos == 0:
                header = ['Fecha','Pago','DNI','ID Taller']
                writer.writerow(header)
            data = manejadorI.getAllData()
            writer.writerows(data)
            archivo.close()
            print('Datos guardados')
            input('Presione ENTER para continuar...')
        miMenu.showMenu()
        op = miMenu.selectOption()
    

