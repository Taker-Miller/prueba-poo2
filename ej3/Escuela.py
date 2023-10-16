from Estudiante import Estudiante
class Escuela:
    def __init__(self, lista_estudiantes):
        self.__lista_estudiantes = lista_estudiantes
    
    def agregarEstudiante(self):
        self.__lista_estudiantes = []
        nombre = input("ingresa nombre: ")
        while True:
            try:
                edad = int(input("ingresa la edad: "))
                break
            except:
                print("valor invalido")
            try:
                promedio = float(input("ingresa promedio: "))
                e = Estudiante(nombre,edad,promedio)
                self.__lista_estudiantes.append(e)
                break
            except:
                print("valor no valido")
        #A continuación, crea una clase llamada Escuela que tenga una lista de estudiantes como atributo. La clase Escuela debe tener los siguientes métodos:
#1.	agregar_estudiante: Este método debe permitir agregar un objeto de la clase Estudiante a la lista de estudiantes de la escuela.
#2.	listar_estudiantes: Este método debe mostrar una lista de todos los estudiantes en la escuela con su nombre, edad y promedio.

    
    def listarEstudiante(self):
        pass
