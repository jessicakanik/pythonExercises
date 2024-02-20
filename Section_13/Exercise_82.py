
def convert (binary):
    if decimal == 0:
        return '0'
    else:
        return (convert(decimal//2)+str(decimal%2)).lstrip("0")


