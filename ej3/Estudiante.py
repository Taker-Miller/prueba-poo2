class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.__nombre = nombre
        self.__edad = edad
        self.__promedio = promedio
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    