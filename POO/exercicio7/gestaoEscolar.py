class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.nome = nome 
        self.matricula = matricula


    def mostra_info(self):
        print(f'Aluno: {self.nome} || Matricula: {self.matricula}')
    
class Curso:
    def __init__(self, nome:str, codigo:int):
        self.nome = nome 
        self.codigo = codigo
        self.alunos = []
    
    def mostra_info_curso(self):
        print(f'Curso: {self.nome} || Codigo: {self.codigo}')

    def adicionar_aluno(self, nome, matricula):
        aluno = Aluno(nome, matricula)
        self.alunos.append(aluno)
        print("Aluno adicionado com sucesso")
    def mostrar_alunos(self):
        for aluno in self.alunos:
            aluno.mostra_info()

class Escola:
    def __init__(self, nome):
        self.nome = nome 
        self.cursos = []
    def adicionar_curso(self,nome,codigo):
        curso = Curso(nome, codigo)
        self.cursos.append(curso)
        print("Curso adicionado com sucesso")
    def mostrar_cursos(self):
        for curso in self.cursos:
            curso.mostra_info_curso()
            

print("---------")
medicina = Curso("Medicina", 123)
medicina.adicionar_aluno("Diego", 2022006560)
medicina.adicionar_aluno("Raposo", 154298)
medicina.adicionar_aluno("Sabrina", 8223544)

print("---------")
print("Alunos de Medicina")
medicina.mostrar_alunos()

print("---------")
escola = Escola("Ifam")
escola.adicionar_curso("Medicina", 12334)
escola.adicionar_curso("Engenharia de Software", 45230)
escola.adicionar_curso("Direito", 78954)
print("---------")
print("Cursos do IFAM")
escola.mostrar_cursos()
print("---------")
engenharia_software = Curso("Engenharia de Software", 45230)
engenharia_software.adicionar_aluno("Carlos", 45670)
engenharia_software.adicionar_aluno("Jonas", 78965)
engenharia_software.adicionar_aluno("Caio", 789540)
print("---------")
print("Alunos de Engenharia de Software")
engenharia_software.mostrar_alunos()
print("---------")
print('Mostrar cursos')
escola.mostrar_cursos()

'''
Perguntas para Reflexão:
1. Como a composição facilita a criação de relações complexas entre
objetos?

2. Qual é a vantagem de usar composição em vez de herança neste
exercício?
3. Como o encapsulamento é utilizado nas classes Aluno, Curso e Escola?
4. Como você pode estender este sistema para incluir novas
funcionalidades, como notas dos alunos e professores para cada curso?

'''