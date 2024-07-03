from random import randint
from time import sleep

lista = ("Pedra", "Papel", "Tesoura")

computer = randint(0, 2)

ask = int(input('''Escolha uma opção para jogar:

[0] Pedra
[1] Papel
[2] Tesoura

Insira sua escolha: '''))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POO!\n")

print("-="*20)
print("O computador escolheu: {}".format(lista[computer]))
print("O jogador escolheu: {}".format(lista[ask]))
print("-="*20)

if computer == 0:
    if ask == 0:
        print("Uma gravata!")
    elif ask == 1:
        print("Jogador perdeu!")
    elif ask == 2:
        print("Computador ganhou!")
    else:
        print("Operação inválida!")

elif computer == 1:
    if ask == 0:
        print("Computador perdeu!")
    elif ask == 1:
        print("Uma gravata!")
    elif ask == 2:
        print("Jogador ganhou!")
    else:
        print("Operação inválida!")

elif computer == 2:
    if ask == 0:
        print("Jogador ganhou!")
    elif ask == 1:
        print("Computador perdeu!")
    elif ask == 2:
        print("Uma gravata!")
    else:
        print("Operação inválida!")
else:
    print("Operação inválida!")
