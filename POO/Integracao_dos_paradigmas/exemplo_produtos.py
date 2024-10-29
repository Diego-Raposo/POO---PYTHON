class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome 
        self.preco = preco 
        self.categoria = categoria 

#Criando uma lista de produtos 

produtos = [ 
    Produto("Camisa", 50, "Vestuário"),
    Produto("Calça",100, "Vestuário"),
    Produto("Notebook", 3000, "Eletrônicos"),
    Produto("Celular", 2300, "Eletrônicos")
]

# Usando `filter` para selecionar apenas produtos eletrônicos

eletronicos = list(filter(lambda p: p.categoria == "Eletrônicos", produtos))
print('Produtos eletrônicos: ', [p.nome for p in eletronicos])

#Usando "Map" para aplicar 10% de desconto em todos os produtos

desconto = list(map(lambda p: Produto(p.nome, p.preco*0.90, p.categoria), produtos))
print("Produtos com desconto:", [(p.nome, p.preco) for p in desconto])