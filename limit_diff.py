

def cos (x , n) :
    
    fst_term = 1

    if n <= 1 or x == 0 :
        return fst_term

    else :
        fst_term = 1

        ans = 1
        prod_1 = 1

        
        for i_term in range (3, 2*n, 2) :
            
            ratio = - x * x /((i_term - 1)*(i_term - 2))
            prod_1 = prod_1 * ratio
            ans = ans + prod_1
                
    return ans

import math
pi = math.pi
# print (cos(1,20))

def sin(x,n):
    fst_term = x

    if n < 1 or x == 0 :
        return 0

    elif (n==1) :
        return x

    else :
        ans = x
        prod_1 = x

        
        for i_term in range (4, 2*n+1, 2) :
            
            ratio =  -x * x /((i_term - 1)*(i_term - 2))
            prod_1 = prod_1 * ratio
            ans = ans + prod_1
                
    return ans


def tan(x):
    return sin(x,20)/cos(x,20)



def limit_diff(x, epsilon) :

    if (epsilon == 0) :
        return 1

    else :   
        a = tan(x)
        b = x + epsilon 
        z1 = tan(b) - tan(x)
        z2 = z1/epsilon
    
        return z2


print (limit_diff(10,0.000001))
