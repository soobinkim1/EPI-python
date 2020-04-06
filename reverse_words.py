# take a list of characters and reverse characters in place

def reverse_in_place(chars):
    # if len == 0 or 1, no swap
    # key off of the first half 
    if len(chars) < 2:
        return chars
    for i in range(0, len(chars)//2):
        target = len(chars) - 1 - i
        chars[i], chars[target] = chars[target], chars[i] # in-place swap
    return chars

def reverse_characters(chars, left, right):
    while left < right: 
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

def reverse_words(chars):
    # reverse all first
    reverse_characters(chars, 0, len(chars)-1)
    # reverse individual words
    start = 0
    end = 0
    while end < len(chars):
        if chars[end] == ' ':
            reverse_characters(chars, start, end-1)
            end += 1
            start = end
        else:
            end += 1
    return chars

print(reverse_words(['a','b',' ','c','a','r']))


    
    