from __future__ import division
import random
import math
import scipy.linalg as slin


# Saldaeva
# Arakelan


#Algebra methods
def x(coords):
    return coords[0]

def y(coords):
    return coords[1]

def simplify(num):
    result = 0
    if num != 0:
        result = num / abs(num)
    return result

def distance(pa, pb, kind="xy"):
    result = 0
    if kind == 'x':
        result = abs(pb[0] - pa[0])
    elif kind == 'y':
        result = abs(pb[1] - pa[1])
    else:
        result = math.hypot(pb[0] - pa[0], pb[1] - pa[1])
    return result

def between(p_one, p_test, p_two, kind = "xy"):
    """
    return true if p_test is between p_one and p_two
    """
    r_x, r_y = False, False
    if 'x' in kind:
        r_x = x(p_one) >= x(p_test) >= x(p_two) or x(p_one) <= x(p_test) <= x(p_two)
    if 'y' in kind:
        r_y = y(p_one) >= y(p_test) >= y(p_two) or y(p_one) <= y(p_test) <= y(p_two)
    if 'x' == kind:
        return r_x
    elif 'y' == kind:
        return r_y
    return (r_x and r_y)
        
    

def points_on_line(pa, pb, pc):
    array = [[x(pa), y(pa), 1],
             [x(pb), y(pb), 1],
             [x(pc), y(pc), 1]]
    if slin.det(array) == 0:
        return True
    return False

#Directions calculating
def to(direction, step = 10):
    """
    to("left") - transforms written directions ("up", "Right", "SE") to (X,Y)
    returns direction
    """
    ld = direction.lower()
    ld = ld.split(" ")
    result = [0, 0]
    for each_d in ld:
        # Evaluate X coordinate
        if each_d in ["left", "w", "nw", "sw"]:
            result[0] = -step
        elif each_d in ["right", "e", "ne", "se"]:
            result[0] = step
        # Evaluate Y coordinate 
        if each_d in ["up", "n", "ne", "nw"]:
            result[1] = -step
        elif each_d in ["down", "s", "se", "sw"]:
            result[1] = step
    return tuple(result)

def to_point_from(pnt_to, pnt_from):
    """
    returns direction
    """
    rx = x(pnt_to) - x(pnt_from)
    ry = y(pnt_to) - y(pnt_from)
    result = (rx, ry)
    if max(rx, ry) >= 10:
        alpha = 10.0 / max(abs(rx), abs(ry))
        result = (alpha * rx, alpha * ry)
    return result

#Useful points calculation
def gates_center(lu, rb, gate, side):
    """
    returns point
    """
    result = [0, 0]
    if side == 0:
        result[0] = lu[0]
    else:
        result[0] = rb[0]
    result[1] = (gate[0] + gate[1]) / 2
    return tuple(result)

def defence_point(my_gates, ball, dist = 39.9):
    """
    returns point
    """
    alpha = dist
    beta = distance(my_gates, ball) - dist
    xr = (alpha * x(my_gates) + beta * x(ball)) / (alpha + beta)
    yr = (alpha * y(my_gates) + beta * y(ball)) / (alpha + beta)
    return (xr, yr)
    
def ofence_point(enemy_gates, ball, dist = 39.9):
    """
    returns point
    """
    dist_b_eg = distance(ball, enemy_gates)
    #print "ball gates dist: ", dist_b_eg
    alpha = (dist_b_eg + dist) / dist_b_eg
    #print "ball gates dist: ", dist_b_eg
    xr = alpha * x(ball) + (1-alpha) * x(enemy_gates)
    yr = alpha * y(ball) + (1-alpha) * y(enemy_gates)
    return (xr, yr)


#Football tactics methods
def is_in_defence(my_gates, my_pos, ball):
    return between(my_gates, my_pos, ball)

def is_point_on_side(point, lu, rb, side):
    center = ((x(rb) - x(lu)) / 2, (y(rb) - y(lu)) / 2)
    result = False
    if side == 0:
        result = between(lu, point, center,'x')
    elif side == 1:
        result = between(center, point, rb ,'x')
    return result
        
def safe_distance(pa, pb):
    result = 0
    if abs(y(pa) - y(pb)) < 5:
        result = 38
    else:
        result = 40
    return result        

#Classes declaration
class CommonLogic():
    _N, _NE, _NW = (0, -1), (1, -1), (-1, -1)
    _E = (1, 0)
    _S, _SE, _SW = (0, 1), (1, 1), (-1, 1)
    _W = (-1, 0)
    
    def __init__(self):
        self.pos = (0, 0)
        self.pos = None
        self.direct_queue = []
        pass
    
    def plan_move(self, the_move):
        self.direct_queue.append(the_move)
    
    def plan_fake(self, the_move):
        move_x = x(the_move)
        move_y = y(the_move)
        #Go back without fake
        if simplify(move_x) == -1:
            self.plan_move(the_move)
            return
        if simplify(move_y) == 0:
            move_xy = move_x / math.sqrt(2.0)
            if random.randint(0, 1) == 0:
                self.plan_move(to("up", move_xy))
                self.plan_move(to("down right", move_x))
            else:
                self.plan_move(to("down", move_xy))
                self.plan_move(to("up right", move_x))
        else:
            self.plan_move(to("right", move_y))
            self.plan_move((0, move_y))
            
    
