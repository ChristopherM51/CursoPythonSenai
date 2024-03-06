# jogo.py
from perguntas import perguntas

def exibir_pergunta(pergunta):
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes"]:
        print(opcao)

def verificar_resposta(pergunta, resposta):
    return pergunta["resposta"].lower() == resposta.lower()

def jogar():
    dinheiro = 0
    for pergunta in perguntas:
        exibir_pergunta(pergunta)
        resposta = input("Digite a letra da sua resposta: ")
        if verificar_resposta(pergunta, resposta):
            print("Resposta correta!\n")
            dinheiro += 1000  # Pontuação arbitrariamente definida
        else:
            print("Resposta incorreta! Fim do jogo.")
            break
    print("Pontuação final: $", dinheiro)

if __name__ == "__main__":
    jogar()
