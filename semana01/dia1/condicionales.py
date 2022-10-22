#ENTRADA
numero1 = input("Numero 1 :")
numero2 = input("Numero 2 :")
operacion = input("Operacion a ejecutar(suma,resta) : ")
#PROCESO
if(operacion =="suma" ) :
    resultado = int(numero1) + int(numero2)
elif(operacion == "resta"):
    resultado = int(numero1) - int(numero2)
else :
    resultado = ""
#SALIDA
if(resultado == ""):
    print("Debe ingresar una operacion valida")
else
    print("El resultado es : " + str(resultado))
print("adios!!!")
