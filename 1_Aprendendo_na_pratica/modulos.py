print("Exemplo de importação de modulo padrão")

import math as mt
from math import sqrt
from math import pi

raiz_quadradra = mt.sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadradra}")

print("\n Exemplo de criação e utilização de um modulo personalizado")

import meu_modulo as mm

mensagem = mm.saudacao("Lucas")
print(mensagem)

resultado = mm.dobro(10)
print(f"O dobro de 10 é {resultado}")