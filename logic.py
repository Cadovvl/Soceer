# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 02:49:07 2014

@author: pasukhov
"""

"""
#####################   Class logic   #############################
## For creating your own logic change CLASSNAME, but do not touch FUNCTIONNAME ##

** lu  --  coordinates of left/upper corner # example: lu == [30,30]
** rb  --  coordinates of right/bottom corner # example: rb == [700,600]
** gate -- ordinate coordinate of gates # example: gate == [230,270]
** index -- your index in team # example: index == 3
** side -- your team. 0 - your are in the left team, 1 - you are in the right team
** balls -- coordinates of all balls in game # example balls = [ (200,200) ]
** your_team -- coordinates of your team in game # example your_team = [ (100,200), (200,300),(50,100) ]
    NB! your_team[index] -- your coordinates
** enemy_team -- coordinates of enemy team in game # example your_team = [ (600,200), (500,300),(650,100) ]


*return value*
    function must return tuple with two floating point values: (speeed_x, speed_y)
    speed on both coordinatex is limited by:
        |speeed| <= 10.0

"""



import random
import math


class SomeLogic:
    a = (0,0)
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        b = random.randint(1,1000)
        if b<300:
            x = random.randint(-10,10)
            y = random.randint(-10,10)
            self.a = (x,y)
            return self.a
        else:
            return self.a 
        
        
    
class MyLogicDudeSmellMondey:
    
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = balls[0][0]
        gy = balls[0][1]

        return ( gx - your_team[index][0] ,gy - your_team[index][1] )
        
        
