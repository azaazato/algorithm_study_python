import copy

a = [0,0,0,1]

def binary(n):
    global a
    if n < 1:
        print(a)
    else:
        a[n-1] = 0
        binary(n-1)
        a[n-1] = 1
        binary(n-1)

binary(4)
