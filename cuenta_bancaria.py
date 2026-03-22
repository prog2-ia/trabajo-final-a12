class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__saldo = nueva_cantidad
        else:
            print("Error: El saldo no puede ser negativo.")
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        return self.saldo
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return True
        return False