<h1> TestBasedGame <h1>


escolha = input("Dejeta jogar este jogo? (Sim/Não): ")
if escolha == "Sim":
  print ("𝓑𝓮𝓶-𝓿𝓲𝓷𝓭𝓸 𝓪̀ 𝓕𝓵𝓸𝓻𝓮𝓼𝓽𝓪!\n Boa Sorte no jogo!!")
else:
  print("OK, o jogo não foi iniciado")

escolha = input("Há tua frente vais encontrar 2 portas a da esquerda e a da direita, qual vais escolher? (Esquerda/Direita): ")
if escolha == "Esquerda":
  print("Encontras-te 3 cobras!, Desejas Atacar ou Fugir para a Direita?")
  escolha = input("(Atacar/Fugir): ")
  if escolha == "Atacar":
    print("Acabas-te de morrer, GAME OVER")
  else:
    print("Encontras-te um troll, desejas atacar ou fugir?")
    escolha = input("(Atacar/Fugir): ")
    if escolha == "Atacar":
      print("Acabas-te de morrer, GAME OVER")
  else:
