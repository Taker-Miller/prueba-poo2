class Circulo:
    def __init__(self, radio):
        self.__radio = radio


    def calcularArea(self):
        return 3.14 * self.__radio ** 2
    
    def calcularPerimetro(self):
        return 2 * 3.14 * self.__radio
    
    def cambiarRadio(self):
        while True:
            opcion = input("quieres cambiar el radio?: s/n ")
            if opcion == "s":
                radio = float(input("ingrese nuevo radio: "))
                r = Circulo(radio)
                r.imprimir_resultados()
            elif opcion == "n":
                print("chao")
                break
            else:
                print("error")
    

    def imprimir_resultados(self):
        print(f"area: {self.calcularArea()}")
        print(f"perimetro: {self.calcularPerimetro()}")
        print(f"nuevo radio: {self.cambiarRadio()}")