import pygame
import sys
import numpy as np
pygame.init()
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])
board = pygame.image.load("penis.png")
board = pygame.transform.scale(board, (200, 200))
board = pygame.transform.rotate(board, 270)
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BACKGROUND = (0, 0, 0)
BALLS = []
BALLS_AMOUNT = 1000
class ball:
    def __init__ (self, rect, display, speed):
        self.rect = pygame.Rect(rect)
        self.display = display
        self.fallspeed = 9.82
        self.velocityY = 0
        self.velocityX = speed
        self.airRes = 5
        self.g = np.random.randint(150, 255)
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
            
        if self.velocityY <= 0:
            self.velocityY += self.fallspeed * dt + (1 * 0.05)
        if self.velocityY >= 0:    
            self.velocityY += self.fallspeed * dt
        self.rect.y = (self.rect.y) + self.velocityY
        self.velocityX -= self.airRes * dt
        self.rect.x = self.rect.x - (self.velocityX * dt)
                    
    def draw(self):
        pygame.draw.circle(self.display, (self.g, self.g, self.g), (self.rect.center), self.rect.width/2)
        
while 1:
    x, y = pygame.mouse.get_pos()
    player_rect_left = board.get_rect(topleft=(x, y))
    player_rect_right = board.get_rect(topleft=(x, y))
    
    dt = clock.tick(240) / 500
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()
            
    display.fill(BACKGROUND) 
    if BALLS_AMOUNT > len(BALLS):
        BALLS.append(ball((x, y + 15, 50, 50), display, 200)) 
    for balls in BALLS:
        balls.update(dt)
        balls.draw()
        
    for balls in BALLS:
        if pygame.Rect.colliderect(balls.rect, player_rect_left):
            balls.velocityX += 100
            balls.velocityY -= 1
        
    # temp work around
    #DISPLAY.blit(pygame.transform.rotate(DISPLAY, 180), (0, 0))
    display.blit(board, pygame.mouse.get_pos())
            
    pygame.display.flip()
    
