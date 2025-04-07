class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitit_som(self):
        pass
class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
    
# Exemlpo de herança múltipla

class Morcego(Mamifero, Ave):
    def _emitir_som(self):
        return f"{self.nome} está emitem sons ultrassônicos."
    
morcego = Morcego(nome="Morceguinho")

# Acessando métodos da classe "Animal"
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitit_som())

# Acessando métodos da classe "Mamifero" e "Ave"
print("Amamentando:", morcego.amamentar())
print("Voando:", morcego.voar())