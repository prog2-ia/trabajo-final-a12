from Adulto import Adulto

class Padre(Adulto):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, salario):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, salario)
        self.dinero_ahorrado = 0

    def trabajo_extra(self, horas, precio_hora=20):
        ganancia = horas * precio_hora
        self.cuenta.ingresar(ganancia)
        return f"Ingreso extra: {ganancia}€. Saldo actual: {self.cuenta.saldo}€."