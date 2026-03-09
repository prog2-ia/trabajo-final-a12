from familiar import Familiar
class Padre(Familiar):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, profesion, salario, dinero_ahorrado=0):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, paga=0, dinero_ahorrado=dinero_ahorrado)
        self.profesion = profesion
        self.salario = salario

    def cobrar_nomina(self):
        self.dinero_ahorrado += self.salario
        return f"{self.nombre} ha cobrado su nómina de {self.salario}€. Total ahorrado: {self.dinero_ahorrado}€."

    def pagar_gastos_del_hogar(self):
        if self.dinero_ahorrado >= self.gastos_fijos:
            self.dinero_ahorrado -= self.gastos_fijos
            return f" Gastos del hogar pagados (-{self.gastos_fijos}€). Quedan {self.dinero_ahorrado}€."
        else:
            return f" ¡Cuidado! {self.nombre} no tiene suficiente dinero para los gastos fijos."

    def dar_paga(self, hijo, cantidad):
        if self.dinero_ahorrado >= cantidad:
            self.dinero_ahorrado -= cantidad
            hijo.dinero_ahorrado += cantidad
            return f" {self.nombre} le ha dado {cantidad}€ a {hijo.nombre}. Generosidad nivel experto."
        else:
            return f" No hay suficiente dinero para la paga. ¡Hay que ahorrar más!"