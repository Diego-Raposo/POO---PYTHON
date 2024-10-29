#Funcões lambda são funções anônimas que facilitam a criação de funções pequenas e rápidas. Elas seguem o formato:
# Lambda argumentos: expressão
#exemplo:
# dobrar = lambda x: x*2 
# print(dobrar(5)) #saida 10 

dobrar = lambda x: x*2
potencia_quadrado = lambda x: x**2 
dividir = lambda x: x/2

print(dobrar(5))
print(potencia_quadrado(5))
print(dividir(100))

pessoas = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
print(pessoas_ordenadas)

produtos = [
    {'nome': 'Camisa', 'preco': 50},
    {'nome': 'Calça', 'preco': 700},
    {'nome': 'Sapato', 'preco': 20}
]

produtos_ordenados = sorted(produtos, key=lambda produto:produto["preco"])
print(produtos_ordenados)