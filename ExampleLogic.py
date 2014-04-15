# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 13:08:06 2014

@author: pasukhov
"""



class GoToTheCenter:
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        # get center coordinates        
        center_x = (lu[0] + rb[0])/2.0
        center_y = (lu[1] + rb[1])/2.0
        # get your coordinates
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        # generate speed
        speed = (center_x - your_position_x , center_y - your_position_y)
        return speed
        



class WalkBetweenTwoPoints:
    position = 0
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        # get first coordinates        
        first_x = (lu[0] + 2*rb[0])/3.0
        first_y = (lu[1] + rb[1])/2.0
        # get second coordinates        
        second_x = (2*lu[0] + rb[0])/3.0
        second_y = (lu[1] + rb[1])/2.0
        # get your coordinates
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        # generate speed
        if self.position == 0:
            speed = (first_x - your_position_x , first_y - your_position_y)
        else:
            speed = (second_x - your_position_x , second_y - your_position_y)
            
        if speed == (0,0):
            self.position = (self.position + 1) % 2
        return speed
        

class WalkOnDiagonal:
    position = 0
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        # get first coordinates        
        first_x = (lu[0] + 2*rb[0])/3.0
        first_y = (lu[1]*2 + rb[1])/3.0
        # get second coordinates        
        second_x = (2*lu[0] + rb[0])/3.0
        second_y = (lu[1] + 2*rb[1])/3.0
        # get your coordinates
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        # generate speed
        if self.position == 0:
            speed = (first_x - your_position_x , first_y - your_position_y)
        else:
            speed = (second_x - your_position_x , second_y - your_position_y)
            
        if speed == (0,0):
            self.position = (self.position + 1) % 2
        return speed
        

class StraightDiagonal:
    position = 0
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        # get first coordinates        
        first_x = (lu[0] + 2*rb[0])/3.0
        first_y = (lu[1]*2 + rb[1])/3.0
        # get second coordinates        
        second_x = (2*lu[0] + rb[0])/3.0
        second_y = (lu[1] + 2*rb[1])/3.0
        # get your coordinates
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        # generate speed
        if self.position == 0:
            speed = (first_x - your_position_x , first_y - your_position_y)
        else:
            speed = (second_x - your_position_x , second_y - your_position_y)

        if speed == (0,0):
            self.position = (self.position + 1) % 2
        
        if max(speed[0],speed[1]) >= 10:
            alpha = 10.0/max(abs(speed[0]),abs(speed[1]))
            speed = (alpha*speed[0], alpha*speed[1])
        
        return speed
        



        


