import random
import pygame
pygame.init()

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
'''
rows, cols = ((int)(height/20), (int)(width/20)) 
arr = [[0 for i in range(cols)] for j in range(rows)] 
arr[0][0] = 1
print(arr)
'''
running = True
while running:
<<<<<<< HEAD
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

=======
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
>>>>>>> 96ea9b370520c28c7a99faaa95f30aa41ba98156
class Inhabitant:
    def __init__(self, name):
        self.name = name
        self.xcoord = None
        self.ycoord = None
        
class Player(Inhabitant):
    def __init__(self, max_hp, max_str, max_defence):
        super().__init__("Warrior")
        self.xcoord = 0
        self.ycoord = 0
        self.hp = random.randint(10, max_hp)
        self.str = random.randint(10, max_str)
        self.defence = random.randint(10, max_defence)

        
class Poison_Shroom(Inhabitant):
    def __init__(self, max_hp):
        super().__init__("Poison Shroom")
        self.xcoord = 0
        self.ycoord = 0
        self.hp = random.randint(10, max_hp)
                
def main():
  print("hello world")
    
if __name__ == "__main__":
  main()
