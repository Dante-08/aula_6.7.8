from random import randint

numero_aleatorio = randint(1,10)
chute = int(input('Digite um numero: '))

if chute == numero_aleatorio:
    print('Você Acertou')
else:
    print('Você errou!!!')
    print(f'O numero correto era {numero_aleatorio}')