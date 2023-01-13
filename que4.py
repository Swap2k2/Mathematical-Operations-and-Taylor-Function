
def expn_coeff(n) :
    if (n==0) :
        return 1

    else :
        x1 = 1
        # i = 1
        for i in range (1,n+1):
            x1 = x1 * (1/i)
        
        return x1


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

# print (cosine_coeff(6))


def expn_t(x,n):
    ans = 0
    for k in range (0,n+1):
        ans += (x**k) * expn_coeff(k)
    return ans

def inverse_coeff(n) :
    return 1

# print (inverse_coeff(5))


def natural_log_coeff(n):

    if (n == 0) :
        return 0

    elif ((n % 2 == 0) and (n!= 0)):
        return -1/(n)

    else :
        return 1/(n)

# print (natural_log_coeff(4))

def tan_inv_coeff(n) :
    if (n % 4 == 0)  :
        return 0

    elif  (n % 4 == 2):
        return 0

    elif (n % 4 == 1) : 
        return 1/n 

    else :
        return -1/n
        

# print (tan_inv_coeff(7))



import math
pi = math.pi

def cosine_t(x,n):
    ans = 0
    for k in range (0,n+1):
        ans += (x**k) * cosine_coeff(k)
    return ans

def inverse_t(x,n):
    ans = 0
    for k in range (0,n+1):
        ans += (x**k) * inverse_coeff(k)
    return ans

def natural_log_t(x,n):
    ans = 0
    for k in range (0,n+1):
        ans += (x**k) * natural_log_coeff(k)
    return ans

def tan_inv_t(x,n):
    ans = 0
    for k in range (0,n+1):
        ans += (x**k) * tan_inv_coeff(k)
    return ans




# print(expn_t(3,3))
# print (cosine_t(pi/2 , 5))