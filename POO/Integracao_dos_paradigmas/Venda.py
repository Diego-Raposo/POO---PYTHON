class Venda: 
    def __init__(self, nome_produto, quantidade_vendida, preco_unitario):
        self._nome_produto = nome_produto
        self._quantidade_vendida = quantidade_vendida
        self._preco_unitario = preco_unitario

    @property
    def nome_produto(self):
        return self._nome_produto

    @nome_produto.setter
    def nome_produto(self, nome_produto):
        if isinstance(nome_produto, str) and nome_produto:
            self._nome_produto = nome_produto
        else: 
            raise ValueError("O nome do produto deve ser uma string não vazia.")
    
    @property
    def quantidade_vendida(self):
        return self._quantidade_vendida
    
    @quantidade_vendida.setter
    def quandidade_vendida(self, quantidade_vendida):
        if isinstance(quantidade_vendida, int) and quantidade_vendida:
            self._quantidade_vendida = quantidade_vendida
        else: 
            raise ValueError("A quantidade vendida deve ser um valor inteiro")
    
    @property 
    def preco_unitario(self):
        return self._preco_unitario 
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        if isinstance(preco_unitario, float) and preco_unitario:
            self._preco_unitario = preco_unitario
        else: 
            raise ValueError("O preco unitario deve ser um valor float")

    def mostra_info(self):
        print(f"Nome produto: {self.nome_produto} || Quantidade Vendida: {self.quantidade_vendida} || preco_unitario: {self.preco_unitario}")
    
    def total_por_produto(self):
        total = self.quandidade_vendida*self._preco_unitario
        print(f'Valor total da venda: {total}')
        
class HistoricoVendas:
    lista_vendas = [
        Venda("Camisa", 2, 35.90), 
        Venda("Calça", 3, 38.80),
        Venda("Notebook", 1, 4500),
        Venda("Celular", 2, 1800.80)
    ]

venda = Venda("Camisa", 2, 35.90)
venda.mostra_info()
venda.total_por_produto()