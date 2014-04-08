# -*- coding: utf-8 -*-

class defenderLogic:
    a=(0,0)
    def move(self, lu, rb, gate, index, side, balls, your_team,enemy_team):
        x,y = (0,0)
#vorota        
        if side==0:
            g1=[rb[0], gate[0]]
            g2=[rb[0], gate[1]]
        else:
            g1=[lu[0],gate[0]]
            g2=[lu[0],gate[1]]

#pole
        minp=[lu[0],lu[1]]
        maxp=[rb[0],rb[1]]

#center vorot
        cg=[g1[0], (g2[1]-g1[1])/2]
        
#move
        count = 0
        if your_team[index]!=cg:
            while your_team[index]!=cg:
                f=your_team[index]            
                px=f[0]
                py=f[1]
                x=cg[0]-px
                y=cg[1]-py
                count += 1
                if count == 100:
                    break
        else:
            x,y=0,0
        return (x,y)