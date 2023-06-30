import numpy
import funciones as fn
edificio = numpy.zeros((2,5),int)
lista_ruts = []
lista_nombre = []
lista_identificador = []
lista_dias = []
lista_piso = []
lista_columna = []



while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion == 1:
        rut = fn.validar_rut()
        nombre = fn.validar_nombre()
        dias = fn.validar_dias()
        identificador = fn.validar_identificador()
        piso = fn.reservar_asiento()


        lista_ruts.append(rut)
        lista_nombre.append(nombre)
        lista_dias.append(dias)
        lista_identificador.append(identificador)
        lista_piso.append(piso)
        print("Registro con exito! ")
       
       

        


    elif opcion == 2:
        rut = int("Ingresar el rut: ")
        if rut in lista_ruts:
            print(f"{rut},{nombre},{dias},{identificador}")

        else:
            print("El rut no esta en la lista")
            
    elif opcion == 3:
        precio = dias * 15.000
        dinero = input("Ingrese el dinero con el que va a pagar: ")
        if dinero >= precio:
            print("Compra realizada con exito, muchas gracias! ")
        else:
            print("Dinero insuficiente")
            break

    
    else:
        break

    

    
 


