class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def ingresar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return True
        return False
