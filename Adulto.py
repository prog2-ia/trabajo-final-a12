from familiar import Familiar
class Adulto(Familiar):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, salario, dinero_ahorrado=0):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, paga=0, dinero_ahorrado=dinero_ahorrado)
        self.salario = salario

    def cobrar_nomina(self):
        self.dinero_ahorrado += self.salario
        return f" {self.nombre} ha ingresado su salario de {self.salario}€."

    def pagar_deuda(self, concepto, cantidad):
        if self.dinero_ahorrado >= cantidad:
            self.dinero_ahorrado -= cantidad
            return f" {self.nombre} ha pagado '{concepto}': -{cantidad}€. Saldo: {self.dinero_ahorrado}€."
        return f" {self.nombre} no tiene suficiente para pagar {concepto}."

    def dar_paga(self, hijo, cantidad):
        if self.dinero_ahorrado >= cantidad:
            self.dinero_ahorrado -= cantidad
            hijo.dinero_ahorrado += cantidad
            return f" {self.nombre} le ha dado {cantidad}€ a {hijo.nombre}."
        return f" {self.nombre} no tiene fondos para la paga."

