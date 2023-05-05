from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.hideturtle()
        self.penup()
        self.goto(-220, 150)
        self.color("black")
        self.atualizar_pontuacao()

    def atualizar_pontuacao(self):
        self.write(f"Score: {self.pontuacao}", align="center", font=("Arial", 20, "bold"))

    def aumentar_pontuacao(self):
        self.pontuacao += 1
        self.clear()
        self.atualizar_pontuacao()