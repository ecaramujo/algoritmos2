from abc import ABCMeta, abstractmethod    

class ContaBancaria(metaclass=ABCMeta):

    @property
    def conta(self):
        pass

    @conta.setter
    @abstractmethod
    def conta(self, valor):
        pass

    @abstractmethod
    def ler_saldo(self):
        pass
