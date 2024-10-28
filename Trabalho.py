escolha = input("Deseja jogar este jogo? (Sim/Não): ")
if escolha == "Sim":
    print ("Bem vindo à floresta!")
    print("O teu objetivo é encontrar a saída sem cair nas armadilhas.\n")
else:
  print("OK, o jogo não foi iniciado")
  exit ()

escolha = input("Estás preso, Tenta sair daí o mais rapido possivel. Escolhe esquerda(E) ou direita(D): ").lower()

if escolha == "e":
    escolha = input("Encontraste um lago. Queres atravessar(A) ou ir á volta(I) do lago?: ").lower()

    if escolha == "i":
        escolha = input("Encontraste uma caverna. Queres entrar(E) na caverna ou seguir em frente(S)?: ").lower()

        if escolha == "e":
            print("Encontraste a saída secreta! Parabéns, escapaste da floresta!")
        else:
            print("Perdeste-te na floresta. GAME OVER!")
    else:
        print("O lago era muito fundo e não conseguiste atravessar. GAME OVER!")

else:
    print("Infelizmente, caíste numa armadilha. GAME OVER!")
