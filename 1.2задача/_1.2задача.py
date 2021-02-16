import math 
def f12(x):
    if(x<105):
       return math.log(16*x**(3)+13*x**7)+math.cos(x**(3)+abs(x)-55)
    if(105<=x<154):
       return math.e**(x)+21*x**6
    if(154<=x<228):
       return math.tan(math.log(x)+x**8)-62*x**7
    if(228<=x<244):
       return x+math.sin(x)
    if(x>=244):
       return math.exp((63*x**(4)+(x**(5)/98)-47)-71*x**(8)+25)

