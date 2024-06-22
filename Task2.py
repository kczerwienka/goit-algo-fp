import turtle

def pyth_tree(t, order, size):
    if order > 0:
        t.forward(size) 
        t.left(45)
        pyth_tree(t, order - 1, size*0.8)
        t.right(2*45)
        pyth_tree(t, order - 1, size*0.8)
        t.left(45)  
        t.forward(-size) 
        

def draw_pyth_tree(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    
    t.left(90)

    pyth_tree(t, order, size)

    window.mainloop()

# Calling the function
draw_pyth_tree(2)