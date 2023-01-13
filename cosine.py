
def cosine (x , n) :
    
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

# print(cosine(pi/2,3))

