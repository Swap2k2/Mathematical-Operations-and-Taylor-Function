
def inverse (x , n) :
    if (abs(x) >= 1) :
        return "function not defined for the given value"

    else :

        value_1 = 1/x

        i_term = 1

        ans = 0

        ratio = x

        for i_term in range (1,n+1):
            
            ans = ans + value_1 * ratio

            value_1 = value_1 * ratio

            
        return ans

# print(inverse(0.5,3))

