#crear una clase
class Automovil :
    #crrear atributos
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar

    #crear metodos
    def encender(self) :
        print('encender ' + self.marca)

    def avanzar(self) :
        print('avanzar ' + self.marca)
    
    def acelerar(self) :
        print('acelerar ' + self.marca)

    def frenar(self) :
        print('frenar ' + self.marca)
    
##creamos objetos
vw = Automovil(1970,"cH-1234","Amarillo","Volkswagen")
tico = Automovil(1985, "AB-124","rojo","tico")

vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()

tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()