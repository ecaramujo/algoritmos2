from ContaBancaria import ContaBancaria
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente


cp = ContaPoupanca( int(101), float(1000.0), float(1200))
print("Imprimindo Dados Conta Poupanca")
print(cp.conta)
print(cp.saldo)
print(cp.saldo_poupanca)



cc = ContaCorrente( int(202), float(2020.0), str("023.305.126.15"))
print("Imprimindo Dados Conta Corrente")
print(cc.conta)
print(cc.saldo)
print(cc.cpf)


