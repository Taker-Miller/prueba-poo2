class Empleado:
    def __init__(self,nombre, hrs_trabajadas, salario_por_hr):
        self.__nombre = nombre
        self.__hrs_trabajadas = hrs_trabajadas
        self.__salario_por_hr = salario_por_hr

    def calcularSalario(self): 
        #Este método debe calcular y devolver el salario total del empleado. El salario total se calcula como el producto del salario por hora y las horas trabajadas.
        return self.__salario_por_hr + self.__hrs_trabajadas

    def verInformacion(self):
        print(f"nombre: {self.__nombre}")
        print(f"Salario total: {self.calcularSalario()}")