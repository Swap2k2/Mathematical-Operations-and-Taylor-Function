
def tan_inv(x , n):


     i_term = 1

     ans = 0

     prod_ = 1
    
     for i_term in range (1,2*n, 2) :

    
         ratio = -x * x
         prod_ = prod_ * ratio
         ans = ans - (prod_/i_term)

     return ans

# print (tan_inv(1,3))