class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def __str__(self):
        return f'Motor de {self.potencia} cavalos está ligado.'
    def ligar(self):
        print(f'Motor de {self.potencia} cavalos está ligado.')

class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = Motor(motor)  # Composição: o carro "tem" um motor

    def ligar_carro(self):
        print(f"Ligando o carro da marca {self.marca}.")
        self.motor.ligar()

# Criando um motor e um carro com esse motor
motor_v8 = Motor(500)
meu_carro = Carro("Ferrari", motor_v8)

meu_carro.ligar_carro()

class Roda:
    def __init__(self, tamanho):
        self.tamanho = tamanho
    def __str__(self):
        return f"Rodando com rodas de {self.tamanho} polegadas."
    def rodar(self):
        print(f"Rodando com rodas de {self.tamanho} polegadas.")

class Chassi:
    def __init__(self, tipo):
        self.tipo = tipo
    def __str__(self):
        return f"Chassi do tipo {self.tipo}." 
    def mostrar_tipo(self):
        print(f"Chassi do tipo {self.tipo}.")

class CarroCompleto:
    def __init__(self, marca, motor, rodas, chassi):
        self.marca = marca
        self.motor = Motor(motor)
        self.rodas = Roda(rodas)
        self.chassi = Chassi(chassi)

    def ligar_carro(self):
        print(f"Ligando o carro da marca {self.marca}.")
        self.motor.ligar()
        self.rodas.rodar()
        self.chassi.mostrar_tipo()

# Criando as partes do carro
motor_v6 = Motor(350)
rodas_aro_18 = Roda(18)
chassi_esportivo = Chassi("esportivo")

# Criando um carro completo com essas partes
carro_esportivo = CarroCompleto("BMW", motor_v6, rodas_aro_18, chassi_esportivo)

carro_esportivo.ligar_carro()