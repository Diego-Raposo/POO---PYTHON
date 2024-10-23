class Pessoa:
    peso = 0
    altura = 0
    def __init__(self, peso_pessoa=float, peso_altura=float):
        self.peso = peso_pessoa
        self.altura = peso_altura

    def calcular_imc(self, peso,altura):
        imc = peso/(altura*altura)
        return imc

if __name__ == "__main__":
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    pessoa1 = Pessoa(peso, altura)
    print(f"O seu IMC é: {pessoa1.calcular_imc(peso, altura):.2f}")
    if pessoa1.calcular_imc(peso,altura) < 18.5:
        print("Magreza")
    elif pessoa1.calcular_imc(peso,altura) >= 18.5 and pessoa1.calcular_imc(peso,altura) < 24.9:
        print('Normal')
    elif pessoa1.calcular_imc(peso,altura) >= 24.9 and pessoa1.calcular_imc(peso,altura) < 30:
        print('Sobrepeso')
    elif pessoa1.calcular_imc(peso,altura) >= 30:
        print('Obesidade')
