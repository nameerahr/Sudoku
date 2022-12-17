import pygame

pygame.init()
pygame.font.init()

windowHeight = 750
windowWidth = 600
gameBoardHeight = 600
gameBoardWidth = 600

blockSize = windowWidth//9 

WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (33, 84, 58)
RED = (255,0,0)

largeFont = pygame.font.SysFont("calibri", 40)
normalFont = pygame.font.SysFont("calibri", 20)
boldFont = pygame.font.SysFont('calibri', 20, bold = True)
optionsFont = pygame.font.SysFont('calibri', 25, bold = True)
pencilFont = pygame.font.SysFont('calibri', 10)

def main():

    global screen
    global pos
    global board , pencilBoard

    # Window
    screen = pygame.display.set_mode((windowWidth, windowHeight))

    # Title and Icon
    pygame.display.set_caption("SUDOKU")
    windowIcon = pygame.image.load('windowIcon.png')
    pygame.display.set_icon(windowIcon)

    # Default Board
    board =[
        [1, 0, 3, 0, 0, 8, 7, 2, 0],
        [8, 6, 7, 0, 4, 0, 0, 1, 9],
        [0, 0, 0, 1, 9, 0, 0, 8, 0],
        [3, 5, 8, 0, 0, 0, 4, 6, 0],
        [0, 0, 0, 7, 3, 4, 0, 0, 0],
        [0, 4, 0, 6, 0, 0, 0, 3, 0],
        [4, 0, 5, 0, 0, 6, 0, 0, 8],
        [2, 7, 0, 0, 5, 0, 9, 0, 3],
        [9, 0, 1, 4, 7, 0, 0, 0, 0]
    ]

    # Penciled Board
    pencilBoard =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    select = False
    marker = None
    pencil = None
    valid = None
    val = 0

    while True:
        screen.fill(WHITE)
        drawBoard()
        drawPencilBoard()
        gameInstructions()
        selectOptions()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if 190 <= position[0] <= 245 and 610 <= position[1] <= 650:
                    marker = False
                    pencil = True
                    val = None
                    valid = None
                elif 325 <= position[0] <= 410 and 610 <= position[1] <= 650:
                    pencil = False
                    marker = True
                    val = None
                    valid = None 
                elif 0 <= position[0] <= 600 and 0 <= position[1] <= 600:
                    pos = pygame.mouse.get_pos()
                    select = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    board =[
                            [1, 0, 3, 0, 0, 8, 7, 2, 0],
                            [8, 6, 7, 0, 4, 0, 0, 1, 9],
                            [0, 0, 0, 1, 9, 0, 0, 8, 0],
                            [3, 5, 8, 0, 0, 0, 4, 6, 0],
                            [0, 0, 0, 7, 3, 4, 0, 0, 0],
                            [0, 4, 0, 6, 0, 0, 0, 3, 0],
                            [4, 0, 5, 0, 0, 6, 0, 0, 8],
                            [2, 7, 0, 0, 5, 0, 9, 0, 3],
                            [9, 0, 1, 4, 7, 0, 0, 0, 0]
                        ]
                    pencilBoard =[
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        ]
                if event.key == pygame.K_BACKSPACE:
                    valid = False
                    val = 0
                if event.key == pygame.K_1:
                    valid = verifyEnteredValue(1)
                    val = 1
                if event.key == pygame.K_2:
                    valid = verifyEnteredValue(2)
                    val = 2
                if event.key == pygame.K_3:
                    valid = verifyEnteredValue(3)
                    val = 3
                if event.key == pygame.K_4:
                    valid = verifyEnteredValue(4)
                    val = 4
                if event.key == pygame.K_5:
                    valid = verifyEnteredValue(5)
                    val = 5
                if event.key == pygame.K_6:
                    valid = verifyEnteredValue(6)
                    val = 6
                if event.key == pygame.K_7:
                    valid = verifyEnteredValue(7)
                    val = 7
                if event.key == pygame.K_8:
                    valid = verifyEnteredValue(8)
                    val = 8
                if event.key == pygame.K_9:
                    valid = verifyEnteredValue(9)
                    val = 9 
        if pencil:
            pencilOutline() 
            if (valid != None):
                enterPencilValue(val)
            val = None
            valid = None 
        elif marker:
            markerOutline()
            if valid == True:
                enterValue(val)     
                valid = None
            elif valid == False:
                if val == 0:
                    populatedGridMessage()
                else:
                    invalidEntry(val)
     
        if select:
            selectGrid(pos)
        if gameComplete():
            completeMessage()

        pygame.display.update()

