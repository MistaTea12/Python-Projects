import pygame
import random
from pygame.locals import *
pygame.init()
particlelist = []

colors = [((255,255,255)),((0,0,255)),((0,255,0)),((255,0,0))]

window = pygame.display.set_mode((600,600))
window_copy = window.copy()
pygame.display.set_caption('Particles')

particles = []
size = 8
lr = 1
gravity = -6
life = 1
spread = 4
height = 1
infinite = True

class Particles():

    def __init__(self, position):
        self.mx, self.my = position
        self.size = size
        particles.append([[self.mx, self.my], [random.randint(0, 20) / 10 - lr, gravity], random.randint(0, self.size)])
            
    def update(self, position):
        #particles.append([position, [random.randint(0, 20) / 10 - lr, gravity], random.randint(0, self.size)])
        for particle in particles:
            particle[0][0] += particle[1][0] * spread  #x value changes
            particle[0][1] += particle[1][1] * height  #y value changes
            particle[2] -= 0.1 #size change
            particle[1][1] += 0.1 #change in y
            pygame.draw.circle(window, (255,255,255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= life:
                particles.remove(particle)

class Particles2():

    def __init__(self, position):
        self.mx, self.my = position
        self.size = random.randint(0, 10)
        self.spread = random.randint(0, 20) / 10 - 2
        self.gravity = -10
        particles.append([[self.mx, self.my], [self.spread, self.gravity], self.size])
            
    def update(self, position):
        #particles.append([position, [random.randint(0, 20) / 10 - lr, gravity], random.randint(0, self.size)])
        for particle in particles:
            particle[0][0] += particle[1][0] * spread  #x value changes
            particle[0][1] += particle[1][1] * height  #y value changes
            particle[2] -= 0.1 #size change
            particle[1][1] += 0.1 #change in y
            pygame.draw.circle(window, (255,255,255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= life:
                particles.remove(particle)



clock = pygame.time.Clock()
running = True

while running:
    window.fill([0, 0, 0])
    positionx, positiony = pygame.mouse.get_pos()
    if infinite:
        newParticles = Particles2([positionx,positiony])
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    infinite = True
            elif event.type == pygame.MOUSEBUTTONUP:
                infinite = False

            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                running = False
            if key[pygame.K_UP]:
                size += 1
            if key[pygame.K_DOWN]:
                if size > 1:
                    size -= 1
            if key[pygame.K_LEFT]:
                lr += 1
            if key[pygame.K_RIGHT]:
                lr -= 1
            if key[pygame.K_PERIOD]:
                gravity += 1
            if key[pygame.K_COMMA]:
                gravity -= 1
            if key[pygame.K_w]:
                life += 0.2
            if key[pygame.K_s]:
                if life > 0:
                    life -= 0.2
            if key[pygame.K_x]:
                spread += 1
            if key[pygame.K_z]:
                spread -= 1
            if key[pygame.K_v]:
                height += 1
            if key[pygame.K_c]:
                height -= 1
            if key[pygame.K_TAB]:
                if infinite == True:
                    infinite = False
                else:
                    infinite = True
    try:
        newParticles.update([positionx,positiony])
    except:
        pass

    
    font = pygame.font.SysFont(None, 24)
    inf = font.render('[TAB]    ON: ' + str(infinite), True, (255,100,10))
    img = font.render('[UP, DOWN]   Size: ' + str(size), True, (235,245,255))
    img2 = font.render('[LEFT, RIGHT]  L/R: ' + str(lr), True, (235,245,255))
    img3 = font.render('[<,>]   Gravity: ' + str(gravity), True, (235,245,255))
    img4 = font.render('[W,S]   Life: ' + str(life), True, (235,245,255))
    img5 = font.render('[z,x]   Spread: ' + str(spread), True, (235,245,255))
    img6 = font.render('[c,v]   Height: ' + str(height), True, (235,245,255))
    window.blit(img, (20, 20))
    window.blit(img2, (20, 40))
    window.blit(img3, (20, 60))
    window.blit(img4, (20, 80))
    window.blit(img5, (20, 100))
    window.blit(inf, (400, 20))
    window.blit(img6, (20, 120))

    pygame.display.update()
    clock.tick(60)

pygame.quit()