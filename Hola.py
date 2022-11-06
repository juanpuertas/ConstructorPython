class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class coche(Vehiculo):
    def Velocidad(self, velocidad):
        self.velocidad=velocidad
    def Cilindridad(self, cilindridad):
        self.cilindridad=cilindridad
    def estado(self):
        print("Color: ", self.color, "\nRuedas: ", self.ruedas, "\nPuertas: ", self.puertas, "\nVelocidad: ", self.velocidad, "\nCilindridad: ", self.cilindridad)



miCoche1 = coche("Rojo", 4, 4)
miCoche1.Velocidad("100km")
miCoche1.Cilindridad("500cc")
miCoche1.estado()