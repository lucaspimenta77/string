def imprimir_tres_primeiros_dias_semana(numero):
    dias_semana = {
        1: "DOM",
        2: "SEG",
        3: "TER",
        4: "QUA",
        5: "QUI",
        6: "SEX",
        7: "SAB"
    }

    if numero in dias_semana:
        print(dias_semana[numero])
    else:
        print("Número inválido. Digite um número de 1 a 7 correspondente a um dia da semana.")

numero_dia = int(input("Digite um número de 1 a 7 correspondente a um dia da semana: "))


imprimir_tres_primeiros_dias_semana(numero_dia)
