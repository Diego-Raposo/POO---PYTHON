#Decorator: Permitem modificar o comportamento de uma função ou métodom sem alterar seu código 

def saudacao_decorator(func):
    def wapper(nome):
        print("Olá")
        func(nome)
        print("Tenha um bom dia!")
    return wapper

@saudacao_decorator 
def saudacao(nome):
    print(f"Prazer em conhecê-lo, {nome}")

saudacao("Diego")

#Decorator com argumentos: Decorators podem também ser parametrizados

def multiplicar_por(n):
    def decorator(func):
        def wapper(x):
            return func(x) * n
        return wapper
    return decorator

@multiplicar_por(4)
def soma_dois(x):
    return x + 2

print(soma_dois(5))