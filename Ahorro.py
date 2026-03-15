from cuenta_bancaria import CuentaBancaria
class Ahorro:
    def __init__(self, nombre: str, objetivo: float):
        self.nombre = nombre
        self.objetivo = objetivo
        self.__ahorro_actual = 0.0
        # creo la clase de ahorro con un nombre de el por que, ejemplo vacaciones y un objetivo
        # de cantidad que queremos ahorrar

    def aportar(self, cuenta: 'CuentaBancaria', monto: float) -> str:
        if monto > 0 and cuenta.retirar(monto):
            self.__ahorro_actual += monto
            progreso = (self.__ahorro_actual / self.objetivo) * 100 # el ahorro que llevamos
            # entre el total multiplicado por 100 para ver el porcentaje de lo que llevamos ahorrado
            return( f"Meta '{self.nombre}': +{monto}€. Progreso: {progreso:}%")
        else:
            return( f"Error: Saldo insuficiente para ahorrar en '{self.nombre}'.")


    def __str__(self):
        return f"{self.nombre}: {self.__ahorro_actual}/{self.objetivo}€"