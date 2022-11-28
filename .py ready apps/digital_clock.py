import time
from datetime import datetime
from turtle import Turtle
t = Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)
t.penup()
t.fillcolor('grey25')
x = 0
conta = 0


def maximize_t(numero_liga, x):

    # Desenha os traços ou "troços" do número digital, são 7. Na sequencia circular:
    # esquerdo alto, esquerdo baixo, baixo, direto baixo, direito alto, alto e meio.

    # troco esquerdo alto
    def troco_esqal():
        t.goto(-150+x, 0)
        t.begin_fill()
        t.pendown()
        t.left(45)
        t.forward(15)
        t.left(45)
        t.forward(30)
        t.left(45)
        t.forward(15)
        t.left(135)
        t.forward(52)
        t.left(90)
        t.end_fill()
        t.penup()

    # troco esquerdo baixo
    def troco_esqba():
        t.goto(-150+x, -55)
        t.begin_fill()
        t.pendown()
        t.left(45)
        t.forward(15)
        t.left(45)
        t.forward(30)
        t.left(45)
        t.forward(15)
        t.left(135)
        t.forward(52)
        t.left(90)
        t.end_fill()
        t.penup()

    # troco baixo
    def troco_baixo():
        t.goto(-148+x, -60)
        t.begin_fill()
        t.pendown()
        t.forward(52)
        t.left(135)
        t.forward(15)
        t.left(45)
        t.forward(30)
        t.left(45)
        t.forward(15)
        t.end_fill()
        t.left(135)
        t.penup()

    # troco direito baixo
    def troco_dirba():
        t.goto(-92+x, -55)
        t.begin_fill()
        t.pendown()
        t.left(90)
        t.forward(52)
        t.left(135)
        t.forward(15)
        t.left(45)
        t.forward(32)
        t.left(45)
        t.forward(15)
        t.left(45)
        t.end_fill()
        t.penup()

    # troco direito alto
    def troco_diral():
        t.goto(-92+x, 0)
        t.begin_fill()
        t.pendown()
        t.left(90)
        t.forward(52)
        t.left(135)
        t.forward(15)
        t.left(45)
        t.forward(32)
        t.left(45)
        t.forward(15)
        t.left(45)
        t.end_fill()
        t.penup()

    # troco alto
    def troco_alto():
        t.goto(-96+x, 57)
        t.begin_fill()
        t.pendown()
        t.left(180)
        t.forward(52)
        t.left(135)
        t.forward(15)
        t.left(45)
        t.forward(32)
        t.left(45)
        t.forward(15)
        t.right(45)
        t.end_fill()
        t.penup()

    # troco meio
    def troco_meio():
        t.goto(-98+x, -2)
        t.begin_fill()
        t.pendown()
        t.left(135)
        t.forward(10)
        t.left(45)
        t.forward(33)
        t.left(45)
        t.forward(10)
        t.left(90)
        t.forward(10)
        t.left(45)
        t.forward(33)
        t.left(45)
        t.forward(10)
        t.right(45)
        t.end_fill()
        t.penup()

 # De acordo com o conteudo da string passada, a função que desenha o troço
 # da posição x é chamada. Ela "liga" o troço para formar o número.

    if numero_liga == '1':
        troco_dirba()
        troco_diral()

    elif numero_liga == '2':
        troco_esqba()
        troco_baixo()
        troco_diral()
        troco_alto()
        troco_meio()

    elif numero_liga == '3':
        troco_alto()
        troco_diral()
        troco_meio()
        troco_dirba()
        troco_baixo()

    elif numero_liga == '4':
        troco_diral()
        troco_esqal()
        troco_meio()
        troco_dirba()

    elif numero_liga == '5':
        troco_alto()
        troco_esqal()
        troco_meio()
        troco_dirba()
        troco_baixo()

    elif numero_liga == '6':
        troco_alto()
        troco_esqal()
        troco_esqba()
        troco_baixo()
        troco_dirba()
        troco_meio()

    elif numero_liga == '7':
        troco_alto()
        troco_diral()
        troco_dirba()

    elif numero_liga == '8':
        troco_alto()
        troco_esqal()
        troco_meio()
        troco_esqba()
        troco_baixo()
        troco_dirba()
        troco_diral()

    elif numero_liga == '9':
        troco_alto()
        troco_esqal()
        troco_diral()
        troco_meio()
        troco_dirba()
        troco_baixo()

    elif numero_liga == '0':
        troco_alto()
        troco_esqal()
        troco_esqba()
        troco_baixo()
        troco_dirba()
        troco_diral()


hora_pass = datetime.now().strftime('%H:%M')
maximize_t(hora_pass[0], 0)
maximize_t(hora_pass[1], 70)
maximize_t(hora_pass[3], 160)
maximize_t(hora_pass[4], 230)

while True:
    conta += 1
    if hora_pass != datetime.now().strftime('%H:%M'):
        hora_pass = datetime.now().strftime('%H:%M')
        conta = 2
        t.clear()
        maximize_t(hora_pass[0], 0)
        maximize_t(hora_pass[1], 70)
        maximize_t(hora_pass[3], 160)
        maximize_t(hora_pass[4], 230)

    if conta % 2 == 0:  # Faz teste se conta é par, imprime os dois pontos do segundo
        t.goto(-8, 15)
        t.dot(10)
        t.goto(-8, -15)
        t.dot(10)
    else:       # apaga os dois pontos do segundo
        t.goto(-8, 15)
        t.dot(10, 'white')
        t.goto(-8, -15)
        t.dot(10, 'white')

    time.sleep(1)
