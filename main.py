import random
import pygame
from pygame.locals import *
import sys
pygame.init()

#2D Array Key:
#0 -> available space (white)
#1 -> obstacle (area that player cannot move) (blue)
#2 -> enemy (kills player) (red)
#3 -> player (green)
#4 -> lava/spikes
#5 -> exit
#6 -> grass
#Example: arr[2][3] = 3 (player location at x = 2 & y = 3)

global DEATH_COUNTER
DEATH_COUNTER = 0
BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WINNINGCOLOR = (6,80,150)

font = pygame.font.Font('freesansbold.ttf', 16) 
# create a text suface object, 
# on which text is drawn on it. 
text = font.render(f"DEATHS: {DEATH_COUNTER}", True, RED, WHITE) 
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
# set the center of the rectangular object. 
textRect.center = (300, 50) 
def updateDEATH():
    global DEATH_COUNTER
    text = font.render(f"DEATHS: {DEATH_COUNTER}", True, RED, WHITE)


def drawRectInArrBlank(color, arrX, arrY):
    startX = arrX * BLOCK_WIDTH
    startY = arrY * BLOCK_HEIGHT
    #(starting x point, starting y point, "move over x steps"", 'move /up y steps )
    pygame.draw.rect(screen, color, (startX, startY, BLOCK_WIDTH, BLOCK_HEIGHT), 1)

def drawRectInArr(color, arrX, arrY):
    startX = arrX * BLOCK_WIDTH
    startY = arrY * BLOCK_HEIGHT
    #(starting x point, starting y point, "move over x steps"", 'move /up y steps )
    pygame.draw.rect(screen, color, (startX, startY, BLOCK_WIDTH, BLOCK_HEIGHT))


FPS = 30
FramePerSec = pygame.time.Clock()
background_colour = (0,0,255) #RGB Value
(width, height) = (800, 400) 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall2020Hackathon')
screen.fill(background_colour)
#drawRectInArr(0,0)
#drawRectInArr(5,5)
#pygame.draw.rect(screen, (255,0,0), (0,0, 40,80))
screen.blit(screen,(0,0))
pygame.display.flip()
rows, cols = ((int)(height/20), (int)(width/20)) 
#arr = [[0 for i in range(cols)] for j in range(rows)]
#print(arr) 

dirt = pygame.image.load("Dirt.png")
dirtRect = dirt.get_rect()
grass = pygame.image.load("GrassMid.png")
grassRect = grass.get_rect()
spikes = pygame.image.load("spikes.png")


#hard coded map
arr = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 1, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 1], 
[1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 5], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 5], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def displayGameboard():
    for r in range(20):
        for c in range (40):
            #if(arr[r][c] == 0):
                #drawRectInArr(WHITE, c,r)
            if(arr[r][c] == 1):
                drawRectInArr(BLACK, c,r)
                screen.blit(dirt, (c*20,r*20))
            elif(arr[r][c] == 4):
                drawRectInArrBlank(RED, c,r)
                screen.blit(spikes, (c*20,r*20))
            elif(arr[r][c] == 5):
                drawRectInArr(WINNINGCOLOR, c,r)
            elif(arr[r][c] == 6):
                drawRectInArr(BLACK, c,r)
                screen.blit(grass, (c*20,r*20))

displayGameboard()

      
class Inhabitant:
    def __init__(self, name):
        self.name = name
        self.xcoord = None
        self.ycoord = None
        