class P3(CommonLogic):  

    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):
        if len(self.direct_queue) > 0 :
            return self.direct_queue.pop(0)
        self.pos = your_team[index]
        ball = balls[0]
        my_gates = gates_center(lu, rb, gate, side)
        enemy_side = 0
        if enemy_side == side:
            enemy_side = 1

        if not between(my_gates, self.pos, ball, 'x'):
            self.plan_move(to_point_from(my_gates, self.pos))
  
        elif is_point_on_side(ball, lu, rb, side):
            if distance(ball, self.pos) < 80:
                self.plan_move(to_point_from(ball, self.pos))
            else:
                dist = distance(my_gates, ball) / 2.0
                self.plan_move(to_point_from(defence_point(my_gates, ball, dist), self.pos))

        elif not is_point_on_side(ball, lu, rb, side):
            direct = to_point_from(ball, self.pos)
            self.plan_move((0,y(direct)))
        #1 do move
        return self.direct_queue.pop(0)


class P2(CommonLogic):

    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):
        if len(self.direct_queue) > 0 :
            return self.direct_queue.pop(0)
        self.pos = your_team[index]
        ball = balls[0]
        my_gates = gates_center(lu, rb, gate, side)
        enemy_side = 0
        if enemy_side == side:
            enemy_side = 1
        enemy_gates = gates_center(lu, rb, gate, enemy_side)

        # three new lines
        if distance(balls[0], gates_center(lu, rb, gate, side)) < 150:
            self.plan_move((0,0))
        else:
            if distance(self.pos, ball) < 25:
                self.plan_fake(to_point_from(enemy_gates, self.pos))
            elif not is_in_defence(my_gates, self.pos, ball):
                self.plan_move(to_point_from(defence_point(my_gates, ball), self.pos))
            else:
                self.plan_move(to_point_from(ball, self.pos))
            #1 do move
        return self.direct_queue.pop(0)


class P4(CommonLogic):
    go_up = False
    
    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):
        self.pos = your_team[index]
        my_x = x(self.pos)
        my_y = y(self.pos)
        ball_y = y(balls[0])
        ball = balls[0]
        my_gates = gates_center(lu, rb, gate, side)

        if distance(self.pos, my_gates, "x") > 25:
            go_to = to_point_from(my_gates, self.pos)
            my_x = x(go_to)
            my_y = y(go_to)
        else:
            if distance(ball, self.pos) < 20:
                my_x = (x(ball) - x(self.pos))
                my_y = (y(ball) - y(self.pos))
            else:
                if ball_y > gate[0] and ball_y < gate[1]:
                    my_x = 0
                    my_y = y(balls[0]) - my_y
                else:
                    my_pos_x = x(your_team[index])
                    my_pos_y = y(your_team[index])
                    
                    if ball_y > gate[0]:
                        if self.go_up:
                            (my_x, my_y) = (0, my_gates[1] - my_pos_y)
                        else:
                            (my_x, my_y) = (0, gate[1] - my_pos_y)
                        if (my_x, my_y) == (0, 0):
                            self.go_up = not self.go_up
                    elif ball_y < gate[1]:
                        if self.go_up:
                            (my_x, my_y) = (0, gate[0] - my_pos_y)
                        else:
                            (my_x, my_y) = (0, my_gates[1] - my_pos_y)
                        if (my_x, my_y) == (0, 0):
                            self.go_up = not self.go_up       
        return (my_x, my_y)


class P1(CommonLogic):

    def move(self, lu, rb, gate, index, side, balls, your_team, enemy_team):
        if len(self.direct_queue) >  0 :
            return self.direct_queue.pop(0)
        self.pos = your_team[index]
        ball = balls[0]
        enemy_side = 0
        if enemy_side == side:
            enemy_side = 1
        enemy_gates = gates_center(lu, rb, gate, enemy_side)
        op = ofence_point(enemy_gates, ball, safe_distance(self.pos, ball))

        #Three new line
        if distance(balls[0], gates_center(lu, rb, gate, side)) < 150:
            self.plan_move((0,0))
        else:
            #print "Distance to attack position:, ", distance(op, self.pos)
            if distance(op, self.pos) < 10:
                self.plan_move(to_point_from(ball, self.pos))
            else:
                self.plan_move(to_point_from(op, self.pos))
        return self.direct_queue.pop(0)

