def subsets(self, nums):
    output = [[]]``
    for num in nums: # outer loop for each number
        output += [curr + [num] for curr in output] # inner loop for each element currently in output
    return output