import pygame

class Ball:
    def __init__(self,x,y,radius,color):
        self.x=x
        self.y=y
        self.radius=radius
        self.circle = pygame.Rect(x-radius,y-radius,2*radius,2*radius)
        self.color = color