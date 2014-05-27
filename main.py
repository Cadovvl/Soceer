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
import time

#import Pillars
#import CirclesOfGood
#import Metida


# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (   0,   0, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
size=[1000,640]
font = pygame.font.Font(pygame.font.get_default_font(), 12)

font_tech = pygame.font.Font( pygame.font.match_font(pygame.font.get_fonts()[0]), 50, bold=True)


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
#team_players1 = [Player([400,300],20,team1, Metida.P1(),"P1"),Player([275,250],20,team1, Metida.P2(),"P2"),Player([275,450],20,team1, Metida.P3(),"P3"),Player([150,300],20,team1, Metida.P4(),"P4")]
#team_players2 = [Player([600,330],20,team2, Metida.P1(),"P1"),Player([725,250],20,team2, Metida.P2(),"P2"),Player([725,450],20,team2, Metida.P3(),"P3"),Player([850,300],20,team2, Metida.P4(),"P4")]
#team_players1 = [Player([400,330],20,team1, Pillars.P1(),"P1"),Player([275,250],20,team1, Pillars.P2(),"P2"),Player([275,450],20,team1, Pillars.P3(),"P3"),Player([150,300],20,team1, Pillars.P4(),"P4")]
#team_players2 = [Player([600,330],20,team2, Pillars.P1(),"P1"),Player([725,250],20,team2, Pillars.P2(),"P2"),Player([725,450],20,team2, Pillars.P3(),"P3"),Player([850,300],20,team2, Pillars.P4(),"P4")]
team_players1 = [Player([300,200],20,team1, logic.MyLogicDudeSmellMondey() ,"Ronaldo"), Player([300,400],20,team1, foot0.GoalKeeper(),"Nikishina"),Player([100,250],20,team1, Logic()) ]
team_players2 = [Player([600,100],20,team2, logic.SomeLogic(),"Crazy Pinguin"), Player([700,400],20,team2, logic.MyLogicDudeSmellMondey(),"Messi"),Player([600,250],20,team2, doubleTrouble.DoubleTrouble2(), "Zidan") ]

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
            score[1] += 1
        if i.centerx + i.vx >= rb[0] and i.vx > 0 and i.centery > uv and i.centery < lv:           
            #pygame.event.post(pygame.event.Event(pygame.QUIT))
            done = True
            score[0] += 1


P1 = [0,0]
P2 = [0,0]
PI = [0,0]

def onP1(lu,rb,gate,side,team):
    resy = (gate[0] + gate[1])/2.0 
    resx = lu[0]      
    if side == 1:
        resx = rb[0]   
    
    count = 0
    for i in team:
        if (i.centerx - resx)**2 + (i.centery - resy)**2 < 2500 :
            count += 1
    if count < 2:
        P1[side] = 0
    else:
        P1[side] += 1


def onP2(lu,rb,gate,side,team, balls):
    resy = (gate[0] + gate[1])/2.0 
    resx = lu[0]      
    if side == 1:
        resx = rb[0]   
    flag = True
    for i in balls:
        if (i.centerx - resx)**2 + (i.centery - resy)**2 <= 150*150:
            flag = False

    if flag:    
        count = 0
        for i in team:
            if (i.centerx - resx)**2 + (i.centery - resy)**2 < 150*150 :
                count += 1
        if count < 3:
            P2[side] = 0
        else:
            P2[side] += 1
    else:
        P2[side] = 0
        
tP1 = [False,False]
tP2 = [False,False]
tPI = [False,False]

def onTechnicalIssue():
    global done
    if P1[0] > 10:
        tP1[0] = True
        done = True
    if P1[1] > 10:
        tP1[1] = True        
        done = True
    if P2[0] > 20:
        tP2[0] = True        
        done = True
    if P2[1] > 20:
        tP2[1] = True
        done = True


def ask_moves(b,t1,t2):
    global done
