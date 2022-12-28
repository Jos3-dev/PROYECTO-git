class Alumno():

    def __init__(self, nombre = "", nota = 0):
        self.nombre = nombre
        self.nota = nota

    def get_nombre(self):
        return self.nombre

    def get_nota(self):
        return self.nota

    def resultado(self):
        if self.nota >= 6:
            return f" El alumno {self.get_nombre()} ha APROBADO con: {self.get_nota()}"
        else:
            return f"El alumno {self.get_nombre()} NO HA APROBADO con: {self.get_nota()}"

nota = float(input("¿Cual es tu promedio?: "))
# nombre = input("¿Cual es tu nombre?: ")

a = Alumno("Jose", nota)
print(a.resultado())