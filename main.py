class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cont = 0
        for i in self.asientos: 
            if type(i) == Asiento:
                cont += 1
        return cont

    def verificarIntegridad(self):
        a = 0
        for i in self.asientos:
            if type(i) == Asiento:
                if a == 0: a = i.registro
                elif a != i.registro: return("Las piezas no son originales")

        if a == self.motor.registro and self.motor.registro == self.registro:
            return("Auto original")                  
                
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, newColor):
        if newColor == "rojo" or newColor == "verde" or newColor == "amarillo" or newColor == "negro" or newColor == "blanco": self.color = newColor 

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, newRegistro):
        self.registro = newRegistro
    
    def asignarTipo(self, newTipo):
        if newTipo == "electrico" or newTipo == "gasolina": self.tipo = newTipo