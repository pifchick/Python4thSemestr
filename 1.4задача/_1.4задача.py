import math
def f14():
    if n==0:
        return 3
    else:
        return 1/82*f14(n-2)-1/18*f14(n-1)**3
