# -*- coding: utf-8 -*-

# Makarova
# Shennicova
# Orehova


import random
from math import sqrt, pow

class Line:
    def __init__(self, point1=None, point2=None):
        if point1 and point2:
            if point1[0] == point2[0]:
                self.a = 0
                self.b = 1
                self.c = -point1[0]
            else:
                self.a = 1
                self.b = (point1[1]-point2[1])/(point1[0]-point2[0])
                self.c = point1[1] - self.b*point1[0]

    def get_perpendicular_line(self, point):
        line = Line()
        if self.a == 0:
            line.a = 1
            line.b = 0
            line.c = -point[1]
        elif self.b == 0:
            line.a = 0
            line.b = 1
            line.c = -point[0]
        else:
            line.a = 1
            line.b = -1 / self.b
            line.c = point[1] - line.b*point[0]
        return line

    def get_minimal_distance(self, point):
        return (self.a*point[0] + self.b*point[1] + self.c) / sqrt(self.a*self.a + self.b*self.b)


def in_sector(up_line, down_line, me, ball):
    if ball[0] == me[0]:
        return False
    k = (ball[1]-me[1]) / (ball[0]-me[0])
    b = me[1] - k*me[0]
    # print (b<=up_line[1] and b>=down_line[1])
    return (b<=up_line.b and b>=down_line.b)

class P1:
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        me = your_team[index]
        ball = balls[0]


        if side == 0:
            up_line = Line([rb[0],gate[0]], ball)
            down_line = Line([rb[0], gate[1]], ball)
            mid_line = Line([rb[0], (gate[1]-gate[0])/2], ball)
            strike_point = [balls[0][0]-31, balls[0][1]]
        else:
            up_line = Line([lu[0],gate[0]], ball)
            down_line = Line([lu[0], gate[1]], ball)
            mid_line = Line([lu[0], (gate[1]-gate[0])/2], ball)
            strike_point = [ball[0]+31, ball[1]]

        if in_sector(up_line, down_line, me, ball) or side == 0:
            return (ball[0]-me[0],ball[1]-me[1])
        else:
            me_to_strike_point = Line(me, strike_point)

            if me_to_strike_point.get_minimal_distance(ball) <= 35:
                perp_to_me_to_sp = me_to_strike_point.get_perpendicular_line(ball)
                a = 1+perp_to_me_to_sp.b
                b = 2*(ball[0]-perp_to_me_to_sp.b*perp_to_me_to_sp.c+perp_to_me_to_sp.b*ball[1])
                c = pow(ball[0], 2) + pow(perp_to_me_to_sp.c, 2) - 2*perp_to_me_to_sp.c*ball[1] + pow(ball[1], 2) - pow(35, 2)
                D = pow(b, 2) - 4*a*c
                if D<0:
                    print("discriminant is negative")
                    D = 0
                x = (-b + sqrt(D))/2/a
                y = perp_to_me_to_sp.b*x + perp_to_me_to_sp.c
                return (x-me[0], y-me[1])
            else:
                return (strike_point[0] - me[0], strike_point[1] - me[1])

class P4:
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
        self.a = tuple(a)
        return self.a

class P2:
    finish = -1
    def getTargetPosition(self,lu,rb,gate,side):
        resy = (gate[0] + gate[1])/2.0 - 60
        resx = lu[0] + 160      
        if side == 1:
            resx = rb[0] - 160  
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
        resy = (gate[0] + gate[1])/2.0 + 40
        resx = lu[0] + 35       
        if side == 1:
            resx = rb[0] - 35  
        return (resx,resy)
        
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        if self.finish == -1:
            self.finish = self.getTargetPosition(lu,rb,gate,side)
        
        speed = (self.finish[0] - your_position_x, self.finish[1] - your_position_y)
        
        return speed
