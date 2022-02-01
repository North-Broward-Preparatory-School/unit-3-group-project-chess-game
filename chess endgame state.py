from re import L
from tkinter import Y


chessboard = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
] 
y=0
y=1
chessboard[x][y]="K"

print (chessboard)

def kinghitbox(chessboard,x,y):
    if chessboard[x-1][y-1]!=0 and chessboard[x][y-`1]!=0 and chessboard[x+1][y-1]!=0 and chessboard[x-1][y]!=0 and chessboard[x][y]!=0 and chessboard[x+1][y]!=0 and chessboard[x-1][y+1]!=0 and chessboard[x][y+1]!=0 and chessboard[x+1][y+1]!=0 and chessboard :
        print(chessboard)
        return "check"

def enpassant(chessboard,z,w):
    if chessboard[z][w]!=0 and chessboard[z][w-1]!=0 and chessboard :  
        return 'pawn captured '

enpassant(chessboard,1,1)
"""

def castle(chessboard,o,p)
    if 
    
"""

