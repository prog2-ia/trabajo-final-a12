from Adulto import Adulto
class Madre(Adulto):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, cuenta,salario ):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, salario)

    def generar_intereses(self, porcentaje=0.02):
        intereses = self.dinero_ahorrado * porcentaje #variable local
        self.dinero_ahorrado += intereses
        return f"Intereses generados: {intereses:.2f}€. "