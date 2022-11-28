import pygame
import os
pygame.init()
pygame.mixer.init()
pygame.font.init()

red = (255,0,0)
fps = 60
rectangle_width, rectangle_height = 30,100


score_font = pygame.font.SysFont("verdana",40)

win = pygame.display.set_mode((900,500))
win.fill(red)
pygame.display.set_caption("My Own Creation")
pygame.display.flip()

ball_sound = pygame.mixer.Sound(os.path.join("Items","bounce.mp3"))

rect1_image = pygame.image.load(os.path.join("Items","rect1.png"))
rect1 = pygame.transform.rotate(pygame.transform.scale(rect1_image,(rectangle_width,rectangle_height)),90)
rect2_image = pygame.image.load(os.path.join("Items","rect1.png"))
rect2 = pygame.transform.rotate(pygame.transform.scale(rect2_image,(rectangle_width,rectangle_height)),90)

'''
def display():
  win.blit(rect1,(100,100))
  win.blit(rect1,(player1.x,player1.y))
 ''' 
def main():
  #player1 = pygame.Rect(700,300,rectangle_width, rectangle_height)
  #player2 = pygame.Rect(100,300,rectangle_width, rectangle_height)
  print("YOO")
  run = True
  clock = pygame.time.clock()
  while run:
    clock.tick(fps)
    for event in pygame.events():
      if event == pygame.QUIT():
        run = False
        pygame.quit()

#display()