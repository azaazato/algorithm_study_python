import copy

a = [0,0,0]

def kstring(n, k):
    global a
    if n < 1:
        print(a)
    else:
        for i in range(0, k):
            a[n-1] = i
            kstring(n-1, k)

kstring(3, 3)
