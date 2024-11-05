class Livro: 
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo 
        self.autor = autor 
        self.ano_publicacao = ano_publicacao
        self.genero = genero 


class Biblioteca:
    def __init__(self):
        pass

    def adicionar_livro(self, titulo, autor, ano_publicacao, genero):
        livros = []
        livros.append(Livro(titulo, autor, ano_publicacao,genero))
    def Listar_por_autor(self, autor):
        return list(filter(lambda livro: livro.autor == autor, self.livros))
    
    
