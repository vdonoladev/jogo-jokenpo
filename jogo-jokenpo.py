from random import randint
from time import sleep

lista = ("Rock", "Paper", "Scissors")

computer = randint(0,2)

ask = int(input('''Choose an option to play:

[0] Stone
[1] Role
[2] Scissors

Enter your choice: '''))

print("JO\n")
sleep(1)
print("KEN\n")
sleep(1)
print("POO!\n")

print("-="*20)
print("The computer chose: {}".format(lista[computer]))
print("The player chose: {}".format(lista[ask]))
print("-="*20)

if computer == 0:
	if ask == 0:
		print("A tie!")
	elif ask == 1:
		print("Player lost!")
	elif ask == 2:
		print("Computer won!")
	else:
		print("Invalid Operation!")

elif computer == 1:
	if ask == 0:
		print("Computer lost!")
	elif ask == 1:
		print("A tie!")
	elif ask == 2:
		print("Player won!")
	else:
		print("Invalid Operation!")

elif computer == 2:
	if ask == 0:
		print("Player won!")
	elif ask == 1:
		print("Computer won!")
	elif ask == 2:
		print("A tie!")
	else:
		print("Invalid Operation!")
else:
	print("Invalid Operation!")
