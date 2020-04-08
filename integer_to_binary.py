def integer_to_binary(n):
    # remainder after dividing by 2 is the binary for the very right
    # subsequent remainders (equivalent to 2^2, 2^3, etc.) will be to the left of the previous remainders (ex. remainder after division by 2^2, remainder after division by 2^3, etc.)
    remainders = []
    while n > 0:
        remainder = n % 2
        remainders.append(remainder)
        n = n // 2
    
    binary = ""
    while len(remainders) > 0:
        binary = binary + str(remainders.pop())
    
    return binary