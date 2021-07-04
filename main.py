#presentation and age begin  here
print("Olá Viajante")
age =int(input("Qual é a tua idade? "))
name = input ("Como te chamas? ")
print(f"Olá {name} ,tu tens {age} anos! ")

if age >= 18:
  print("Bem vindo ao jogo! ")
  wants_to_play = input("Queres embarcar nesta aventura ? ")
  if wants_to_play.lower() == "sim":
    print("Vamos lá embora ")

#game begins here

    caminhado_or_cavalo = input("Vamos a cavalo ou caminhado ? ")
    if caminhado_or_cavalo.lower() == "cavalo":
      ans = input(
        "Vês 2 casas ao longe , qual vais entrar ? Direita ou Esquerda ? ,escreve D ou E .")

      if ans == "D":
        print("Chegaste a casa , fim do jogo !")
      elif ans == "E":
        print("Estás na casa do vizinho")
      else:
        print("Continuaste na estrada ,a tua aventura termina aqui . F ")

    else:
      print("Vieram 3 gajos e apanharam-te, a tua aventura termina aqui . F ")


#non player input 
  else:
    print("Percebo, adeus.")

else: 
  print ("Não podes entrar nesta aventura,tenta mais tarde")





