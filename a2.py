# Faça uma função que calcule a hipotenusa. Os catetos são os dados de entrada e a hipotenusa é o dado de saída.

import math


def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa


a = float(input("Digite o valor do cateto A: "))
b = float(input("Digite o valor do cateto B: "))
hipotenusa = calcular_hipotenusa(a, b)
print(f"A hipotenusa com catetos {a} e {b} é igual a {hipotenusa:.2f}.")