#    ball_positions = [(i.centerx,i.centery) for i in b]
#    team1_positions = [(i.centerx,i.centery) for i in t1]
#    team2_positions = [(i.centerx,i.centery) for i in t2]
    count = 0   
    for j in t1:
        try:            
            ball_positions = [(i.centerx,i.centery) for i in b]
            team1_positions = [(i.centerx,i.centery) for i in t1]
            team2_positions = [(i.centerx,i.centery) for i in t2]
            r = j.logic.move(lu,rb,[uv,lv],count,0,ball_positions,team1_positions,team2_positions)
            j.move(r[0],r[1])
        except Exception as e:
            print "Error while getting move"
            print e.message
            tPI[0] = True
            done = True
        count += 1
    count = 0   
    for j in t2:
        try:
            ball_positions = [(i.centerx,i.centery) for i in b]
            team1_positions = [(i.centerx,i.centery) for i in t1]
            team2_positions = [(i.centerx,i.centery) for i in t2]
            r = j.logic.move(lu,rb,[uv,lv],count,1,ball_positions,team2_positions,team1_positions)
            j.move(r[0],r[1])
        except Exception as e:
            print "Error while getting move"
            print e.message
            tPI[1] = True
            done = True
        
        count += 1



# -------- Основной цикл программы -----------

pygame.time.set_timer(pygame.QUIT, 300000)
startTime = time.time()

forceQuit = False

while score[0] < 3 and score[1] < 3:
    
    t1 = [copy.copy(i) for i in team_players1]
    t2 = [copy.copy(i) for i in team_players2]
    balls = [copy.copy(i) for i in balls_init]
    
    for i in t1:
        i.centerx += random.randint(-30,30)
        i.centery += random.randint(-30,30)
    for i in t2:
        i.centerx += random.randint(-30,30)
        i.centery += random.randint(-30,30)
    
    while done==False:
    	# ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                forceQuit = True
         
    	# ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
     
    	# ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
         
        onP1(lu,rb,[uv,lv],0,t1)        
        onP1(lu,rb,[uv,lv],1,t2)
        onP2(lu,rb,[uv,lv],0,t1,balls)        
        onP2(lu,rb,[uv,lv],1,t2,balls)
        
        onTechnicalIssue()
        
        #print P1,P2
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
        
        time_string = "{0:02}:{1:02}".format( time.localtime( time.time() - startTime).tm_min, time.localtime( time.time() - startTime).tm_sec )
        time_label = font_score.render(time_string,1,white)
        screen.blit(score_label, (311,10))
        screen.blit(time_label, (850,10))
        
        pygame.display.flip()
        # Ограничить до 20 кадров в секунду
        clock.tick(20)	

    if tP1[0] or tP1[1] or tP2[1] or tP2[0] or tPI[0] or tPI[1]:
        final = pygame.image.load("img/tech.jpg")#.convert()
        final = pygame.transform.scale(final, (300,300))
        screen.blit(final, (350,150))
        
        score_string = ""
        if tP1[0] or tP2[0] or tPI[0] :
            score_string = "<== Technical Error from This Team"    
        else:
            score_string = "Technical Error from This Team ==>"   
        
        score_label = font_tech.render(score_string,1,red)
        screen.blit(score_label, (150,500))    
        print "score:",score
        print "P1:",tP1,P1
        print "P2:",tP2,P2
        print "PI:",tPI
        pygame.display.flip()  
        time.sleep(3)
        break
    else:
        final = pygame.image.load("img/final.png")#.convert()
        final = pygame.transform.scale(final, (300,300))
        screen.blit(final, (350,150))
        
        score_string = "Score: >>===>  {0} :: {1}  <===<<".format(score[0],score[1])
        score_label = font_tech.render(score_string,1,red)
        
        screen.blit(score_label, (150,500))            
        pygame.display.flip()
        score_label = font_score.render(score_string,1,white)
        done = False
        print "score:",score
        print "P1:",tP1,P1
        print "P2:",tP2,P2
        print "PI:",tPI
        time.sleep(3)
    if forceQuit:
        break

print "score:",score
print "P1:",tP1,P1
print "P2:",tP2,P2
print "PI:",tPI

time.sleep(3)

pygame.quit()
