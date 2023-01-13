
def natural_log_coeff(n):

    if (n == 0) :
        return 0

    elif ((n % 2 == 0) and (n!= 0)):
        return -1/(n)

    else :
        return 1/(n)

print (natural_log_coeff(2))