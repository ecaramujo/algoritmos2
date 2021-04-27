from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, conta, saldo, cpf):
        self._conta = conta
        self.saldo = saldo
        self.cpf = cpf
    
    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, valor):
        self._conta = valor

    def ler_saldo(self):
        return self.saldo

    def cpf(self):
        return self.cpf

