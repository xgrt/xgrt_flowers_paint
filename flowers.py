import turtle
import random as ran


def flower(s):
    turtle.hideturtle()
    turtle.speed(9)
    turtle.pensize(3)
    for i in range(s):
        r = ran.random()
        g = ran.random()
        b = ran.random()
        turtle.color(r, g, b)
        turtle.penup()  # 笔抬起
        turtle.goto(ran.randint(-500, 500), ran.randint(-250, 250))  # 笔移动
        turtle.pendown()  # 笔落下
        petal_num = ran.randint(10, 20)  # 花瓣数
        flower_size = ran.randint(10, 35)  # 花瓣大小
        for _ in range(petal_num):
            turtle.forward(flower_size)  # 向当前方向移动snowflake_size距离
            turtle.right(30)
            turtle.forward(flower_size / 2)
            turtle.lt(60)
            turtle.backward(flower_size / 2)
            turtle.right(30)
            turtle.backward(flower_size)  # 向当前方向的反方向移动snowflake_size距离
            turtle.right(360 / petal_num)  # 顺时针移动的度数
        turtle.right(90)
        for _ in range(petal_num):
            turtle.forward(flower_size / 2)
            turtle.right(360 / petal_num)
        turtle.left(90)
    turtle.done()
