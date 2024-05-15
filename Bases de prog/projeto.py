class Perfil:
    def __init__(self, nome, matricula, materias):
        self.nome = nome
        self.matricula = matricula
        self.materias = materias


class Materia:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        self.situacao = self.calcular_situacao(nota)

    def calcular_situacao(self, nota):
        if nota >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"


def registrarAluno():

    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")

    materias = []
    disciplinas = ["Português", "Matemática", "Biologia", "Física", "Química", "Artes",
                   "Educação Física", "Inglês", "Geografia", "História", "Filosofia", "Sociologia"]

    for disciplina in disciplinas:
        nota = float(input(f"Digite a nota de {disciplina}: "))
        materias.append(Materia(disciplina, nota))

    aluno = Perfil(nome, matricula, materias)

    return aluno


def main():
    aluno = registrarAluno()

    print("\nPerfil do Aluno:")
    print(f"Nome: {aluno.nome}")
    print(f"Matrícula: {aluno.matricula}")
    print("Notas:")
    for materia in aluno.materias:
        print(f"{materia.nome}: Nota {materia.nota} - Situação: {materia.situacao}")


if __name__ == "__main__":
    main()
