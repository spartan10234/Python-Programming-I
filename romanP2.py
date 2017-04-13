"""
Program: CS 115 Project 2
Author: Eduardo Roman
Description: This program creates a simple matching game by using the users clicks on cards to flip them
over and find pairs. Flashing in the end until all pairs have been matched.
"""
from match_graphics import *
from random import seed, shuffle

import random

def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name of the card in
    row i and column j. It is a 5x5 grid comprised of 12 card pairs and one extra card.

    :param: None
    :return: a shuffled pair of cards
    '''
    # seed the random number generator
    seed()
    # shuffle the images
    random.shuffle(images)
    deck=[]
    len(images)
    for i in range(len(images)-1):
        deck.append(images[i])
        deck.append(images[i])
    deck.append(images[-1])
    # shuffle that list
    random.shuffle(deck)

    # use the list of these 25 shuffled cards to build a 5x5 array of cards
    # TODO: fix this code. It currently is a 5x5 array of nothing but one card
    cards = []
    count=0
    for i in range(5):
        row = []
        for j in range(5):
            item = deck[count]
            row.append(item)
            count += 1
        cards.append(row)
    return cards


def show_card(win, cards, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.
    :param: takes graphics window, the shuffled cards, and the column (i) and row (j)
    :returns: image where user clicks in the grid of the game.
    '''
    CARD_HEIGHT = 125  # height of the card (matched the height of each image)
    CARD_WIDTH = 125  # width of the card (matches the width of each image)
    X = i*125+25  # margin on the left and right of the board
    Y= j*125+25

    top_left_point = Point(X, Y)
    bottom_right_point = Point(X + CARD_WIDTH, Y + CARD_HEIGHT)
    enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
    enclosing_rectangle.setOutline('Yellow')
    enclosing_rectangle.setWidth(5)
    enclosing_rectangle.setFill('LightGreen')
    enclosing_rectangle.draw(win)
    #  at the location associated with card (i,j)
    # Then, place the image for cards[i][j] at the center of the rectangle.
    card = Image(Point(X+62.5, Y+62.5), cards[j][i])
    card.draw(win)

    return


def hide_card(win, cards, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.
    :param: takes graphics window, the shuffled cards, and the column (i) and row (j)
    :returns: image is hidden where user clicks in the grid of the game.
    '''
    CARD_HEIGHT = 125
    CARD_WIDTH = 125
    X = i * 125 + 25
    Y = j * 125 + 25

    top_left_point = Point(X, Y)
    bottom_right_point = Point(X + CARD_WIDTH, Y + CARD_HEIGHT)
    enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
    enclosing_rectangle.setOutline('Yellow')
    enclosing_rectangle.setWidth(5)
    enclosing_rectangle.setFill('LightGreen')
    enclosing_rectangle.draw(win)

    return


def mark_card(win, cards, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j with a red X.
    :param: takes graphics window, the shuffled cards, and the column (i) and row (j)
    :returns: no value.
    '''
    CARD_HEIGHT = 125
    CARD_WIDTH = 125
    X = i * 125 + 25
    Y = j * 125 + 25
    top_left_point = Point(X, Y)
    bottom_right_point = Point(X + CARD_WIDTH, Y + CARD_HEIGHT)
    line= Line(top_left_point, bottom_right_point)
    line.setOutline('red')
    line.setWidth(5)
    line.draw(win)

    top_right_point= Point(X+CARD_WIDTH, Y)
    bottom_left_point= Point(X, Y + CARD_WIDTH)
    line = Line(top_right_point,bottom_left_point )
    line.setOutline('red')
    line.setWidth(5)
    line.draw(win)
    return None



def get_col(x):
    '''
    Takes the x-coordinate and returns the column.
    It the x coordinate is outside the board, returns -1.
    :param: takes the (x) coordinate of the grid
    :returns: the column number or -1 if the user clicks outside the grid.
    '''

    column_num = ((x - XMARGIN) // (CARD_WIDTH ))
    if (0<=column_num<=4):
        return column_num
    if x<XMARGIN or x>(BOARD_HEIGHT-XMARGIN):
        return -1





def get_row(y):
    '''
    Takes the y-coordinate and returns the row.
    If it it outside the board, returns -1.
    :param: takes the (y) coordinate of the grid
    :returns: the row number, or -1 if the user clicks outside the grid.
    '''
    row_num = ((y- YMARGIN)//(CARD_HEIGHT))
    if (0<= row_num <= 4):
        return row_num
    if y<YMARGIN or y>(BOARD_WIDTH-YMARGIN):
        return -1

def main():
    '''
    generates game window, shuffles cards and sets them in the grid by calling the
    show card function or hidden function, based on whether it is a match or not.
    '''
    win = create_board()
    cards = shuffle_cards()
    # place all the cards, face-up
    for i in range(5):
        for j in range(5):
            show_card(win, cards, i, j)
            hide_card(win, cards, i, j)

    match_list= []
    clicks = 0
    while True:
        try:
            c_point = win.getMouse()
            x_point = c_point.getX()
            y_point = c_point.getY()
            row1= int(get_row(y_point))
            colm1= int(get_col(x_point))
            if (colm1, row1) in match_list:
                continue
            if row1==-1 or colm1==-1:
                continue
            show_card(win, cards, colm1, row1)

            if clicks == 0:
                row2=row1
                colm2=colm1
            clicks+=1

            if clicks>=2:
                #check to see if clicks is on the same card.
                if row1== row2 and colm1==colm2:
                    continue
                #if not, delay and show cards for 1 sec
                game_delay(1)

                #if images match leave them flip
                if cards[row2][colm2]== cards[row1][colm1]:

                    image1= (colm1, row1)
                    image2= (colm2, row2)
                    match_list.append(image1)
                    match_list.append(image2)
                    mark_card(win, cards, colm2, row2)
                    mark_card(win, cards, colm1, row1)
                else:
                    hide_card(win, cards,colm1,row1)
                    hide_card(win,cards,colm2, row2)
                if len(match_list)== 24:
                    you_won(win,delay=0.2)
                    win.close()

                clicks=0
        except GraphicsError:
            sys.exit(-1)


main()