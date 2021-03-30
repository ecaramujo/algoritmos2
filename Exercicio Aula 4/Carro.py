from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.qtdPortas = int(qtdPortas)

    def imprimirinformacoes(self):
        Automovel.imprimirinformacoes(self)
        print(f"Por conta de ser um Carro ele possue {self.qtdPortas} portas.")






