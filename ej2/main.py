from Empleado import Empleado
from Gerente import  Gerente
print("1- empleado")
print("2- gerente")
opcion = input("ingresa una opcion: ")
if opcion =="1":
    nombre = input("ingresa nombre empleado: ")
    hrs_trabajadas = int(input("ingresa hrs trabajadas: "))
    salario_por_hr = int(input("ingresa salario por hr: "))
    e = Empleado(nombre, hrs_trabajadas, salario_por_hr)
    e.verInformacion()
elif opcion =="2":
    nombre = input("ingresa nombre empleado: ")
    hrs_trabajadas = int(input("ingresa hrs trabajadas: "))
    salario_por_hr = int(input("ingresa salario por hr: "))
    bono = int(input("ingresa bono: "))
    g = Gerente(nombre, hrs_trabajadas, salario_por_hr, bono)
    g.verInformacion()
else:
    print("error")