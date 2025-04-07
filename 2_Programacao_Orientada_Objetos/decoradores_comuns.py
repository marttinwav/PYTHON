# Decoradores comuns

# Decoradores comuns são funções que podem ser aplicadas a outras funções ou métodos para modificar seu comportamento. Eles são frequentemente usados para adicionar funcionalidades, como autenticação, registro de logs, etc. Aqui estão alguns exemplos de decoradores comuns em Python:
# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # atributo de classe
    def __init__(self, nome):
        self.nome = nome

    # Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instancia: {self.nome}"
    @classmethod
    def metodo_classe(cls):
        return f"Método de classe: {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estatico: Não requer instância ou classe."

obj = MinhaClasse(nome="Exemplo")
print(obj.metodo_instancia()) # Chama o método de instancia
print(MinhaClasse.valor) # Acessa o atributo de classe
print(MinhaClasse.metodo_classe()) # Chama o método de classe
print(MinhaClasse.metodo_estatico()) # Chama o método estático

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))

configuracao1 = "Toyota,Corolla,2025"
carro1 = Carro.criar_carro(configuracao1)
print(f"Carro 1: {carro1.marca} {carro1.modelo} {carro1.ano}")

class Matematica:
    
    @staticmethod
    def somar(a,b):
        return a + b
    
print(Matematica.somar(a=5, b=10)) # Chama o método estático somar

