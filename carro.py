from turtle import Turtle
import random

class CarroConfig:
    def __init__(self):
        self.carros = []
        self.local = [(0, 100), (60, 100), (120, 100), (-60, 100), (-120, 100)]
        self.criar_carro()

    def criar_carro(self):
        novo_carro = Turtle("square")
        cores = ["red", "orange", "yellow", "green", "blue", "purple"]
        novo_carro.shape("square")
        novo_carro.penup()
        novo_carro.shapesize(2.2, 3.2)
        novo_carro.setheading(270)
        novo_carro.goto(random.choice(self.local))
        novo_carro.color(random.choice(cores))
        self.carros.append(novo_carro)

    def aparecer_carro(self):
        if self.carros[-1].ycor() <= 20:
            self.criar_carro()

    def mover_carro(self):
        for carro in self.carros:
            carro.forward(30)