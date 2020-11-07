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
        self.xcoord = None
        self.ycoord = None
    
    def display(self):
        print(f"{self.name} {self.xcoord} {self.ycoord}")
