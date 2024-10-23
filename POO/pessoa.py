class Pessoa:
    nome = ""
    idade = 0 
    peso = 0.0
    altura = 0.0 
    def __init__(self, nome = str, idade = int, peso = float, altura=float):
        self.nome = nome 
        self.idade = idade 
        self.peso = peso 
        self.altura = altura 

    def envelhecer(soma_idade): 
        Pessoa.crescer(soma_idade*0.5)
        idade+=soma_idade
        return idade 
    def engordar(peso_mais):
        peso +=peso_mais 
        return peso 
    def emagrecer(peso_menos):
        peso -=peso_menos
        return peso 
    def crescer(altura_mais):
        altura +=altura_mais
        return altura

if __name__ == "__main__":
    nome = input("Nome: ")
    idade = input("Idade: ")
    peso = input("peso: ")
    altura = input("altura(): ")
    pessoa1 = Pessoa(nome,idade,peso,altura)
    print(f"Nome: {pessoa1.nome} || Idade: {pessoa1.idade} || Peso: {pessoa1.peso} || Altura: {pessoa1.altura}")
    pessoa1.emagrecer(2)
    print(f"Nome: {pessoa1.nome} || Idade: {pessoa1.idade} || Peso: {pessoa1.peso} || Altura: {pessoa1.altura}")
    



        