
# Last two digits of my entry number is 56 and remainder when divided by 4 is 0.

## Question 1

def expn (x,n) :
# value of function till x^n using taylor expansion of funtion e^x
#
# Input Parameters
# x : float --- the point at which value of function is to be calculated
# n : int --- power till which value of function is to be calculated in taylor expansion
# 
# variable fst_term contains value to be returned when n<= 1 or x == 0 (the base case)
#
# Output : ans is the output for cases other than n<=1 or x==0

    fst_term = 1

# Conditionals on n and x :

    if n <= 1 or x == 0 :    # T(k) for considering time k where k is constant for checking the conditions and returning output
        return fst_term    

    else :    # T(k) where k is constant
          
        # ans is the variable that contains output of the function
        ans = 1 # initialise ans to 1                             T(k) where k is constant - just assigning a variable
        # prod_ is the product of previous ratio and last power coeff 
        prod_ = 1  # initialise prod_ to 1                       T(k) where k is constant - assigning variable 
        # i_term varies from 2 to n                                            
        # so we exit the loop when i_term = n+1
        # invariants : ratio = x/(i_term - 1)
        #              ans = sum(x^i/i!) i_term varies from 2 to i
        for i_term in range (2,n+1) :                                 # T(n) - passing n-1 values through loop
           # initialises from i_term = 2
            ratio = x / (i_term - 1) # T(k) where k is constant
            prod_ = prod_ * ratio  # T(k) where k is constant
            ans = ans + prod_   # T(k) where k is constant
            # Terminates for i_term = n+1
            # Exits the loop for i_term > n
        return ans # gives out the value of function # Time complexity of function is O(n)


import math
pi = math.pi


def cosine (x , n) :
    # value of function till x^n using taylor expansion of funtion Cos(x)
    #
    # Input Parameters
    # x : float --- the point at which value of function is to be calculated
    # n : int --- power till which value of function is to be calculated in taylor expansion
    # 
    # variable fst_term contains value to be returned when n<= 1 or x == 0 (the base case)
    #
    # Output : ans is the output for cases other than n<=1 or x==0
    fst_term = 1

    # Conditionals on n and x :
    if n <= 1 or x == 0 :         # T(k) for considering time k for checking the conditions and returning output
        return fst_term

    else :          # T(k) where k is constant for condition
          
        # ans is the variable that contains output of the function
        ans = 1 # initialise ans to 1                         T(k) where k is constant for assigning variable
        # prod_ is the product of previous ratio and last power coeff
        fst_term = 1

        prod_1 = 1   # initialise prod_ to 1            T(k) where k is constant
        # i_term varies from 2 to n                                            
        # so we exit the loop when i_term = n+1
        # invariants : ratio = -x * x/(i_term - 1)*(i_term-2)
        #              
        
        for i_term in range (3, 2*n, 2) :      # T(n) - passing n-2 values through loop
            # initialises from i_term = 2 
            ratio = - x * x /((i_term - 1)*(i_term - 2))  # T(k) where k is constant
            prod_1 = prod_1 * ratio # T(k) where k is constant for multiplying
            ans = ans + prod_1 # T(k) where k is constant for adding
            # Terminates for i_term = 2*n
            # Exits the loop for i_term > 2*n - 1   
    return ans  # gives out the value of function # Time complexity of function is O(n)




def inverse (x , n) :
    # value of function till x^n using taylor expansion of funtion 1/1-x
    #
    # Input Parameters
    # x : float --- the point at which value of function is to be calculated such that |x|<1
    # n : int --- power till which value of function is to be calculated in taylor expansion
    # 
    # Output : ans is the output for cases other than  |x|>=1
    #
    # Conditionals on n and x :
    if (abs(x) >= 1) :          # T(k) for considering time k for checking the conditions and returning output
        return "function not defined for the given value"

    elif (x==0) :
        return 1

    else :      # T(k) where k is constant for condition
          
        # ans is the variable that contains output of the function

        value_1 = 1/x    # initialise value_1 to 1/x

        _ = 1  # initialise i_term to 1

        ans = 0

        ratio = x

        # i varies from 1 to n                                            
        # so we exit the loop when i_term = n+1
        # invariants : i_term = x^(i) where i varies from 1 to n

        for i_term in range (1,n+1):             # T(n) - passing n values through loop
            # i initialises from i=1
            ans = ans + value_1 * ratio     # T(k') where k' is some constant

            value_1 = value_1 * ratio       # T(k) where k is constant for muultiplying
            
        # Terminates for i_term = n + 1
        # Exits the loop for i_term > n
            
        return ans # gives out the value of function # Time complexity of function is O(n)


