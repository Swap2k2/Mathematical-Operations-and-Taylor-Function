import math

def f(x):
    return (math.cos(x) + math.exp(-x))

e = math.exp(1)



def bisect(a , b , eps):
    print (f(a))
    print (f(b))
    x0 = a
    found = False
    L = []
     
    while (a<b) and (not found):
        x0 = (a + b)/2
        L.append(x0)
        val = f(x0)
        
        if ((f(a) > 0 and f(b) < 0) or (f(a) < 0 and f(b) > 0)):

            if (abs(val) < eps)  :
                found = True

            elif val > 0 :
                b = x0
                found = False


            elif val < 0 :
                a = x0
                found = False
            

        elif (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0) :
            return found
            

    return (found , x0 , L)

print (bisect(4,5,1e-2))
print (bisect(1,2,0.1))
