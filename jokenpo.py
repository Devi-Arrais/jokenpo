from random import randint
from time import sleep

items = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print("Escolha um:\n[0] Pedra \n[1] Papel \n[2]Tesoura")

player = int(input("Sua opção: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(2)
print("#"*10)
print(f"O computador escolheu: {items[computador]}")
print(f"Você escolheu: {items[player]}")
print("#"*10)

if computador == 0:
   if player == 0:
      print("EMPATE")
   elif player == 1:
      print("VOCÊ VENCEU!!!!")
   elif player == 2:
      print("O COMPUTADOR VENCEU, QUE PENA")
   else:
      print("jogada invalida")

if computador == 1:
   if player == 0:
      print("O COMPUTADOR VENCEU, QUE PENA")
   elif player == 1:
      print("EMPATE")
   elif player == 2:
      print("VOCÊ VENCEU!!!!")
   else:
      print("jogada invalida")

if computador == 2:
   if player == 0:
      print("VOCÊ VENCEU!!!!")
   elif player == 1:
      print("O COMPUTADOR VENCEU, QUE PENA")
   elif player == 2:
      print("EMPATE")
   else:
     print("jogada invalida")

