<h1> TestBasedGame <h1>


escolha = input("Deseja jogar este jogo? (Sim/Não): ")
if escolha == "Sim":
    print ("Bem vindo à floresta!")
else:
  print("OK, o jogo não foi iniciado")
  exit ()
escolha = input("Há tua frente vais encontrar 2 portas a da esquerda e a da direita, qual vais escolher? (Esquerda/Direita): ")
if escolha == "Esquerda":
  print("Encontras-te 3 cobras!, Desejas Atacar ou Fugir para a Direita?")
  escolha = input("(Atacar/Fugir): ")
  if escolha == "Atacar":
    print("Acabas-te de morrer\n |GAME OVER|")
  else:
    escolha == "Fugir"
    print("Conseguis-te fugir com sucesso para a porta da Direita!")
else:
escolha == "Direita":
  print("Á tua frente tens mais 3 portas a Porta Vermelha a Azul e a Preta, qual vais escolher? (Vermelha/Azul/Preta): ")
  escolha == "Vermelha":
    print("á tua frente tens uma espada, pega nela, mas se vires bem não consegues passar, tenta outra porta")
  escolha == "Preta":
    print("Tens um escudo á tua frente, mas continuas sem conseguir passar, tenta a ultima porta (Azul) ")
  escolha == "Azul":
    print("Tens um monstro á tua frente, como conseguiste o escudo e a espada tenta atacar o tigre: ")
  
