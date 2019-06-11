from graphics import*
from random import randrange

class Project:
        def __init__(self):
            pass
#this function draws the graphical user interface 
        def start_game(self, win,atl):
            win.setCoords(0.0,0.0,15.0,8.0)
            win.setBackground("beige")
            wi = Text(Point(7,7),"Welcome to THE MATCHMAKER!!")
            wi.setStyle("bold italic")
            wi.setFill("orange")
            wi.setSize(20)
            wi.draw(win)
            wit = Text(Point(7,6),"This game is a fun way to learn sign language!")
            wit.setStyle("bold italic")
            wit.setFill("orange")
            wit.setSize(20)
            wit.draw(win)
            wit1 = Text(Point(7,5),"Click anywhere to start")
            wit1.setStyle("bold italic")
            wit1.setFill("orange")
            wit1.setSize(20)
            wit1.draw(win)
            win.getMouse()
            wit.undraw()
            wit1.undraw()
            wi.setText("There will be 5 boxes drawn in the window")
            atl.setStyle("bold italic")
            atl.setFill("orange")
            atl.setSize(20)
            atl.draw(win)
            wo = Text(Point(7,5), "Click anywhere to start")
            wo.setStyle("bold italic")
            wo.setFill("orange")
            wo.setSize(20)
            wo.draw(win)
            win.getMouse()
            wi.setText("")
            atl.setText("")
            wo.setText("")
            atl.setText("Click on the two boxes you think match!!!") 
     
        def draw_rectangles(self,win,atl):
            un = Rectangle(Point(0.5,2),Point(2.5,4))
            un.setFill("red")
            un.setOutline("black")
            un2 = un.clone()
            un2.move(2.5,0)
            un.draw(win)
            un2.draw(win)
            un3 = un2.clone()
            un3.move(2.5,0)
            un3.draw(win)
            un4 = un3.clone()
            un4.move(2.5,0)
            un4.draw(win)
            un5 = un4.clone()
            un5.move(2.5,0)
            un5.draw(win)

##alpha randomly picks between 1 - 26 to represent the 26 english alphabets
##when either of them is chosen it draws two of the correspnding letters when
##clicked and 3 other letters
            alpha = randrange(1,27)
            print(alpha)
            if alpha == 1:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                    r = 'a'
                    at = Image(Point(1,3),"A.png")
                    at.draw(win)
                    un.undraw()                        
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                    r1 = 'a'
                    at1 = Image(Point(3.5,3),"A.png")
                    at1.draw(win)
                    un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                    r2 = 't'
                    at2 = Image(Point(6.5,3),"T.png")
                    at2.draw(win)
                    un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                    r3 = 'x'
                    at3 = Image(Point(9.5,3),"X.png")
                    at3.draw(win)
                    un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                    r4='y'
                    at4 = Image(Point(12.5,3),"Y.png")
                    at4.draw(win)
                    un5.undraw()

                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                    r = 'a'
                    at = Image(Point(1,3),"A.png")
                    at.draw(win)
                    un.undraw()                        
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                    r1 = 'a'
                    at1 = Image(Point(3.5,3),"A.png")
                    at1.draw(win)
                    un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                    r2 = 't'
                    at2 = Image(Point(6.5,3),"T.png")
                    at2.draw(win)
                    un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                    r3 = 'x'
                    at3 = Image(Point(9.5,3),"X.png")
                    at3.draw(win)
                    un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                    r4='y'
                    at4 = Image(Point(12.5,3),"Y.png")
                    at4.draw(win)
                    un5.undraw()
                    

