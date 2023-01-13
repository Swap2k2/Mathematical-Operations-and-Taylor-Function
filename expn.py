# Question 1

# e^x

def expn (x,n) :

    fst_term = 1


   
    if n <= 1 or x == 0 :
        return fst_term

    else :
        fst_term = 1

        i_term = 2

        ans = 1
        prod_ = 1

        
        for i_term in range (2,n+1) :
            
            ratio = x / (i_term - 1)
            prod_ = prod_ * ratio
            ans = ans + prod_
            
        return ans

# print (expn(1,6))

# -----------------------------------------------------------------------------------------------------------


