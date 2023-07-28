def verificar_divisibilidade(x, y):
    if x % y == 0:
        return 1
    else:
        return 0

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))


resultado = verificar_divisibilidade(x, y)
print(f"Resultado: {resultado}")