def natural_log(x , n) :
    # value of function till x^n using taylor expansion of funtion ln(1+x)
    #
    # Input Parameters
    # x : float --- the point at which value of function is to be calculated such that x>-1
    # n : int --- power till which value of function is to be calculated in taylor expansion
    # 
    # Output : ans is the output 
    
    i_term = 1       # initialise i_term to 1
    ans = 0              # initialise ans to 0
    prod_ = 1
    # i varies from 1 to n                                            
    # so we exit the loop when i_term = n+1
    # invariants : ratio = -x
    #              
    for i_term in range (1,n+1) :       # T(n) - passing n values through loop

        ratio = -x 
        prod_ = prod_ * ratio           # T(k') where k' is some constant
        ans = ans - (prod_/i_term)      # T(k') where k' is some constant
        # Terminates for i_term = n + 1
        # Exits the loop for i_term > n
    return ans      # gives out the value of function # Time complexity of function is O(n)



def tan_inv(x , n):
    # value of function till x^n using taylor expansion of funtion arc tan(x)
    #
    # Input Parameters
    # x : float --- the point at which value of function is to be calculated 
    # n : int --- power till which value of function is to be calculated in taylor expansion
    # 
    # Output : ans is the output 

     i_term = 1 # initialise i_term to 1

     ans = 0    # initialise ans to 0

     prod_ = 1
    # i_term varies from 1 to 2*n-1 with a jump of 2 integers                                            
    # so we exit the loop when i_term = 2n
    # invariants : ratio = -x * x
     for i_term in range (1,2*n, 2) :       # T(n) - passing n values through loop

    
         ratio = -x * x             # T(k) where k is some constant
         prod_ = prod_ * ratio      # T(k) where k is some constant
         ans = ans - (prod_/i_term) # T(k) where k is some constant
        # Terminates for i_term = 2*n
        # Exits the loop for i_term > 2*n-1
     return ans    # gives out the value of function      # Time complexity of function is O(n)

#-----------------------------------------------------------------------------------------------------

## Qusetion 2

import math

def f(x):
    return (math.cos(x) + math.exp(-x))

e = math.exp(1)



def bisect(a , b , eps):
    # roots of the function cos(x) + e^(-x) with a tolerance of eps
    #
    # Input Parameters
    # a , b : float 
    # eps : float
    # 
    # Output : (found , x0 , L) where x0 is root of equation and L is the iterative list formed
    x0 = a #initialise x0=a 
    found = False
    L = []
    # Let the time taken of bisect(a,b,eps) for singlefirst step is T(b-a) 
    # For the subsequent step, it will become T(b-a/2) as the interval becomes half , similarly it will be halved to T(b-a/4) in the next
    #   step ..............We can see T(1) [where b-a is 1 for the respective step] = 1. So by solving the series of equations formed
    #    we get time complexity for the function is O(log(n))  where n is difference of the interval initially taken and base of log is 2
    # invariant x0 = (a+b)/2
    while (a<b) and (not found):    # exits the loop when a=b or found true
        x0 = (a + b)/2  # T(k)          
        L.append(x0)    # T(k)
        val = f(x0)     # T(k)
        # invariant x0 = (a+b)/2
        if ((f(a) > 0 and f(b) < 0) or (f(a) < 0 and f(b) > 0)):

            if (abs(val) < eps)  :
                found = True

            elif val > 0 :
                a = x0
                found = False


            elif val < 0 :
                b = x0
                found = False
            

        elif (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0) :
            return (found , x0 , L)
    # Exits the loop when a=b or found == true 

    return (found , x0 , L)
# print (bisect(0,3,0.1))
#--------------------------------------------------------------------------------------------------------------

## Question 3


def expn_coeff(n) : # gives the coefficient of x^n in e^x taylor expansion
    # n: int ---- the power of x whose coeff to find
    if (n==0) : #T(1) for checking value of n
        return 1

    else :
        x1 = 1 #initialise x1 to 1
        # invariant ratio = 1/i
        for i in range (1,n+1): # i varies from 1 to n     # T(n) for passing n values through loop
            x1 = x1 * (1/i) # T(1) for performing multiplication
        # exit loop for i > n+1
        # terminates for i = n + 1 
        return x1 # givves coeff. of x^n # O(n) is the time complexity



def cosine_coeff(n) :        #Time complexity is O(n)

    if (n==0) :     #T(1) for checking value of n
        return 1

    else :

        if (n%2 != 0) : #T(1) for checking value of n
            return 0

        else :
            x1 = 1
            # invariant : ratio = -1/((i - 1)*(i - 2))
            # exit loop when i = n + 2 i.e. i-n-2 decreases to 0
            for i in range (3,n+2,2) : # T(n) for passing order n (count) values
                ratio = - 1 /((i - 1)*(i - 2))
                x1 = x1 * ratio
                # Loop terminates for i = n+2
            return x1  


def inverse_coeff(n) : # Time complexity of order O(1) for retuning constant 1 
    return 1


def natural_log_coeff(n):# Time complexity of order O(1) for simply returning a value without operations 

    if (n == 0) :  #T(1)
        return 0

    elif ((n % 2 == 0) and (n!= 0)): # T(1)
        k1 = -1/n
        return k1

    else : #T(1)
        k2 = 1/n
        return k2


