# -*- coding: utf-8 -*-

# Nikishina
# Vunova

import math

def dist(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

class P1:
    ball_last_coord = [500,100]
    goal = None
    go_to = None
    obxod = None
    finish_straight = 0
    cant_touch_ball = 0
    kick = 0
    flag = None
    br = None
    _xx=0
    _yy=0
    en_sp = [(0,0),(0,0),(0,0),(0,0)]
    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):

        gx = lu[0]
        if side == 0:
            gx = rb[0]
        enemy_gate = [(gx,gate[0]),(gx,gate[1])]
        ball_speed = [balls[0][0] - self.ball_last_coord[0], balls[0][1] - self.ball_last_coord[1]]
        self.ball_last_coord = balls[0]

        if balls[0][0] + ball_speed[0] <= lu[0] and ball_speed[0] < 0 and balls[0][0] > gate[0] and balls[0][1] < gate[1] or balls[0][0] + ball_speed[0] >= rb[0] and ball_speed[0] > 0 and balls[0][0] > gate[0] and balls[0][1] < gate[1] :
            self.goal = None
            self.go_to = None
            self.obxod = None
            self.finish_straight = 0
            self.cant_touch_ball = 0
            self.kick = 0

        me = your_team[index]
        dist_to_ball_enemy = [dist(i,balls[0]) for i in enemy_team]
        dist_to_ball_friend = [dist(i,balls[0]) for i in your_team]

        if side==1:
            if ball_speed[0]<=0.5 and ball_speed[1]<=0.5:
                return (balls[0][0]-your_team[index][0],balls[0][1]-your_team[index][1])

        ball_belong_enemy = 0
        ball_belong_friend = 0
        ball_belong_me = 0

        ball = balls[0]

        kick_point_up = (enemy_gate[0][0]-450,enemy_gate[0][1]-100)
        kick_point_down = (enemy_gate[1][0]-450,enemy_gate[1][1]+50)

        if side == 1:
            kick_point_up = (enemy_gate[0][0]+450,enemy_gate[0][1]-100)
            kick_point_down = (enemy_gate[1][0]+450,enemy_gate[1][1]+100)

        if me == kick_point_down or me == kick_point_up:
            self.finish_straight = 1

        if min(dist_to_ball_friend) < min(dist_to_ball_enemy) and min(dist_to_ball_enemy) > 50:
            ball_belong_friend = 1
            if min(dist_to_ball_friend) == dist(me,balls[0]):
                ball_belong_friend = 0
                ball_belong_me = 1
        else:
            ball_belong_enemy = 1

        ind_min_fr = dist_to_ball_friend.index(min(dist_to_ball_friend))
        ind_min_en = dist_to_ball_enemy.index(min(dist_to_ball_enemy))



        if ball_belong_friend:
            if min(dist_to_ball_enemy) < 100:
                dist_to_en=[]
                for i in enemy_team:
                    dist_to_en.append(dist(i,your_team[index]))
                    self.enemy = dist_to_en.index(min(dist_to_en))
                    enemy_x = enemy_team[self.enemy][0]
                    enemy_y = enemy_team[self.enemy][1]

                    if dist(ball,enemy_team[0]) > dist(ball,enemy_team[1]):
                        min1 = dist(ball,enemy_team[1])
                        num_min1 = 1
                        min2 = dist(ball,enemy_team[0])
                        num_min2 = 0
                    else:
                        min1 = dist(ball,enemy_team[0])
                        num_min1 = 0
                        min2 = dist(ball,enemy_team[1])
                        num_min2 = 1

                    for i in range(0,3,1):
                        en_dist = dist(ball,enemy_team[i])
                        if en_dist < min1 and en_dist < min2:
                            min2 = min1
                            num_min2 = num_min1
                            min1 = en_dist
                            num_min1 = i
                        elif min1 < en_dist < min2:
                            min2 = en_dist
                            num_min2 = i

                    he_has_ball = 1
                    his_dist_to_ball = dist(ball,your_team[1])

                    for i in range(2, 3, 1):
                        fr_dist = dist(ball,your_team[i])
                        if fr_dist < his_dist_to_ball:
                            he_has_ball = i
                            his_dist_to_ball = fr_dist

                    for i in range(1, 3, 1):
                        if i != he_has_ball:
                            if dist(enemy_team[num_min1], me) < dist(enemy_team[num_min1], me):
                                speed = (enemy_team[num_min1][0] - me[0], enemy_team[num_min1][1]-me[1])
                            else:
                                speed = (enemy_team[num_min1][0] - me[0], enemy_team[num_min1][1]-me[1])
                    if max(abs(speed[0]), abs(speed[1])) >= 10:
                        alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                        speed = (alpha * speed[0], alpha * speed[1])

                    return speed
            else:
                return (0,0)
                speed = (ball[0]+200-me[0],ball[1]-me[1])
                if max(abs(speed[0]), abs(speed[1])) >= 10:
                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                    speed = (alpha * speed[0], alpha * speed[1])

                return speed

        if ball_belong_enemy:
            try:
                for i in your_team:
                    if dist(balls[0], your_team[index]) <= dist(balls[0], i):
                        self.index_fight = index
                        speed = (balls[0][0]-me[0], balls[0][1]-me[1])
                        break

                    x1 = your_team[self.index_fight][0]
                    y1 = your_team[self.index_fight][1]
                    x2 = enemy_team[ind_min_en][0]
                    y2 = enemy_team[ind_min_en][1]
                    x0 = ball[0]
                    y0 = ball[1]

                    if x0 <= x2 and x0 >= x1 and y0 <= y2 + 20 and y0 >= y1-20:
                        for friend in your_team:
                            if dist(your_team[self.index_fight],your_team[index]) <= dist(your_team[self.index_fight],friend):
                                x1 = your_team[self.index_fight][0]
                                y1 = your_team[self.index_fight][1]
                                x2 = enemy_team[ind_min_en][0]
                                y2 = enemy_team[ind_min_en][1]
                                x0 = ball[0]
                                y0 = ball[1]
                                xe = enemy_team[self.enemy][0]
                                ye = enemy_team[self.enemy][1]
                                a = x1-xe
                                b = y1-ye


                                if b!=0:
                                    _y = (a*b*(x1-x0)+a*a*y0+b*b*y1)/(a*a+b*b)
                                    _x = (a*_y-a*y0+b*x0)/b

                                else:
                                    return self.br

                                speed = (_x-me[0],_y-me[1])

                                if max(abs(speed[0]), abs(speed[1])) >= 10:
                                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                                    speed = (alpha * speed[0], alpha * speed[1])
            except:
                speed = (ball[0]-me[0],ball[1]-me[1])


            if max(abs(speed[0]), abs(speed[1])) >= 10:
                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                    speed = (alpha * speed[0], alpha * speed[1])
            self.br = speed
            return speed

        if ball_belong_me:

            vect_up = (kick_point_up[0]-ball[0],kick_point_up[1]-ball[1])
            vect_down = (kick_point_down[0]-ball[0],kick_point_down[1]-ball[1])

            count_up = 0
            count_down = 0


            for enemy in enemy_team:
                if (enemy[0] >= me[0] and side == 0 or enemy[1] <= me[0] and side == 1) and enemy != enemy_team[0]:
                    a = vect_up[0]
                    b = vect_up[1]
                    c = vect_down[0]
                    d = vect_down[1]
                    x0 = ball[0]
                    y0 = ball[1]
                    x1 = kick_point_up[0]
                    x2 = kick_point_down[0]
                    y1 = kick_point_up[1]
                    y2 = kick_point_down[1]
                    xe = enemy[0]
                    ye = enemy[1]

                    if a == 0:
                        result_y_up = ye
                    else:
                        result_y_up = (a*b*xe+b*b*ye-a*b*x1+a*a*y1)/(a*a+b*b)

                    if b == 0:
                        result_x_up = xe
                    else:
                        result_x_up = (b*x1-a*y1+a*result_y_up)/b

                    if d == 0:
                        result_y_down = ye
                    else:
                        result_y_down = (c*d*xe+d*d*ye-c*d*x2+c*c*y2)/(c*c+d*d)

                    if c == 0:
                        result_x_down = xe
                    else:
                        result_x_down = (d*x2-c*y2+c*result_y_down)/d


                    if dist(enemy,(result_x_down,result_y_down)) < dist(enemy,(result_x_up,result_y_up)):
                        count_down+=1
                    elif dist(enemy,(result_x_down,result_y_down)) == dist(enemy,(result_x_up,result_y_up)):
                        count_up+=1
                        count_down+=1
                    elif dist(enemy,(result_x_down,result_y_down)) > dist(enemy,(result_x_up,result_y_up)):
                        count_up+=1

            if self.goal == None:
                if count_up > count_down:
                    self.goal = kick_point_up
                else:
                    self.goal = kick_point_down

            #Код движения нападающего
            x0 = ball[0]
            y0 = ball[1]
            x1 = self.goal[0]
            y1 = self.goal[1]

            alpha = 60/math.sqrt((x0-x1)**2+(y0-y1)**2)
            _x = alpha*(x0-x1)+x0
            _y = alpha*(y0-y1)+y0

            cant_touch_ball_x = alpha*(y0-y1)+x0
            cant_touch_ball_y = alpha*(x1-x0)+y0


            if dist(me, (cant_touch_ball_x, cant_touch_ball_y)) > dist(me, (alpha*(y1-y0)+x0, alpha*(x0-x1)+y0)):
                cant_touch_ball_x = alpha*(y1-y0)+x0
                cant_touch_ball_y = alpha*(x0-x1)+y0

            a = x1 - x0
            b = y0 - y1

            if self.goal[1] < ball[1]:
                if me[1]+10 < (a/b)*me[0]-(a/b)*x0+y0:
                    self.cant_touch_ball = 0
            else:
                if me[1]-10 > (a/b)*me[0]-(a/b)*x0+y0:
                    self.cant_touch_ball = 0


            if self.cant_touch_ball == 0:
                self.go_to = (cant_touch_ball_x, cant_touch_ball_y)
            if self.cant_touch_ball == 1:
               self.go_to = (_x, _y)
            if self.cant_touch_ball == 2:
                self.go_to = self.goal
            if self.cant_touch_ball == 3:
                if self.goal == kick_point_down:
                    self.goal = (enemy_gate[0][0],enemy_gate[0][1]+60)
                    self.kick = 1
                    self.cant_touch_ball = 1
                elif self.goal == kick_point_up:
                    self.goal = (enemy_gate[1][0],enemy_gate[1][1]-60)
                    self.kick = 1
                    self.cant_touch_ball = 1

            if dist(me,self.go_to) < 30 and self.cant_touch_ball in [0,1] or dist(ball,self.go_to) < 30 and self.cant_touch_ball in [2,3] :
                self.cant_touch_ball += 1
                if self.cant_touch_ball > 3:
                    self.cant_touch_ball = 3

            speed = (self.go_to[0] - me[0], self.go_to[1]-me[1])

            """
            if me[0] == lu[0] and speed[0] < 0 or me[0] == rb[0] and speed[0] > 0 or me[1] == lu[1] and speed[1] < 0  or me[1] == rb[1]and speed[1] > 0:
                self.goal = None
                self.go_to = None
                self.flag = None
                self.obxod = None
                self.finish_straight = 0
                self.cant_touch_ball = 1
                self.kick = 0
                speed = (ball[0]-me[0],ball[1]-me[1])
            """
            if max(abs(speed[0]), abs(speed[1])) >= 10:
                alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                speed = (alpha * speed[0], alpha * speed[1])


            return speed

