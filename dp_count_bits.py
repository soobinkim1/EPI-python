def countBits(self, num: int) -> List[int]:
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]
    result = [None] * (num+1)
    result[0] = 0
    result[1] = 1

    prev_end = 1
    new_end = 2
    i = 2
    j = 0
    while i <= num:
        result[i] = result[j] + 1
        j += 1
        if result[i] == new_end:
            prev_end = new_end
            new_end += 1
            j = 0
        i += 1
    return result