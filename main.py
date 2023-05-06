import time
import turtle
from turtle import Screen
from pista import Pista
from jogador import Jogador
from carro import CarroConfig
from pontuacao import Pontuacao

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor('beige')
tela.tracer(0)
tela.title("Turtle Crossing")
tela.listen()

pista = Pista()

pontuacao = Pontuacao()

jogador = Jogador()
carro_config = CarroConfig()
tela.onkey(jogador.mover_para_direita, "Right")
tela.onkey(jogador.mover_para_esquerda, "Left")

jogo_on = True
while jogo_on == True:
    time.sleep(0.1)
    carro_config.mover_carro()
    carro_config.aparecer_carro()
    if jogador.xcor() >= 180 or jogador.xcor() <= -180:
        turtle.write(f"Game over!", align="center", font=("Arial", 30, "bold"))
        pontuacao.atualizar_maior_pontuacao()
        jogo_on = False
    for carro in carro_config.carros:
        if abs(jogador.xcor() - carro.xcor()) < 1 and jogador.distance(carro) < 65:
            turtle.write(f"Game over!", align="center", font=("Arial", 30, "bold"))
            jogo_on = False
        if carro.ycor() < -230:
            pontuacao.aumentar_pontuacao()
            carro_config.carros.remove(carro)
            carro.hideturtle()

    if not jogo_on:
        time.sleep(2)
        jogador.resetar_posicao()
        for carro in carro_config.carros:
            carro.hideturtle()
        carro_config.__init__()
        pontuacao.pontuacao = 0
        pontuacao.clear()
        turtle.clear()
        pontuacao.atualizar_pontuacao()
        jogo_on = True

    tela.update()
tela.exitonclick()
