def calculate_power(a, b):
    if b == 1:
        return a
    else:
        return a* calculate_power(a,b-1)