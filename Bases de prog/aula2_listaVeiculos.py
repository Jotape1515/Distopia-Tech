class Veiculos:
    def __init__(self, nome):
        self.nome = nome
        self.componentes = []
        self.atributos = {}

    def listar(self):
        print(f"\nOs principais componentes de um {self.nome} são: ")
        for componente in self.componentes:
            print("-", componente)
        print("\n")

        print(f"\nOs atributos médios de um {self.nome} são: ")
        for atributo, valor in self.atributos.items():
            print(f"- {atributo}: {valor}")
        print("\n")

class Carro(Veiculos):
    def __init__(self):
        super().__init__("Carro")
        self.componentes = ["Carroceria", "Direção", "Rodas", "Pneus", "Freios", "Conjunto Élétrico", "Motor", "Transmissão"]
        self.atributos = {
            "Velocidade Máxima em Km/h" : 240,
            "Combustível em Litros": 70,
            "Passageiros": 5,
            "Terreno": "Terrestre" 
        }

class Barco(Veiculos):
    def __init__(self):
        super().__init__("Barco")
        self.componentes = ["Casco", "Proa", "Popa", "Convés", "Timão", "Motor", "quilha"]
        self.atributos = {
            "Velocidade Máxima em Km/h" : 120,
            "Combustível em Litros": 300,
            "Passageiros": 10,
            "Terreno": "Aquático" 
        }
class Aeronave(Veiculos):
    def __init__(self):
        super().__init__("Aeronave")
        self.componentes = ["Fuselagem", "Asas", "Motores", "Cauda", "Superfícies de controle", "Trem de pouso", "Sistema de controle", "Aviônicos"]
        self.atributos = {
            "Velocidade Máxima em Km/h" : 850,
            "Combustível em Litros": 35000,
            "Passageiros": 150,
            "Terreno": "Aéreo" 
        }

def main():

    while True:
        print("Escolha um dos veículos:")
        print("1-> Carro")
        print("2-> Barco")
        print("3-> Avião")
        print("4-> Encerrar")
        escolha = input("Digite uma opção: ")

        match escolha:
            case "1":
                veiculo = Carro()
                veiculo.listar()
            case "2":
                veiculo = Barco()
                veiculo.listar()
            case "3":
                veiculo = Aeronave()
                veiculo.listar()
            case "4":
                break
            case _:
                raise ValueError("Opção inválida!")
             
if __name__ == "__main__":
    main()
