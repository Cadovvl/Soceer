import random
import pygame
import math

class GoalKeeper:
    a = (0,0)
    b = 15
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = lu[0]
        if side == 1:
            gx = rb[0]
        gy = (gate[0] + gate[1])/2.0
        a =[gx - your_team[index][0], gy - your_team[index][1]]
        k = random.randint(0,1000)
        if k < 600:
            self.b = -self.b
        a[1] += self.b
        """b = random.randint(gate[0],gate[1])
        if gate[1] - b <= b - gate[0]:
            a[1]=random.randint(b,b-gate[0])
        else:
            a[1]=random.randint(gate[1]-b,b)"""
        self.a = tuple(a)
        return self.a