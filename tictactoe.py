import turtle

screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.bgcolor("white")
# draw a white grid and test
#define the array to store the game state
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

current_player = "X"
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

#define writer
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
#goes above the grid to write the current player's turn

def declare_winner(player):
    writer.clear()
    writer.goto(0, 200)
    writer.write("Player " + player + " wins!", align="center", font=("Arial", 24, "bold"))  # disable further clicks
    writer.goto(0, -200)
    writer.write("Click anywhere to play again", align="center", font=("Arial", 14, "normal"))
      # reset the game when the user clicks after a win or draw
    screen.onclick(reset_game)

def draw_turn():
    writer.clear()
    writer.goto(0, 200)
    writer.write("Player " + current_player + "'s turn", align="center", font=("Arial", 16, "bold"))
# draw the grid
def drawLines():
    # vertical lines
    pen.penup()
    pen.goto(-50, 150)
    pen.pendown()
    pen.goto(-50, -150)

    pen.penup()
    pen.goto(50, 150)
    pen.pendown()
    pen.goto(50, -150)

    # horizontal lines
    pen.penup()
    pen.goto(-150, 50)
    pen.pendown()
    pen.goto(150, 50)

    pen.penup()
    pen.goto(-150, -50)
    pen.pendown()
    pen.goto(150, -50)

drawLines()
draw_turn()

#draw the X and O

#center of each square
def get_coords(row, col):
    x = -100 + (col * 100)
    y = 100 - (row * 100)
    return x, y

#draw the X and O
def draw_x(x, y):
    pen.penup()
    pen.goto(x - 30, y + 30)
    pen.pendown()
    pen.goto(x + 30, y - 30)
    pen.penup()
    pen.goto(x + 30, y + 30)
    pen.pendown()
    pen.goto(x - 30, y - 30)
def draw_o(x, y):
    pen.penup()
    pen.goto(x, y - 30)
    pen.pendown()
    pen.circle(30)


def get_square(x, y):
    if x < -50:
        col = 0
    elif x < 50:
        col = 1
    else:
        col = 2

    if y > 50:
        row = 0
    elif y > -50:
        row = 1
    else:
        row = 2

    return row, col
#now we will draw the X and O
def on_click(x, y):
    global current_player
    row, col = get_square(x, y)
    if board[row][col] == "":
        board[row][col] = current_player
        for r in board:
            print(r)
        x, y = get_coords(row, col)
        if current_player == "X":
            draw_x(x, y)
        else:
            draw_o(x, y)
        if current_player == "X":
            current_player = "O"
            
        else:
            current_player = "X"
        draw_turn()
        check_winner()

def check_winner():
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            declare_winner(row[0])
            return

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            declare_winner(board[0][col])
            return

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        declare_winner(board[0][0])
        return

    if board[0][2] == board[1][1] == board[2][0] != "":
        declare_winner(board[0][2])
        
        return
    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        declare_winner("Draw - nobody")    
screen.onclick(on_click)
#reset the game when the user clicks after a win or draw
def reset_game(x, y):
    global board, current_player
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]
    current_player = "X"
    pen.clear()
    drawLines()
    draw_turn()
    screen.onclick(on_click)


turtle.done()
