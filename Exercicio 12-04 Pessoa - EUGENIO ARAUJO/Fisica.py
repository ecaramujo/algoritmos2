from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = str(cpf)
        self.idade = int(idade)
        self.peso = float(peso)
        self.altura = float(altura)
    
    def imprimeCPF(self):
        print(f"O CPF desta pessoa física é {self.__cpf}.")

    def __calculaIMC(self):
        print(f"O IMC desta pessoa física é {((self.peso)/(self.altura)**2)}.")


