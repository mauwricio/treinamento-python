'''Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado. '''

nota1 = float (input("insira a primeira nota: "))
nota2 = float (input("insira a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("você foi aprovado")
else:
    print("você foi reprovado")
