def chekingpawns(chessboard, x, y, x1, y1):
    if chessboard [x1] [y1] ==0:
        if x==x1 and y+1==y1:
            return True 
        elif x==x1 and y+2==y1:
            return True
        else:
            return False
    else:
        if x+1==x1 and y+1==y1:
            print ("take the piece")
            return True 
        elif x-1==x1 and y+1==y1:
            return True
        else: 
            return False 

def checkingknights (chessboard, x, y, x2, y2):
    return True
   
def checkingbishops (chessboard, x, y, x3, y3):

    

def checkingrooks (chessboard, x, y, x4, y4):
    if chessboard [x4] [y4] ==0:
        if x==x4 and y+1==y4:
            return True
        elif x==x4 and y+2==y4:
            return True
        elif x==x4 and y+3==y4:
            return True
        elif x==x4 and y+4==y4:
            return True
        elif x==x4 and y+5==y4:
            return True
        elif x==x4 and y+6==y4:
            return True
        elif x==x4 and y+7==y4:
            return True
        elif x==x4 and y-1==y4:
            return True
        elif x==x4 and y-2==y4:
            return True
        elif x==x4 and y-3==y4:
            return True
        elif x==x4 and y-4==y4:
            return True
        elif x==x4 and y-5==y4:
            return True
        elif x==x4 and y-6==y4:
            return True
        elif x==x4 and y-7==y4:
            return True
        elif x+1==x4 and y==y4:
            return True
        elif x+2==x4 and y==y4:
            return True
        elif x+3==x4 and y==y4:
            return True
        elif x+4==x4 and y==y4:
            return True
        elif x+5==x4 and y==y4:
            return True
        elif x+6==x4 and y==y4:
            return True
        elif x+7==x4 and y==y4:
            return True
        elif x-1==x4 and y==y4:
            return True
        elif x-2==x4 and y==y4:
            return True
        elif x-3==x4 and y==y4:
            return True
        elif x-4==x4 and y==y4:
            return True
        elif x-5==x4 and y==y4:
            return True
        elif x-6==x4 and y==y4:
            return True
        elif x-7==x4 and y==y4:
            return True
        else: 
            return False 
        



