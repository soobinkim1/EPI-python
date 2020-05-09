def permutation(arr, k):
    # permutation of an array
    # choice: which item to add next
    # constraint: if already used, then should not add
    result = []
    used = [False] * len(arr)

    def helper(depth = 0, solution = []):
        # when depth is k, append to result
        # at each execution context, need candidate, depth, 
        if depth == k:
            result.append(solution[:])
            return

        for i in range(len(arr)):
            # constraint for the search
            if not used[i]:
                used[i] = True
                solution.append(arr[i]) 
                    # build up the partial solution
                    # partial solution is maintained by appending, rather than passing candidate + arr[i] which would return a new array
                #print(solution)
                helper(depth + 1, solution)
                # backtrack by removing the last adjustment from the solution
                solution.pop()
                #print('backtrack: ', solution)
                used[i] = False
    helper()
    return result

print(permutation([1,2,3], 3))
print(permutation([1,2,3], 1))