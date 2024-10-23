from Funcionario_mensal import Funcionario_pago_mensal 
from Funcionario_hora import Funcionario_pago_hora
from Funciona_comissao import Funcionario_pago_comissao 
from Funcionario_projeto import Projetista



def main():
    lista_de_funcionarios = []
    mensalista = Funcionario_pago_mensal("Diego Raposo", 45786, 2000.50)
    horistas = Funcionario_pago_hora("Jonas Santos", 45786, 40, 112.75)
   
    comissionado = Funcionario_pago_comissao("Sabrina Frazão", 45687, 2500.75, 3000.24, 25.35)
    projetista = Projetista("Carlos Souza", 78546, 2000.50, 5)
    lista_de_funcionarios = [mensalista, horistas, comissionado, projetista]
    def processar_pagamento(funcionario):
        funcionario.calcular_salario()

  
    for funcionario in lista_de_funcionarios:
        print("-------")
        processar_pagamento(funcionario)
       

if __name__ == '__main__':
    main()