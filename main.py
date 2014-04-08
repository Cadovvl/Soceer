# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import sys
from game import *
import logic
import loogic
import foot0
import doubleTrouble

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (   0,   0, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
size=[700,500]
font = pygame.font.Font(pygame.font.get_default_font(), 12)
screen=pygame.display.set_mode(size)

pygame.display.set_caption('I\'m PAVEEEEEEL')

bg_image = pygame.image.load("img/back.jpg").convert()
bg_image = pygame.transform.scale(bg_image, tuple(size))

ball = pygame.image.load("img/ball.png")#.convert()
ball = pygame.transform.scale(ball, (20,20))

team1 = pygame.image.load("img/team1.png")#.convert()
team1 = pygame.transform.scale(team1, (40,40))

team2 = pygame.image.load("img/team2.png")#.convert()
team2 = pygame.transform.scale(team2, (40,40))


       
#Оставаться в цикле, пока пользователь не нажмёт на кнопку закрытия окна


score = [0,0]

# Используется для контроля частоты обновления экрана

font_color = white

balls = [ Ball([350,250],10,ball)]

"""
balls[0].vx = 10.0
balls[0].vy = 6.3
"""


t1 = [Player([300,200],20,team1, logic.MyLogicDudeSmellMondey(),"Ronaldo"), Player([300,400],20,team1, foot0.GoalKeeper(),"Nikishina"),Player([100,250],20,team1, Logic()) ]
t2 = [Player([500,200],20,team2, logic.SomeLogic(),"Crazy Pinguin"), Player([500,400],20,team2, logic.MyLogicDudeSmellMondey(),"Messi"),Player([600,250],20,team2, doubleTrouble.DoubleTrouble2(), "Zidan") ]

global done
# -------- Основной цикл программы -----------
while done==False:
	# ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
     
	# ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
 
	# ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ

    #player's moves

    ask_moves(balls,t1,t2)

    # event analize
    on_player_game(balls,t1,t2)
    on_player_fight(t1,t2)
    
    on_victory(balls,screen)
    
    on_board_playres(t1)
    on_board_playres(t2)
    on_board_objects(balls)
    move(t1)
    move(t2)    
    move(balls)
    

	# ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

	
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
#    screen.fill(white)
    screen.blit(bg_image, [0,0])    

    # Отрисовка игроков
    for i in t1:
        i.display(screen)
    for i in t2:
        i.display(screen)

    # Отрисовка мяча    
    for i in balls:
        i.display(screen)

    # Вывести сделанную картинку на экран в точке (250, 250)
    #text = font.render("{0} {1}".format(score[0],score[1]),True,font_color)
    #screen.blit(text, [0,0])

    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
    pygame.display.flip()
    # Ограничить до 20 кадров в секунду
    clock.tick(20)	

final = pygame.image.load("img/final.png")#.convert()
final = pygame.transform.scale(final, (300,300))
screen.blit(final, (200,100))

pygame.display.flip()

time.sleep(3)

pygame.quit()