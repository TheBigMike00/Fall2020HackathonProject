import pygame
pygame.init()

class Inhabitant:
    def __init__(self, name):
        self.name = name
        self.xcoord = None
        self.ycoord = None
    
    def display(self):
        print(f"{self.name} {self.xcoord} {self.ycoord}")
