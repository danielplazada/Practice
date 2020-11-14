import turtle #import liblary turtle
mycolor="blue" #assign variable to "color"
loop_2=[1, 2, 3, 4, 5]
length=[30, 40, 50, 60, 70]#List of lengths forward for turtle
fred = turtle.Turtle() #assign string to turtle
fred.color("mycolor") #assign color using variable my color
for loop_1 in [1, 2, 3, 4]: #loop that is called side (loops 4 times)
    fred.forward(100) #move forward 100 (inside the loop)
    fred.right(135) #move right 135 degrees(inside the loop)
    fred.penup() # turtle stops drawing
    fred.pendown() #turtle starts drawing
    for side in loop_2: #loop that run inside loop_1
        fred.forward(length) #move forward based on number in the list (inside the loop)
        fred.right(135) #move right 135 degrees(inside the loop)


def square(sides, turn): #define a function that draws a sqaure
            #sides parameter for forward
            #turn  parameter for how much to turn
    t = turtle.Turtle() #create a new turtle fr the function
    t.color("cyan")
    for side in range(4): #loop to make a sqaure
        t.forward(sides)
        t.right(turn)

square(100, 90) # calling upon the function to run.
                #must imput both parameters

t = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number * number

for n in range(540):
    angle = square(n)
    t.right(angle + .5)
    t.forward(5)



def super_reptile():
    t = turtle.Turtle()
    t.width(10)
    t.color("green")
    return t

clark = super_reptile()
clark.forward(100)
clark.left(45)
clark.forward(100)
# up, up, and away!
