import random

#Gera os 9 primeiros números aleatórios
a = random.randrange(1, 10)
b = random.randrange(1, 10)
c = random.randrange(1, 10)
d = random.randrange(1, 10)
e = random.randrange(1, 10)
f = random.randrange(1, 10)
g = random.randrange(1, 10)
h = random.randrange(1, 10)
i = random.randrange(1, 10)

digito1 = int()
digito2 = int()

soma1 = (a * 10) + (b * 9) + (c * 8) + (d * 7) + (e * 6) + (f * 5) + (g * 4) + (h * 3) + (i * 2)
resto1 = soma1 % 11

if resto1 < 2:
    digito1 = 0

else:
    digito1 = 11 - resto1

soma2 = (a * 11) + (b * 10) + (c * 9) + (d * 8) + (e * 7) + (f * 6) + (g * 5) + (h * 4) + (i * 3) + (digito1 * 2)
resto2 = soma2 % 11

if resto2 < 2:
    digito2 = 0

else:
    digito2 = 11 - resto2

print(a, b, c, d, e, f, g, h, i, digito1, digito2)