class P2:
    ball_last_coord = [500,100]
    goal = None
    go_to = None
    obxod = None
    finish_straight = 0
    cant_touch_ball = 0
    kick = 0
    flag = None
    br = None
    _xx=0
    _yy=0
    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):

        gx = lu[0]
        if side == 0:
            gx = rb[0]
        enemy_gate = [(gx,gate[0]),(gx,gate[1])]
        ball_speed = [balls[0][0] - self.ball_last_coord[0], balls[0][1] - self.ball_last_coord[1]]
        self.ball_last_coord = balls[0]

        if balls[0][0] + ball_speed[0] <= lu[0] and ball_speed[0] < 0 and balls[0][0] > gate[0] and balls[0][1] < gate[1] or balls[0][0] + ball_speed[0] >= rb[0] and ball_speed[0] > 0 and balls[0][0] > gate[0] and balls[0][1] < gate[1] :
            self.goal = None
            self.go_to = None
            self.obxod = None
            self.finish_straight = 0
            self.cant_touch_ball = 0
            self.kick = 0

        me = your_team[index]
        dist_to_ball_enemy = [dist(i,balls[0]) for i in enemy_team]
        dist_to_ball_friend = [dist(i,balls[0]) for i in your_team]
        alldist = []
        for i in your_team:
            curr_dist = []
            for j in enemy_team:
                curr_dist.append(dist(i,j))
            alldist.append(curr_dist)

        ball_belong_enemy = 0
        ball_belong_friend = 0
        ball_belong_me = 0

        ball = balls[0]

        kick_point_up = (enemy_gate[0][0]-450,enemy_gate[0][1]-100)
        kick_point_down = (enemy_gate[1][0]-450,enemy_gate[1][1]+50)

        if side == 1:
            kick_point_up = (enemy_gate[0][0]+450,enemy_gate[0][1]-100)
            kick_point_down = (enemy_gate[1][0]+450,enemy_gate[1][1]+100)

        if me == kick_point_down or me == kick_point_up:
            self.finish_straight = 1

        if min(dist_to_ball_friend) < min(dist_to_ball_enemy) and min(dist_to_ball_enemy) > 50:
            ball_belong_friend = 1
            if min(dist_to_ball_friend) == dist(me,balls[0]):
                ball_belong_friend = 0
                ball_belong_me = 1
        else:
            ball_belong_enemy = 1

        ind_min_fr = dist_to_ball_friend.index(min(dist_to_ball_friend))
        ind_min_en = dist_to_ball_enemy.index(min(dist_to_ball_enemy))

        if ball_belong_friend:
            if min(dist_to_ball_enemy) < 100:
                dist_to_en=[]
                for i in enemy_team:
                    dist_to_en.append(dist(i,your_team[index]))
                    self.enemy=dist_to_en.index(min(dist_to_en))
                    enemy_x = enemy_team[self.enemy][0]
                    enemy_y = enemy_team[self.enemy][1]

                    if dist(ball,enemy_team[0]) > dist(ball,enemy_team[1]):
                        min1 = dist(ball,enemy_team[1])
                        num_min1 = 1
                        min2 = dist(ball,enemy_team[0])
                        num_min2 = 0
                    else:
                        min1 = dist(ball,enemy_team[0])
                        num_min1 = 0
                        min2 = dist(ball,enemy_team[1])
                        num_min2 = 1

                    for i in range(0,3,1):
                        en_dist = dist(ball,enemy_team[i])
                        if en_dist < min1 and en_dist < min2:
                            min2 = min1
                            num_min2 = num_min1
                            min1 = en_dist
                            num_min1 = i
                        elif min1 < en_dist < min2:
                            min2 = en_dist
                            num_min2 = i

                    he_has_ball = 1
                    his_dist_to_ball = dist(ball,your_team[1])

                    for i in range(2, 3, 1):
                        fr_dist = dist(ball,your_team[i])
                        if fr_dist < his_dist_to_ball:
                            he_has_ball = i
                            his_dist_to_ball = fr_dist

                    for i in range(1, 3, 1):
                        if i != he_has_ball:
                            if dist(enemy_team[num_min1], me) < dist(enemy_team[num_min1], me):
                                speed = (enemy_team[num_min1][0] - me[0], enemy_team[num_min1][1]-me[1])
                            else:
                                speed = (enemy_team[num_min1][0] - me[0], enemy_team[num_min1][1]-me[1])
                    if max(abs(speed[0]), abs(speed[1])) >= 10:
                        alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                        speed = (alpha * speed[0], alpha * speed[1])

                    return speed
            else:
                return (0,0)
                speed = (ball[0]+200-me[0],ball[1]-me[1])

                if max(abs(speed[0]), abs(speed[1])) >= 10:
                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                    speed = (alpha * speed[0], alpha * speed[1])

                return speed

        if ball_belong_enemy:
            try:
                for i in your_team:
                    if dist(balls[0], your_team[index]) <= dist(balls[0], i):
                        self.index_fight = index
                        speed = (balls[0][0]-me[0], balls[0][1]-me[1])
                        break

                    x1 = your_team[self.index_fight][0]
                    y1 = your_team[self.index_fight][1]
                    x2 = enemy_team[ind_min_en][0]
                    y2 = enemy_team[ind_min_en][1]
                    x0 = ball[0]
                    y0 = ball[1]

                    if x0 <= x2 and x0 >= x1 and y0 <= y2 + 20 and y0 >= y1-20:
                        for friend in your_team:
                            if dist(your_team[self.index_fight],your_team[index]) <= dist(your_team[self.index_fight],friend):
                                x1 = your_team[self.index_fight][0]
                                y1 = your_team[self.index_fight][1]
                                x2 = enemy_team[ind_min_en][0]
                                y2 = enemy_team[ind_min_en][1]
                                x0 = ball[0]
                                y0 = ball[1]
                                xe = enemy_team[self.enemy][0]
                                ye = enemy_team[self.enemy][1]
                                a = x1-xe
                                b = y1-ye


                                if b!=0:
                                    _y = (a*b*(x1-x0)+a*a*y0+b*b*y1)/(a*a+b*b)
                                    _x = (a*_y-a*y0+b*x0)/b

                                else:
                                    return self.br

                                speed = (_x-me[0],_y-me[1])

                                if max(abs(speed[0]), abs(speed[1])) >= 10:
                                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                                    speed = (alpha * speed[0], alpha * speed[1])
            except:
                speed = (ball[0]-me[0],ball[1]-me[1])


            if max(abs(speed[0]), abs(speed[1])) >= 10:
                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                    speed = (alpha * speed[0], alpha * speed[1])
            self.br = speed
            return speed

        if ball_belong_me:

            vect_up = (kick_point_up[0]-ball[0],kick_point_up[1]-ball[1])
            vect_down = (kick_point_down[0]-ball[0],kick_point_down[1]-ball[1])

            count_up = 0
            count_down = 0


            for enemy in enemy_team:
                if (enemy[0] >= me[0] and side == 0 or enemy[1] <= me[0] and side == 1) and enemy != enemy_team[0]:
                    a = vect_up[0]
                    b = vect_up[1]
                    c = vect_down[0]
                    d = vect_down[1]
                    x0 = ball[0]
                    y0 = ball[1]
                    x1 = kick_point_up[0]
                    x2 = kick_point_down[0]
                    y1 = kick_point_up[1]
                    y2 = kick_point_down[1]
                    xe = enemy[0]
                    ye = enemy[1]

                    if a == 0:
                        result_y_up = ye
                    else:
                        result_y_up = (a*b*xe+b*b*ye-a*b*x1+a*a*y1)/(a*a+b*b)

                    if b == 0:
                        result_x_up = xe
                    else:
                        result_x_up = (b*x1-a*y1+a*result_y_up)/b

                    if d == 0:
                        result_y_down = ye
                    else:
                        result_y_down = (c*d*xe+d*d*ye-c*d*x2+c*c*y2)/(c*c+d*d)

                    if c == 0:
                        result_x_down = xe
                    else:
                        result_x_down = (d*x2-c*y2+c*result_y_down)/d


                    if dist(enemy,(result_x_down,result_y_down)) < dist(enemy,(result_x_up,result_y_up)):
                        count_down+=1
                    elif dist(enemy,(result_x_down,result_y_down)) == dist(enemy,(result_x_up,result_y_up)):
                        count_up+=1
                        count_down+=1
                    elif dist(enemy,(result_x_down,result_y_down)) > dist(enemy,(result_x_up,result_y_up)):
                        count_up+=1

            if self.goal == None:
                if count_up > count_down:
                    self.goal = kick_point_up
                else:
                    self.goal = kick_point_down

            #Код движения нападающего
            x0 = ball[0]
            y0 = ball[1]
            x1 = self.goal[0]
            y1 = self.goal[1]

            alpha = 60/math.sqrt((x0-x1)**2+(y0-y1)**2)
            _x = alpha*(x0-x1)+x0
            _y = alpha*(y0-y1)+y0

            cant_touch_ball_x = alpha*(y0-y1)+x0
            cant_touch_ball_y = alpha*(x1-x0)+y0


            if dist(me, (cant_touch_ball_x, cant_touch_ball_y)) > dist(me, (alpha*(y1-y0)+x0, alpha*(x0-x1)+y0)):
                cant_touch_ball_x = alpha*(y1-y0)+x0
                cant_touch_ball_y = alpha*(x0-x1)+y0

            a = x1 - x0
            b = y0 - y1

            if self.goal[1] < ball[1]:
                if me[1]+10 < (a/b)*me[0]-(a/b)*x0+y0:
                    self.cant_touch_ball = 0
            else:
                if me[1]-10 > (a/b)*me[0]-(a/b)*x0+y0:
                    self.cant_touch_ball = 0


            if self.cant_touch_ball == 0:
                self.go_to = (cant_touch_ball_x, cant_touch_ball_y)
            if self.cant_touch_ball == 1:
               self.go_to = (_x, _y)
            if self.cant_touch_ball == 2:
                self.go_to = self.goal
            if self.cant_touch_ball == 3:
                if self.goal == kick_point_down:
                    self.goal = (enemy_gate[0][0],enemy_gate[0][1]+60)
                    self.kick = 1
                    self.cant_touch_ball = 1
                elif self.goal == kick_point_up:
                    self.goal = (enemy_gate[1][0],enemy_gate[1][1]-60)
                    self.kick = 1
                    self.cant_touch_ball = 1

            if dist(me,self.go_to) < 30 and self.cant_touch_ball in [0,1] or dist(ball,self.go_to) < 30 and self.cant_touch_ball in [2,3] :
                self.cant_touch_ball += 1
                if self.cant_touch_ball > 3:
                    self.cant_touch_ball = 3

            speed = (self.go_to[0] - me[0], self.go_to[1]-me[1])

            """
            if me[0] == lu[0] and speed[0] < 0 or me[0] == rb[0] and speed[0] > 0 or me[1] == lu[1] and speed[1] < 0  or me[1] == rb[1]and speed[1] > 0:
                self.goal = None
                self.go_to = None
                self.flag = None
                self.obxod = None
                self.finish_straight = 0
                self.cant_touch_ball = 1
                self.kick = 0
                speed = (ball[0]-me[0],ball[1]-me[1])
            """
            if max(abs(speed[0]), abs(speed[1])) >= 10:
                alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                speed = (alpha * speed[0], alpha * speed[1])


            return speed


