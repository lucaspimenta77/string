def polegadas_para_cm(pol):
    return pol * 2.54

valor_pol = float(input("Digite o valor em polegadas: "))

valor_cm = polegadas_para_cm(valor_pol)
print(f"{valor_pol} polegadas equivalem a {valor_cm} centímetros.")
