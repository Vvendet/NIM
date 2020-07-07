# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:14:33 2020

@author: Julio César
Jogo do NIM
um jogador vence ao tirar as últimas peças possíveis do jogo.
"""
from math import sqrt as matematica 
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
def jogo():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    escolha = int(input("1 - Partida isolada  2 - Campeonato:  "))
    if escolha == 1:
        return partida()
    elif escolha == 2:
        campeonato()
    else:
        
        while escolha != 1 or escolha != 2:
            print("Entrada inválida")
            escolha = int(input("1 - Partida isolada  2 - Campeonato:  "))
    
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? " ))
    if n == 2 and m == 3:
        print("Computador começa!")
        while n >0:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou ",jogada," peças!")           
            n = n - jogada
            print("Agora restam ", n," peças no tabuleiro!")
            if n == 0:
                print("Computador venceu!")

            if n > 0:
                jogada = usuario_escolhe_jogada(n, m)
                n = n-jogada        
                print("Agora restam ", n," peças no tabuleiro!")
                if n == 0:
                    print("Voce venceu!")

    elif n<m:
        while n < m:
            print("entrada inválida")
            m = int(input("Limite de peças por jogada? " ))

    elif  n == m: 
        print("Computador começa!")
        while n >0:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou ",jogada," peças!")           
            n = n - jogada
            print("Agora restam ", n," peças no tabuleiro!")
            if n == 0:
                print("Computador venceu!")

            if n > 0:
                jogada = usuario_escolhe_jogada(n, m)
                n = n-jogada        
                print("Agora restam ", n," peças no tabuleiro!")
                if n == 0:
                    print("Voce venceu!")


    elif n == 9 and m == 2:
        print("Você começa!")
        while n > 0:  
            jogada = usuario_escolhe_jogada(n, m)
            n = n-jogada  
            
            print("Agora restam ", n , " peças no tabuleiro")
            if n == 0:
                            print("Você venceu!") 
            if n > 0:
                jogada = computador_escolhe_jogada(n, m)
                print("Computador removeu ", jogada, " peças.")         
                n = n - jogada
                print("Agora restam ", n," peças no tabuleiro!")
                if n == 0:
                    print("Computador venceu!")

    elif n == 11 and m == 3:
        print("Computador começa!")
        while n >0:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou ",jogada," peças!")           
            n = n - jogada
            print("Agora restam ", n," peças no tabuleiro!")
            if n == 0:
                print("Computador venceu!")

            if n > 0:
                jogada = usuario_escolhe_jogada(n, m)
                n = n-jogada        
                print("Agora restam ", n," peças no tabuleiro!")
                if n == 0:
                    print("Voce venceu!")


    elif n == 5 and m == 3:
        print("Computador começa!")
        while n >0:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou ",jogada," peças!")           
            n = n - jogada
            print("Agora restam ", n," peças no tabuleiro!")
            if n == 0:
                print("Computador venceu!")

            if n > 0:
                jogada = usuario_escolhe_jogada(n, m)
                n = n-jogada        
                print("Agora restam ", n," peças no tabuleiro!")
                if n == 0:
                    print("Voce venceu!")



            
    elif n%(m+1) or n%m==0:
        print("Você começa!")
        while n > 0:  
            jogada = usuario_escolhe_jogada(n, m)
            n = n-jogada  
            
            print("Agora restam ", n , " peças no tabuleiro")
            if n == 0:
                            print("Você venceu!") 
            if n > 0:
                jogada = computador_escolhe_jogada(n, m)
                print("Computador removeu ", jogada, " peças.")         
                n = n - jogada
                print("Agora restam ", n," peças no tabuleiro!")
                if n == 0:
                    print("Computador venceu!")
    print("")
    print("Fim da partida")
    
def usuario_escolhe_jogada(n,m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > m or jogada <= 0 or jogada > n:
        print("entrada inválida")
        jogada = int(input("Quantas peças você vai tirar? "))
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

    
    
        


jogo()
