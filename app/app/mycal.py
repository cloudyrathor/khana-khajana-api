def addit(x,y):
    return x + y

def subit(x,y):
    return x-y

def multit(x,y):
    return x * y

def divit(x,y):
    try:
        return x/y
    except:
        if y ==0:
            print("Denominator should not zero")
        else:
            print("It should be number")