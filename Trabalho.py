escolha = input("Deseja jogar este jogo? (Sim/Não): ") #pregunta ao jogador se quer jogar o jogo ou não
if escolha == "Sim":
    print ("Bem vindo à floresta!") #se escolher "Sim" o jogo irá ler esse print e o que está a baixo 
    print("O teu objetivo é encontrar a saída sem cair nas armadilhas.\n")
else:
  print("OK, o jogo não foi iniciado") # se escolher não o jogo irá ler esse print
  exit ()

escolha = input("Estás preso, Tenta sair daí o mais rapido possivel. Escolhe esquerda(E) ou direita(D): ").lower() # pede para escolher esquerda ou direita

if escolha == "e": 
    escolha = input("Encontraste um lago. Queres atravessar(A) ou ir á volta(I) do lago?: ").lower() #diz ao jogador que encontrou um lago e se quer atravessar ou ir á volta

    if escolha == "i":
        escolha = input("Encontraste uma caverna. Queres entrar(E) na caverna ou seguir em frente(S)?: ").lower() #diz ao jogador que encontrou uma caberna e pergunta se quer entrar ou seguir em frente

        if escolha == "e":
            print("Encontraste a saída secreta! Parabéns, escapaste da floresta!") # diz ao jogador que encontrou a saida
        else:
            print("Perdeste-te na floresta. GAME OVER!") #se escolher seguir em frente o codigo lê o print
    else:
        print("O lago era muito fundo e não conseguiste atravessar. GAME OVER!") #se escolher atravessar o lago o codigo lê o print

else:
    print("Infelizmente, caíste numa armadilha. GAME OVER!") # se escolher direita o codigo lê o print 
