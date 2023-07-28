def soma_intervalo(n1, n2):

    soma = 0

    if n1 <= n2:
        
        for num in range(n1, n2 + 1):
            soma += num
    else:
        for num in range(n2, n1 + 1):
            soma += num

    return soma


n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))

resultado = soma_intervalo(n1, n2)
print(f"A soma dos números inteiros no intervalo [{n1}, {n2}] é: {resultado}")
