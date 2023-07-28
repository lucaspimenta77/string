# Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça uma função que receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).


def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


def aprovacao(media):
    if media >= 6.0:
        print(f"Parabens voce foi aprovado!!! Sua media final foi {media}")
    else:
        print("Voce foi reprovado")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = calcular_media(nota1, nota2)

aprovacao(media)

print(f"Sua média semestral é {media} ")
