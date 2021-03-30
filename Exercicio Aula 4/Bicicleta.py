from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo,  numMarchas, bagageiro, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = int(numMarchas)
        self.bagageiro = bool(bagageiro)

    def imprimirinformacoes(self):
        Veiculo.imprimirinformacoes(self)
        print(f"Por conta de ser uma bicicleta ela também possui {self.numMarchas} marchas.")
        if self.bagageiro == True:
            print(f"Além disso também conta com um bagageiro.")
        else:
            print(f"Esta Bicicleta não possui um bagageiro.")



