from freegames import vector, square # importing both vector and square from freegames 
from random import randrange # allows random number generator to get a random ranged number
import turtle # used for writing text to graphics
from turtle import * # allows to create shapes 



# these are the three elements of the game (Need to figure out what aim does)
bait = vector(0, 0) # we start in position 0,0 for the beginning of the bait 
snakeBody = [vector(0, 0)] # snake will be starting in 10,0
score = vector(-200,200)   
direction = vector(0, -10) 

# changing the direction of snake function
def change(x, y):
    direction.x = x
    direction.y = y

# this is the boundary of the snake
def inside(head):
    return -320 < head.x < 320 and -280 < head.y < 280

# this is the moving the snake
def move():
    head = snakeBody[-1].copy()
    head.move(direction)

    # checks if snake is out of bounds or inside the snake to call it game over
    if not inside(head) or head in snakeBody:
        square(head.x, head.y, 9, 'red') # position x, position y, size of the block, and the color
        style = ('Arial', 20, 'italic')
        square(0, 0, 0, 'red')
        turtle.write("GAME OVER", font=style, align='center')
        update() # call the update method 
        return

    # what makes the snake show on the screen / alive
    snakeBody.append(head)

    # if snake eats bait, we have to randomize bait spawn
    if head == bait:
        bait.x = randrange(-25, 25) * 10
        bait.y = randrange(-25, 25) * 10
    else:
        # keeps the snake the same length and not becoming bigger by the distance
        snakeBody.pop(0)
      
     
    # clears the screen so then it doesn't show the new snake and not the old, 
    # which would make the snake still be large by distance, making the pop useless
    clear()

    for body in snakeBody:
        square(body.x, body.y, 9, 'green')

    square(bait.x, bait.y, 9, 'red')
    square(-300, 240, 0, 'black')
    style = ('Arial', 20, 'italic')
    turtle.write("Score:", font=style)
    square(-220, 240, 0, 'black')
    turtle.write(len(snakeBody), font=style)
    update()
    ontimer(move, 100)


# hides the cursor that usually makes the red bait or snake crash, will appear in those areas
# now disappear
hideturtle()

# avoids the program from 'drawing' every box, in a very slow fashion, by setting it to False
tracer(False)

# listens to keywords, to actually read what the human is pressing, and prompting accordingly.
listen()

# lambda is anonymous function with one return
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
# must be last statement in Tkinter loop for turtle graphics program
done()
