

class Persona:

    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getTelefono(self):
        return self.telefono

class Cliente(Persona):

    def __init__(self, nombre, edad, telefono, credito):
        super().__init__(nombre, edad, telefono)
        self.credito = credito

    def get_total(self):
        return f"{self.nombre}, {self.edad}, {self.telefono}, {self.credito}"


class Trabajador(Persona):
    def __init__(self, nombre, edad, telefono, salario):
        super().__init__(nombre, edad, telefono)
        self.salario = salario

    def get_total(self):
        return f"{self.nombre}, {self.edad}, {self.telefono}, {self.salario}"


objeto_Principal = Cliente("jose", 21, 6647519815, 65000)
print(objeto_Principal.get_total())

# INFO TRABAJADOR CON SALARIO
objeto_trabajador = Trabajador("Angel", 25, 6647519816, 98000)
print(objeto_trabajador.get_total())
