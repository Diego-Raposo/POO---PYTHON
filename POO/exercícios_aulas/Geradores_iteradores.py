#Geradores e Iteradores são técnicas úteis para manipular grandes volumes de dados sem sobrecarregar a memória 

#Geradores são funções que utilizam a palavra chave yield para retornar valores de forma sequencial, sem armazenar tudo na memória

def gerar_pares(limite):
    n = 0 
    while n<limite:
        yield n 
        n+=2

for numero in gerar_pares(10):
    print(numero)

