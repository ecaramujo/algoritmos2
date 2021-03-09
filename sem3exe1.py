produtos = ["Coca-cola", "Ajax", "Bombril", "Gilette", "TV"]
precos = [4.00, 2.50, 5.00, 60.00, 1000.00]
quantidade = [50, 25, 80, 40, 12]

def imprimir_produto(num):
    print(f"O produto escolhido foi {produtos[num]} que custa R${precos[num]} e atualmente o estoque possue {quantidade[num]} unidades.\n")

def remover_produtos(num):
    produtos.pop(num)
    precos.pop(num)
    quantidade.pop(num)

while True:
    ind = 0
    for produto in produtos:
        print(ind,"-", produto)
        ind+=1
    print("Você deseja saber mais detalhes de um produto ou excluir um produto da lista?")
    escolha = int(input("Digite 0 para detalhes ou 1 para excluir: "))
    num = int(input("Agora digite o número do produto selecionado: "))
    if escolha == 0:
        imprimir_produto(num)
    elif escolha == 1:
        print(f"Produto {produtos[num]} Removido com Sucesso!\n")
        remover_produtos(num)
    exit = input("Para sair do programa digite SAIR: ")
    if exit == "SAIR":
        break


