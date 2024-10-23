from Funcionario import Funcionario

class Funcionario_pago_hora(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        if horas_trabalhadas <= 0:
            raise ValueError("Horas trabalhada deve ser positivo")
        self._horas_trabalhadas = horas_trabalhadas
        if valor_hora <= 0:
            raise ValueError("Valor da hora deve ser positivo")
        self._valor_hora = valor_hora
    
    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f'Funcionário: {self.nome} || Matricula: {self.matricula} || Salario Total: R${salario}')
    
    @property
    def horas_trabalhadas(self):
        return self._horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self,horas_trabalhadas):
        if horas_trabalhadas <= 0:
            raise ValueError("Horas trabalhada deve ser positivo")
        self._horas_trabalhadas = horas_trabalhadas

    @property
    def valor_hora(self):
        return self._valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        if valor_hora <= 0:
            raise ValueError("Valor da hora deve ser positivo")
        self._valor_hora = valor_hora 