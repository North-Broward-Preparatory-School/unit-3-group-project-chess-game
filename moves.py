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

    return False 

def chekingbishops(chessboard, x, y, x3, y3):        
    for i in range (-6,6):
        if x+i==x3 and y+i==y3:
            return True
        elif x+i==x3 and y-i==y3:
            return True
        elif x-i==x3 and y+i==y3:
            return True
        elif x-i==x3 and y-i==y3:
            return True
 
    return False 

def checkingrooks (chessboard, x, y, x4, y4):
    for i in range (-6,6):
        if chessboard [x4] [y4] ==0:
            if x-i==x4 and y==y4:
                return True 
            elif x+i==x4 and y==y4:
                return True
            elif x==x4 and y-i==y4:
                return True 
            elif x==x4 and y+i==y4:
                return True

    return False 

def checkingqueen (chessboard, x, y, x5, y5):
    if chessboard [x5] [y5] ==0:
        for i in range (-6,6):
            if x+i==x5 and y+i==y5:
                return True
            elif x+i==x5 and y-i==y5:
                return True
            elif x-i==x5 and y+i==y5:
                return True
            elif x-i==x5 and y-i==y5:
                return True
            elif x-i==x5 and y==y5:
                return True 
            elif x+i==x5 and y==y5:
                return True
            elif x==x5 and y-i==y5:
                return True 
            elif x==x5 and y+i==y5:
                return True
    
    return False

print (checkingqueen (chessboard, 1,1, 1,3))

print (checkingqueen (chessboard, 1,1, 2,3))

print (chekingbishops (chessboard, 1,1, 2,2))

print (chekingbishops (chessboard, 1,1, 2,1))

print (checkingrooks (chessboard, 1,1, 4,1))

print (checkingrooks (chessboard, 1,1, 4,0))

print (chekingpawns (chessboard, 1,1, 1,3))

print (chekingpawns (chessboard, 1,1, 1,4))





