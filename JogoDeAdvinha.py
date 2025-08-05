import random

def jogar():
    print("🎯 Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1

            if chute < 1 or chute > 100:
                print("⛔ O número precisa estar entre 1 e 100!")
                continue

            if chute == numero_secreto:
                print(f"✅ Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif chute < numero_secreto:
                print("🔺 Tente um número MAIOR.")
            else:
                print("🔻 Tente um número MENOR.")

        except ValueError:
            print("⚠️ Por favor, digite um número válido!")

# Executa o jogo
jogar()
