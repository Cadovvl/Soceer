# -*- coding: utf-8 -*-
"""
Created on Mon May 26 20:17:19 2014

@author: Helga Derz
"""

# Bukanova
# Kolkina
# Lahova


import random

#вратарь       
class P4:
    p_ball=None
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
#определяемся с воротами
        if side==0:
            ug=[lu[0],gate[0]-10]
            dg=[lu[0],gate[1]+10]
            c=20
        else:
            ug=[rb[0],gate[0]-10]
            dg=[rb[0],gate[1]+10]
            c=-20
#мяч
        ball=tuple([int(balls[0][0]), int(balls[0][1])])
#проверяем, стоит ли, где нужно        
        if your_team[index][0]==ug[0]+c:
            if self.p_ball==None or self.p_ball==ball or self.p_ball[0]==ball[0]:
                a=[0,0]
            else:
#определяем, проходит ли траектория через ворота
                k=(ball[1]-self.p_ball[1])/(ball[0]-self.p_ball[0])            
                b=ball[1]-k*ball[0]
#где будет мяч на линии ворот            
                my=ug[0]*k+b
#если может попасть в ворота
                if my<=dg[1] and my>=ug[1]:
                    ny=k*your_team[index][0]+b
                    a=[0, ny-your_team[index][1]+10]
                else:
                    a=[0,0]
        else:
            a=[ug[0]+c-your_team[index][0], (ug[1]+dg[1])/2-your_team[index][1]]
        if a==[0,0]:
            a=[ug[0]+c-your_team[index][0], (ug[1]+dg[1])/2-your_team[index][1]]
        self.p_ball=ball
        return tuple(a)
        
        
#по врагу
class P2:
    p_ball=None
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
#определяемся с прямоугольником вражеских ворот
        if side==0:
            lug=(rb[0]-100,gate[0])
            rbg=(rb[0],gate[1])
            c=-5
        else:
            lug=(lu[0],gate[0])
            rbg=(lu[0]+100,gate[1])
            c=5
#ищем врага
        eindex=0
        ex=enemy_team[0][0]
        for i in range(len(enemy_team)):
            if side==0:
                if enemy_team[i][0]<lug[0]:
                    if enemy_team[i][0]>ex: 
                        ex=enemy_team[i][0]
                        eindex=i
            if side==1:
                if enemy_team[i][0]>rbg[0]:
                    if enemy_team[i][0]<ex:
                        ex=enemy_team[i][0]
                        eindex=i
#подходим к нему сверху
        x=enemy_team[eindex][0]+c
        y=enemy_team[eindex][1]-100
        a=[x-your_team[index][0],y-your_team[index][1]]
#бьём
        if your_team[index][0]==enemy_team[eindex][0]+c:
            a=[0,10]
#насчет мяча
        ball=tuple([int(balls[0][0]), int(balls[0][1])])
        if self.p_ball!=None and self.p_ball!=ball and self.p_ball[0]!=ball[0]:    
            ball=tuple([int(balls[0][0]), int(balls[0][1])])
            k=(ball[1]-self.p_ball[1])/(ball[0]-self.p_ball[0])            
            b=ball[1]-k*ball[0]
    #где будет мяч на линии ворот            
            my=your_team[index][0]*k+b
    #если может попасть в ворота
            if my==your_team[index][1] and abs(ball[0]-your_team[index][0]<=50) and abs(ball[1]-your_team[index][1]<=50):
                a=[0,-10]
        self.p_ball=ball
        return tuple(a)
        
        
#защитник
class P3:
#1-для на нашей половине только один чужак (без мяча), 2-когда несколько (тогда берем ближнего), 3-когда один с мячом(без разницы, один он на нашей половине или нет), 4-когда на нашем прямоугольнике
    z1=None
    z2=None
    z3=None
    z4=None
    eindex=None
    p_enemy=None
    
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
#определяемся с прямоугольником ворот
    
        if side==0:
            lug=[lu[0],gate[0]-100]
            rbg=[lu[0]+100,gate[1]+100]
        else:
            lug=[rb[0]-100,gate[0]-100]
            rbg=[rb[0],gate[1]+100]
