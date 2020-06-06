# Definilção de variáveis de números dois inteiros
inteiro1 = 3
inteiro2 = 5
soma_inteiros = inteiro1 + inteiro2

print("Que tipo de mumero é 3 + 5?")

# Imprime a classe/tipo da variável soma_inteiros
print(type(soma_inteiros))

print()
print()

# define os decimais para o teste
decimal1 = 3.35
decimal2 = 4.98
soma_decimais = decimal1 + decimal2

# imprime os decimais para o teste
print("É decimais os numeros 3.35 com 4.98?")
print(type(soma_decimais))

print()
print()

# define os numeros complexos
complexo1 = 5j
complexo2 = 7j
soma_complexos = complexo1 + complexo2
soma_complexos_inteiros = soma_inteiros + soma_complexos

print(f"{soma_complexos_inteiros} é um resultado complexo?")
print(type(soma_complexos_inteiros))
