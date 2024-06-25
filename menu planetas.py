import pygame
import os
import sys 

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((800, 400),0,32)
fondo = pygame.image.load(os.path.join("fondo.jpg"))
fondo = pygame.transform.scale(fondo, (800, 400))
font = pygame.font.SysFont('Arial', 60)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.blit(fondo, (0,0))

        mercurio = pygame.image.load('mercurio.png')
        mercurio = pygame.transform.scale(mercurio, (100, 100))
        venus = pygame.image.load('venus.png')
        venus = pygame.transform.scale(venus, (100, 100))
        tierra = pygame.image.load('tierra.png')
        tierra = pygame.transform.scale(tierra, (100, 100))
        marte = pygame.image.load('marte.png')
        marte = pygame.transform.scale(marte, (100, 100))
        jupiter = pygame.image.load('jupiter.png')
        jupiter = pygame.transform.scale(jupiter, (100, 100))
        saturno = pygame.image.load('saturno.png')
        saturno = pygame.transform.scale(saturno, (120, 100))
        urano = pygame.image.load('urano.png')
        urano = pygame.transform.scale(urano, (100, 100))
        neptuno = pygame.image.load('neptuno.png')
        neptuno = pygame.transform.scale(neptuno, (100, 100))
        pluton = pygame.image.load('pluton.png')
        pluton = pygame.transform.scale(pluton, (100, 100))

        mx, my = pygame.mouse.get_pos()
       
        button_1 = mercurio.get_rect()
        button_1.center = (150, 170)
        button_2 = venus.get_rect()
        button_2.center = (230, 85)
        button_3 = tierra.get_rect()
        button_3.center = (370, 50)
        button_4 = marte.get_rect()
        button_4.center = (520, 85)
        button_5 = jupiter.get_rect()
        button_5.center = (650, 170)
        button_6 = saturno.get_rect()
        button_6.center = (590, 280)
        button_7 = urano.get_rect()
        button_7.center = (470, 340)
        button_8 = neptuno.get_rect()
        button_8.center = (320, 340)
        button_9 = pluton.get_rect()
        button_9.center = (200, 280)
        
        if button_1.collidepoint((mx, my)):
            if click:
                planet1()
        if button_2.collidepoint((mx, my)):
            if click:
                planet2()
        if button_3.collidepoint((mx, my)):
            if click:
                planet3()
        if button_4.collidepoint((mx, my)):
            if click:
                planet4()
        if button_5.collidepoint((mx, my)):
            if click:
                planet5()
        if button_6.collidepoint((mx, my)):
            if click:
                planet6()
        if button_7.collidepoint((mx, my)):
            if click:
                planet7()
        if button_8.collidepoint((mx, my)):
            if click:
                planet8()
        if button_9.collidepoint((mx, my)):
            if click:
                planet9()
       
        screen.blit(mercurio, button_1)
        screen.blit(venus, button_2)
        screen.blit(tierra, button_3)
        screen.blit(marte, button_4)
        screen.blit(jupiter, button_5)
        screen.blit(saturno, button_6)
        screen.blit(urano, button_7)
        screen.blit(neptuno, button_8)
        screen.blit(pluton, button_9)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def planet1():
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        draw_text('Mercurio', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def planet2():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Venus', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet3():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Tierra', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet4():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Marte', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet5():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Jupiter', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet6():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Saturno', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet7():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Urano', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet8():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Neptuno', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def planet9():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Pluton', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()