class SaldoInsuficienteError(Exception):
    pass

class LimitExcedError(Exception):
    pass

class ContaDestinoInvalidaError(Exception):
    pass

class Conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo 
        self.limite = limite 
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado com sucesso!")
        else:
            print("O valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError (f"Saldo insuficiente para sacar {valor} || Saldo atual: {self.saldo}")
        self.saldo -= valor
        return self.saldo
    
    def transferir(self,valor, conta_destino):
        if not isinstance(conta_destino, Conta):
            raise ContaDestinoInvalidaError(f'Erro ao transferir!! Conta de destino não existe')
        if valor > self.limite:
            raise LimitExcedError (f'Erro ao tranferir!!  Valor superior ao limite {self.limite}')
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente para sacar {valor} || Saldo atual: {self.saldo}")
        
        self.saldo -= valor 
        conta_destino.saldo += valor
        print(f"Transferência de {valor} para {conta_destino.titular} realizada com sucesso!") 



try:
    conta1 = Conta("Diego", saldo=500, limite=1000)
    conta2 = Conta("Sabrina", saldo=300, limite=500)

    conta1.depositar(200) 
    conta1.transferir(200,conta_destino=conta2) 
    conta1.transferir(300,conta_destino=None)
    conta1.transferir(45500,conta_destino=conta2)
    conta1.sacar(800)      

except SaldoInsuficienteError as e:
    print(e)
except LimitExcedError as e:
    print(e)
except ContaDestinoInvalidaError as e:
    print(e)
