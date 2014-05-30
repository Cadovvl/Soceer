
# Dorbisheva
# Balashova

import random
import pygame
import math

class P1:
    speed = (0,0)
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = lu[0]+30
        gy = (gate[0] + gate[1])/2.0
        if side == 1:
            gx = rb[0]-30
            if (balls[0][0] > (lu[0]+rb[0])/2) and (balls[0][1] > 150) and (balls[0][1] < 450):
                    gy = balls[0][1]
        if (balls[0][0] < (lu[0]+rb[0])/2) and (balls[0][1] > 150) and (balls[0][1] < 450):
                gy = balls[0][1]
        speed = [gx - your_team[index][0], gy - your_team[index][1]]
        self.speed = tuple(speed)
        
        return self.speed

class P2:
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = lu[0]
        if side == 1:
            gx = rb[0]
        if (abs(balls[0][0] - your_team[index][0]) < 5) and (abs(balls[0][1] - your_team[index][1]) < 5):
            speed = (gx - your_team[index][0] + random.randint(-2,2), (gate[0] + gate[1])/2.0 - your_team[index][1] + random.randint(-2,2)) 
        else:
            speed = (balls[0][0] - your_team[index][0] + random.randint(-3,3), balls[0][1] - your_team[index][1] + random.randint(-3,3))
            
        return speed

class P3:
    speed = (0,0)
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = lu[0]+200
        gy = (gate[0] + gate[1])/2.0
        
        if side == 1:
            gx = rb[0]-200
            if balls[0][0] > (lu[0]+rb[0])/2:
                gy = balls[0][1]
            else:
                if (abs(balls[0][0] - your_team[index][0]) < 5) and (abs(balls[0][1] - your_team[index][1]) < 5):
                    speed = (rb[0] - your_team[index][0] + random.randint(-2,2), (gate[0] + gate[1])/2.0 - your_team[index][1] + random.randint(-2,2))
                else:
                    speed = (balls[0][0] - your_team[index][0] + random.randint(-3,3), balls[0][1] - your_team[index][1] + random.randint(-3,3))
                self.speed = tuple(speed)
                
                return self.speed
                
        if balls[0][0] < (lu[0]+rb[0])/2:
            gy = balls[0][1]
        else:
            if (abs(balls[0][0] - your_team[index][0]) < 2) and (abs(balls[0][1] - your_team[index][1]) < 2):
                speed = (lu[0] - your_team[index][0] + random.randint(-1,1), (gate[0] + gate[1])/2.0 - your_team[index][1] + random.randint(-1,1))
            else:
                speed = (balls[0][0] - your_team[index][0] + random.randint(-3,3), balls[0][1] - your_team[index][1] + random.randint(-3,3))
            self.speed = tuple(speed)
            
            return self.speed
            
        speed = [gx - your_team[index][0], gy - your_team[index][1]] 
        self.speed = tuple(speed)
        
        return self.speed

class P4:
    speed = (0,0)
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = lu[0]+100
        gy = (gate[0] + gate[1])/2.0
        if side == 1:
            gx = rb[0]-100
            if balls[0][0] > (lu[0]+rb[0])/2:
                gy = balls[0][1]
        if balls[0][0] < (lu[0]+rb[0])/2:
            gy = balls[0][1]
        speed = [gx - your_team[index][0], gy - your_team[index][1]] 
        self.speed = tuple(speed)

        return self.speed
