import perguntas

saldo = 1000
# Função para exibir a pergunta e opções de resposta
def exibir_pergunta_e_respostas(pergunta):
    print(pergunta["pergunta"])
    for opcao in pergunta["opcoes_resposta"]:
        print(opcao)

# Função para verificar se a resposta do usuário está correta
def verificar_resposta(pergunta, resposta_usuario):
    return resposta_usuario.lower() == pergunta["resposta_correta"]


# Loop principal do jogo
for pergunta in perguntas_e_respostas:
    exibir_pergunta_e_respostas(pergunta)
    resposta_usuario = input("Digite a letra da sua resposta (a, b, c ou d): ")
    if verificar_resposta(pergunta, resposta_usuario):
        print("Resposta correta!\n")
        saldo * 2
        print (saldo)
    else:
        print("Resposta incorreta!\n")