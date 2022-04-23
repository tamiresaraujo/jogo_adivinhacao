import random

print("Bem vindo ao jogo de Adivinhação")

numero_secreto = random.randrange(1,21)
total_tentativas = 0
pontos = 1000

print("Níveis de Dificuldade")
print("1 - Fácil | 2 - Médio | 3 - Díficil")
nivel = int(input("Escolha seu nível: "))

if (nivel == 1):
    total_tentativas = 10
elif (nivel == 2):
    total_tentativas = 6
else:
    total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))

    chute_entrada = input("Digite um número entre 1 e 20: ")
    print("Você digitou: ", chute_entrada)
    chute = int(chute_entrada)

    if (chute < 1 or chute > 20):
        print("Você deve digitar um número entre 1 e 20!")
        continue

    acertou_chute = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if (acertou_chute):
        print("Você acertou e fez um total de {} pontos!".format(pontos))
        break
    else:
        if (chute_maior):
            print("Você errou! Seu chute foi maior que o número correto!")
        elif (chute_menor):
            print("Você errou! Seu chute foi menor que o número secreto!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim de jogo!")