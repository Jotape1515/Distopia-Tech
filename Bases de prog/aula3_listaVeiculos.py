from abc import ABC, abstractmethod

class Veiculos(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.componentes = []
        self.atributos = {}

    @abstractmethod
    def definir_componentes(self):
        pass

    @abstractmethod
    def definir_atributos(self):
        pass

    def listar(self):
        self.definir_componentes()
        self.definir_atributos()

        print(f"\nOs principais componentes de um {self.nome} são: ")
        for componente in self.componentes:
            print("-", componente)
        print("\n")

        print(f"\nOs atributos médios de um {self.nome} são: ")
        for atributo, valor in self.atributos.items():
            print(f"- {atributo}: {valor}")
        print("\n")

    def __str__(self):
        componentes_str = ', '.join(self.componentes)
        atributos_str = ', '.join([f"{atributo}: {valor}" for atributo, valor in self.atributos.items()])
        return f"{self.nome}\nComponentes: {componentes_str}\nAtributos: {atributos_str}"

def criar_atributos(max_speed, fuel, capacity, terrain):
    atributos = {
        "Velocidade Máxima em Km/h": max_speed,
        "Combustível em Litros": fuel,
        "Passageiros": capacity,
        "Terreno": terrain
    }
    return atributos

class Carro(Veiculos):
    def __init__(self):
        super().__init__("Carro")

    def definir_componentes(self):
        self.componentes = ["Carroceria", "Direção", "Rodas", "Pneus", "Freios", "Conjunto Elétrico", "Motor", "Transmissão"]

    def definir_atributos(self):
        self.atributos = criar_atributos("240", "70", "5", "Terrestre")

class Barco(Veiculos):
    def __init__(self):
        super().__init__("Barco")

    def definir_componentes(self):
        self.componentes = ["Casco", "Proa", "Popa", "Convés", "Timão", "Motor", "Quilha"]

    def definir_atributos(self):
        self.atributos = criar_atributos("120", "300", "10", "Aquático")

class Aeronave(Veiculos):
    def __init__(self):
        super().__init__("Aeronave")

    def definir_componentes(self):
        self.componentes = ["Fuselagem", "Asas", "Motores", "Cauda", "Superfícies de controle", "Trem de pouso", "Sistema de controle", "Aviônicos"]

    def definir_atributos(self):
        self.atributos = criar_atributos("850", "35000", "150", "Aéreo")

def main():
    while True:
        print("\nEscolha um dos veículos:")
        print("1-> Carro")
        print("2-> Barco")
        print("3-> Avião")
        print("4-> Encerrar")
        escolha = input("Digite uma opção: ")

        if escolha == "1":
            veiculo = Carro()
            veiculo.listar()
        elif escolha == "2":
            veiculo = Barco()
            veiculo.listar()
        elif escolha == "3":
            veiculo = Aeronave()
            veiculo.listar()
        elif escolha == "4":
            print("\nPrograma encerrado com sucesso!\n\n")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
