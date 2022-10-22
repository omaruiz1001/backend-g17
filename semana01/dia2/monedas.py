#PROGRAMA PARA CONVERTIR MONEDAS POR EL TIPO DE CAMBIO
#SOLES A DOALRES Y VICEVERSA
#ENTRADA
option = 0
while(opcion !=3)
print ("""
================================================
        CONVERTIDOR DE MONEDAS VERSION 1.0
================================================
OPCION 1 : Convertir de soles a dolares
OPCION 2 : Convertir de dolares a soles 
================================================
""")
opcion = int(input("Ingrese una opccion segun el menu : "))
#PROCESO
if(opcion == 1) :
    #CONVERTIR DE SOLES A DOLARES
    montoOrigen = input("Ingrese monto en soles :")
    montoDestino = float (montoOrigen) / 3.8
    monedaDestino = "Dolares"
    
elif(opcion == 2):
    #CONVERTIR DE DOLARES A SOLES
    montoOrigen = float(input("Ingrese monto en soles :"))
    montoDestino = montoOrigen *  3.9
    monedaDestino = "Soles"
   
else:
    print("debe ingresar una opcion valida ...")
    
#SALIDA
print("El monto en " + monedaDestino + " es " + str(montoDestino))