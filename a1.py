#Faça uma função para converter uma temperatura em graus Fahrenheit para Celsius. A temperatura em Fahrenheit é o dado de entrada e a temperatura em Celsius é o dado de saída. Utilize a fórmula C = (F - 32) * 5/9, onde F é a temperatura em Fahrenheit e C é a temperatura em Celsius.

def fahrenheit_para_celsius(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    return temp_celsius

fahrenheit = float(input('Digite a temperatura em Fahrenheit:  '))
celsius = fahrenheit_para_celsius(fahrenheit)
print(f"{fahrenheit} graus Fahrenheit é igual a {celsius:.2f} graus Celsius.")
