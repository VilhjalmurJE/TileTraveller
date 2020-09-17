# Vilhjálmur, Katrín 
# Leikmaðurinn er staddur í 3x3 grid, byrjar á 1,1 og hann vinnur ef hann fer á 3,1
# Leikmaðurinn getur valið hvort hann vilji fara suður, vestur, norður og austur
# Leikmaðurinn byrjar á að geta bara farið norður. Ef leimaðurinn skrifar inn átt sem ekki er hægt að fara í á að koma invalid.


def north(x,y):
    if x == 1:
        if y == 1 or y == 2:
            return True
        elif y == 3:
            return False
    elif x == 2:
        if y == 1:
            return True
        elif y == 2 or y == 3:
            return False
    elif x == 3:
        if y == 1 or y == 2:
            return True
        elif y == 3:
            return False

def east(x,y):
    if x == 1:
        if y == 2 or y == 3:
            return True
        elif y == 1:
            return False
    if x == 2:
        if y == 3:
            return True
        elif y == 1 or y == 2:
            return False
    else:
        return False
    
def south(x,y):
    if x == 1:
        if y == 2 or y == 3:
            return True
        elif y == 1:
            return False
    if x == 2:
        if y == 2:
            return True
        elif y == 1 or y == 3:
            return False
    if x == 3:
        if y == 3 or y == 2:
            return True
        elif y == 1:
            return False

def west(x,y):
    if x == 2:
        if y == 2 or y == 3:
            return True
        elif y == 1:
            return False
    if x == 3:
        if y == 3:
            return True
        else:
            return False
    else:
        return False

def move_title_y(x, y, direction):
    if direction == "n" or direction == "N":
        if north(x,y) == True:
            return y + 1
        else:
            print("Not a valid direction!")
            return y
    elif direction == "s" or direction == "S":
        if south(x,y) == True:
            return y-1
        else:
            print("Not a valid direction!")
            return y
    else:
        return y

def move_title_x(x, y, direction):
    if direction == "e" or direction == "E":
        if east(x, y) == True:
            return x + 1
        else:
            print("Not a valid direction!")
            return x
    elif direction == "w" or direction == "W":
        if west(x, y) == True:
            return x-1
        else:
            print("Not a valid direction!")
            return x
    else:
        return x
            

title_x = 1
title_y = 1

while True:

    print("You can travel: ", end="")
    if(north(title_x,title_y) == True):
        print("(N)orth", end="")
    if (east(title_x,title_y) == True):
        if north(title_x,title_y) == True:
            print(" or", end=" ")
        print("(E)ast", end="")
    if (south(title_x,title_y) == True):
        if east(title_x,title_y) == True or north(title_x,title_y) == True:
            print(" or", end=" ")
        print("(S)outh", end="")
    if (west(title_x,title_y) == True):
        if south(title_x,title_y) == True or east(title_x,title_y) == True or north(title_x,title_y) == True:
            print(" or", end=" ")
        print("(W)est", end="")
    print(".")

    direction = input("Direction: ")

    title_x = move_title_x(title_x,title_y, direction)
    title_y = move_title_y(title_x,title_y, direction)

    if (title_x == 3) and (title_y == 1):
        print("Victory!")

