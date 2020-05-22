def subsets(nums):
    result = []
    def helper(size, first = 0, subset = []):
        if size == 0:
            print(subset)
            result.append(subset[:])
            return
        # branching to generate additional nodes
        for i in range(first, len(nums)):
            subset.append(nums[i])
            helper(size-1, i+1, subset)
            subset.pop()
    # unique tree for each possible size
    for n in range(0, len(nums)+1):
        helper(n)
    return result

print(subsets([1,2,3]))
