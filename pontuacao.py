from turtle import Turtle

class Pontuacao(Turtle):
    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.maior_pontuacao = 0
        self.hideturtle()
        self.color("black")
        self.atualizar_pontuacao()

    def atualizar_pontuacao(self):
        self.penup()
        self.goto(-220, 150)
        self.write(f"Score: {self.pontuacao}", align="center", font=("Arial", 20, "bold"))
        self.goto(-220, 180)
        self.write(f"Record: {self.maior_pontuacao}", align="center", font=("Arial", 20, "bold"))

    def aumentar_pontuacao(self):
        self.pontuacao += 1
        self.clear()
        self.atualizar_maior_pontuacao()
        self.atualizar_pontuacao()

    def atualizar_maior_pontuacao(self):
        if self.pontuacao >= self.maior_pontuacao:
            self.maior_pontuacao = self.pontuacao
            self.atualizar_pontuacao()
