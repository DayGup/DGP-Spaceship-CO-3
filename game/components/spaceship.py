import pygame

from pygame.sprite import Sprite

from game.utils.constants import  SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP


class SpaceShip(Sprite):
    def __init__(self): 
        self.image = pygame.transform.scale(SPACESHIP, (60,40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
    
    def update(self, user_input):
     if user_input[pygame.K_LEFT]:
         self.move_left()
     elif user_input[pygame.K_RIGHT]:
         self.move_right()
     elif user_input[pygame.K_UP]:
             self.move_up()
     elif user_input[pygame.K_DOWN]:
             self.move_dowm()
   
   #Izquierda                  
    def move_left(self):
         if self.rect.left > 0:
             self.rect.x -= 10
        #le añadi una nueva secuencia
         elif self.rect.left <= 0:
               self.rect.x = SCREEN_WIDTH
               
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
            #le añadi una nueva secuencia
        elif self.rect.right >= SCREEN_WIDTH:
             self.rect.x = 0
             
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT //2:
           self.rect.x -= 10
    def move_dowm(self):
        if self.rect.y < SCREEN_HEIGHT-50:
            self.rect.y += 10  
    def draw (self,screen):
      screen.blit(self.image,(self.rect.x, self.rect.y))
      
  
