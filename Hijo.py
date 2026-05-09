from familiar import Familiar

class Hijo(Familiar):
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, escuela, paga=0):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, paga)
        self.escuela = escuela
        self.dinero_ahorrado = 0
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
    # Añado el metodo add para que los hijos puedan sumar su paga y comprar cosas de mas valor
    def __add__(self, otro):
        try:
            # Intentamos sumar asumiendo que 'otro' tiene el atributo 'paga'
            return self.paga + otro.paga
        except AttributeError:
            # Si 'otro' no lo tiene (ej. un string o un int), saltará este error
            return "Error: No se puede sumar un Hijo con un objeto que no tiene paga."
    def realizar_tarea_diaria(self):
        import random
        materias = ["Matemáticas", "Lengua", "Historia", "Programación"]
        materia_hoy = random.choice(materias)
        accion = f"{self.nombre} ha ido a la escuela {self.escuela}."
        estudio = self.hacer_deberes(materia_hoy)
        return f"{accion} {estudio}"