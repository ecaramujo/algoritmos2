from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = float(potenciaDoMotor)

    def imprimirinformacoes(self):
        Veiculo.imprimirinformacoes(self)
        print(f"Por conta de ser um Automóvel a potência do motor é de {self.potenciaDoMotor} cv.")







