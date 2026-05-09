from abc import ABC, abstractmethod #importamos la herramnienta
from cuenta_bancaria import CuentaBancaria

class Familiar(ABC):#Heredar de ABC
    def __init__(self, nombre,apellido1,apellido2,edad,gastos_fijos,cuenta,paga=0):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.edad = edad
        self.gastos_fijos = gastos_fijos
        self.paga = paga
        self.cuenta = cuenta

    def comprar(self,valor_de_compra,producto):
        if self.cuenta.retirar(valor_de_compra): # if true entonces
            return (f"Has comprado {producto}, te quedan {self.cuenta.saldo}€ en la cuenta.")
        else:
            return (f"No tienes saldo suficiente para comprar {producto}.")

    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}" #imprimo el nombre completo

    @abstractmethod #Decorador
    def realizar_tarea_diaria(self):
        pass #Función que obliga a que cada familiar diga que hará en su día a día