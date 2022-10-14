import turtle

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

def tree(branchLen, t):
    if branchLen > 1:
        t.color('yellow')
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)
        t.color('black')

def main():
    t = turtle.Turtle()
    turtle.delay(0)
    
    t.speed('fastest')
    t.ht()
    myWin = turtle.Screen()
    # myWin.setworldcoordinates(100,200,100,200)
    # myWin.yscale = .15
    # myWin.xscale = .15
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(20, t)
    myWin.exitonclick()

main()

# myWin.exitonclick()