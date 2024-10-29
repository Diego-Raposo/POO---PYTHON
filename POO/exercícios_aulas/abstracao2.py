from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processa_pagamento(self):
        pass 
    def detalhes_pagamento(self, method):
        print(f"Processando pagamento via {method}")

class Pagamento_cartao_Credito(Pagamento):
    def processa_pagamento(self):
        print("Pagamento processado com cartão de crédito")
    
    def detalhes_pagamento(self, method):
        print(f"Processando pagamento via {method}")

class Pagamento_boleto(Pagamento):
    def processa_pagamento(self):
        print("Pagamento processado com boleto")

    def detalhes_pagamento(self, method):
        print(f"Processando pagamento via {method}")


class Pagamento_pix(Pagamento):
    def processa_pagamento(self):
        print("Pagamento processado com pix")
    
    def detalhes_pagamento(self, method):
        print(f"Processando pagamento via {method}")



def testar_pagamento():
    pagamento = Pagamento_pix()
    pagamento2 = Pagamento_cartao_Credito()
    pagamento3 = Pagamento_boleto()

    
    pagamento.detalhes_pagamento("Pix")
    pagamento.processa_pagamento()
    print("----------")
    pagamento2.detalhes_pagamento("Cartão de crédito")
    pagamento2.processa_pagamento()
    print("----------")
    pagamento3.detalhes_pagamento("Boleto")
   
    pagamento3.processa_pagamento()
    print("----------")



testar_pagamento()