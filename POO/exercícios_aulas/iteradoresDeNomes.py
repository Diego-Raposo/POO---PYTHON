class IteradoresDeNomes:
    def __init__(self, nomes):
        self.nomes = nomes
        self.indice = 0 
    def __iter__(self):
        #retorna o próprio objeto como iterador
        return self
    
    def __next__(self):
        #retorna o próprio nome em maiusculas, se disponivel 
        if self.indice < len(self.nomes):
            nome = self.nomes[self.indice].upper()
            self.indice +=1
            return nome 
        else: 
            #levanta StopIteration ao final da lista 
            raise StopIteration
        
#Usando o iterador personalizado 

nomes = ["Alice", "Bob", "Charlie"]
iterador_nomes = IteradoresDeNomes(nomes)

for nome in iterador_nomes:
    print(nome)