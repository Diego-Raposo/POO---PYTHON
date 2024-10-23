from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

    def dormir(self):
        print("Esta animal está dormindo")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro está latindo")
    
class Gato(Animal):
    def fazer_som(self):
        print("O gato está miando")
    
cachorro = Cachorro()
gato = Gato()

cachorro.fazer_som()
gato.fazer_som()