#filtrar pares
numeros = [1,2,3,4,5,6]
pares = list(filter(lambda x: x%2==0, numeros))
print(pares)

#filtrar palavras com mais de 5 letras 
palavras = ["Python", "é", "incrível", "para", "data", "science" ]
palavras_longas = list(filter(lambda palavra: len(palavra)>=5, palavras))
print(palavras_longas)

