import random

Porta_AvioesX = random.randint(1, 10)
Porta_AvioesY = random.randint(1, 10)
Contra_TorpedeiroX = random.randint(1, 10)
Contra_TorpedeiroY = random.randint(1, 10)
SubmarinoX = random.randint(1, 10)
SubmarinoY = random.randint(1, 10)
Barco_De_PatrulhaX = random.randint(1, 10)
Barco_De_PatrulhaY = random.randint(1, 10)
EncouracadoX = random.randint(1, 10)
EncouracadoY = random.randint(1, 10)

# Tabuleiro
tabuleiro = [["agua"] * 10 for _ in range(10)]

# Função para verificar e atualizar o tabuleiro
def verificar_e_atualizar_tabuleiro(x, y):
    if x == Porta_AvioesX and y == Porta_AvioesY:
        tabuleiro[y - 1][x - 1] = "Porta Aviões"
    elif x == Contra_TorpedeiroX and y == Contra_TorpedeiroY:
        tabuleiro[y - 1][x - 1] = "Contra Torpedeiro"
    elif x == SubmarinoX and y == SubmarinoY:
        tabuleiro[y - 1][x - 1] = "Submarino"
    elif x == Barco_De_PatrulhaX and y == Barco_De_PatrulhaY:
        tabuleiro[y - 1][x - 1] = "Barco de Patrulha"
    elif x == EncouracadoX and y == EncouracadoY:
        tabuleiro[y - 1][x - 1] = "Encouraçado"
    else:
        print("Você não acertou nenhuma embarcação.")

# Jogo
while True:
    Coordenada_Em_X = int(input("Digite a coordenada em X (1-10): "))
    Coordenada_Em_Y = int(input("Digite a coordenada em Y (1-10): "))

    if Coordenada_Em_X < 1 or Coordenada_Em_X > 10 or Coordenada_Em_Y < 1 or Coordenada_Em_Y > 10:
        print("Disparo fora do campo de batalha.")
        continue

    verificar_e_atualizar_tabuleiro(Coordenada_Em_X, Coordenada_Em_Y)

    # Imprime o tabuleiro após cada jogada
    for linha in tabuleiro:
        print(" ".join(linha))

    # Verifica se todas as embarcações foram encontradas
    if all("agua" not in linha for linha in tabuleiro):
        print("Parabéns, você encontrou todas as embarcações!")
        break
    