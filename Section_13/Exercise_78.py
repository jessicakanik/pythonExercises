# greates common divisor

# need to use function for this

def find_gcd (a,b):
    if b == 0:
        return a
    else :
        return find_gcd(b,a%b)