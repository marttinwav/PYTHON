# POO

# Classes são moldes para criar objetos. Elas definem as propriedades e comportamentos que os objetos terão.
# Objetos são instâncias de classes. Eles têm suas próprias características e podem executar ações definidas pela classe.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Objetos

pessoa1 = Pessoa("Martin", 30)
print(pessoa1.nome)
print(pessoa1.idade)
# print(pessoa1.__dict__)  # Mostra todos os atributos do objeto pessoa1
mensagem = pessoa1.saudacao()
print(mensagem) # Chama o método saudacao da classe Pessoa

pessoa2 = Pessoa("Ana", 25)
mensagem = pessoa2.saudacao()
print(mensagem)
