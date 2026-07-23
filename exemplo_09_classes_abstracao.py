from abc import ABC, abstractmethod

# exemplo IA

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")

cachorro = Cachorro()
gato = Gato()

cachorro.fazer_som()
gato.fazer_som()

# exemplo próprio

class Passear(ABC):
    @abstractmethod
    def iniciar_passeio(self):
        pass

class Caminhada(Passear):
    def iniciar_passeio(self):
        print("Caminhando")

class Corrida(Passear):
    def iniciar_passeio(self):
        print("Correndo")

caminhada = Caminhada()
corrida = Corrida()

caminhada.iniciar_passeio()
corrida.iniciar_passeio()