#мяч          
        ball=tuple([int(balls[0][0]), int(balls[0][1])])    
#ищем врага            
        lindex=[]
        for i in range(len(enemy_team)):
#1
#ищем тех, кто на нашей половине и добавляем в список lindex
            if side==1:
                if enemy_team[i][0]>=(rb[0]/2+lu[0]):
                    lindex.append(i)
                    self.z1=1
            else:
                if enemy_team[i][0]<=(rb[0]/2+lu[0]):
                    lindex.append(i)
                    self.z1=1
#на случай, если в списке более одного чужака
        if len(lindex)>1:
#2
#берем того, кто ближе к нашим воротам
            lt=[]
            for i in lindex:
                lt.append(enemy_team[i])
#ищем максимальную координату, если side=1
            if side==1:
                self.z2=1                    
                m=max(lt)
#и наоборот
            else:
                self.z2=1
                m=min(lt)
            self.eindex=lt.index(m)
#3
#на случай если появится чувак с мячом
            if abs(enemy_team[i][0]-ball[0])<=60 and abs(enemy_team[i][1]-ball[1])<=60:
                self.z3=1                
                self.eindex=i
#4
#если кто-то в нашем прямоугольнике                
            if enemy_team[i][0]<=rbg[0] and enemy_team[i][0]>=lug[0] and enemy_team[i][1]>=lug[1] and enemy_team[i][1]<=rbg[1]:
                self.eindex=i
                self.z4=1
#если он один в списке-его и добавляем
        elif lindex==[]:
            a=[0,0]
        elif len(lindex)==1 and abs(enemy_team[i][0]-ball[0])<=60 and abs(enemy_team[i][1]-ball[1])<=60:
            self.z3=1            
            self.eindex=i
        elif len(lindex)==1 and enemy_team[i][0]<=rbg[0] and enemy_team[i][0]>=lug[0] and enemy_team[i][1]>=lug[1] and enemy_team[i][1]<=rbg[1]:
                self.eindex=i
                self.z4=1
        else:
            self.z1=1
            self.eindex=lindex[0]

#после определения
        if self.z1==1 or self.z2==1 or self.z3==1:
            if self.p_enemy==None or (enemy_team[self.eindex][0]-self.p_enemy[0])==0:
                a=[0,0]
            else:
#определяем траекторию
                k=(enemy_team[self.eindex][1]-self.p_enemy[1])/(enemy_team[self.eindex][0]-self.p_enemy[0])
                b=enemy_team[self.eindex][1]-k*enemy_team[self.eindex][0]
#ЗДЕСЬ
#находим нашу точку и определяем скорость
#когда враг левее                
                if enemy_team[self.eindex][0]<your_team[index][0]:
                    if side==0:
                        x=enemy_team[self.eindex][0]
                        y=enemy_team[self.eindex][1]-50
                        a=[x-your_team[index][0]-10,y-your_team[index][1]]
                    else:
                        x=your_team[index][0]-10
                        y=k*x+b
                        a=[x-your_team[index][0],y-your_team[index][1]]
#иксы равные                        
                elif enemy_team[self.eindex][0]==your_team[index][0]:
                    if enemy_team[self.eindex][1]>your_team[index][1]:
                        a=[0,10]
                    else:
                        a=[0,-10]
#когда враг правее
                else:
                    if side==0:
                        x=your_team[index][0]+10
                        y=k*x+b
                        a=[x-your_team[index][0],y-your_team[index][1]]
                    else:
                        x=enemy_team[self.eindex][0]
                        y=enemy_team[self.eindex][1]-50
                        a=[x-your_team[index][0]+10,y-your_team[index][1]]

#когда нечего делать, возвращаемся на место
        if a==[0,0]:
            if side==0:
                a=[lu[0]+151-your_team[index][0], (gate[0]+(gate[1]-gate[0])/2)-your_team[index][1]]
            else:
                a=[rb[0]-151-your_team[index][0], (gate[0]+(gate[1]-gate[0])/2)-your_team[index][1]]
#конец  
        if self.eindex!=None:
            self.p_enemy=tuple([enemy_team[self.eindex][0], enemy_team[self.eindex][1]])
        self.z1=None
        self.z2=None
        self.z3=None
        self.z4=None
