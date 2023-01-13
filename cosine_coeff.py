
def cosine_coeff(n) :

    if (n==0) :
        return 1

    else :

        if (n%2 != 0) :
            return 0

        else :
            x1 = 1
            for i in range (3,n+2,2) :
                x1 = x1 * - 1 /((i - 1)*(i - 2))
            return x1

print (cosine_coeff(2))
