from Adulto import Adulto
class Madre(Adulto):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, salario, dinero_ahorrado=0):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, salario, dinero_ahorrado)

    def generar_intereses(self, porcentaje=0.02):
        intereses = self.dinero_ahorrado * porcentaje
        self.dinero_ahorrado += intereses
        return f"Intereses generados: {intereses:.2f}€."