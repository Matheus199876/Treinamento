def quiz_futebol():
    print("🏆 Bem-vindo ao quiz do flamengo ⚽\n")
    pontuacao = 0

    perguntas = [
        {
            "pergunta": "1. qual o maior artilheiro do flamengo?",
            "opcoes": ["A) zico", "B) gabigol", "C) arrascaeta", "D) adriano imperador"],
            "resposta": "A"
        },
        {
            "pergunta": "2. qual ano o flamengo foi fundado?",
            "opcoes": ["A) 1890", "B) 1900", "C) 1895", "D) 2000"],
            "resposta": "C"
        },
        {
            "pergunta": "3. quantos mundiais o flamengo tem?",
            "opcoes": ["A) 5", "B) 1", "C) 3", "D) 2"],
            "resposta": "B"
        },
        {
            "pergunta": "4. quantas libertadores o flamengo tem?",
            "opcoes": ["A) 1", "B) 4", "C) 2", "D) 3"],
            "resposta": "D"
        },
        {
            "pergunta": "5. quantas copas do brasil o flamengo tem?",
            "opcoes": ["A) 1", "B) 4", "C) 3", "D) 5"],
            "resposta": "D"
        }
    ]

    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)
        resposta_usuario = input("Sua resposta (A, B, C ou D): ").strip().upper()

        if resposta_usuario == pergunta["resposta"]:
            print("✅ Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"❌ Resposta errada! A resposta correta era {pergunta['resposta']}.\n")

    print(f"🎯 Fim do quiz! Você acertou {pontuacao} de {len(perguntas)} perguntas.")

if __name__ == "__main__":
    quiz_futebol()