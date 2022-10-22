class Persona :
    def __init__(self,nom,ema,cel) :
        self.nombre = nom
        self.email = ema
        self.celular = cel

    def mostrar(self) :
        print("Nombre : " + self.nombre)

class Alumno(Persona) :
    def matricular(self,cur) :
        self.curso = cur
        print("alumno matriculado en el curso" + self.curso)

#objetos
nuevoAlumno = Alumno ("Jose Perez","jose@gmail.com","434343")
nuevoAlumno.mostrar()
nuevoAlumno.matricular("REACT")