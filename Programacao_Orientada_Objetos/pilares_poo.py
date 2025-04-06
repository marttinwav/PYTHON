 # Herança

# Exemplo de herança

class Animal:
    def __init__(self, nome):
        self.nome = nome

        def andar(sef):
            return f"{self.nome} está andando."
        def emitir_som(self):
            pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"
    

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    


# Exemplo de polimorfismo
dog = Cachorro(nome="Rex")
cat = Gato(nome="Mimo")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz o som: {animal.emitir_som()}")

# Exemplo de encapsulamento

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria(saldo=1000)
print(f"Saldo das conta: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo das conta: {conta.consultar_saldo()}")
conta.depositar(valor=-500) # Não deve alterar o saldo
print(f"Saldo das conta: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo das conta: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)

# Exemplo de abstração

from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar (self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass
    def ligar(self):
        return "Carro ligado."
    
    def desligar(self):
        return "Carro desligado."

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())

