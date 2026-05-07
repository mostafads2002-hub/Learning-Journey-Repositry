from turtle import Turtle,Screen
window=Screen()
window.bgcolor("white")
window.setup(700,700)
sam=Turtle()
sam.speed("slow")
#دالة المربع
def spuare():
    sam.shape("turtle")
    sam.color("red")
    sam.pencolor("red")
    sam.pensize(10)
    for _ in range(4):
        sam.forward(100)
        sam.left(90)
#دالة الدائرة
def circle():
    sam.shape("square")
    sam.color("black")
    sam.pencolor("black")
    sam.pensize(5)
    sam.circle(100)
    
#دالة المثلث
def triangle():
    sam.shape("triangle")
    sam.color("purple")
    sam.pencolor("purple")
    sam.pensize(3)
    for _ in range(3):
        sam.forward(150)
        sam.left(120)


ask_inp=window.textinput("لحظة من فضلك","ماذا تريد ان ترسم؟ دائرة,مربع,مثلث")
while ask_inp !="exit":
    if ask_inp=="spuare" or ask_inp== "مربع":
        spuare()
    elif ask_inp=="circle" or ask_inp== "دائرة":
        circle()
    elif ask_inp=="triangle" or ask_inp== "مثلث":
        triangle()
    
        
    ask_inp=window.textinput("لحظة من فضلك","ماذا تريد ان ترسم؟ دائرة,مربع,مثلث")
sam.clear()
sam.hideturtle()
sam.pencolor("blue")


sam.write(f"Press any key to exit\nاضغط في اي  مكان للخروج",font=("arual",40,"normal"),align=("center"))


window.exitonclick()

