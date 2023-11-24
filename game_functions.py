import pygame
import serial
from GameConstants import *

# arduinoData = serial.Serial("com6",9600)

def drawRect(surface,rect,text,color):
    pygame.draw.rect(surface,color,rect)
    font = pygame.font.Font(None,72)
    text = font.render(text,True,(255,255,255))
    text_rect = text.get_rect(center = rect.center)
    surface.blit(text,text_rect)

def get_coordinates_and_draw(screen,rect):

    while True:

        dataPacket = arduinoData.readline()
        dataPacket = str(dataPacket,"utf-8")
        dataPacket.strip("\r\n")
        splitPacket = dataPacket.split(",")

        x = float(splitPacket[0])

        rect.y = (-750*x)/1020 + 750

            