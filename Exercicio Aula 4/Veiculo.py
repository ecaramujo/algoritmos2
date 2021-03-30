class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = str(marca)
        self.qtdRodas = int(qtdRodas)
        self.modelo = str(modelo)
        self.velocidade = int(velocidade)
    
    def imprimirinformacoes(self):
        print(f"Este Veiculo é da marca {self.marca}, possui {self.qtdRodas} rodas, modelo {self.modelo} e velocidade de {self.velocidade} km/h.")

    def acelerar(self, valor):
        aceleracao = self.velocidade + valor
        print(f"O valor de aceleracao foi {aceleracao}.")
    
    def frear(self, valor):
        freiada = self.velocidade - valor     
        print(f"O valor de freiada foi de {freiada}.")






