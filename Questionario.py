def fazer_pergunta(pergunta, alternativas, resposta_certa):
    print("\n" + pergunta)
    for i, alt in enumerate(alternativas):
        print(f"{i + 1}. {alt}")

    try:
        escolha = int(input("Digite o número da resposta: "))
        if alternativas[escolha - 1].lower() == resposta_certa.lower():
            print("✅ Correto!")
            return True
        else:
            print(f"❌ Errado! A resposta certa era: {resposta_certa}")
            return False
    except (ValueError, IndexError):
        print("⚠️ Entrada inválida. Contando como errada.")
        return False

def questionario():
    print("📚 Iniciando o questionário...\n")

    pontuacao = 0
    perguntas = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "alternativas": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
            "resposta": "Brasília"
        },
        {
            "pergunta": "Qual linguagem estamos usando agora?",
            "alternativas": ["Java", "Python", "C++", "JavaScript"],
            "resposta": "Python"
        },
        {
            "pergunta": "quem desbriu o Brasil'?",
            "alternativas": ["indios", "pelé", "neymar", "Bolsonaro"],
            "resposta": "indios"
        }
    ]

    for q in perguntas:
        if fazer_pergunta(q["pergunta"], q["alternativas"], q["resposta"]):
            pontuacao += 1

    print(f"\n🏁 Fim do questionário! Sua pontuação: {pontuacao}/{len(perguntas)}")
    if pontuacao == len(perguntas):
        print("🎉 Mandou muito bem!")
    elif pontuacao >= 2:
        print("😎 Foi bem!")
    else:
        print("🧐 Dá pra melhorar...")

# Executa o questionário
questionario()
