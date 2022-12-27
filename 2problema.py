class Vehiculo:

    def __init__(self, Color, Ruedas, Puertas):
        self.color = Color
        self.ruedas = Ruedas
        self.puertas = Puertas

class Coche(Vehiculo):
    def __init__(self, Color, Ruedas, Puertas, Velocidad, Cilindrada):
        super().__init__("Rojo", 4, 4)
        self.velocidad = Velocidad
        self.cilindrada = Cilindrada

    def info_completa(self):
        nota = f"El coche es de color {self.color}, cuenta con {self.puertas} puertas y {self.ruedas} ruedas. Ademas de {self.cilindrada} y alcanza {self.velocidad} Km/h"
        return nota
x = Coche("Rojo", 4, 5, 260, "V8")

print(x.info_completa())