class CuentaBancaria:
    banco = "Banco Central de Python"

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito realizado. Nuevo saldo de {self.titular}: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar el retiro.")
    def pagar_deuda:
        pass