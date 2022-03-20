class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = 0

    def cantidadAsientos(asientos):
        return asientos.len()
    
    def verificarIntegridad(self, motor, asientos):
        a = ""
        for i in len(asientos): 
                if a == "": a = asientos.registro
                elif a != asientos.registro: print("Las piezas no son originales")
        if self.registro == motor.registro and self.registro == a: print("Vehiculo original")
        

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, newColor):
        if newColor == "rojo" or newColor == "amarillo" or newColor == "negro" or newColor == "blanco": self.color = newColor 

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, newRegistro):
        self.registro = newRegistro
    
    def asignarTipo(self, newTipo):
        if newTipo == "electrico" or newTipo == "gasolina": self.tipo == newTipo
