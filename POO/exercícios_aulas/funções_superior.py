#map(): Aplica uma função a cada elemento de uma coleção, retornando uma nova coleção com os resultados
#filter(): Filtra elementos de uma coleção com base em uma condição, retornando apenas os elementos que satisfaçam a condição  
#reduce(): Reduz uma coleção a um único valor acumulado. reduce é importado da biblioteca functools

numeros = [1,2,3,4,5]
dobrados = list(map(lambda x: x*2, numeros))
print(dobrados)

num1 = [2,4,6,8]
num2 = [3,1,4,2]
somas = list(map(lambda x, y: x + y, num1, num2))
produtos = list(map(lambda x,y: x*y, num1, num2))
print(somas)
print(produtos)

numeros_int = [50,30,40,80]
convertidos = list(map(lambda x: str(x), numeros_int))
print(convertidos)

palavras = ['Python', 'Jonas', 'Diego']
conta_letras = list(map(len, palavras))
print(conta_letras)


