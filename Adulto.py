from familiar import Familiar
from cuenta_bancaria import CuentaBancaria
class Adulto(Familiar):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, cuenta,salario):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, paga=0)
        self.salario = salario

    def cobrar_nomina(self):
        self.cuenta.ingresar(self.salario)
        return f"{self.nombre} ha ingresado su salario de {self.salario}€. Saldo: {self.cuenta.saldo}€."

    def dar_paga(self, hijo, cantidad):
        if self.cuenta.retirar(cantidad):
            hijo.cuenta.ingresar(cantidad)
            return f"{self.nombre} le ha dado {cantidad}€ a {hijo.nombre}."
        return f"{self.nombre} no tiene fondos para la paga."

