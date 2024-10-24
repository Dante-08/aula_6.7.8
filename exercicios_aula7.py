# # Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
# lista = list(range(2,21))
# print(lista)

# # Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 em 5 até 50, em seguida, calcule e imprima a soma desses múltiplos.
# lista2 = list(range(5,55,5))
# soma_lista = sum(lista2)
# print(soma_lista)

# # Exercício 3: Crie uma lista chamada pessoas que contenha os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.
# pessoa1 = 5
# pessoa2 = 4
# pessoa3 = 3
# pessoa4 = 2
# pessoa5 = 1
# pessoas = [pessoa1,pessoa2,pessoa3,pessoa4,pessoa5]
# print(pessoas)

# # Exercício 4: Acesse e imprima o terceiro elemento da lista numeros.
# number = [1,2,3,4,5]
# print(number[2])

# # Exercício 5: Adicione o número 9 à lista numeros e imprima a lista atualizada.
# number.append(9)
# print(number)

# # Exercício 6: Remova o número 5 da lista numeros e imprima a lista resultante.
# del number[4]
# print(number)

# # Exercício 7: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.
# carros = ['Chevrolet','Citroën','Fiat']
# number2 = [1,2,3,4,5]
# carros_e_numeros = carros + number2
# print(carros_e_numeros)


pessoas = ['pessoa1','pessoa2']
pessoas[0] = 1
print(pessoas)