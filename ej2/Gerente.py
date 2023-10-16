from Empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, hrs_trabajadas, salario_por_hr, bono):
        super().__init__(nombre, hrs_trabajadas, salario_por_hr)
        self.__bono = bono
    def calcularSalario(self): 
        #un método llamado calcular_salario que tenga en cuenta tanto el salario por hora como el bono anual para calcular el salario total del gerente.
        return self.__salario_por_hr + self.__hrs_trabajadas + self.__bono
