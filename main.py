import pygame
import sys
pygame.init()
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN])
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BACKGROUND = (0, 0, 0)

class ball:
    def __init__ (self, rect, display):
        self.rect = pygame.Rect(rect)
        self.display = display
        self.gravity = 9.82
        self.velocity = 0
        
    def update(self, dt):
        self.velocity += self.gravity
        self.rect.y = self.rect.y - (self.velocity * dt)
        print(self.rect.y, self.velocity)
    
    def draw(self):
        pygame.draw.circle(self.display, (255, 255, 255), (self.rect.center), self.rect.width/2)
        
balls = ball((WIDTH/2, HEIGHT/2, 50, 50), DISPLAY)
while 1:
    dt = clock.tick(240) / 500
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()
            
    DISPLAY.fill(BACKGROUND)  
    balls.update(dt)
    if balls.rect.y >= HEIGHT - balls.rect.height:
        balls.velocity *= -1
    if balls.rect.y <= 0:
        balls.velocity *= -1
    balls.draw()
    pygame.display.flip()
    
