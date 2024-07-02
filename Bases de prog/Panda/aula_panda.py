import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv("exemplo.csv")

def main():
    global df  # Indica que estamos referenciando a variável global df

    while True:
        print("\nEscolha uma das opções:")
        print("1 -> Organizar por idade")
        print("2 -> Organizar por nome")
        print("3 -> Organizar por cidade")
        print("4 -> Remover uma coluna")
        print("5-> Modificar um valor")
        print("6-> Mostrar o dataframe")
        print("7 -> SAIR")
        escolha = input("Digite uma opção: ")

        if escolha in ["1", "2", "3"]:
            ordem = input("Digite 'asc' para ordem ascendente ou 'desc' para ordem descendente: ").strip().lower()
            if ordem == 'asc':
                ascending = True
            elif ordem == 'desc':
                ascending = False
            else:
                print("Opção inválida! Ordem ascendente será usada como padrão.")
                ascending = True

            if escolha == "1":
                df_sorted = df.sort_values(by='Idade', ascending=ascending)
                print(df_sorted)
            elif escolha == "2":
                df_sorted = df.sort_values(by='Nome', ascending=ascending)
                print(df_sorted)
            elif escolha == "3":
                df_sorted = df.sort_values(by='Cidade', ascending=ascending)
                print(df_sorted)

        elif escolha == "4":
            removida = input("Qual coluna você quer remover? (Nome/Idade/Cidade): ")
            if removida in df.columns:
                df = df.drop(columns=[removida])
                print(f"Coluna '{removida}' removida com sucesso.")
            else:
                print(f"Coluna '{removida}' não encontrada.")

        elif escolha == "5":
            coluna = input("Qual coluna você quer alterar? (Nome/Idade/Cidade): ")
            if coluna in df.columns:
                linha = int(input(f"Em qual linha você quer alterar a/o '{coluna}'?: "))
                if linha in df.index:
                    novo_valor = input("Digite o novo valor: ")
                    df.loc[linha, coluna] = novo_valor
                    print(f"Valor alterado com sucesso em ({linha}, '{coluna}') para '{novo_valor}'.")
                else:
                    print(f"Linha '{linha}' não encontrada.")
            else:
                print(f"Coluna '{coluna}' não encontrada.")

        
        elif escolha == "6":
            print(df)

        elif escolha == "7":
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
