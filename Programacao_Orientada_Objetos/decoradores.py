# Decoradores

# Decoradores são funções que permitem modificar o comportamento de outras funções ou métodos.
# Eles são frequentemente usados para adicionar funcionalidades, como autenticação, registro de logs, etc.
# Decoradores são definidos usando o símbolo "@" seguido do nome da função decoradora, e são aplicados antes da definição da função que desejamos decorar.

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada!")

minha_funcao()

# Utilizando o decorador como classe

class MeuDecoradorClasse:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwds):
        print("Antes da função ser chamada(Decorador de classe)")
        self.func()
        print("Depois da função ser chamada(Decorador de classe)")

@MeuDecoradorClasse
def segunda_funcao():
    print("Segunda função foi chamada!")

segunda_funcao()
