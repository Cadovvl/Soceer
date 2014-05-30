# -*- coding: utf-8 -*-
"""
Created on Mon May 19 20:27:09 2014

@author: pasukhov
"""


class P1:
    finish = -1
    def getTargetPosition(self,lu,rb,gate,side):
        resy = (gate[0] + gate[1])/2.0 + 90
        resx = lu[0] + 145       
        if side == 1:
            resx = rb[0] - 145  
        return (resx,resy)
        
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        if self.finish == -1:
            self.finish = self.getTargetPosition(lu,rb,gate,side)
        
        speed = (self.finish[0] - your_position_x, self.finish[1] - your_position_y)
        
        return speed

class P2:
    finish = -1
    def getTargetPosition(self,lu,rb,gate,side):
        resy = (gate[0] + gate[1])/2.0 + 40
        resx = lu[0] + 175       
        if side == 1:
            resx = rb[0] - 175  
        return (resx,resy)
        
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        if self.finish == -1:
            self.finish = self.getTargetPosition(lu,rb,gate,side)
        
        speed = (self.finish[0] - your_position_x, self.finish[1] - your_position_y)
        
        return speed
                
class P3:
    finish = -1
    def getTargetPosition(self,lu,rb,gate,side):
        resy = (gate[0]*2 + 3*gate[1])/5.0
        resx = lu[0] + 90       
        if side == 1:
            resx = rb[0] - 90  
        return (resx,resy)
        
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        if self.finish == -1:
            self.finish = self.getTargetPosition(lu,rb,gate,side)
        
        speed = (self.finish[0] - your_position_x, self.finish[1] - your_position_y)
        
        return speed

  
class P4:
    finish = -1
    def getTargetPosition(self,lu,rb,gate,side):
        resy = (gate[0]*5 + 2*gate[1])/7.0 + 20
        resx = lu[0] + 40       
        if side == 1:
            resx = rb[0] - 40  
        return (resx,resy)
        
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        if self.finish == -1:
            self.finish = self.getTargetPosition(lu,rb,gate,side)
        
        speed = (self.finish[0] - your_position_x, self.finish[1] - your_position_y)
        
        return speed              
