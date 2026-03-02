class Familiar:
    def __init__(self, nombre,apellido1,apellido2,edad,gastos_fijos,paga=0,dinero_ahorrado=0):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        self.gastos_fijos = gastos_fijos
        self.paga = paga
        self.dinero_ahorrado=dinero_ahorrado
    def comprar(self,valor_de_compra,producto):
        self.valor_de_compra = valor_de_compra
        self.producto=producto
        if self.valor_de_compra >= self.dinero_ahorrado:
            self.dinero_ahorrado-=self.valor_de_compra
            return (f"Has comprado {self.producto} te quedan {self.dinero_ahorrado}")
