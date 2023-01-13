
def expn_coeff(n) :
    if (n==0) :
        return 1

    else :
        x1 = 1
        # i = 1
        for i in range (1,n+1):
            x1 = x1 * (1/i)
        
        return x1

# print (expn_coeff(3))