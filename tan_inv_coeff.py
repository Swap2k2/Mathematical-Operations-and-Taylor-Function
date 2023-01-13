def tan_inv_coeff(n) :
    if (n % 4 == 0)  :
        return 0

    elif  (n % 4 == 2):
        return 0

    elif (n % 4 == 1) : 
        return 1/n 

    else :
        return -1/n
        

print (tan_inv_coeff(7))