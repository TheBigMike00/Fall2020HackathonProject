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
#Example: arr[2][3] = 3 (player location at x = 2 & y = 3)

BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


def drawRectInArr(color, arrX, arrY):
    startX = arrX * BLOCK_WIDTH
    startY = arrY * BLOCK_HEIGHT
    #(starting x point, starting y point, "move over x steps"", 'move /up y steps )
    pygame.draw.rect(screen, color, (startX, startY, BLOCK_WIDTH, BLOCK_HEIGHT))

FPS = 200
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
arr = [[0 for i in range(cols)] for j in range(rows)] 


      
class Inhabitant:
    def __init__(self, name):
        self.name = name
        self.xcoord = None
        self.ycoord = None
        
class Player(Inhabitant):

    def __init__(self):
        super().__init__("Player")
        self.xcoord = 0
        self.ycoord = rows-1
        self.displayPlayer()
        arr[0][rows-1] = 3
        isInAir = True
        isAlive = True

    def update(self, key_pressed):
        if (key_pressed == K_LEFT):
            self.moveLeft()
        if (key_pressed == K_RIGHT):
            self.moveRight()

    def moveRight(self):
        currentLocation = arr[self.xcoord][self.ycoord]
        attemptingLocation = arr[self.xcoord + 1][self.ycoord]
        if(attemptingLocation == 0):
            currentLocation = 0
            drawRectInArr(BLUE,self.xcoord, self.ycoord)
            attemptingLocation = 3
            self.xcoord = self.xcoord + 1
            self.displayPlayer()
        elif(attemptingLocation == 2):
            self.playerDeath()
    
    def moveLeft(self):
        currentLocation = arr[self.xcoord][self.ycoord]
        attemptingLocation = arr[self.xcoord - 1][self.ycoord]
        if(attemptingLocation == 0):
            currentLocation = 0
            drawRectInArr(BLUE,self.xcoord, self.ycoord)
            attemptingLocation = 3
            self.xcoord = self.xcoord - 1
            self.displayPlayer()
        elif(attemptingLocation == 2):
            self.playerDeath()
    '''
    def jump(self):
        currentLocation = arr[self.xcoord][self.ycoord]
        attemptingLocation = arr[self.xcoord][self.ycoord - 3]
        if(attemptingLocation == 0):
            self.xcoord = attemptingLocation
        elif(attemptingLocation == 2):
            self.playerDeath()
        '''
    
    def displayPlayer(self):
        drawRectInArr(GREEN, self.xcoord, self.ycoord)

    def playerDeath(self):
        pass
        
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
            elif event.type == QUIT:
                running = False
            '''
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == keys[pygame.K_LEFT]:
                player.moveLeft()
            if event.type == keys[pygame.K_RIGHT]:
                player.moveRight()
            '''
        pygame.display.update()
        FramePerSec.tick(FPS)

    
if __name__ == "__main__":
  main()
