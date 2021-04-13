from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica


print("---Somente Pessoa---")
jonas = Pessoa(111, "Jonas", "Ipanema", "51-9999")
jonas.imprimeNome()
jonas.imprimeTelefone()

print("---Somente Pessoa Fisica---")
jonasfisico = Fisica(222, "JonasFisico", "Cavalhada", "52-9999", "023.849", "25", 62.5, 1.66)
jonasfisico.imprimeCPF()

print("---Somente Pessoa Juridica---")
jonasjuridico = Juridica(333, "JonasJuridico", "Tristeza", "53-9999", "506.240", "Porto Alegre 564", 2000)
jonasjuridico.imprimeCNPJ()


print("---Métodos com __ não foram rodados.---")