import math
def f13(n):
    summa1 = 0
    summa2 = 0
    for i in range(1, n+1):
        summa1 += (52*i**(3)-abs(i))
    for i in range(1, n+1):
        summa2 += (math.tan(i)+i**(5))

    return 28*summa1+99*summa2


