import random
import pygame
pygame.init()

background_colour = (255,255,255) #RGB Value
(width, height) = (800, 400) 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fall2020Hackathon')
screen.fill(background_colour)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
class Inhabitant:
    def __init__(self, name):
        self.name = name
        self.hp = -1
        self.str = -1
        self.defence = -1
        self.xcoord = None
        self.ycoord = None
        
class Player(Inhabitant):
    def __init__(self, max_hp, max_str, max_defence):
        super().__init__("Warrior")
        self.xcoord = 1
        self.ycoord = 400
        self.hp = random.randint(10, max_hp)
        self.str = random.randint(10, max_str)
        self.defence = random.randint(10, max_defence)       
        
def main():
  print("hello world")
    
if __name__ == "__main__":
  main()
