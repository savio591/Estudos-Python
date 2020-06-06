""""
Cria sequencias numéricas não aleatórias, de forma especificada
Util para o repetidor 'for'

    Uso geral
        range(valor_de_parada)
        range(valor_de_inicio, valor_de_parada)
        range)valor_de_inicio, valor_de_entrada, passo)
    o valor deve ser inteiro.
"""

# forma 1: imprimir 10 números em seq, 0 a 10
for num in range(11):
    print(num)

print()

# forma 2: imprimir 10 números em seq, 1 a 10
for num in range(1, 11):
    print(num)

print()

# forma 3: imprimir números em seqência de 1 a 10, com passe de 2(1, 3, 5, 7, 9)
for num in range(1, 11, 2):
    print(num)

print()

# forma 4: imprimir números em sequência de 5 a 20, com passe de 5(5, 10, 15, 20)
for num in range(5, 21, 5):
    print(num)

print()

# forma 5: imprimir números em sequência inversa, 1 a 10. O passe -1 deve ser adicionado
# para comprovar ordem inversa
for num in range(10, 0, -1):
    print(num)
