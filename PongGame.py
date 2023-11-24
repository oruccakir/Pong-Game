from GameConstants import *
import pygame
import sys
from Ball import * 
from game_functions import *
import random
import math
import threading

# initialize the Pygame
pygame.init()


class PongGame:
    def __init__(self) -> None:
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.running = True

        self.left_rect = pygame.Rect(LEFT_RECT_X,LEFT_RECT_Y,RECT_WIDTH,RECT_HEIGHT)
        self.left_rect_color = RED

        self.right_rect = pygame.Rect(RIGHT_RECT_X, RIGHT_RECT_Y,RECT_WIDTH,RECT_HEIGHT)
        self.right_rect_color = GREEN,

        self.middle_rect = pygame.Rect(MIDDLE_RECT_X,MIDDLE_RECY_Y,MIDDLE_RECT_WIDTH,MIDEE_RECT_HEIGHT)
        self.middle_rect_color = WHITE

        self.ball = Ball(BALL_X,BALL_Y,BALL_RADIUS,AQUA)

        self.left_score = 0
        self.right_score = 0

        self.left_score_rect = pygame.Rect(LEFT_SCORE_X,LEFT_SCORE_Y,LEFT_SCORE_WIDTH,LEFT_SCORE_HEIGHT)
        self.right_score_rect = pygame.Rect(RIGHT_SCORE_X,RIGHT_SCORE_Y,RIGHT_SCORE_WIDTH,RIGHT_SCORE_HEIGHT)

        self.left_velocity = 1
        self.right_velocity = 1

        self.ball_velocity_x = 0.8
        self.ball_velocity_y = 0.6 

        self.left_turn = False


    def play_game(self):

        #thread = threading.Thread(target=get_coordinates_and_draw,args=(self.game_screen,self.right_rect))
        #thread.start()

        while self.running:

            # important code segment
            if self.left_turn:
                self.ball.x = self.ball.x + self.ball_velocity_x
            else:
                self.ball.x = self.ball.x - self.ball_velocity_x

            self.ball.y = self.ball.y - self.ball_velocity_y

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False


            if self.ball.x <= 0:
                self.right_score = self.right_score + 1
                self.ball = Ball(BALL_X,BALL_Y,BALL_RADIUS,AQUA)
                self.left_turn = True
                self.ball_velocity_x = 0.8
                self.ball_velocity_y = 0.6


            
            elif self.ball.x >= SCREEN_WIDTH:
                self.left_score = self.left_score + 1
                self.ball = Ball(BALL_X,BALL_Y,BALL_RADIUS,AQUA)
                self.left_turn = False
                self.ball_velocity_x = 0.8
                self.ball_velocity_y = 0.6

            
            elif self.ball.y <=0  or self.ball.y >= SCREEN_HEIGHT:
                self.ball_velocity_y = - self.ball_velocity_y
            
            elif self.right_rect.collidepoint(self.ball.x + BALL_RADIUS,self.ball.y) or self.left_rect.collidepoint(self.ball.x - BALL_RADIUS,self.ball.y):
                if self.ball_velocity_x <=0:
                    self.ball_velocity_x -= 0.2
                else:
                    self.ball_velocity_x += 0.2
                
                if self.ball_velocity_y <=0:
                    self.ball_velocity_y -= 0.2
                else:
                    self.ball_velocity_y += 0.2
                self.ball_velocity_x = - self.ball_velocity_x


             # Get the state of all keys
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                if self.left_rect.y <=0:
                    self.left_rect.y = 0
                else:
                    self.left_rect.y = self.left_rect.y - self.left_velocity
            elif keys[pygame.K_s]:
                if self.left_rect.y >=SCREEN_HEIGHT - RECT_HEIGHT:
                    self.left_rect.y = SCREEN_HEIGHT - RECT_HEIGHT
                else:
                    self.left_rect.y = self.left_rect.y + self.left_velocity
                
            if keys[pygame.K_UP]:
                if self.right_rect.y <=0:
                    self.right_rect.y = 0
                else:
                    self.right_rect.y = self.right_rect.y - self.right_velocity
            elif keys[pygame.K_DOWN]:
                if self.right_rect.y >=SCREEN_HEIGHT - RECT_HEIGHT:
                    self.right_rect.y = SCREEN_HEIGHT - RECT_HEIGHT
                else:
                    self.right_rect.y = self.right_rect.y + self.right_velocity


            self.game_screen.fill(BLACK)
            pygame.draw.rect(self.game_screen,self.left_rect_color,self.left_rect)
            pygame.draw.rect(self.game_screen,self.right_rect_color,self.right_rect)
            pygame.draw.rect(self.game_screen,self.middle_rect_color,self.middle_rect)
            pygame.draw.circle(self.game_screen,self.ball.color,(self.ball.x,self.ball.y),self.ball.radius)
            drawRect(self.game_screen,self.left_score_rect,f"{self.left_score}",BLACK)
            drawRect(self.game_screen,self.right_score_rect,f"{self.right_score}",BLACK)

            



            pygame.display.flip()

            


        #thread.join()




        # Quit Pygame
        pygame.quit()
        sys.exit()
        


game = PongGame()
game.play_game()
