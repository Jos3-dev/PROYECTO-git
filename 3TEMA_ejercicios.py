
##### PRIMER PARTE ##############

def sumatoria(param1, param2, param3):
    return param1 + param2 + param3

sumatoria(15, 15, 20.5)



##### SEGUNDA PARTE ##############

class COCHE:

    def __init__(self, puertas):
        self.puertas = puertas

    puertas = 5

    def agrega_puertas(self):
        self.puertas += 1
        return self.puertas

    def quitar_puertas(self):
        self.puertas -= 1
        return self.puertas

    def info_completa(self):
        return f"Ahora el vehiculo tiene '{self.puertas}' puertas"


coche = COCHE(5)  # coche que tiene 5 puertas inicialmente

coche.agrega_puertas()
print(coche.info_completa())
