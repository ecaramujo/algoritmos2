from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade)
        self.partidaEletrica = bool(partidaEletrica)

    def imprimirinformacoes(self):
        Automovel.imprimirinformacoes(self)
        if self.partidaEletrica == True:
            print(f"Além disso essa moto possui também partida elétrica.")
        else:
            print(f"Esta Moto não possui uma partida elétrica.")






