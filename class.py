from project import Project
from graphics import*
from random import randrange

def main():
    match_maker = Project()
    win = GraphWin("MATCHMAKER", 1500, 800)
    atl = Text(Point(7,6),"Two of the boxes contain the same letter")

    match_maker.start_game(win,atl)
    match_maker.draw_rectangles(win,atl)
    #match_maker.restart(win,atl)


main()
