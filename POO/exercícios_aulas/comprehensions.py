#Comprehensions (List, Dictionary e set)

#List comprehensions 
numeros = [1,2,3,4]
quadrados = [x**2 for x in numeros]
print(quadrados)


#Dictionary comprehensions
numeros = [1,2,3,4]
quadrados_dict = {x: x**2 for x in numeros}
print(quadrados_dict)

#set Compreehensions 
numeros = [1,2,2,3,4,4,5]
quadrados_set = {x**2 for x in numeros}
print(quadrados_set)