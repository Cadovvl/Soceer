import math

# Matveeva
# Gladkih
# Kadaev

class P1:
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = balls[0][0]
        gy = balls[0][1]
        ball=tuple([int(gx-your_team[index][0]), int(gy-your_team[index][1])])
        if side==0:
            g1=[rb[0], gate[0]]
            g2=[rb[0], gate[1]]
        else:
            g1=[lu[0],gate[0]]
            g2=[lu[0],gate[1]]

		
        return ball
    

class P2:
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        gx = enemy_team [index][0]
        gy = enemy_team [index][1]

        return (gx - your_team [index][0], gy - your_team [index][1])


class P4:
    state = 0
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        # get first coordinates        
        first_x = lu[0]
        first_y = gate[1]
        # get second coordinates        
        second_x = lu[0]
        second_y = gate[0]
        # get your coordinates
        your_position_x = your_team[index][0]
        your_position_y = your_team[index][1]
        # generate speed
        if self.state == 0:
            speed = (first_x - your_position_x , first_y - your_position_y)
        else:
            speed = (second_x - your_position_x , second_y - your_position_y)

        if speed == (0,0):
            self.state = (self.state + 1) % 2
        return speed
       
    


class P3:
    state = 0
    def move(self,lu,rb,gate,index,side,balls,your_team,enemy_team):
        if enemy_team [index][0]< lu[1] + rb[1]/2.0:
        # get first coordinates        
            first_x = (lu[0]*14 + rb[0])/15.0
            first_y = (lu[1]*4 + rb[1])/5.0
        # get second coordinates        
            second_x = (lu[0]*6 + rb[0])/7.0
            second_y = (lu[1]*4 + rb[1])/5.0
        # get third coordinates
            third_x = (lu[0]*6 + rb[0])/7.0
            third_y = (lu[1] + 4*rb[1])/5.0
        # get fourth coordinates
            fourth_x = (lu[0]*14 + rb[0])/15.0
            fourth_y = (lu[1] + 4*rb[1])/5.0
        # get your coordinates
            your_position_x = your_team[index][0]
            your_position_y = your_team[index][1]
        # generate speed
            if self.state == 0:
                speed = (first_x - your_position_x , first_y - your_position_y)
            elif self.state == 1:
                speed = (second_x - your_position_x , second_y - your_position_y)
            elif self.state ==2:
                speed = (third_x - your_position_x, third_y - your_position_y)
            else:
                speed = (fourth_x - your_position_x, fourth_y - your_position_y)
            if speed == (0,0):
                self.state = (self.state + 1) % 4
            return speed

        else:
            # get first coordinates        
            first_x = (lu[0]*2 + rb[0])/3.0
            first_y = (lu[1]*4 + rb[1])/5.0
        # get second coordinates        
            second_x = (lu[0] + rb[0])/2.0
            second_y = (lu[1]*4 + rb[1])/5.0
        # get third coordinates
            third_x = (lu[0] + rb[0])/2.0
            third_y = (lu[1]+ 4*rb[1])/5.0
        # get fourth coordinates
            fourth_x = (lu[0]*2 + rb[0])/3.0
            fourth_y = (lu[1] + 4*rb[1])/5.0
        # get your coordinates
            your_position_x = your_team[index][0]
            your_position_y = your_team[index][1]
        # generate speed
            if self.state == 0:
                speed = (first_x - your_position_x , first_y - your_position_y)
            elif self.state == 1:
                speed = (second_x - your_position_x , second_y - your_position_y)
            elif self.state ==2:
                speed = (third_x - your_position_x, third_y - your_position_y)
            else:
                speed = (fourth_x - your_position_x, fourth_y - your_position_y)
            if speed == (0,0):
                self.state = (self.state + 1) % 4
            return speed


        
        
        
