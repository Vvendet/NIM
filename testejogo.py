
def partida():

    print(" ")

    # Solicita ao usuário os valores de n e m:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Define uma variável para controlar a vez do computador:
    is_computer_turn = True

    # Decide quem iniciará o jogo:
    if n % (m+1) == 0: is_computer_turn = False

    # Execute enquanto houver peças no jogo:
    while n > 0:

        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peças.".format(jogada))

        # Retira as peças do jogo:
        n = n - jogada

        # Mostra o estado atual do jogo:
        print("Restam apenas {} peças em jogo.\n".format(n))

    # Fim de jogo, verifica quem ganhou:
    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0
def usuario_escolhe_jogada(n, m):

    # Vez do usuário:
    print("Sua vez!\n")

    # Define o número de peças do usuário:
    jogada = 0

    # Enquanto o número não for válido
    while jogada == 0:

        # Solicita ao usuário quantas peças irá tirar:
        jogada = int(input("Quantas peças irá tirar? "))

        # Condições: jogada < n, jogada < m, jogada > 0
        if jogada > n or jogada < 1 or jogada > m:

            # Valor inválido, continue solicitando ao usuário:
            jogada = 0

    # Número de peças válido, então retorne-o:
    return jogada
def computador_escolhe_jogada(n, m):

    # Vez do computador:
    print("Vez do computador!")

    # Pode retirar todas as peças?
    if n <= m:

        # Retira todas as peças e ganha o jogo:
        return n

    else:

        # Verifica se é possível deixar uma quantia múltipla de m+1:
        quantia = n % (m+1)

        if quantia > 0:
            return quantia

        # Não é, então tire m peças:
        return m
def campeonato():

    # Pontuações:
    usuario = 0
    computador = 0

    # Executa 3 vezes:
    for _ in range(3):

        # Executa a partida:
        vencedor = partida()

        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1

    # Exibe o placar final:
    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))

tipo_jogo = 0

# Enquanto não for uma opção válida:
while tipo_jogo == 0:

    # Menu de opções:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print(" ")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")

    # Solicita a opção ao usuário:
    tipo_jogo = int(input("Sua opção: "))
    print(" ")

    # Decide o tipo de jogo:
    if tipo_jogo == 1:
        print("Voce escolheu partida isolada!")
        partida()
        break
    elif tipo_jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Opção inválida!")
        tipo_jogo = 0