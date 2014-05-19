# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 00:56:59 2014

@author: pasukhov
"""

import pygame
from pygame.locals import *
import random
import time

pygame.init()
font = pygame.font.Font(pygame.font.get_default_font(), 12)

font_score = pygame.font.Font(pygame.font.get_default_font(), 20)

clock=pygame.time.Clock()
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (   0,   0, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

class Obj(object):
    centerx = 20.0;
    centery = 20.0;
    R = 10.0;
    pic = None;
    def __init__(self,pos,size,pic):
        self.R = size
        self.centerx,self.centery = tuple(pos)
        self.pic = pic
    def display(self,screen):
        screen.blit(self.pic,((self.centerx-self.R,self.centery-self.R), (self.centerx+self.R,self.centery+self.R)))
        

class Ball(Obj):
    vx = 0.0
    vy = 0.0
    maxvx = 20.0
    maxvy = 20.0

    def __init__(self,pos,size,pic,maxvx = 20.0,maxvy = 20.0):
        Obj.__init__(self,pos,size,pic)
        self.maxvx = maxvx
        self.maxvy = maxvy
        
    def  cannon(self,vx,vy):
        if (self.vx*vx + self.vy*vy <= 0):
            self.vx = -self.vx
            self.vy = -self.vy
        self.vx = self.vx + 2*vx
        self.vy = self.vy + 2*vy
        self.vx = min(self.vx,self.maxvx)
        self.vy = min(self.vy,self.maxvy)
        self.vx = max(self.vx,-self.maxvx)
        self.vy = max(self.vy,-self.maxvy)
    def on_move(self):
        self.centerx += self.vx
        self.centery += self.vy
        self.vx = self.vx*0.95
        self.vy = self.vy*0.95

class Logic:    
    a=(0,0) 
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        b = random.randint(1,1000)
        if b<150:
            x = random.randint(-10,10)
            y = random.randint(-10,10)
            self.a = (x,y)
            return self.a
        else:
            return self.a            

class Player(Obj):
    vx = 0.0
    vy = 0.0
    maxvx = 10.0
    maxvy = 10.0
    name = "NoName"
    logic = None
    def __init__(self,pos,size,pic,move_logic, name = "NoName", maxvx = 10.0,maxvy = 10.0):
        Obj.__init__(self,pos,size,pic)
        self.logic = move_logic
        self.maxvx = maxvx
        self.maxvy = maxvy
        self.name = name
        
    def  cannon(self,vx,vy):
        self.vx = vx
        self.vy = vy
        self.vx = min(self.vx,self.maxvx)
        self.vy = min(self.vy,self.maxvy)
        self.vx = max(self.vx,-self.maxvx)
        self.vy = max(self.vy,-self.maxvy)
    def move(self,vx,vy):
        self.vx = vx
        self.vy = vy
        self.vx = min(self.vx,self.maxvx)
        self.vy = min(self.vy,self.maxvy)
        self.vx = max(self.vx,-self.maxvx)
        self.vy = max(self.vy,-self.maxvy)
        
    def on_move(self):
        self.centerx += self.vx
        self.centery += self.vy
    def display(self,screen):
        label = font.render(self.name,1,white)
        screen.blit(label, (self.centerx - self.R,self.centery - self.R - 10))
        Obj.display(self,screen)


# board constants 
lu = [50,40]
ru = [950,40]
rb = [950,600]
lb = [50,600]

uv = 275
lv = 365


score = [0,0]
score_string = "Score: >>===>  {0} :: {1}  <===<<".format(score[0],score[1])
score_label = font_score.render(score_string,1,white)

def on_board_objects(t):
    for i in t:
        if i.centerx + i.vx < lu[0] or i.centerx + i.vx > rb[0]:
            i.vx = -i.vx
        if i.centery + i.vy < lu[1] or i.centery + i.vy > rb[1]:
            i.vy = -i.vy

def on_board_playres(t):
    for i in t:
        if (i.centerx + i.vx < lu[0] and i.vx < 0 ) or (i.centerx + i.vx > rb[0] and i.vx > 0):
            i.vx = 0
        if (i.centery + i.vy < lu[1] and i.vy < 0 ) or (i.centery + i.vy > rb[1] and i.vy > 0):
            i.vy = 0

def on_player_game(objects,players1,players2):
    for i in objects:
        for j in players1:
            if (j.centerx + j.vx - i.centerx)**2 + (j.centery + j.vy - i.centery)**2 <= (i.R + j.R)**2:
                i.cannon(j.vx,j.vy)
        for j in players2:
            if (j.centerx + j.vx - i.centerx)**2 + (j.centery + j.vy - i.centery)**2 <= (i.R + j.R)**2:
                i.cannon(j.vx,j.vy)

def on_player_fight(players1,players2):
        for j in players1:
            for i in players2:
                if (j.centerx + j.vx - i.centerx - i.vx)**2 + (j.centery + j.vy - i.centery  - i.vx )**2 <= (i.R + j.R)**2:
                    vx,vy = i.vx, i.vy
                    i.cannon(j.vx,j.vy)
                    j.cannon(vx,vy)
       

 

def ask_moves(b,t1,t2):
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
        
        count += 1

def move(objects):
    for i in objects:
        i.on_move()
        
        
    
def technical_error_validator(b,t1,t2):
    ball_positions = [(i.centerx,i.centery) for i in b]
    team1_positions = [(i.centerx,i.centery) for i in t1]
    team2_positions = [(i.centerx,i.centery) for i in t2] 
    radius = 150
    # testing side 0
    
    # testing side 1
    
    
    
    
    
    