class P3:
    ball_last_coord = [500,100]
    goal = None
    go_to = None
    obxod = None
    finish_straight = 0
    cant_touch_ball = 0
    kick = 0
    flag = None
    br = None
    _xx=0
    _yy=0
    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):

        gx = lu[0]
        if side == 0:
            gx = rb[0]
        enemy_gate = [(gx,gate[0]),(gx,gate[1])]
        ball_speed = [balls[0][0] - self.ball_last_coord[0], balls[0][1] - self.ball_last_coord[1]]
        self.ball_last_coord = balls[0]

        if balls[0][0] + ball_speed[0] <= lu[0] and ball_speed[0] < 0 and balls[0][0] > gate[0] and balls[0][1] < gate[1] or balls[0][0] + ball_speed[0] >= rb[0] and ball_speed[0] > 0 and balls[0][0] > gate[0] and balls[0][1] < gate[1] :
            self.goal = None
            self.go_to = None
            self.obxod = None
            self.finish_straight = 0
            self.cant_touch_ball = 0
            self.kick = 0

        me = your_team[index]
        dist_to_ball_enemy = [dist(i,balls[0]) for i in enemy_team]
        dist_to_ball_friend = [dist(i,balls[0]) for i in your_team]
        alldist = []
        for i in your_team:
            curr_dist = []
            for j in enemy_team:
                curr_dist.append(dist(i,j))
            alldist.append(curr_dist)

        ball_belong_enemy = 0
        ball_belong_friend = 0
        ball_belong_me = 0

        ball = balls[0]

        kick_point_up = (enemy_gate[0][0]-450,enemy_gate[0][1]-100)
        kick_point_down = (enemy_gate[1][0]-450,enemy_gate[1][1]+50)

        if side == 1:
            kick_point_up = (enemy_gate[0][0]+450,enemy_gate[0][1]-100)
            kick_point_down = (enemy_gate[1][0]+450,enemy_gate[1][1]+100)

        if me == kick_point_down or me == kick_point_up:
            self.finish_straight = 1

        if min(dist_to_ball_friend) < min(dist_to_ball_enemy) and min(dist_to_ball_enemy) > 50:
            ball_belong_friend = 1
            if min(dist_to_ball_friend) == dist(me,balls[0]):
                ball_belong_friend = 0
                ball_belong_me = 1
        else:
            ball_belong_enemy = 1

        ind_min_fr = dist_to_ball_friend.index(min(dist_to_ball_friend))
        ind_min_en = dist_to_ball_enemy.index(min(dist_to_ball_enemy))

        if ball_belong_friend:
            if min(dist_to_ball_enemy) < 100:
                dist_to_en=[]
                for i in enemy_team:
                    dist_to_en.append(dist(i,your_team[index]))
                    self.enemy=dist_to_en.index(min(dist_to_en))
                    enemy_x = enemy_team[self.enemy][0]
                    enemy_y = enemy_team[self.enemy][1]


                    if dist(ball,enemy_team[0]) > dist(ball,enemy_team[1]):
                        min1 = dist(ball,enemy_team[1])
                        num_min1 = 1
                        min2 = dist(ball,enemy_team[0])
                        num_min2 = 0
                    else:
                        min1 = dist(ball,enemy_team[0])
                        num_min1 = 0
                        min2 = dist(ball,enemy_team[1])
                        num_min2 = 1

                    for i in range(0,3,1):
                        en_dist = dist(ball,enemy_team[i])
                        if en_dist < min1 and en_dist < min2:
                            min2 = min1
                            num_min2 = num_min1
                            min1 = en_dist
                            num_min1 = i
                        elif min1 < en_dist < min2:
                            min2 = en_dist
                            num_min2 = i

                    he_has_ball = 1
                    his_dist_to_ball = dist(ball,your_team[1])

                    for i in range(2, 3, 1):
                        fr_dist = dist(ball,your_team[i])
                        if fr_dist < his_dist_to_ball:
                            he_has_ball = i
                            his_dist_to_ball = fr_dist

                    for i in range(1, 3, 1):
                        if i != he_has_ball:
                            if dist(enemy_team[num_min1], me) < dist(enemy_team[num_min1], me):
                                speed = (enemy_team[num_min1][0] - me[0], enemy_team[num_min1][1]-me[1])
                            else:
                                speed = (enemy_team[num_min1][0] - me[0], enemy_team[num_min1][1]-me[1])
                    if max(abs(speed[0]), abs(speed[1])) >= 10:
                        alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                        speed = (alpha * speed[0], alpha * speed[1])

                    return speed
            else:
                speed = (ball[0]+200-me[0],ball[1]-me[1])
                return (0,0)
                if max(abs(speed[0]), abs(speed[1])) >= 10:
                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                    speed = (alpha * speed[0], alpha * speed[1])

                return speed

        if ball_belong_enemy:
            try:
                for i in your_team:
                    if dist(balls[0], your_team[index]) <= dist(balls[0], i):
                        self.index_fight = index
                        speed = (balls[0][0]-me[0], balls[0][1]-me[1])
                        break

                    x1 = your_team[self.index_fight][0]
                    y1 = your_team[self.index_fight][1]
                    x2 = enemy_team[ind_min_en][0]
                    y2 = enemy_team[ind_min_en][1]
                    x0 = ball[0]
                    y0 = ball[1]

                    if x0 <= x2 and x0 >= x1 and y0 <= y2 + 20 and y0 >= y1-20:
                        for friend in your_team:
                            if dist(your_team[self.index_fight],your_team[index]) <= dist(your_team[self.index_fight],friend):
                                x1 = your_team[self.index_fight][0]
                                y1 = your_team[self.index_fight][1]
                                x2 = enemy_team[ind_min_en][0]
                                y2 = enemy_team[ind_min_en][1]
                                x0 = ball[0]
                                y0 = ball[1]
                                xe = enemy_team[self.enemy][0]
                                ye = enemy_team[self.enemy][1]
                                a = x1-xe
                                b = y1-ye


                                if b!=0:
                                    _y = (a*b*(x1-x0)+a*a*y0+b*b*y1)/(a*a+b*b)
                                    _x = (a*_y-a*y0+b*x0)/b

                                else:
                                    return self.br

                                speed = (_x-me[0],_y-me[1])

                                if max(abs(speed[0]), abs(speed[1])) >= 10:
                                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                                    speed = (alpha * speed[0], alpha * speed[1])
            except:
                speed = (ball[0]-me[0],ball[1]-me[1])


            if max(abs(speed[0]), abs(speed[1])) >= 10:
                    alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                    speed = (alpha * speed[0], alpha * speed[1])
            self.br = speed
            return speed

        if ball_belong_me:

            vect_up = (kick_point_up[0]-ball[0],kick_point_up[1]-ball[1])
            vect_down = (kick_point_down[0]-ball[0],kick_point_down[1]-ball[1])

            count_up = 0
            count_down = 0


            for enemy in enemy_team:
                if (enemy[0] >= me[0] and side == 0 or enemy[1] <= me[0] and side == 1) and enemy != enemy_team[0]:
                    a = vect_up[0]
                    b = vect_up[1]
                    c = vect_down[0]
                    d = vect_down[1]
                    x0 = ball[0]
                    y0 = ball[1]
                    x1 = kick_point_up[0]
                    x2 = kick_point_down[0]
                    y1 = kick_point_up[1]
                    y2 = kick_point_down[1]
                    xe = enemy[0]
                    ye = enemy[1]

                    if a == 0:
                        result_y_up = ye
                    else:
                        result_y_up = (a*b*xe+b*b*ye-a*b*x1+a*a*y1)/(a*a+b*b)

                    if b == 0:
                        result_x_up = xe
                    else:
                        result_x_up = (b*x1-a*y1+a*result_y_up)/b

                    if d == 0:
                        result_y_down = ye
                    else:
                        result_y_down = (c*d*xe+d*d*ye-c*d*x2+c*c*y2)/(c*c+d*d)

                    if c == 0:
                        result_x_down = xe
                    else:
                        result_x_down = (d*x2-c*y2+c*result_y_down)/d


                    if dist(enemy,(result_x_down,result_y_down)) < dist(enemy,(result_x_up,result_y_up)):
                        count_down+=1
                    elif dist(enemy,(result_x_down,result_y_down)) == dist(enemy,(result_x_up,result_y_up)):
                        count_up+=1
                        count_down+=1
                    elif dist(enemy,(result_x_down,result_y_down)) > dist(enemy,(result_x_up,result_y_up)):
                        count_up+=1

            if self.goal == None:
                if count_up > count_down:
                    self.goal = kick_point_up
                else:
                    self.goal = kick_point_down

            #Код движения нападающего
            x0 = ball[0]
            y0 = ball[1]
            x1 = self.goal[0]
            y1 = self.goal[1]

            alpha = 60/math.sqrt((x0-x1)**2+(y0-y1)**2)
            _x = alpha*(x0-x1)+x0
            _y = alpha*(y0-y1)+y0

            cant_touch_ball_x = alpha*(y0-y1)+x0
            cant_touch_ball_y = alpha*(x1-x0)+y0


            if dist(me, (cant_touch_ball_x, cant_touch_ball_y)) > dist(me, (alpha*(y1-y0)+x0, alpha*(x0-x1)+y0)):
                cant_touch_ball_x = alpha*(y1-y0)+x0
                cant_touch_ball_y = alpha*(x0-x1)+y0

            a = x1 - x0
            b = y0 - y1

            if self.goal[1] < ball[1]:
                if me[1]+10 < (a/b)*me[0]-(a/b)*x0+y0:
                    self.cant_touch_ball = 0
            else:
                if me[1]-10 > (a/b)*me[0]-(a/b)*x0+y0:
                    self.cant_touch_ball = 0


            if self.cant_touch_ball == 0:
                self.go_to = (cant_touch_ball_x, cant_touch_ball_y)
            if self.cant_touch_ball == 1:
               self.go_to = (_x, _y)
            if self.cant_touch_ball == 2:
                self.go_to = self.goal
            if self.cant_touch_ball == 3:
                if self.goal == kick_point_down:
                    self.goal = (enemy_gate[0][0],enemy_gate[0][1]+60)
                    self.kick = 1
                    self.cant_touch_ball = 1
                elif self.goal == kick_point_up:
                    self.goal = (enemy_gate[1][0],enemy_gate[1][1]-60)
                    self.kick = 1
                    self.cant_touch_ball = 1

            if dist(me,self.go_to) < 30 and self.cant_touch_ball in [0,1] or dist(ball,self.go_to) < 30 and self.cant_touch_ball in [2,3] :
                self.cant_touch_ball += 1
                if self.cant_touch_ball > 3:
                    self.cant_touch_ball = 3

            speed = (self.go_to[0] - me[0], self.go_to[1]-me[1])

            """
            if me[0] == lu[0] and speed[0] < 0 or me[0] == rb[0] and speed[0] > 0 or me[1] == lu[1] and speed[1] < 0  or me[1] == rb[1]and speed[1] > 0:
                self.goal = None
                self.go_to = None
                self.flag = None
                self.obxod = None
                self.finish_straight = 0
                self.cant_touch_ball = 1
                self.kick = 0
                speed = (ball[0]-me[0],ball[1]-me[1])
            """
            if max(abs(speed[0]), abs(speed[1])) >= 10:
                alpha = 10 / max(abs(speed[0]), abs(speed[1]))
                speed = (alpha * speed[0], alpha * speed[1])


            return speed

