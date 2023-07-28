def calcular_maior_valor(a, b):
    if a > b:
        return a
    else:
        return b

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

maior_valor = calcular_maior_valor(valor1, valor2)
print(f"O maior valor entre {valor1} e {valor2} é: {maior_valor}")
