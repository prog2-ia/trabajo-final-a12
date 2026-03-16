import random
from Adulto import Adulto
class AgenteFinanciero(Adulto):
    inversion =[0.25,0.5,1,2,4]
    moneda = '€'
    def __init__(self, nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, salario):
        super().__init__(nombre, apellido1, apellido2, edad, gastos_fijos, cuenta, salario)
    def realizar_transaccion(self, cantidad):
        if self.cuenta.retirar(cantidad): # llamamos al metodo retirar que nos devolvera true si tiene fondos
            # en caso de que no tenga nos devolvera false por lo que pasara al else
            print(f"Transacción de {cantidad}{self.moneda} realizada con éxito.")
            print(f"Saldo actual de {self.nombre}: {self.cuenta.saldo}{self.moneda}")
            return True
        else:
            print(f"Fondos insuficientes en la cuenta de {self.nombre}.")
            return False
    def realizar_inversión(self,cantidad):
        if self.cuenta.retirar(cantidad):
            resultado = random.choice(self.inversion) * cantidad
            self.cuenta.ingresar(resultado)
            if resultado >= cantidad:
                print(f"Has invertido {cantidad} y has conseguido {resultado - cantidad} {self.moneda} de beneficio"
                      f" te has quedado con {resultado} {self.moneda} respecto a tu inversión inicial" )
            else:
                print(f"Has invertido {cantidad} y has perdido {cantidad - resultado} {self.moneda}"
                      f" te has quedado con {resultado} {self.moneda} respecto a tu inversión inicial")
        else:
            print("No tienes esa cantidad de dinero para invertir")