#this for loop checks for matches between the two boxes selected                    
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 3<= i1<=5 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r1 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win) 
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win)
                        
                    
                   
            elif alpha == 2:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r = 'b'
                   an = Image(Point(1,3), "B.png")
                   an.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1 = 'c'
                   an1 = Image(Point(3.5,3), "C.png")
                   an1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2 = 'z'
                   an2 = Image(Point(6.5,3), "Z.png")
                   an2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3 = 'b' 
                   an3 = Image(Point(9.5,3), "B.png")
                   an3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4 = 'f' 
                   an4 = Image(Point(12.5,3), "F.png")
                   an4.draw(win)
                   un5.undraw()

                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r = 'b' 
                   an = Image(Point(1,3), "B.png")
                   an.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1 = 'c' 
                   an1 = Image(Point(3.5,3), "C.png")
                   an1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2 = 'z' 
                   an2 = Image(Point(6.5,3), "Z.png")
                   an2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3 = 'b' 
                   an3 = Image(Point(9.5,3), "B.png")
                   an3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4 = 'f' 
                   an4 = Image(Point(12.5,3), "F.png")
                   an4.draw(win)
                   un5.undraw()

                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 8<= i2 <= 10 and 2 <=e2 <= 4:
                            if r == r3:
                                atl.undraw()
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 8<= i1<=10 and 2<= e1<=4:
                        if 0.5<= i2 <= 2.5 and 2 <=e2 <= 4:
                            if r3 == r:
                                atl.undraw()
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win)


            elif alpha == 3:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r = 'x'
                   ad = Image(Point(1,3),"X.png")
                   ad.draw(win)
                   un.undraw() 
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1 = 'd' 
                   ad1 = Image(Point(3.5,3),"D.png")
                   ad1.draw(win)
                   un2.undraw()
                if 5.5 <= i1<= 7.5 and 2 <= e1 <=4:
                   r2 = 'y' 
                   ad2 = Image(Point(6.5,3),"Y.png")
                   ad2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3 = 'c' 
                   ad3 = Image(Point(9.5,3),"C.png")
                   ad3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4 = 'c' 
                   ad4 = Image(Point(12.5,3),"C.png")
                   ad4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r = 'x' 
                   ad = Image(Point(1,3),"X.png")
                   ad.draw(win)
                   un.undraw() 
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1 = 'd' 
                   ad1 = Image(Point(3.5,3),"D.png")
                   ad1.draw(win)
                   un2.undraw()
                if 5.5 <= i2<= 7.5 and 2 <= e2<=4:
                   r2 = 'y' 
                   ad2 = Image(Point(6.5,3),"Y.png")
                   ad2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3 = 'c' 
                   ad3 = Image(Point(9.5,3),"C.png")
                   ad3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4 = 'c' 
                   ad4 = Image(Point(12.5,3),"C.png")
                   ad4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 8<= i1 <= 10 and 2 <=e1 <= 4:
                        if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                            if r3 == r4 :
                                atl.undraw()
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 10.5<= i1 <= 12.5 and 2 <=e1 <= 4:
                        if 8 <= i2 <= 10 and 2 <= e2 <= 4:
                            if r4 == r3 :
                                atl.undraw()
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

            elif alpha == 4:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r = 'x' 
                   ade = Image(Point(1,3),"X.png")
                   ade.draw(win)
                   un.undraw() 
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1 = 'd' 
                   ade1 = Image(Point(3.5,3),"D.png")
                   ade1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2 = 'd' 
                   ade2 = Image(Point(6.5,3),"D.png")
                   ade2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3 = 'c' 
                   ade3 = Image(Point(9.5,3),"C.png")
                   ade3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4 = 'e' 
                   ade4 = Image(Point(12.5,3),"E.png")
                   ade4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r = 'x' 
                   ade = Image(Point(1,3),"X.png")
                   ade.draw(win)
                   un.undraw() 
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1 = 'd' 
                   ade1 = Image(Point(3.5,3),"D.png")
                   ade1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2 = 'd' 
                   ade2 = Image(Point(6.5,3),"D.png")
                   ade2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3 = 'c' 
                   ade3 = Image(Point(9.5,3),"C.png")
                   ade3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4 = 'e' 
                   ade4 = Image(Point(12.5,3),"E.png")
                   ade4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 3 <= i1 <= 5 and 2<= e1<= 4:
                        if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                            if r1 == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 5.5 <= i1 <= 7.5 and 2<= e1<= 4:
                        if 3 <= i2 <= 5 and 2 <= e2 <=4:
                            if r2 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 
                
                   
            elif alpha == 5:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='e' 
                   ado = Image(Point(1,3),"E.png")
                   ado.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='d' 
                   ado1 = Image(Point(3.5,3),"D.png")
                   ado1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='y' 
                   ado2 = Image(Point(6.5,3),"Y.png")
                   ado2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='e' 
                   ado3 = Image(Point(9.5,3),"E.png")
                   ado3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='c' 
                   ado4 = Image(Point(12.5,3),"C.png")
                   ado4.draw(win)
                   un5.undraw()
                
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='e' 
                   ado = Image(Point(1,3),"E.png")
                   ado.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='d' 
                   ado1 = Image(Point(3.5,3),"D.png")
                   ado1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='y' 
                   ado2 = Image(Point(6.5,3),"Y.png")
                   ado2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='e' 
                   ado3 = Image(Point(9.5,3),"E.png")
                   ado3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='c' 
                   ado4 = Image(Point(12.5,3),"C.png")
                   ado4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 8<= i1<=10 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r3 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

            elif alpha == 6:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='x' 
                   adi = Image(Point(1,3),"X.png")
                   adi.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='f' 
                   adi1 = Image(Point(3.5,3),"F.png")
                   adi1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='f' 
                   adi2 = Image(Point(6.5,3),"F.png")
                   adi2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='s' 
                   adi3 = Image(Point(9.5,3),"S.png")
                   adi3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='i' 
                   adi4 = Image(Point(12.5,3),"I.png")
                   adi4.draw(win)
                   un5.undraw()
                
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='x'
                   adi = Image(Point(1,3),"X.png")
                   adi.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='f' 
                   adi1 = Image(Point(3.5,3),"F.png")
                   adi1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='f' 
                   adi2 = Image(Point(6.5,3),"F.png")
                   adi2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='s' 
                   adi3 = Image(Point(9.5,3),"S.png")
                   adi3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='i' 
                   adi4 = Image(Point(12.5,3),"I.png")
                   adi4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 3<= i1<=5 and 2<= e1<=4:
                        if 5.5 <= i2 <= 7.5 and 2<= e2<= 4:
                            if r1 == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 5.5<= i1<=7.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r2 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

            elif alpha == 7:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='g' 
                   ap = Image(Point(1,3),"G.png")
                   ap.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='g' 
                   ap1 = Image(Point(3.5,3),"G.png")
                   ap1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='g' 
                   ap2 = Image(Point(6.5,3),"G.png")
                   ap2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='g' 
                   ap3 = Image(Point(9.5,3),"G.png")
                   ap3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='g' 
                   ap4 = Image(Point(12.5,3),"G.png")
                   ap4.draw(win)
                   un5.undraw()

                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='g' 
                   ap = Image(Point(1,3),"G.png")
                   ap.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='g' 
                   ap1 = Image(Point(3.5,3),"G.png")
                   ap1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='g' 
                   ap2 = Image(Point(6.5,3),"G.png")
                   ap2.draw(win)
                   un3.undraw()
                if 8<= i2<= 10 and 2 <=e2 <= 4:
                   r3='g' 
                   ap3 = Image(Point(9.5,3),"G.png")
                   ap3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='g' 
                   ap4 = Image(Point(12.5,3),"G.png")
                   ap4.draw(win)
                   un5.undraw()

                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 3<= i1<=5 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r1 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You won")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

            elif alpha == 8:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='t' 
                   ape = Image(Point(0.5,3),"T.png")
                   ape.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='d' 
                   ape1 = Image(Point(3.5,3),"D.png")
                   ape1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='h' 
                   ape2 = Image(Point(6.5,3),"H.png")
                   ape2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='h' 
                   ape3 = Image(Point(9.5,3),"H.png")
                   ape3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='l' 
                   ape4 = Image(Point(12.5,3),"L.png")
                   ape4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='t' 
                   ape = Image(Point(0.5,3),"T.png")
                   ape.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='d' 
                   ape1 = Image(Point(3.5,3),"D.png")
                   ape1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='h' 
                   ape2 = Image(Point(6.5,3),"H.png")
                   ape2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='h' 
                   ape3 = Image(Point(9.5,3),"H.png")
                   ape3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='l' 
                   ape4 = Image(Point(12.5,3),"L.png")
                   ape4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 5.5<= i1<=7.5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r2 == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    if 8<= i1<=10 and 2<= e1<=4:
                        if 5.5 <= i2 <= 7.5 and 2<= e2<= 4:
                            if r3 == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 9:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='x' 
                   af = Image(Point(1,3),"X.png")
                   af.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='d' 
                   af1 = Image(Point(3.5,3),"D.png")
                   af1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='y' 
                   af2 = Image(Point(6.5,3),"Y.png")
                   af2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='i' 
                   af3 = Image(Point(9.5,3),"I.png")
                   af3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='i' 
                   af4 = Image(Point(12.5,3),"I.png")
                   af4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='x' 
                   af = Image(Point(1,3),"X.png")
                   af.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='d' 
                   af1 = Image(Point(3.5,3),"D.png")
                   af1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='y' 
                   af2 = Image(Point(6.5,3),"Y.png")
                   af2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='i' 
                   af3 = Image(Point(9.5,3),"I.png")
                   af3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='i' 
                   af4 = Image(Point(12.5,3),"I.png")
                   af4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 8<= i1<=10 and 2<= e1<=4:
                        if 10.5 <= i2 <= 12.5 and 2<= e2<= 4:
                            if r3 == r4:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 10.5<= i1<=12.5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r4 == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

            elif alpha == 10:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='p' 
                   ano = Image(Point(1,3), "P.png")
                   ano.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='j' 
                   ano1 = Image(Point(3.5,3), "J.png")
                   ano1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='z' 
                   ano2 = Image(Point(6.5,3), "Z.png")
                   ano2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='u' 
                   ano3 = Image(Point(9.5,3), "U.png")
                   ano3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='j' 
                   ano4 = Image(Point(12.5,3), "J.png")
                   ano4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='p' 
                   ano = Image(Point(1,3), "P.png")
                   ano.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='j' 
                   ano1 = Image(Point(3.5,3), "J.png")
                   ano1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2<=4:
                   r2='z' 
                   ano2 = Image(Point(6.5,3), "Z.png")
                   ano2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='u' 
                   ano3 = Image(Point(9.5,3), "U.png")
                   ano3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='j' 
                   ano4 = Image(Point(12.5,3), "J.png")
                   ano4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 3<= i1<=5 and 2<= e1<=4:
                        if 10.5 <= i2 <= 12.5 and 2<= e2<= 4:
                            if r1 == r4:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 10.5<= i1<=12.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r4 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 11:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='o' 
                   att = Image(Point(1,3),"O.png")
                   att.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='z' 
                   att1 = Image(Point(3.5,3),"Z.png")
                   att1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='n' 
                   att2 = Image(Point(6.5,3),"N.png")
                   att2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='k' 
                   att3 = Image(Point(9.5,3),"K.png")
                   att3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='k' 
                   att4 = Image(Point(12.5,3),"K.png")
                   att4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='o' 
                   att = Image(Point(1,3),"O.png")
                   att.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='z' 
                   att1 = Image(Point(3.5,3),"Z.png")
                   att1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='n' 
                   att2 = Image(Point(6.5,3),"N.png")
                   att2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='k' 
                   att3 = Image(Point(9.5,3),"K.png")
                   att3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='k' 
                   att4 = Image(Point(12.5,3),"K.png")
                   att4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 8<= i1<=10 and 2<= e1<=4:
                        if 10.5<= i2 <= 12.5 and 2<= e2<= 4:
                            if r3 == r4:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    if 10.5<= i1<=12.5 and 2<= e1<=4:
                        if 8<= i2 <= 10 and 2<= e2<= 4:
                            if r4 == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 12:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='t' 
                   aden = Image(Point(1,3),"T.png")
                   aden.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='l' 
                   aden1 = Image(Point(3.5,3),"L.png")
                   aden1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='l' 
                   aden2 = Image(Point(6.5,3),"L.png")
                   aden2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='c' 
                   aden3 = Image(Point(9.5,3),"C.png")
                   aden3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='e' 
                   aden4 = Image(Point(12.5,3),"E.png")
                   aden4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='t' 
                   aden = Image(Point(1,3),"T.png")
                   aden.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='l' 
                   aden1 = Image(Point(3.5,3),"L.png")
                   aden1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='l' 
                   aden2 = Image(Point(6.5,3),"L.png")
                   aden2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='c' 
                   aden3 = Image(Point(9.5,3),"C.png")
                   aden3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='e' 
                   aden4 = Image(Point(12.5,3),"E.png")
                   aden4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 3 <= i1<=5 and 2<= e1<=4:
                        if 5.5<= i2 <= 7.5 and 2<= e2<= 4:
                            if r1 == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 5.5<= i1<=7.5 and 2<= e1<=4:
                        if 3<= i2 <= 5 and 2<= e2<= 4:
                            if r2 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win)  

            elif alpha == 13:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='m' 
                   ani = Image(Point(0.5,3), "M.png")
                   ani.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='c' 
                   ani1 = Image(Point(3.5,3), "C.png")
                   ani1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='z' 
                   ani2 = Image(Point(6.5,3), "Z.png")
                   ani2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='m' 
                   ani3 = Image(Point(9.5,3), "M.png")
                   ani3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='f' 
                   ani4 = Image(Point(12.5,3), "F.png")
                   ani4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='m' 
                   ani = Image(Point(0.5,3), "M.png")
                   ani.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='c' 
                   ani1 = Image(Point(3.5,3), "C.png")
                   ani1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='z' 
                   ani2 = Image(Point(6.5,3), "Z.png")
                   ani2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='m' 
                   ani3 = Image(Point(9.5,3), "M.png")
                   ani3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='f' 
                   ani4 = Image(Point(12.5,3), "F.png")
                   ani4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    elif 8<= i1<=10 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r3 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win) 
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 14:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='n' 
                   adu = Image(Point(1,3),"N.png")
                   adu.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='n' 
                   adu1 = Image(Point(3.5,3),"N.png")
                   adu1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='n' 
                   adu2 = Image(Point(6.5,3),"N.png")
                   adu2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='n' 
                   adu3 = Image(Point(9.5,3),"N.png")
                   adu3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='n' 
                   adu4 = Image(Point(12.5,3),"N.png")
                   adu4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='n' 
                   adu = Image(Point(1,3),"N.png")
                   adu.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='n' 
                   adu1 = Image(Point(3.5,3),"N.png")
                   adu1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='n' 
                   adu2 = Image(Point(6.5,3),"N.png")
                   adu2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='n' 
                   adu3 = Image(Point(9.5,3),"N.png")
                   adu3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='n' 
                   adu4 = Image(Point(12.5,3),"N.png")
                   adu4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 3<= i1<=5 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r1 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You won")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 15:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='o' 
                   adel = Image(Point(1,3),"O.png")
                   adel.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='d' 
                   adel1 = Image(Point(3.5,3),"D.png")
                   adel1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='y' 
                   adel2 = Image(Point(6.5,3),"Y.png")
                   adel2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='o' 
                   adel3 = Image(Point(9.5,3),"O.png")
                   adel3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='e' 
                   adel4 = Image(Point(12.5,3),"E.png")
                   adel4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='o' 
                   adel = Image(Point(1,3),"O.png")
                   adel.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='d' 
                   adel1 = Image(Point(3.5,3),"D.png")
                   adel1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='y' 
                   adel2 = Image(Point(6.5,3),"Y.png")
                   adel2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='o' 
                   adel3 = Image(Point(9.5,3),"O.png")
                   adel3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='e' 
                   adel4 = Image(Point(12.5,3),"E.png")
                   adel4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 8<= i1<=10 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r3 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

            elif alpha == 16:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='b' 
                   anin = Image(Point(1,3), "B.png")
                   anin.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='v' 
                   anin1 = Image(Point(3.5,3), "V.png")
                   anin1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='z' 
                   anin2 = Image(Point(6.5,3), "Z.png")
                   anin2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='p' 
                   anin3 = Image(Point(9.5,3), "P.png")
                   anin3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='p' 
                   anin4 = Image(Point(12.5,3), "P.png")
                   anin4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='b' 
                   anin = Image(Point(1,3), "B.png")
                   anin.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='v' 
                   anin1 = Image(Point(3.5,3), "V.png")
                   anin1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='z' 
                   anin2 = Image(Point(6.5,3), "Z.png")
                   anin2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='p' 
                   anin3 = Image(Point(9.5,3), "P.png")
                   anin3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='p' 
                   anin4 = Image(Point(12.5,3), "P.png")
                   anin4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 8<= i1<=10 and 2<= e1<=4:
                        if 10.5 <= i2 <= 12.5 and 2<= e2<= 4:
                            if r3 == r4:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 10.5<= i1<=12.5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r4 == r3: 
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 17:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='i' 
                   ado = Image(Point(1,3),"I.png")
                   ado.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='q' 
                   ado1 = Image(Point(3.5,3),"Q.png")
                   ado1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='j' 
                   ado2 = Image(Point(6.5,3),"J.png")
                   ado2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='q' 
                   ado3 = Image(Point(9.5,3),"Q.png")
                   ado3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='a' 
                   ado4 = Image(Point(12.5,3),"A.png")
                   ado4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='i' 
                   ado = Image(Point(1,3),"I.png")
                   ado.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='q' 
                   ado1 = Image(Point(3.5,3),"Q.png")
                   ado1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='j' 
                   ado2 = Image(Point(6.5,3),"J.png")
                   ado2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='q' 
                   ado3 = Image(Point(9.5,3),"Q.png")
                   ado3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='a' 
                   ado4 = Image(Point(12.5,3),"A.png")
                   ado4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 3<= i1<=5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r1 == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 8<= i1<=10 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r3 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 18:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='t' 
                   od = Image(Point(1,3),"T.png")
                   od.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='s' 
                   od1 = Image(Point(3.5,3),"S.png")
                   od1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='r' 
                   od2 = Image(Point(6.5,3),"R.png")
                   od2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='r' 
                   od3 = Image(Point(9.5,3),"R.png")
                   od3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='e' 
                   od4 = Image(Point(12.5,3),"E.png")
                   od4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='t' 
                   od = Image(Point(1,3),"T.png")
                   od.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='s' 
                   od1 = Image(Point(3.5,3),"S.png")
                   od1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='r' 
                   od2 = Image(Point(6.5,3),"R.png")
                   od2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='r' 
                   od3 = Image(Point(9.5,3),"R.png")
                   od3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='e' 
                   od4 = Image(Point(12.5,3),"E.png")
                   od4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 5.5<= i1<=7.5 and 2<= e1<=4:
                        if 8 <= i2 <= 10 and 2<= e2<= 4:
                            if r2 == r3:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    if 8<= i1<=10 and 2<= e1<=4:
                        if 5.5 <= i2 <= 7.5 and 2<= e2<= 4:
                            if r3 == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

                   
            elif alpha == 19:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='s' 
                   on = Image(Point(1,3), "S.png")
                   on.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='c' 
                   on1 = Image(Point(3.5,3), "C.png")
                   on1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='s' 
                   on2 = Image(Point(6.5,3), "S.png")
                   on2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='b' 
                   on3 = Image(Point(9.5,3), "B.png")
                   on3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='d' 
                   on4 = Image(Point(12.5,3), "D.png")
                   on4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='s' 
                   on = Image(Point(1,3), "S.png")
                   on.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='c' 
                   on1 = Image(Point(3.5,3), "C.png")
                   on1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='s' 
                   on2 = Image(Point(6.5,3), "S.png")
                   on2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='b' 
                   on3 = Image(Point(9.5,3), "B.png")
                   on3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='d' 
                   on4 = Image(Point(12.5,3), "D.png")
                   on4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 5.5 <= i2 <= 7.5 and 2<= e2<= 4:
                            if r == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    elif 5.5<= i1<=7.5 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r2 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 20:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='x' 
                   ed = Image(Point(1,3),"X.png")
                   ed.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='t' 
                   ed1 = Image(Point(3.5,3),"T.png")
                   ed1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='y' 
                   ed2 = Image(Point(6.5,3),"Y.png")
                   ed2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='c' 
                   ed3 = Image(Point(9.5,3),"C.png")
                   ed3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='t'
                   ed4 = Image(Point(12.5,3),"T.png")
                   ed4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='x' 
                   ed = Image(Point(1,3),"X.png")
                   ed.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='t' 
                   ed1 = Image(Point(3.5,3),"T.png")
                   ed1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='y' 
                   ed2 = Image(Point(6.5,3),"Y.png")
                   ed2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='c' 
                   ed3 = Image(Point(9.5,3),"C.png")
                   ed3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='t' 
                   ed4 = Image(Point(12.5,3),"T.png")
                   ed4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 3<= i1<=5 and 2<= e1<=4:
                        if 10.5 <= i2 <= 12.5 and 2<= e2<= 4:
                            if r1 == r4:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    elif 10.5<= i1<=12.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r4 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 21:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='u' 
                   de = Image(Point(1,3),"U.png")
                   de.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='u' 
                   de1 = Image(Point(3.5,3),"U.png")
                   de1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='d' 
                   de2 = Image(Point(6.5,3),"D.png")
                   de2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='c' 
                   de3 = Image(Point(9.5,3),"C.png")
                   de3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='e' 
                   de4 = Image(Point(12.5,3),"E.png")
                   de4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='u' 
                   de = Image(Point(1,3),"U.png")
                   de.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='u' 
                   de1 = Image(Point(3.5,3),"U.png")
                   de1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='d' 
                   de2 = Image(Point(6.5,3),"D.png")
                   de2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='c' 
                   de3 = Image(Point(9.5,3),"C.png")
                   de3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='e' 
                   de4 = Image(Point(12.5,3),"E.png")
                   de4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 3<= i1<=5 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r1 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 

            elif alpha == 22:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='v' 
                   ann = Image(Point(1,3), "V.png")
                   ann.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='v' 
                   ann1 = Image(Point(3.5,3), "V.png")
                   ann1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='v' 
                   ann2 = Image(Point(6.5,3), "V.png")
                   ann2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='v' 
                   ann3 = Image(Point(9.5,3), "V.png")
                   ann3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='v' 
                   ann4 = Image(Point(12.5,3), "V.png")
                   ann4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='v' 
                   ann = Image(Point(1,3), "V.png")
                   ann.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='v' 
                   ann1 = Image(Point(3.5,3), "V.png")
                   ann1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='v' 
                   ann2 = Image(Point(6.5,3), "V.png")
                   ann2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='v' 
                   ann3 = Image(Point(9.5,3), "V.png")
                   ann3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='v' 
                   ann4 = Image(Point(12.5,3), "V.png")
                   ann4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You won")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 


            elif alpha == 23:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='w' 
                   po = Image(Point(1,3),"W.png")
                   po.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='o' 
                   po1 = Image(Point(3.5,3),"O.png")
                   po1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='w' 
                   po2 = Image(Point(6.5,3),"W.png")
                   po2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='p' 
                   po3 = Image(Point(9.5,3),"P.png")
                   po3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='c' 
                   po4 = Image(Point(12.5,3),"C.png")
                   po4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='w' 
                   po = Image(Point(1,3),"W.png")
                   po.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='o' 
                   po1 = Image(Point(3.5,3),"O.png")
                   po1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2 ='w' 
                   po2 = Image(Point(6.5,3),"W.png")
                   po2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='p' 
                   po3 = Image(Point(9.5,3),"P.png")
                   po3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='c' 
                   po4 = Image(Point(12.5,3),"C.png")
                   po4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 5.5 <= i2 <= 7.5 and 2<= e2<= 4:
                            if r == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 5.5<= i1<=7.5 and 2<= e1<=4:
                        if 0.5 <= i2 <= 2.5 and 2<= e2<= 4:
                            if r2 == r:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 
                   
            elif alpha == 24:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r='b' 
                   pan = Image(Point(1,3), "B.png")
                   pan.draw(win)
                   un.undraw()
                if 3 <= i1<= 5 and 2<= e1<= 4:
                   r1='x' 
                   pan1 = Image(Point(3.5,3), "X.png")
                   pan1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='x' 
                   pan2 = Image(Point(6.5,3), "X.png")
                   pan2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='e' 
                   pan3 = Image(Point(9.5,3), "E.png")
                   pan3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4='f' 
                   pan4 = Image(Point(12.5,3), "F.png")
                   pan4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r='b' 
                   pan = Image(Point(1,3), "B.png")
                   pan.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1='x' 
                   pan1 = Image(Point(3.5,3), "X.png")
                   pan1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2='x' 
                   pan2 = Image(Point(6.5,3), "X.png")
                   pan2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3='e' 
                   pan3 = Image(Point(9.5,3), "E.png")
                   pan3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='f' 
                   pan4 = Image(Point(12.5,3), "F.png")
                   pan4.draw(win)
                   un5.undraw()
                for i in range (100):
                    atl.undraw()
                    if 3<= i1<=5 and 2<= e1<=4:
                        if 5.5 <= i2 <= 7.5 and 2<= e2<= 4:
                            if r1 == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 5.5<= i1<=7.5 and 2<= e1<=4:
                        if 3 <= i2 <= 5 and 2<= e2<= 4:
                            if r2 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win)  


            elif alpha == 25: 
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r ='o' 
                   adm = Image(Point(1,3),"O.png")
                   adm.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1='y' 
                   adm1 = Image(Point(3.5,3),"Y.png")
                   adm1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2='y' 
                   adm2 = Image(Point(6.5,3),"Y.png")
                   adm2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3='q' 
                   adm3 = Image(Point(9.5,3),"Q.png")
                   adm3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4 ='r' 
                   adm4 = Image(Point(12.5,3),"R.png")
                   adm4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r ='o' 
                   adm = Image(Point(1,3),"O.png")
                   adm.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1 ='y' 
                   adm1 = Image(Point(3.5,3),"Y.png")
                   adm1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2 = 'y' 
                   adm2 = Image(Point(6.5,3),"Y.png")
                   adm2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3 = 'q' 
                   adm3 = Image(Point(9.5,3),"Q.png")
                   adm3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4='r' 
                   adm4 = Image(Point(12.5,3),"R.png")
                   adm4.draw(win)
                   un5.undraw()

                for i in range (100):
                    atl.undraw()
                    if 3 <= i1 <= 5 and 2<= e1<= 4:
                        if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                            if r1 == r2:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 5.5 <= i1 <= 7.5 and 2<= e1<= 4:
                        if 3 <= i2 <= 5 and 2 <= e2 <=4:
                            if r2 == r1:
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win) 
                   
                
                

            elif alpha == 26:
                ty = win.getMouse()
                i1 = ty.getX()
                e1 = ty.getY()
                if 0.5<= i1<=2.5 and 2<= e1<=4:
                   r = 'z' 
                   adn = Image(Point(1,3),"Z.png")
                   adn.draw(win)
                   un.undraw()
                if 3 <= i1 <= 5 and 2<= e1<= 4:
                   r1 = 'd' 
                   adn1 = Image(Point(3.5,3),"D.png")
                   adn1.draw(win)
                   un2.undraw()
                if 5.5 <= i1 <= 7.5 and 2 <= e1 <=4:
                   r2 = 'y' 
                   adn2 = Image(Point(6.5,3),"Y.png")
                   adn2.draw(win)
                   un3.undraw()
                if 8<= i1 <= 10 and 2 <=e1 <= 4:
                   r3 = 'z' 
                   adn3 = Image(Point(9.5,3),"Z.png")
                   adn3.draw(win)
                   un4.undraw()
                if 10.5 <= i1 <= 12.5 and 2 <= e1 <= 4:
                   r4 = 'c' 
                   adn4 = Image(Point(12.5,3),"C.png")
                   adn4.draw(win)
                   un5.undraw()
                ty2 = win.getMouse()
                i2 = ty2.getX()
                e2 = ty2.getY()
                if 0.5<= i2<=2.5 and 2<= e2<=4:
                   r = 'z' 
                   adn = Image(Point(1,3),"Z.png")
                   adn.draw(win)
                   un.undraw()
                if 3 <= i2 <= 5 and 2<= e2<= 4:
                   r1 = 'd' 
                   adn1 = Image(Point(3.5,3),"D.png")
                   adn1.draw(win)
                   un2.undraw()
                if 5.5 <= i2 <= 7.5 and 2 <= e2 <=4:
                   r2 = 'y' 
                   adn2 = Image(Point(6.5,3),"Y.png")
                   adn2.draw(win)
                   un3.undraw()
                if 8<= i2 <= 10 and 2 <=e2 <= 4:
                   r3 = 'z' 
                   adn3 = Image(Point(9.5,3),"Z.png")
                   adn3.draw(win)
                   un4.undraw()
                if 10.5 <= i2 <= 12.5 and 2 <= e2 <= 4:
                   r4 = 'c' 
                   adn4 = Image(Point(12.5,3),"C.png")
                   adn4.draw(win)
                   un5.undraw()

                for i in range (100):
                    atl.undraw()
                    if 0.5<= i1<=2.5 and 2<= e1<=4:
                        if 8<= i2 <= 10 and 2 <=e2 <= 4:
                            if r == r3:                                
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)

                    elif 8<= i1<=10 and 2<= e1<=4:
                        if 0.5<= i2 <= 2.5 and 2 <=e2 <= 4:
                            if r3== r:                                
                                wins = Text(Point(4,5),"You won")
                                wins.setStyle("bold italic")
                                wins.setFill("orange")
                                wins.setSize(30)
                                wins.draw(win)
                    else:
                        atl.undraw()
                        lose = Text(Point(4,5),"You lost")
                        lose.setStyle("bold italic")
                        lose.setFill("orange")
                        lose.setSize(30)
                        lose.draw(win)           

    ## Play again button to restart the game
            ri = Rectangle(Point(10,0.5), Point(12,1.5))
            ri.setFill("white")
            ri.draw(win)
            Text(Point(11,1),"Play again").draw(win)
            rin = win.getMouse()
            rinX = rin.getX()
            rinY = rin.getY()
            if 10<= rinX <= 12 and 0.5 <= rinY <= 1.5:
                win.delete('all')
                atl2 = Text(Point(7,6),"Click on the two boxes you think match")
                atl2.setStyle("bold italic")
                atl2.setFill("orange")
                atl2.setSize(20)
                atl2.draw(win)
                self.draw_rectangles(win,atl)

def main():
    match_maker = Project()
    win = GraphWin("MATCHMAKER", 1500, 800)
    atl = Text(Point(7,6),"Two of the boxes contain the same letter!!")
    match_maker.start_game(win,atl)
    match_maker.draw_rectangles(win,atl)
    
main()





                        

