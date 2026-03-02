from familiar import Familiar
class Hijo(Familiar):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, escuela, paga=0, dinero_ahorrado=0):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, paga, dinero_ahorrado)
        self.escuela = escuela
        self.prohibidos = ["tabaco", "videojuegos +18", "apuestas", "alcohol"]

    def comprar(self, valor_de_compra, producto):
        if producto.lower() in self.prohibidos:
            return f" ERROR: {self.nombre} tiene {self.edad} años. No tiene permitido comprar {producto}."
        return super().comprar(valor_de_compra, producto)

    def pedir_paga(self):
        self.dinero_ahorrado += self.paga
        return f"{self.nombre} ha recibido su paga de {self.paga}. Ahora tiene {self.dinero_ahorrado}."

    def hacer_deberes(self, materia):
        recompensa = 5
        self.dinero_ahorrado += recompensa
        return f"{self.nombre} ha estudiado {materia} y ha ganado una bonificación de {recompensa}€."