# Draw the main board on the screen and populate it with the sodoku board
def drawBoard():
    # Draw containers and print numbers
    for x in range(9):
        for y in range(9):
            if board[x][y] != 0:

                numberContainer = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, GREEN, numberContainer)

                boardEntry = largeFont.render(str(board[x][y]), 1, BLACK)
                screen.blit(boardEntry, (x * blockSize + 23, y * blockSize + 13))

    # Draw horizontal and vertical borders	
    for x in range(10):
        if x % 3 == 0 :
            borderThickness = 7
        else:
            borderThickness = 2

        pygame.draw.line(screen, BLACK, (0, x * blockSize), (gameBoardWidth - 3, x * blockSize), borderThickness) # Horizontal borders
        pygame.draw.line(screen, BLACK, (x * blockSize, 0), (x * blockSize, gameBoardHeight - 3), borderThickness)	# Vertical borders

# Draw the pencil board on the screen
def drawPencilBoard():
    for x in range(9):
        for y in range(9):
            if pencilBoard[x][y] != 0:

				# Fill board with pencil numbers
                pencilEntry = pencilFont.render(str(pencilBoard[x][y]), 1, BLACK)
                screen.blit(pencilEntry, (x * blockSize + 52, y * blockSize + 4))

# Outline the selected box
def selectGrid(pos):
    x, y = pos

    leftBorder = (x // blockSize) * blockSize
    topBorder = (y // blockSize) * blockSize

    outline = pygame.Rect(leftBorder, topBorder, blockSize + 2, blockSize + 2)
    pygame.draw.rect(screen, RED, outline, 5)

# Make sure that the entered value does not exist in the same horizontal, vertical or 3x3 grid as the selected box
def verifyEnteredValue(value):
    x = pos[0] // blockSize
    y = pos[1] // blockSize

    if value == 0:
        return False

    if board[x][y] != 0:
        return False

    # board[i][j]   where i = x, j = y
    valid = True 

    # Check horizontal 
    for i in range(9):
        if board[i][y] == value:
            valid = False

    # Check vertical 
    for j in range(9):
        if board[x][j] == value:
            valid = False

    # Check 3x3 grid]
    startingX = (x // 3) * 3
    startingY = (y // 3) * 3

    for i in range(startingX, startingX + 3):
        for j in range(startingY, startingY + 3):
            if board[i][j] == value:
                valid = False
    
    return valid

# Add the value on to the board
def enterValue(value):
    x = pos[0] // blockSize
    y = pos[1] // blockSize

    board[x][y] = value

# Add the value on the screen in pencil form
def enterPencilValue(value):
    if value != None:
        x = pos[0] // blockSize
        y = pos[1] // blockSize
        pencilBoard[x][y] = value

# Verify the board has been completed
def gameComplete():
    complete = True
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return complete

# Display select options
def selectOptions():
    options = optionsFont.render("Pencil             Marker", 1, GREEN)

    optionsRect = options.get_rect(center=(windowWidth/2, 630))

    screen.blit(options, optionsRect)	

# Outline the pencil option to show selection
def pencilOutline():
    outline = pygame.Rect(165, 612, 95, 36)
    pygame.draw.rect(screen, BLACK, outline, 5)

# Outline the marker option to show selection
def markerOutline():
    outline = pygame.Rect(330, 612, 105, 36)
    pygame.draw.rect(screen, BLACK, outline, 5)

# Display the game's instructions
def gameInstructions():
    instructions = normalFont.render("Select a pen type. Click the board to enter your value.", 1, GREEN)
    instructions2 = normalFont.render("Press X to start over.", 1, GREEN)

    instructionsRect = instructions.get_rect(center=(windowWidth/2, 665))
    instructions2Rect = instructions2.get_rect(center=(windowWidth/2, 685))

    screen.blit(instructions, instructionsRect)	
    screen.blit(instructions2, instructions2Rect)

# Display a message for an invalid entered value
def invalidEntry(Value):
    invalidMessage = boldFont.render(f"{Value} is invalid at this position. Please try again.", 1, BLACK)

    invalidMessageRect = invalidMessage.get_rect(center=(windowWidth/2, 710))
    screen.blit(invalidMessage, invalidMessageRect)	

# Display a message when player tries to remove a populated grid
def populatedGridMessage():
    populatedMessage = boldFont.render("Cannot delete a populated grid. Reset the game if needed.", 1, BLACK)

    populatedMessageRect = populatedMessage.get_rect(center=(windowWidth/2, 710))
    screen.blit(populatedMessage, populatedMessageRect)	

# Display a message when the game completes
def completeMessage():
    completeMessage = boldFont.render("Congrats! You have completed the board.", 1, RED)

    completeMessageRect = completeMessage.get_rect(center=(windowWidth/2, 705))
    screen.blit(completeMessage, completeMessageRect)	

main()