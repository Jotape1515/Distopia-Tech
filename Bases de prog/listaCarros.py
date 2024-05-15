class Carro:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa




def main():

    while True:
        print("Lista de carros, Escolha uma das opções:")
        print("1. Adicionar um veículo")
        print("2. Remover um veículo")
        print("3. Listar todos os carros da lista")
        print("4. Fechar")

        escolha = input("Digite uma opção: ")

        if escolha == "1":
            
        elif escolha == "2":
            
        elif escolha == "3":
            
        elif escolha == "4":
            print("Programa encerrado com sucesso!")
            break
        else:
            print("Escolha inexistente, digite novamente")


if __name__ == "__main__":
    main()
