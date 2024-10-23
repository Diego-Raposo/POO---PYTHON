class Livro: 
    def __init__(self, titulo=str, autor=str,disponivel=bool):
        self.titulo = titulo 
        self.autor = autor
        self.disponivel = disponivel
    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"Livro {self.titulo} emprestado")
        else:
            print("Livro indisponível")
    def devolver(self):
        self.disponivel = True
        print("Livro devolvido")
    def mostrar_info(self):
        if self.disponivel == True:
            print(f"Título: {self.titulo} || Autor: {self.autor} || Status: Disponivel")
        else:
            print(f"Título: {self.titulo} || Autor: {self.autor} || Status: Indisponivel")
        
class livraria(): 

    def __init__(self):
        self.invetario = []

    def adicionar_livro(self, livro):
        self.invetario.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado ao inventário.')
    def emprestar_livro(self,titulo):
        print(f'O livro "{titulo}" não foi encontrado no inventário.')
    def mostrar_inventario(self):
        if len(self.invetario) == 0:    
            for i in self.invetario:
                self.invetario.mostrar_info()

if __name__ == "__main__":
    # Criando a livraria
    livraria = livraria()

    # Adicionando livros à livraria
    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")

    livraria.adicionar_livro(livro1)
    livraria.adicionar_livro(livro2)

    # Exibindo o inventário
    livraria.mostrar_inventario()

    # Emprestando um livro
    livraria.emprestar_livro("1984")

    # Tentando emprestar novamente o mesmo livro
    livraria.emprestar_livro("1984")

    # Devolvendo o livro
    livro1.devolver()

    # Exibindo o inventário novamente
    livraria.mostrar_inventario()