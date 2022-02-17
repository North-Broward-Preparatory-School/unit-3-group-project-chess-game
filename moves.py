chessboard = [
    ["&#9820;","&#9822;","&#9821;","&#9819;","&#9818;","&#9821;","&#9822;","&#9820;"],
    ["&#9823;","&#9823;","&#9823;","&#9823;","&#9823;","&#9823;","&#9823;","&#9823;"],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ["&#9817;","&#9817;","&#9817;","&#9817;","&#9817;","&#9817;","&#9817;","&#9817;"],
    ["&#9814;","&#9816;","&#9815;","&#9813;","&#9812;","&#9815;","&#9816;","&#9814;"]
] 
def checkingpawns(chessboard, x, y, x1, y1):
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

def checkingbishops(chessboard, x, y, x3, y3):        
    for i in range (-7,7):
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
    for i in range (-7,7):
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
        for i in range (-7,7):
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

print (checkingbishops (chessboard, 1,1, 2,2))

print (checkingbishops (chessboard, 1,1, 2,1))

print (checkingrooks (chessboard, 1,1, 4,1))

print (checkingrooks (chessboard, 1,1, 4,0))

print (checkingpawns (chessboard, 1,1, 1,3))

print (checkingpawns (chessboard, 1,1, 1,4))

print (checkingqueen (chessboard, 3,0, 3,2))

def checkmove (chessboard, x, y, x4, y4, piece):
    if piece == "&#9814;":
        checkingrooks (chessboard, x, y, x4, y4)
    if piece == "&#9817;":
        checkingpawns (chessboard, x, y, x4, y4)
    if piece == "&#9823;":
        checkingpawns (chessboard, x, y, x4, y4)
    if piece == "&#9820;":
        checkingrooks (chessboard, x, y, x4, y4)
    if piece == "&#9815;":
        checkingbishops (chessboard, x, y, x4, y4)
    if piece == "&#9821;":
        checkingbishops (chessboard, x, y, x4, y4)
    if piece == "&#9813;":
        checkingqueen (chessboard, x, y, x4, y4)
    if piece == "&#9819;":
        checkingqueen (chessboard, x, y, x4, y4)
    
    





