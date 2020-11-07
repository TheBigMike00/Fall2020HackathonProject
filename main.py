import random
import pygame
pygame.init()

#2D Array Key:
#0 -> available space
#1 -> obstacle (area that player cannot move)
#2 -> enemy (kills player)

BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20

def drawRectInArr(arrX, arrY):
    startX = arrX * BLOCK_WIDTH
    startY = arrY * BLOCK_HEIGHT
    #(starting x point, starting y point, "move over x steps"", 'move /up y steps )
    pygame.draw.rect(screen, (255,0,0), (startX, startY, BLOCK_WIDTH, BLOCK_HEIGHT))

background_colour = (0,0,255) #RGB Value
(width, height) = (800, 400) 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall2020Hackathon')
screen.fill(background_colour)
drawRectInArr(0,0)
drawRectInArr(5,5)
#pygame.draw.rect(screen, (255,0,0), (0,0, 40,80))
screen.blit(screen,(0,0))
pygame.display.flip()
rows, cols = ((int)(height/20), (int)(width/20)) 
arr = [[0 for i in range(cols)] for j in range(rows)] 
arr[0][0] = 1
#print(arr)

      
class Inhabitant:
    def __init__(self, name):
        self.name = name
        self.xcoord = None
        self.ycoord = None
        
class Player(Inhabitant):

    def __init__(self):
        super().__init__("Player")
        self.xcoord = 0
        self.ycoord = rows
        isInAir = True
        isAlive = True

    def moveRight(self):
        currentLocation = arr[self.xcoord][self.ycoord]
        attemptingLocation = arr[self.xcoord + 1][self.ycoord]
        if(attemptingLocation == 0):
            self.xcoord = attemptingLocation
            self.displayPlayer()

        elif(attemptingLocation == 2):
            self.playerDeath()
    
    def moveLeft(self):
        currentLocation = arr[self.xcoord][self.ycoord]
        attemptingLocation = arr[self.xcoord - 1][self.ycoord]
        if(attemptingLocation == 0):
            self.xcoord = attemptingLocation
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
    
    def displayPlayerOnBlock(self):
        drawRectInArr(self.xcoord, self.ycoord, BLOCK_WIDTH, BLOCK_HEIGHT)

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
    keys=pygame.key.get_pressed()
    player = Player()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.key == pygame.K_LEFT:
                player.moveLeft()
            if event.key == pygame.K_RIGHT:
                player.moveRight()

    
if __name__ == "__main__":
  main()
