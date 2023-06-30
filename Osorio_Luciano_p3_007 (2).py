#Funciones
import numpy
edificio = numpy.zeros((2,5),int)

def mostrar_menu():
    print("""MENU:
    1- Grabar
    2- Buscar
    3- Retirarse
    4- Salir""")


def validar_opcion():
    opc = int(input("Ingrese su opcion: "))  
    if opc in (1,2,3,4):
        return opc
    else:
        print("Opcion incorrecta")


def mostrar_asientos():
    print("       A B C D")
    for x in range (2):
        print(x)
        for y in range (5):
            print(y,end=" ")

            
def reservar_asiento():
    print(edificio)
    piso = input("Ingrese el numero de la fila: ")      
    columna = input("Ingrese la columna: ")      
    posicion = piso and columna
    if [piso] [columna] == 0:
        [piso] [columna] = 1
        
    else:
        print("Esta ocupado")    
        
          

def validar_nombre():
    nombre = input("Ingrese su nombre: ")     
    if len(nombre) > 3 and nombre.isalpha:
        return nombre
    else:
        print("Su nombre no es valido")   

def validar_identificador():
    try:
        indentificador = int(input("Cree su identificador unico:  "))        
        if 1 in indentificador:
            return indentificador
        else:
            print("Identificador unico invalido")
    except:
        print("ERROR!")        


def validar_dias():
    dias = int(input("Ingrese la cantidad de dias: "))    
    if dias > 0:
        return dias
    else:
        print("Debe ingresar un numero valido")    

def validar_piso():
    piso = input("Ingrese el piso")




def validar_columna():
    columna = input("Ingrese la columna")    

def validar_rut():
        rut = int(input("Ingrese su rut: "))
        if rut > 100000000 and rut < 999999999:
            return rut
        else:
            print("Rut invalido")
    