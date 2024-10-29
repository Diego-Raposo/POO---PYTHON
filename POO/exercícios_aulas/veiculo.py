class Veiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo 
    def informacao(self):
        return print(f'Marca: {self.marca} || Modelo: {self.modelo}')
    
class Carro(Veiculo):
    def __init__(self,marca, modelo,numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas
    def informacao_completa(self):
        return print(f'Marca: {self.marca} || Modelo: {self.modelo} || Numero de Portas: {self.numero_portas}')
    

carro1 = Veiculo('Wolkswagen', 'gol')
carro1.informacao()

carro2 = Carro("Honda", "Honda Civic",4)
carro2.informacao_completa()