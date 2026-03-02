class AgenteFinanciero:
    moneda = 'USD'
    def __init__(self,nombre,saldo_inicial):
        self.nombre = nombre
        self.presupuesto = saldo_inicial
    def realizar_transaccion(self):
        if CuentaBancaria.cantidad <= self.presupuesto:
            self.presupuesto -= CuentaBancaria.cantidad
            print(f"{self.nombre} gastó {CuentaBancaria.cantidad} {AgenteFinanciero.moneda}")
        else:
            print("Fondos insuficientes")
