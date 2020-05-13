
def sortColors(arr):
    '''
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    '''
    b1 = 0 # all zeros are to the left of this
    # all 1s are between b1 and b2
    b2 = len(arr) - 1 # all 2s are to the right of this
    i = 0
    while i <= b2: # everything past b2 is 2
        if arr[i] == 0:
            arr[i], arr[b1] = arr[b1], arr[i]
            b1 += 1 # since there's a 0 to its left
            i += 1 # since 0 has been properly placed & no longer needs to be processed
        elif arr[i] == 1:
            i += 1 # 0s and 2s have not changed, and therefore pointers do not need to be moved
        elif arr[i] == 2:
            arr[i], arr[b2] = arr[b2], arr[i]
            b2 -= 1 # since there's 2 to the right
            # i does not change, since the new number also needs to be checked
    return arr