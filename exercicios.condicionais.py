# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = int(input('Digite um numero: '))
if numero > 0:
    print('O numero é positivo')
elif numero == 0:
    print('O numero é 0')
else:
    print('O numero é negativo')

# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você já pode votar!!!')
else:
    print('Você ainda não pode votar!!!')

# 3*
# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
n = int(input('>>>'))
if n % 2 == 0:
    print('Numero par')
else:
    print('Numero impar')

# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
l1 = int(input('Digite um numero'))
l2 = int(input('Digite um numero'))
l3 = int(input('Digite um numero'))
if (l1 == l2) and (l2 == l3) and (l3 == l1):
    print('Esse triângulo é equilátero!')
elif (l1 != l2) and (l2 != l3) and (l3 != l1):
    print('Esse triangulo é escaleno!')
else:
    print('Esse triângulo é isósceles')

# 5*
# Determine se um número é múltiplo de 5 e 7.
number = int(input('>>>'))
if number % 5 == 0 and number % 7 == 0:
    print('É multiplo de  5 e  7')
else:
    print('Nãp é multiplo')

# 6*
# Verifique se um número é positivo e maior que 10
numeral = int(input('>>>'))
if numeral > 10 and numeral > 0:
    print('É maior!!)

# 7
# Verifique se um número é divisível por 3 ou 5.
numeroso = int(input('>>>'))
if numeroso % 3 == 0:
    print('É divisivel por 3')
elif numeroso % 5 == 0:
    print('É divisivel por 5')
else:
    print('Não é divisilvel por 3 e nem 5')
