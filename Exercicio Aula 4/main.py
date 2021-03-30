from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Carro import Carro
from Moto import Moto


veiculo_do_professor = Veiculo("Ferrari", 4, "F50", 200)
veiculo_do_professor.imprimirinformacoes()
valor = 50
print(f"Considerando um {valor} de valor alteração de velocidade: ")
veiculo_do_professor.acelerar(valor)
veiculo_do_professor.frear(valor)

print("")

bicicleta_do_professor = Bicicleta("Caloi", 2, "Caloi 10", 32, False, 25)
bicicleta_do_professor.imprimirinformacoes()
print("")

automovel_do_professor = Automovel("Nissan", 4, "March", 112, 180)
automovel_do_professor.imprimirinformacoes()
print("")

carro_do_professor = Carro("Lamburguini", 4, "Aventador", 1000, 6, 300)
carro_do_professor.imprimirinformacoes()
print("")

moto_do_professor = Moto("Ducati", 2, "Panigale", 200, True, 360)
moto_do_professor.imprimirinformacoes()
print("")