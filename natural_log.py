
def natural_log(x , n) :

    i_term = 1
    ans = 0
    prod_ = 1
    
    for i_term in range (1,n+1) :

        ratio = -x 
        prod_ = prod_ * ratio
        ans = ans - (prod_/i_term)

    return ans

print (natural_log(0.5,2))

# -----------------------------------------------------------------------------------------------------------


