def summ(a,b):
    return a+b

def mins(a,b):
    return a-b

def pr(a,b):
    return a*b

def dl(a,b):
    if b==0:
        raise ValueError('error')
    return a/b

def stp(a,b):
    return a**b