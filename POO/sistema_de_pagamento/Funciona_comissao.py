from Funcionario import Funcionario
class Funcionario_pago_comissao(Funcionario):
    def __init__(self, nome, matricula, salario_base, valor_vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self._salario_base = salario_base
        self._valor_vendas = valor_vendas 
        self._taxa_comissao = taxa_comissao
    
    def calcular_salario(self):
        salario = self.salario_base + (self.valor_vendas * self.taxa_comissao/100)
        print(f'Funcionário pago por comissão: {self.nome} || Matricula: {self.matricula}|| Salario Base: R${self.salario_base:.2f} || Salario Total: R${salario:.2f}')

    @property 
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self, salario_base):
        self._salario_base = salario_base 

    @property 
    def valor_vendas(self):
        return self._valor_vendas
    
    @valor_vendas.setter
    def valor_vendas(self, valor_vendas):
        self._valor_vendas = valor_vendas 

    @property 
    def taxa_comissao(self):
        return self._taxa_comissao
    
    @taxa_comissao.setter
    def taxa_comissao(self,taxa_comissao):
        self._taxa_comissao = taxa_comissao
        