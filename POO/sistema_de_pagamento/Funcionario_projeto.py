from Funcionario import Funcionario
class Projetista(Funcionario):
    def __init__(self, nome, matricula, valor_por_projeto, quant_projeto):
        super().__init__(nome, matricula)
        self._valor_por_projeto = valor_por_projeto
        self._quant_projeto = quant_projeto
    
    @property 
    def valor_por_projeto(self):
        return self._valor_por_projeto 
    
    @valor_por_projeto.setter
    def valor_por_projeto(self, valor_por_projeto):
        self._valor_por_projeto = valor_por_projeto 

    @property 
    def quant_projeto(self):
        return self.quant_projeto
    
    @quant_projeto.setter
    def quant_projeto(self, quant_projeto):
        self._quant_projeto = quant_projeto

    def calcular_salario(self):
        salario = self.valor_por_projeto * self._quant_projeto
        print(f'Funcionário: {self.nome} || Matricula: {self.matricula} || Salario Total do Projetista: R${salario:.2f}')