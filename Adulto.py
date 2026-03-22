from familiar import Familiar
from cuenta_bancaria import CuentaBancaria
class Adulto(Familiar):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, cuenta,salario):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, paga=0)
        self.salario = salario
        self.dias_trabajados = 0

    def cobrar_nomina(self):
        self.cuenta.ingresar(self.salario)
        return f"{self.nombre} ha ingresado su salario de {self.salario}€. Saldo: {self.cuenta.saldo}€."

    def realizar_tarea_diaria(self):

        self.dias_trabajados += 1

        if self.dias_trabajados >= 30:
            return f"{self.nombre} ha trabajado el día 30. " + self.cobrar_nomina()
        else:
            return f"{self.nombre} ha ido a trabajar. (Día {self.dias_trabajados}/30 para la nómina)."


    def dar_paga(self, hijo, cantidad):
        if self.cuenta.retirar(cantidad):
            hijo.cuenta.ingresar(cantidad)
            return f"{self.nombre} le ha dado {cantidad}€ a {hijo.nombre}."
        return f"{self.nombre} no tiene fondos para la paga."

