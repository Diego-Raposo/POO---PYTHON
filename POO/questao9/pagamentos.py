class Pagamento:
    def processar_pagamento(self):
        pass

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, num_cartao):
        self.num_cartao = num_cartao
    def processar_pagamento(self):
        print(f"Cartão de Crédito com o numero {self.num_cartao} foi processado")
        #return super().processar_pagamento()


class PagamentoBoleto(Pagamento):
    def __init__(self, codigoBoleto):
        self.codigoBoleto = codigoBoleto
    def processar_pagamento(self):
        print(f"Pagamento do boleto {self.codigoBoleto} foi processado")
        #return super().processar_pagamento()
class PagamentoPix(Pagamento):
    def __init__(self, chavePix):
        self.chavePix= chavePix
    def processar_pagamento(self):
        print(f"Pagamento via pix foi processado: {self.chavePix}")
        #return super().processar_pagamento()

pagamento = PagamentoBoleto("785fff9985")
pagamento.processar_pagamento()
print("-------")
pagamento2 = PagamentoCartaoCredito(7856988755)
pagamento2.processar_pagamento()
print("-------")
pagamento3 = PagamentoPix(202200650)
pagamento3.processar_pagamento()
print("-------")

'''
    1. O que acontece se você adicionar um novo método de pagamento sem
    modificar a função processar?
    2. Como o polimorfismo ajuda a manter o código flexível e extensível?
    3. Qual é a diferença entre a função processar e os métodos
    processar_pagamento nas subclasses?
    4. Como você pode garantir que todos os métodos de pagamento
    implementem o método processar_pagamento corretamente?


'''