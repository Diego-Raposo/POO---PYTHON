class Usuario:
    def __init__(self, nome, idade, email):

        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        
        if not isinstance(idade, int):
            raise TypeError("A idade deve ser um número inteiro.")
        
        if "@" not in email:
            raise ValueError("O email deve conter um '@'.")

        self.nome = nome
        self.idade = idade
        self.email = email

try:

    usuario1 = Usuario("", 25, "exemple@example.com")  
except ValueError as e:
    print(f"Erro de valor: {e}")
except TypeError as e:
    print(f"Erro de tipo: {e}")

try:
    usuario2 = Usuario("Diego", "vinte e cinco", "diego.eimec@gmail.com") 
except ValueError as e:
    print(f"Erro de valor: {e}")
except TypeError as e:
    print(f"Erro de tipo: {e}")

try:
    usuario3 = Usuario("Sabrina", 48, "sabrinanexample.com") 
except ValueError as e:
    print(f"Erro de valor: {e}")
except TypeError as e:
    print(f"Erro de tipo: {e}")