class Player(Inhabitant):
    def __init__(self):
        super().__init__("Player")
        self.xcoord = 2
        self.ycoord = 9
        self.displayPlayer()
        arr[self.ycoord][self.xcoord] = 3

    def update(self, key_pressed):
        if (key_pressed == K_LEFT):
            self.moveLeft()
        if (key_pressed == K_RIGHT):
            self.moveRight()
        if (key_pressed == K_UP):
            self.jump()

    def moveRight(self):
        currentLocation = arr[self.ycoord][self.xcoord]
        attemptingLocation = arr[self.ycoord][self.xcoord + 1]
        if(attemptingLocation == 0):
            currentLocation = 0
            drawRectInArr(BLUE,self.xcoord, self.ycoord)
            attemptingLocation = 3
            self.xcoord = self.xcoord + 1
            self.displayPlayer()
        elif(attemptingLocation == 2):
            self.playerDeath()
    
    def moveLeft(self):
        currentLocation = arr[self.ycoord][self.xcoord]
        attemptingLocation = arr[self.ycoord][self.xcoord + 1]
        if(attemptingLocation == 0):
            currentLocation = 0
            drawRectInArr(BLUE,self.xcoord, self.ycoord)
            attemptingLocation = 3
            self.xcoord = self.xcoord - 1
            self.displayPlayer()
        elif(attemptingLocation == 2):
            self.playerDeath()
    
    def jump(self):
        currentLocation = arr[self.ycoord][self.xcoord]
        attemptingLocation = arr[self.ycoord - 3][self.xcoord]
        if(attemptingLocation == 0):
            currentLocation = 0
            drawRectInArr(BLUE,self.xcoord, self.ycoord)
            attemptingLocation = 3
            self.ycoord = self.ycoord - 3
            self.displayPlayer()
        elif(attemptingLocation == 2):
            self.playerDeath()
    
    def fallIfNeeded(self):
        currentLocation = arr[self.ycoord][self.xcoord]
        attemptingLocation = arr[self.ycoord + 1][self.xcoord]
        if(attemptingLocation == 0):
            currentLocation = 0
            drawRectInArr(BLUE,self.xcoord, self.ycoord)
            
            pygame.draw.rect(screen, GREEN, (self.xcoord * 20, (self.ycoord * 20) + 5, BLOCK_WIDTH, BLOCK_HEIGHT))
            FramePerSec.tick(FPS)
            pygame.draw.rect(screen, BLUE, (self.xcoord * 20, (self.ycoord * 20) + 5, BLOCK_WIDTH, BLOCK_HEIGHT))
            pygame.draw.rect(screen, GREEN, (self.xcoord * 20, (self.ycoord * 20) + 10, BLOCK_WIDTH, BLOCK_HEIGHT))
            FramePerSec.tick(FPS)
            pygame.draw.rect(screen, BLUE, (self.xcoord * 20, (self.ycoord * 20) + 10, BLOCK_WIDTH, BLOCK_HEIGHT))
            pygame.draw.rect(screen, GREEN, (self.xcoord * 20, (self.ycoord * 20) + 15, BLOCK_WIDTH, BLOCK_HEIGHT))
            FramePerSec.tick(FPS)
            pygame.draw.rect(screen, BLUE, (self.xcoord * 20, (self.ycoord * 20) + 15, BLOCK_WIDTH, BLOCK_HEIGHT))
            pygame.draw.rect(screen, GREEN, (self.xcoord * 20, (self.ycoord * 20) + 20, BLOCK_WIDTH, BLOCK_HEIGHT))
            FramePerSec.tick(FPS)
            
            attemptingLocation = 3
            self.ycoord = self.ycoord + 1
            self.displayPlayer()

            if(arr[self.ycoord + 1][self.xcoord] == 2):
                self.playerDeath()

        elif(attemptingLocation == 4):
            self.playerDeath()
        #print(self.xcoord, self.ycoord)
        
    def playerDeath(self):
        global DEATH_COUNTER
        DEATH_COUNTER = DEATH_COUNTER + 1
        pygame.draw.rect(screen, BLUE, (self.xcoord * 20, self.ycoord * 20, BLOCK_WIDTH, BLOCK_HEIGHT))
        self.xcoord = 2
        self.ycoord = 9
        self.displayPlayer()
        updateDEATH()
    
    def displayPlayer(self):
        drawRectInArr(GREEN, self.xcoord, self.ycoord)


        
class Poison_Shroom(Inhabitant):
    def __init__(self, max_hp):
        super().__init__("Poison Shroom")
        self.xcoord = 0
        self.ycoord = 0
        self.hp = random.randint(10, max_hp)
                
def main():
    running = True
    keys = pygame.key.get_pressed()
    player = Player()
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_LEFT:
                    player.update(event.key)
                elif event.key == K_RIGHT:
                    player.update(event.key)
                elif event.key == K_UP:
                    player.update(event.key)
            elif event.type == QUIT:
                running = False
            else:
                pass
        if((FramePerSec.tick(FPS) % 2) == 0):
            player.fallIfNeeded()
        screen.blit(text, textRect)
        pygame.display.update()
        FramePerSec.tick(FPS)
    
main()
