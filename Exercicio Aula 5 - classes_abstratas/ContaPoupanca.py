from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, conta, saldo, saldo_poupanca):
        self._conta = conta
        self.saldo = saldo
        self._saldo_poupanca = saldo_poupanca
    
    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, valor):
        self._conta = valor

    def ler_saldo(self):
        return self.saldo

    @property
    def saldo_poupanca(self):
        return self._saldo_poupanca

    @conta.setter
    def conta(self, valor):
        self._saldo_poupanca = valor

