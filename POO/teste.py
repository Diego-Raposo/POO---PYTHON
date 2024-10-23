class Aluno:
    def __init__(self, nome = str, matricula = int, idade=int):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade 

aluno1 = Aluno("Diego", 2022006560, 24)
print(aluno1.nome)

