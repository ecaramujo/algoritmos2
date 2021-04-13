class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = int(codigo)
        self.nome = str(nome)
        self._endereco = str(endereco)
        self.__telefone = str(telefone)

    def imprimeNome(self):
        print(f"O nome desta pessoa é {self.nome}.")

    def __imprimeTelefone(self):
        print(f"O telefone desta pessoa é {self.__telefone}.")



