# -*- coding: utf-8 -*-
"""
Created on Mon May 19 22:26:21 2014

@author: pasukhov
"""


# -*- coding: utf-8 -*-
"""
Created on Mon May 19 20:27:09 2014

@author: pasukhov
"""
import math

def solve(a,b,c, flag = True):
    D = b**2 - 4.0*a*c
    if D < 0:
        return None
    if flag:
        return (-1.0*b + math.sqrt(D))/(2.0*a)
    else:
        return (-1.0*b - math.sqrt(D))/(2.0*a)

def nextCircleCoordinate(x1,y1,x2,y2, flag = True):# second is ball
    x0 = x2 - x1
    y0 = y2 - y1
    a = x0**2 + y0**2
    return (solve(a,-100*x0,2500.0 - 100.0* y0**2,(y1 > y2) ^ flag  ) + x1, solve(a,-100*y0,2500.0 - 100.0* x0**2, (x1 < x2)  ^ flag ) + y1 )
    


class P1:

    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        gy = (gate[0] + gate[1])/2.0
        gx = rb[0]        
        if side == 1:
            gx = lu[0] 
        v1x = your_position_x - gx
        v1y = your_position_y - gy
        v2x = balls[0][0] - gx
        v2y = balls[0][1] + 40 - gy
        v3x = balls[0][0] - gx
        v3y = balls[0][1] - 40 - gy
        
        
        speed = (balls[0][0] - your_position_x, balls[0][1] - your_position_y)
        if (( your_position_x - balls[0][0])**2 + ( your_position_y - balls[0][1])**2   ) < 100:
            speed = (gx - your_position_x, gy - your_position_y)
            alpha = 10.0/max(abs(speed[0]),abs(speed[1]))
            speed = (alpha*speed[0], alpha*speed[1])
            return speed            
            
        if (v1x*v2y - v2x*v1y)*((v1x*v3y - v3x*v1y)) < 0 and (balls[0][0] - your_position_x) * (0.5 - side) > 0 :
            alpha = 10.0/max(abs(speed[0]),abs(speed[1]))
            speed = (alpha*speed[0], alpha*speed[1])
            return speed            
        
        if (( your_position_x - balls[0][0])**2 + ( your_position_y - balls[0][1])**2   ) > 400:
            target = nextCircleCoordinate( your_position_x,your_position_y, balls[0][0], balls[0][1], False )
            speed = (target[0] - your_position_x, target[1] - your_position_y) 
            alpha = 10.0/max(abs(speed[0]),abs(speed[1]))
            speed = (alpha*speed[0], alpha*speed[1])
            return speed 
        else:
            return (0,0)
            
class P2:
        
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]

        
        return speed
                
class P3:
        
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        
        return speed

  
class P4:

    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        
        
        return speed              