class P4:
    ball_last_coord = [500,100]
    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):
        gx = lu[0]
        if side == 1:
            gx = rb[0]
        ball_speed = [balls[0][0] - self.ball_last_coord[0], balls[0][1] - self.ball_last_coord[1]]
        self.ball_last_coord = balls[0]
        try:
            x0 = balls[0][0]
            y0 = balls[0][1]
            me = your_team[index]
            c = ball_speed[0]
            d = ball_speed[1]
            if side == 0:
                x = lu[0]+25
            else:
                x = rb[0]-25
            if c != 0:
                y = d * (x - x0) / c + y0
            else:
                if y0 >= gate[0] and y0 <= gate[1]:
                    speed = (x - me[0], y0 - me[1])
                elif y0 < gate[0]:
                    speed = (x - me[0], gate[0] - me[1])
                elif y0 > gate[1]:
                    speed = (x - me[0], gate[1] - me[1])
            yzap = 0
            if c == 0 and d == 0:
                if y0 >= gate[0] and y0 <= gate[1]:
                    speed = (x - me[0], y0 - me[1])
                elif y0 < gate[0]:
                    speed = (x - me[0], gate[0] - me[1])
                elif y0 > gate[1]:
                    speed = (x - me[0], gate[1] - me[1])

            if y >= gate[0] and y <= gate[1]:
                speed = (x - me[0], y - me[1])
            else:
                if y0 >= gate[0] and y0 <= gate[1]:
                    speed = (x - me[0], y0 - me[1])
                elif y0 < gate[0]:
                    speed = (x - me[0], gate[0] - me[1])
                elif y0 > gate[1]:
                    speed = (x - me[0], gate[1] - me[1])
        except:
            speed = (x-me[0],(gate[0]+gate[1])/2-me[1])
        return speed
