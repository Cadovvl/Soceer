import random

# Krasnopolskaya
# Istomina

class P4:
    position = 0
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        my_x = your_team[index][0]
        my_y = your_team[index][1]
        ball_x = balls[0][0]
        ball_y = balls[0][1]

        if side == 0:
            if my_x > lu[0] + 20:
                target_x = lu[0]
                return (-10, 0)
            else:
                if ball_y > gate[0] and ball_y < gate[1]:
                    if (ball_x - my_x) < 30:
                        return (ball_x - my_x, ball_y - my_y)
                    return (0, ball_y - my_y)
                
                
                else:
                    if self.position == 0:
                        speed = (0, gate[1] - my_y)
                    else:
                        speed = (0, gate[0] - my_y)
                            
                    if speed == (0,0):
                        self.position = (self.position + 1) % 2
                    return speed
                
        elif side == 1:
            if my_x < rb[0] - 20:
                target_x = rb[0]
                return (10, 0)
            else:
                if ball_y > gate[0] and ball_y < gate[1]:
                    if (ball_x - my_x) < 30:
                        return (ball_x - my_x, ball_y - my_y)
                    return (0, ball_y - my_y)
                
                
                else:
                    if self.position == 0:
                        speed = (0, gate[1] - my_y)
                    else:
                        speed = (0, gate[0] - my_y)
                            
                    if speed == (0,0):
                        self.position = (self.position + 1) % 2
                    return speed


class P2:
    
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        my_x = your_team[index][0]
        my_y = your_team[index][1]
        ball_x = balls[0][0]
        ball_y = balls[0][1]
        if side == 0:
            if ball_x < lu[0] + 100:
                return (0,0)
            return (ball_x - my_x ,ball_y - my_y)
        
        elif side == 1:
            if ball_x > rb[0] - 100:
                return (0,0)
            return (ball_x - my_x ,ball_y - my_y)


class P1:
    position = 0
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        my_x = your_team[index][0]
        my_y = your_team[index][1]
        ball_x = balls[0][0]
        ball_y = balls[0][1]

        if side == 0:
            if my_x > lu[0] + 60:
                target_x = lu[0]
                return (-10, 0)
            
            else:
                if ball_y < (gate[0] + 200) and ball_y > (gate[1] - 200):
                    if (ball_x - my_x) < 40:
                        return (ball_x - my_x, ball_y - my_y)
                    return (0, ball_y - my_y)
                
                
                else:
                    if self.position == 0:
                        speed = (0, (gate[1] - 200) - my_y)
                    else:
                        speed = (0, (gate[0] + 200) - my_y)
                            
                    if speed == (0,0):
                        self.position = (self.position + 1) % 2
                    return speed
                
        elif side == 1:
            if my_x < rb[0] - 60:
                target_x = rb[0]
                return (10, 0)
            else:
                if ball_y < (gate[0] + 200) and ball_y > (gate[1] - 200):
                    if (ball_x - my_x) < 40:
                        return (ball_x - my_x, ball_y - my_y)
                    return (0, ball_y - my_y)
                
                
                else:
                    if self.position == 0:
                        speed = (0, (gate[1] - 200) - my_y)
                    else:
                        speed = (0, (gate[0] + 200) - my_y)
                            
                    if speed == (0,0):
                        self.position = (self.position + 1) % 2
                    return speed


class P3:
    a = (0,0)
    en = random.randint(0,2)
    
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):

        if self.en >= len(enemy_team):
            self.en = random.randint(0,len(enemy_team))
        gx = enemy_team[self.en][0]
        gy = enemy_team[self.en][1]

        return (gx - your_team[index][0], gy - your_team[index][1])

 
    




