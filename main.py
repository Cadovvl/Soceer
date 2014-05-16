# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import sys
from game import *
import logic
import loogic
import foot0
import doubleTrouble
import ExampleLogic
import copy

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (   0,   0, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
size=[1000,640]
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


# Используется для контроля частоты обновления экрана

font_color = white

balls_init = [ Ball([(lu[0] + rb[0])/2,(lu[1] + rb[1])/2],10,ball)]


#logic.MyLogicDudeSmellMondey()
#doubleTrouble.DoubleTrouble2()

"""
***********************************
###  initialization of players  ###
***********************************
"""

#team1 = []
#team2 = [Player([600,100],20,team2, ExampleLogic.GoToTheCenter(),"Sample Pinguin")]
team1 = [Player([300,200],20,team1, logic.MyLogicDudeSmellMondey() ,"Ronaldo"), Player([300,400],20,team1, foot0.GoalKeeper(),"Nikishina"),Player([100,250],20,team1, Logic()) ]
team2 = [Player([600,100],20,team2, logic.SomeLogic(),"Crazy Pinguin"), Player([700,400],20,team2, logic.MyLogicDudeSmellMondey(),"Messi"),Player([600,250],20,team2, doubleTrouble.DoubleTrouble2(), "Zidan") ]

"""
***************************************
###  eof initialization of players  ###
***************************************
"""


done=False

def on_victory(b,screen):
    global done
    for i in b:
        if i.centerx + i.vx <= lu[0] and i.vx < 0 and i.centery > uv and i.centery < lv:
            #pygame.event.post(pygame.event.Event(pygame.QUIT))
            done = True
            score[0] += 1
        if i.centerx + i.vx >= rb[0] and i.vx > 0 and i.centery > uv and i.centery < lv:           
            #pygame.event.post(pygame.event.Event(pygame.QUIT))
            done = True
            score[1] += 1


# -------- Основной цикл программы -----------

while score[0] < 3 and score[1] < 3:
    
    t1 = [copy.copy(i) for i in team1]
    t2 = [copy.copy(i) for i in team2]
    balls = [copy.copy(i) for i in balls_init]
    
    while done==False:
    	# ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                score = [10,10]
         
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
        screen.blit(score_label, (350,10))
        pygame.display.flip()
        # Ограничить до 20 кадров в секунду
        clock.tick(20)	
    
    final = pygame.image.load("img/final.png")#.convert()
    final = pygame.transform.scale(final, (300,300))
    screen.blit(final, (350,150))
    
    score_string = "Score: >>===>  {0} :: {1}  <===<<".format(score[0],score[1])
    score_label = font_score.render(score_string,1,white)
    
    screen.blit(score_label, (350,500))    
    
    pygame.display.flip()
    done = False
    time.sleep(3)


print score
time.sleep(5)

pygame.quit()
