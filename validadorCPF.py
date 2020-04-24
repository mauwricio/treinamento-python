def calcularDigito1(cpf):
    soma1 = int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) * 2
    resto1 = soma1 % 11

    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1
    return digito1

def calcularDigito2(cpf):
    soma2 = int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + digito1 * 2
    resto2 = soma2 % 11

    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2
    return digito2



cpf = '38321903843'

digito1 = calcularDigito1(cpf)
digito2 = calcularDigito2(cpf)




if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
    cpf = 'CPF válido'
else:
    cpf = 'CPF inválido'

print(cpf)
