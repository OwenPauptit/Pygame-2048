import pygame,random, sys

pygame.init()

screenHeight = 400
screenWidth = 400
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("2048")



def newTile(board):
    if random.randint(1,10) == 10:
        value = 4
    else:
        value = 2

    pos = [-1,-1]    
    
    while pos == [-1,-1]:
        temp = [random.randint(0,3),random.randint(0,3)]
        if board[temp[0]][temp[1]] == 0:
            pos = temp          

    return pos[0],pos[1],value

def moveUP(board):
    for x in range(0,4):
        for i in range(0,4):
            if board[i][0] == 0:
                board[i][0] = board[i][1]
                board[i][1] = 0
            if board[i][1] == 0:
                board[i][1] = board[i][2]
                board[i][2] = 0
            if board[i][2] == 0:
                board[i][2] = board[i][3]
                board[i][3] = 0
                
            if board[i][0] == board[i][1]:
                board[i][0] = board[i][1]*2
                board[i][1] = 0
            if board[i][1] == board[i][2]:
                board[i][1] = board[i][2]*2
                board[i][2] = 0
            if board[i][2] == board[i][3]:
                board[i][2] = board[i][3]*2
                board[i][3] = 0
    return board
    
def moveDown(board):
    for x in range(0,4):
        for i in range(0,4):
            if board[i][3] == 0:
                board[i][3] = board[i][2]
                board[i][2] = 0
            if board[i][2] == 0:
                board[i][2] = board[i][1]
                board[i][1] = 0
            if board[i][1] == 0:
                board[i][1] = board[i][0]
                board[i][0] = 0

            if board[i][3] == board[i][2]:
                board[i][3] = board[i][2]*2
                board[i][2] = 0
            if board[i][2] == board[i][1]:
                board[i][2] = board[i][1]*2
                board[i][1] = 0
            if board[i][1] == board[i][0]:
                board[i][1] = board[i][0]*2
                board[i][0] = 0
    return board

def moveLeft(board):
    for x in range(0,4):
        for i in range(0,4):
            if board[0][i] == 0:
                board[0][i] = board[1][i]
                board[1][i] = 0
            if board[1][i] == 0:
                board[1][i] = board[2][i]
                board[2][i] = 0
            if board[2][i] == 0:
                board[2][i] = board[3][i]
                board[3][i] = 0

            if board[0][i] == board[1][i]:
                board[0][i] = board[1][i]*2
                board[1][i] = 0
            if board[1][i] == board[2][i]:
                board[1][i] = board[2][i]*2
                board[2][i] = 0
            if board[2][i] == board[3][i]:
                board[2][i] = board[3][i]*2
                board[3][i] = 0
    return board
    
def moveRight(board):
    for x in range(0,4):
        for i in range(0,4):
            if board[3][i] == 0:
                board[3][i] = board[2][i]
                board[2][i] = 0
            if board[2][i] == 0:
                board[2][i] = board[1][i]
                board[1][i] = 0
            if board[1][i] == 0:
                board[1][i] = board[0][i]
                board[0][i] = 0

            if board[3][i] == board[2][i]:
                board[3][i] = board[2][i]*2
                board[2][i] = 0
            if board[2][i] == board[1][i]:
                board[2][i] = board[1][i]*2
                board[1][i] = 0
            if board[1][i] == board[0][i]:
                board[1][i] = board[0][i]*2
                board[0][i] = 0
    return board
   

def showTiles(board):
    for i in range(0,4):
        for k in range(0,4):
            
            if board[i][k] != 0:
                Rect1 = (100*i,100*k,100,100)
                pygame.draw.rect(screen,(178, 121, 67),Rect1)
                Rect2 = (100*i+5,100*k+5,90,90)
                pygame.draw.rect(screen,(219,142,70),Rect2)
                font = pygame.font.Font("C:/Users/owenp/OneDrive/Good Python stuff/2048/8-BIT WONDER.ttf",18)
                label = font.render(str(board[i][k]),1,(255,255,255))
                labelpos = label.get_rect()
                labelpos.center = (i*100+50,k*100+50)
                screen.blit(label,labelpos)
        



def clearScreen():
    screen.fill((196, 188, 162))

def gameover():
    font = pygame.font.Font("C:/Users/owenp/OneDrive/Good Python stuff/2048/8-BIT WONDER.ttf",45)
    label = font.render("GAMEOVER",1,(0,0,0))
    screen.blit(label,(10,175))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                game()

def isOver(board):
    for i in range(0,4):
        for k in range(0,4):
            if board[i][k] == 0:
                return False
    return True

def game():

    board = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    
    while True:

        clearScreen()
        showTiles(board)
        print(board)
        
        if isOver(board) == True:
            pygame.display.update()
            gameover()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:

                    board = moveUP(board)
                    x,y,value = newTile(board)
                    board[x][y] = value
                    
                elif event.key == pygame.K_DOWN:

                    board = moveDown(board)
                    x,y,value = newTile(board)
                    board[x][y] = value

                elif event.key == pygame.K_LEFT:

                    board = moveLeft(board)
                    x,y,value = newTile(board)
                    board[x][y] = value

                elif event.key == pygame.K_RIGHT:

                    board = moveRight(board)
                    x,y,value = newTile(board)
                    board[x][y] = value
                    
                    
                    
        

        
        pygame.display.update()
        pygame.time.delay(10)

game()        
