"""
itera sobre sequências booleanas.(True, False)
    while expressão_booleana
    //execução do loop:
"""
num = 1
pergunta = True

while pergunta:
    print(num)
    num = num + 1
    if num > 10:
        pergunta = False

print()

num = 1
while num < 10 + 1:
    print(num)
    num = num + 1

print()

jessica_acabou = ' '

while jessica_acabou != "sim":
    print("já acabou, Jéssica?")
    jessica_acabou = input("->")

print("Que bom!")
