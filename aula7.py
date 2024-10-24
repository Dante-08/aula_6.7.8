lista = [1,2,3,4,5,6]
print(lista)

 n = 20
 n1 = lista[0]
 n2 = lista[1]
 soma = n1 + n2
 print(soma)

# ADICIONAR ITENS A LISTA
 lista[0] = 25
 lista.append(10)
 lista.append(50)
 lista += (30,18,28,2,'test',n)
 lista.extend([30,5.5])
 lista.insert(0,18)
 print(lista)


 # REMOVER ITENS DA LISTA
del lista[3]
lista.remove(5)
 lista.pop()
 print(lista)

# COPIAR E LIMPAR UMA LISTA
nova_lista = lista.copy()
 print(nova_lista)
 lista.clear()
 print(lista)

# CRIAÇÃO DE UMA LISTA USANDO LIST()
 lista2 = list(range(1,150))
 print(lista2)


lista = [10,10,10,10,10,10,10,10,10,10,10,10,10]
n = int(input('Digite o valor "10" e veja quantos tem dentro da lista: '))
print(lista.count(n))
