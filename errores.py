

class Persona:

    # PYTHON no tiene variables privadas, por naturaleza todas sus variables son publicas y de acceso libre; se cuenta con una convencion la cual es incluir doble "__"al inicio de la varible o metodo para indicar a otros desarrolladores que no deberian de acceder ni modificar dicho elemento (variable o metodo)
    __edad = 21
    __nombre = "Angel"
    __telefono = 6647519814

    def set_edad(self, edad):
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_edad(self):
        return self.edad

    def get_nombre(self):
        return self.nombre

    def get_telefono(self):
        return self.telefono


persona = Persona()

# dar valores a las variables
persona.set_edad(25)
persona.set_nombre("Esteban")
persona.set_telefono("6647519815")


# mostrar valores de variables
print(persona.get_edad())
print(persona.get_nombre())
print(persona.get_telefono())
