def reverseInteger(x):
    s = int(str(abs(x))[::-1])
    return s * (-1 if x < 0 else 1) if -2**31 <= s <= 2**31 - 1 else 0
