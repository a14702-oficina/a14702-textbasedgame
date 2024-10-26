escolha = input("Deseja jogar este jogo? (Sim/Não): ")
if escolha == "Sim":
    print ("Bem vindo à floresta!")
    print("O teu objetivo é encontrar a saída sem cair nas armadilhas.\n")
else:
  print("OK, o jogo não foi iniciado")
  exit ()

escolha = input("Estás preso, Tenta sair daí o mais rapido possivel. Escolhe 'esquerda' ou 'direita': ").lower()

if escolha == "esquerda":
    escolha = input("Encontraste um lago. Queres 'atravessar' ou 'ir á volta' do lago?: ").lower()

    if escolha == "ir á volta":
        escolha = input("Encontraste uma caverna. Queres 'entrar' na caverna ou 'seguir em frente'?: ").lower()

        if escolha == "entrar":
            print("Encontraste a saída secreta! Parabéns, escapaste da floresta!")
        else:
            print("Perdeste-te na floresta. GAME OVER!")
    else:
        print("O lago era muito fundo e não conseguiste atravessar. GAME OVER!")

else:
    print("Infelizmente, caíste numa armadilha. GAME OVER!")
