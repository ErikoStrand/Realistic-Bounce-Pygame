import pygame
import sys
import numpy as np
pygame.init()
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])
board = pygame.image.load("board.png")
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BACKGROUND = (0, 0, 0)
BALLS = []
BALLS_AMOUNT = 1
class ball:
    def __init__ (self, rect, display, speed):
        self.rect = pygame.Rect(rect)
        self.display = display
        self.fallspeed = 9.82
        self.velocityY = 0
        self.velocityX = speed
        self.airRes = 5
        
    def update(self, dt): 
        if self.rect.y >= HEIGHT - self.rect.height:
            self.velocityY *= -1
        if self.rect.y <= 0:
            self.velocityY *= -1
        if self.rect.x > WIDTH - self.rect.height:
            self.airRes *= -1
            self.velocityX *= -1
        if self.rect.x < 0:
            self.airRes *= -1
            self.velocityX *= -1
        if -1 < self.velocityX < 1:
            self.velocityX = 0
            
        self.velocityX -= self.airRes * dt
        self.velocityY += self.fallspeed
        self.rect.y = self.rect.y + (self.velocityY * dt)
        self.rect.x = self.rect.x - (self.velocityX * dt)
            
    def draw(self):
        pygame.draw.circle(self.display, (255, 255, 255), (self.rect.center), self.rect.width/2)
        
while 1:
    player_rect = board.get_rect(topleft=(pygame.mouse.get_pos()))
    
    dt = clock.tick(240) / 500
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()
            
    DISPLAY.fill(BACKGROUND) 
    if BALLS_AMOUNT > len(BALLS):
        BALLS.append(ball((WIDTH/2, HEIGHT/2, 50, 50), DISPLAY, 200)) 
    for balls in BALLS:
        balls.update(dt)
        balls.draw()
        
    for balls in BALLS:
        if pygame.Rect.colliderect(balls.rect, player_rect):
            balls.velocityX += 200
        
    # temp work around
    #DISPLAY.blit(pygame.transform.rotate(DISPLAY, 180), (0, 0))
    DISPLAY.blit(board, pygame.mouse.get_pos())
            
    pygame.display.flip()
    
