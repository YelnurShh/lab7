import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
clock = pygame.time.Clock()


clockk = pygame.image.load(r"/Users/elnrsahar/Desktop/Python tasks/lab7/clock_game/clock.png")
l = pygame.image.load(r"/Users/elnrsahar/Desktop/Python tasks/lab7/clock_game/leftarm.png")
r = pygame.image.load(r"/Users/elnrsahar/Desktop/Python tasks/lab7/clock_game/rightarm.png")

rect = clockk.get_rect(center=(415, 418))

while True:
    screen.fill((255, 255, 255))  
    screen.blit(clockk, rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    t = datetime.now().time()
    
    
    sec_angle = -t.second * 6  
    sec_hand = pygame.transform.rotate(l, sec_angle)
    sec_rect = sec_hand.get_rect(center=rect.center)  
    screen.blit(sec_hand, sec_rect.topleft)

   
    min_angle = -t.minute * 6  
    min_hand = pygame.transform.rotate(r, min_angle)
    min_rect = min_hand.get_rect(center=rect.center)  
    screen.blit(min_hand, min_rect.topleft)

    pygame.display.flip()
    clock.tick(60)
