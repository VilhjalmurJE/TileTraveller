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
    

    


