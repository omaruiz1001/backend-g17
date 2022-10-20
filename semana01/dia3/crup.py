import os
import time
from libCrup import *
"""
CRUD
C = CREATE
R = READ
U = UPDATE
D = DELETE
"""
alumno = {
    'nombre':'César Mayta',
    'email':'cesarmayta@gmail.com',
    'celular':'9992222'

   
}


listaAlumnos = [alumno]

opcion = "0"
while(opcion != "5"):
    if(opcion != "0"):
        time.sleep(1)
        os.system("clear")
    #mostrarMenu
    mostrarMenu()
    opcion = input("INGRESE UN OPCIÓN DEL PROGRAMA : ")
    os.system("clear")
    if(opcion == "1"):
        #insertarAlumno
        insertarAlumno(listaAlumnos)
    elif(opcion == "2"):
        #mostrarAlumnos
        mostrarAlumno(listaAlumnos)
         input('presione un tecla para continuar ...')   
    elif(opcion == "3"):
       valorBusqueda = input ('Ingrese el email de alumno a actualiar')  
        posicionBusqueda = buscarAlumno(valorBusqueda,listaAlumnos)

        if(posicionBusqueda == -1)
            print('No se encontro el alumno con el email ingresado :-(')
        else:
            #actualizar alumno
            actualizarAlumno(listaAlumnos,posicionBusqueda)
            
    elif(opcion == "4"):
        print("[4] ELIMINAR ALUMNO")
        #PASO 1 : Buscar por el diccionario el email para eliminar
    elif(opcion == "5"):
        print(" [5] ESTA SALIENDO DEL PROGRAMA ...")
    else:
        print(" OPCIÓN NO VALIDA !!!!!!")