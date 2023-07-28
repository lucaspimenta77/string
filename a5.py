#Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça uma função que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
#• Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
#• Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
#• Se o número de lados for igual a 5, escrever PENTÁGONO.

def calcular_poligono(num_lados, medida_lado):
    if num_lados == 3:
        perimetro = num_lados * medida_lado
        print(f"TRIÂNGULO - Perímetro: {perimetro} cm")
    elif num_lados == 4:
        area = medida_lado * medida_lado
        print(f"QUADRADO - Área: {area} cm²")
    elif num_lados == 5:
        print("PENTÁGONO")
    else:
        print("Número de lados inválido. Informe apenas 3, 4 ou 5.")

num_lados = int(input("Digite o número de lados do polígono: "))
medida_lado = float(input("Digite a medida do lado do polígono (em cm): "))

if num_lados in [3, 4, 5]:
    calcular_poligono(num_lados, medida_lado)
else:
    print("Número de lados inválido. Informe apenas 3, 4 ou 5.")
