from turtle import Turtle,Screen
window=Screen()
window.setup(width=1000,height=1000)
window.bgcolor("black")
sam=Turtle()
sam.shape("turtle")
sam.color("white")
sam.pensize(3)
sam.speed("slow")

def draw_circles():
    sam.penup()
    sam.goto(-300,-200)
    sam.pendown()
    for _ in range(10):
        sam.circle(50)
        sam.left(360/10)
    sam.penup()
     
def draw_squares():
    sam.goto(0,0)
    sam.pendown()
    for _ in range(10):
        for _ in range(4):
            sam.forward(80)
            sam.left(90)
        sam.left(360/10)
    sam.penup()

def draw_triangles():
    sam.penup()
    sam.goto(300,200)
    sam.pendown()
    for _ in range(10):
        for _ in range(3):
            sam.forward(100)
            sam.left(120)
        sam.left(360/10)
    sam.penup()
def asks():
    user_name=window.textinput("welcome...!","Enter your name")
    ask=window.textinput(f"welcome {user_name}","What shape do you want to see?\n1-draw circles\n2-draw squares\n3-draw_triangles")
    if ask=="1"or ask.lower()=="draw circles":
        draw_circles()
    elif ask=="2" or ask.lower()=="draw squares":
        draw_squares()
    elif ask=="3" or ask.lower()=="draw triangles":
        draw_triangles()

asks()

ask2=window.textinput("","Do you wabt to try again?:(yes.,no)")
    
while ask2.lower()=="yes":
    sam.clear()
    asks()
    ask2=window.textinput("","Do you wabt to try again?:(yes.,no)")
end=window.textinput("bay....!","thank you for your experience Press Enter to exit......")
window.exitonclick()