def tan_inv_coeff(n) :  # Time complexity of order O(1) for simply returning a value without operations by checking codition for n
    if (n % 4 == 0)  :    #T(1)
        return 0

    elif  (n % 4 == 2):   #T(1)
        return 0

    elif (n % 4 == 1) : #T(1)
        k1 = 1/n
        return k1

    else :      #T(1)
        k2 = -1/n
        return k2

#---------------------------------------------------------------------------------------------------------

## Question 4

def expn_t(x,n):
    ans = 0  #initialise ans to 0
    # invariant : ratio = x*k
    # loop exits when k=n+1
    # k-n-1 decreases to 0 
    for k in range (0,n+1):     # T(n) for passing n+1 values in loop with constant time operations
        # k varies from 0 to n
        ratio = (x**k)
        ans += ratio * expn_coeff(k)   # T(1) for multiplying and performing expn_coeff(k) function
        #Loop Terminates for k = n + 1 
    return ans  # gives out sum of series till power n # Time complexity O(n)

def cosine_t(x,n):
    ans = 0  # initialise ans to 0
    # invariant : ratio = x**k
    # loop exits when k=n+1
    # k-n-1 decreases to 0
    for k in range (0,n+1):     # T(n) for passing n+1 values in loop with constant time operations
        # k varies from 0 to n
        ratio = x**k
        ans += ratio * cosine_coeff(k)      # T(1) for multiplying and performing cosine_coeff(k) function
    #Loop Terminates for k = n + 1
    return ans  # gives out sum of series till power n    # Time complexity O(n)


def inverse_t(x,n):
    ans = 0 # initialise ans to 0
     # invariant : ratio = x**k
    # loop exits when k=n+1
    # k-n-1 decreases to 0
    for k in range (0,n+1):# T(n) for passing n+1 values in loop with constant time operations
        ans += (x**k) * inverse_coeff(k) # T(1) for multiplying and performing inverse_coeff(k) function
    return ans  # gives out sum of series till power n  # Time complexity O(n)


def natural_log_t(x,n):
    ans = 0 # initialise ans to 0
    # invariant : ratio = x**k
    # loop exits when k=n+1
    # k-n-1 decreases to 0
    for k in range (0,n+1): # T(n) for passing n+1 values in loop with constant time operations
        ans += (x**k) * natural_log_coeff(k)  # T(1) for multiplying and performing natural_log_coeff(k) function
    return ans  # gives out sum of series till power n    # Time complexity O(n)

def tan_inv_t(x,n):
    ans = 0  # initialise ans to 0
    # invariant : ratio = x**k
    # loop exits when k=n+1
    # k-n-1 decreases to 0
    for k in range (0,n+1):
        ans += (x**k) * tan_inv_coeff(k)
    return ans      # gives out sum of series till power n     # Time complexity O(n)

#-----------------------------------------------------------------------------------------------------------

## Question 5
               
def add_coeff(n):   # T(n) = T(cosine_coeff(n)) + T(natural_log_coeff(n)) = = O(1)
    return  cosine_coeff(n) + natural_log_coeff(n)      # adding coefficient of x^n in both expansions

def mul_coeff(n):  
    i = 0 # initialise i = 0
    ans = 0 # initialise ans = 0
    # invariant : term = (natural_log_coeff(i)) * (cosine_coeff(n-i))
    # Exits loop when i > n 
    while i<= n : # T(n+1) * 1
        # using basic concept of binomial theorem to find coefficient from product variable sums
        z1 = (natural_log_coeff(i))
        z2 = (cosine_coeff(n-i))
        term = z1 * z2 # T(natural_log_coeff(i))+T(cosine_coeff(n-i)+1
        ans = ans + term # T(1) for adding 
        i = i + 1
    # Loop exit : i > n
    # loop terminates for i = n+1
    return ans  # Time complexity is O(n)

def diff_coeff(n) :         # Time complexity is O(n)
    # By observing pattern we can see coeff. of x^n in diff. of cosine is (n+1) times coeff. of x^(n+1) in expansion of cosine
    z1 = cosine_coeff(n+1)
    finalcoeff =  (n+1) * z1  # T(1) for multiplying and T(cosine_coeff) is O(n)
    return finalcoeff

#--------------------------------------------------------------------------------------------------------------

## Question 6


## HELPER FUNCTIONS


def sin(x,n):       # Time complexity w.r.t x and constant n=20 is O(1) as it is O(n)  similar to Cosine function
    _ = x

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


def tan(x):     #Time complexity is O(1) for dividing the functions with time complexities of O(1)
    return sin(x,20)/cosine(x,20)

## MAIN FUNCTION

def limit_diff(x, epsilon) :  # Time complexity of the function is O(1) w.r.t x  

    if (epsilon == 0) :
        return 1   # T(1) for returning the value

    else :   
        a = tan(x) # T(1)
        b = x + epsilon # T(1) for addition
        z1 = tan(b) - tan(x) # T(1) for subtracting and executing tan(b) andtan(x)
        z2 = z1/epsilon # T(1) for dividing
    
        return z2

# print (limit_diff(10,0.000001))

#-------------------------------------------------------------------------------------------------------------

