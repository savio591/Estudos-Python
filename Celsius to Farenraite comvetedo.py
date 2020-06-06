print("Olá, Digite seu primeiro nome!")
nome = input("nome: ")
nome = nome.split()[0]
nome = nome.capitalize()

print()

print(f"Bem vindo(a) {nome}, digite o valor em Celsius p eu converter em farinrait pfv")
valor = input("valor ->")
valor = float(valor)
resultado = valor * (9.0 / 5.0) + 32.0
resultado = int(resultado)
print()

if valor < 60:
    print(f"{nome} o resultado é {resultado}")

if valor > 60:
    print(f"o result é {resultado}, mas cara?")
print()
if valor > 40:
    print("Meu filho? tu mora no inferno é?")
