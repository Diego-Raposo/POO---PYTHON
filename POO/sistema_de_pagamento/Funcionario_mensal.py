from Funcionario import Funcionario

class Funcionario_pago_mensal(Funcionario):
    def __init__(self, nome, matricula, salario_total):
        super().__init__(nome, matricula)
        self._salario_total = salario_total 

    @property 
    def salario_total(self):
        return self._salario_total 
    @salario_total.setter
    def salario_total(self, salario_total):
        self._salario_total = salario_total

    def calcular_salario(self):
        print(f'Funcionário: {self.nome} || Matricula: {self.matricula} || Salario Mensal: R${self.salario_total}')
