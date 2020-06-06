"""
Aq vamo brincar com as condicionais se(if), senão(else), se e somente(elif)
"""
print("Atenção! Não leve este programa a sério, "
      "\nse você NÃO tem amor próprio e TER depressão, "
      "\nvocê NÃO pode utilizar esse programa")

print()
print()

print("Vamos ver se vc é gordo!")
print("Primeiro, digite o seu nome")
nome = input("nome -> ")
nome = nome.split()[0]
nome = nome.capitalize()

print(f"Olá {nome}!, digite o seu peso!")
peso = input("peso -> ")
peso = float(peso)

print()

print("Certo! agora digite o a sua altura.")
altura = input("altura -> ")
altura = float(altura)

print()

resultado = (altura / peso) * 1000

if resultado < 26:
    print(f"{nome.upper()} VOCÊ É GORDO(A)")
elif int(resultado) == 37:
    print(f"{nome} sua magreza é nível sávio kkk")
elif int(altura > 3):
    print("Rapaz? tu é um prédio? kkkk")
else:
    print(f"vc é magrelo(a) ein kkkk")