#чтоб не подходил к воротам
        if side==0:
            if (a[0]+your_team[index][0])<=(lu[0]+50):
                a=[0,0]
        if side==1:
            if (a[0]+your_team[index][0])>=(rb[0]-50):
                a=[0,0]
        return tuple(a)
        
#нападающий        
class P1:
    delta = 40
    ch = 1
    dir_k = [0,0]
    ready = 0
 
    def get_len(self, vec):
        return round(pow( (vec[0])*(vec[0]) + (vec[1])*(vec[1]), 0.5 ))
 
    def is_near_ball(self, ball_x, ball_y, i_x, i_y):
        if ( ( abs( i_x - ball_x ) < self.delta ) and ( abs( i_y - ball_y ) < self.delta ) ):
            return 6 * ( i_x - ball_x, i_y - ball_y )
        else:
            return (0, 0)
 
    def change_dir(self, enemy_gate_x, enemy_gate_y):
        r = random.randint(0, 1)
        if ( r == 0 ):
            self.dir_k[1] -= 40
        else:
            self.dir_k[1] += 40        
 
    def diagonal_speed(self, speed):
        if max(speed[0],speed[1]) >= 10:
            alpha = 10.0/max(abs(speed[0]),abs(speed[1]))
            speed = (alpha*speed[0], alpha*speed[1])        
        return speed
 
    def is_ready(self, side, i_x, i_y, ball_x, ball_y):
        a1 = ( ball_x - i_x, ball_y - i_y )
        b1 = ( self.dir_k[0] - ball_x, self.dir_k[1] - ball_y )
        c = ( self.dir_k[0] - i_x, self.dir_k[1] - i_y)
        if ( self.get_len(a1) + self.get_len(b1) == self.get_len(c) ):
            if ( ( side == 0 and i_x < ball_x ) or ( side == 1 and i_x > ball_x ) ):
                return True
            else:
                return False
        else:
            return False
 
    def is_close(self, side, ball_x, ball_y, enemy_team):
        for enemy in enemy_team:
            if ( self.is_ready( side, ball_x, ball_y, enemy[0], enemy[1] ) ):
                return True
        return False                
           
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
# вычисляем ситуацию
        kick_position = [-2, -2]
 
        ball_x = balls[0][0]
        ball_y = balls[0][1]
 
 
        if (side == 0):
            enemy_gate_x = rb[0]
            my_gate_x = lu[0]
            my_gate_y = 320
            delta_x = -self.delta
        else:
            enemy_gate_x = lu[0]
            my_gate_x = rb[0]
            my_gate_y = 320
            delta_x = self.delta
 
        if (ball_x == enemy_gate_x):
            return self.diagonal_speed( ( ball_x - i_x, ball_y - i_y ) )
 
        enemy_gate_y = (gate[0] + gate[1]) / 2.0
       
        i_x = your_team[index][0]
        i_y = your_team[index][1]
 
 
        self.dir_k[0] = enemy_gate_x
        self.dir_k[1] = enemy_gate_y
 
# если, нужно меняем направление удара
 
        while ( self.is_close( side, ball_x, ball_y, enemy_team ) ):
            self.change_dir(enemy_gate_x, enemy_gate_y)
 
# считаем позицию для удара
 
        a = abs(ball_y - self.dir_k[1])
        b = abs(rb[0] - ball_x)
 
        delta_y = round(abs(delta_x) * a  / b)
 
        kick_position[0] = ball_x + delta_x
        if ( ball_y <= self.dir_k[1] ):
            kick_position[1] = ball_y - delta_y
        else:
            kick_position[1] = ball_y + delta_y
 
# смотрим, готовы ли ударить
 
        if ( self.is_ready( side, i_x, i_y, ball_x, ball_y ) ):
            self.ready = 1
        else:
            self.ready = 0
 
        if ( self.ready == 0 ):
# подходим к позиции для удара, обходя мяч, если нужно
            self.ready = 1
            return self.diagonal_speed( (kick_position[0] - i_x, kick_position[1] - i_y) )
        else:
            return self.diagonal_speed( ( ball_x - i_x, ball_y - i_y ) )
