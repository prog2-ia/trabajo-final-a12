class Hijo(Familiar):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, escuela, paga=0, dinero_ahorrado=0):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, paga, dinero_ahorrado)
        self.escuela = escuela

    def pedir_paga(self):
        self.dinero_ahorrado += self.paga
        return f"{self.nombre} ha recibido su paga de {self.paga}. Ahora tiene {self.dinero_ahorrado}."