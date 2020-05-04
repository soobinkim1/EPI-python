
'''
Process:
1. get [items less than pivot][pivot][items more than pivot]
2. get location of pivot
3. re-arrange [items < pivot] and [items > pivot] into [items less than pivot][pivot][items more than pivot]
4. when [one or no item less than pivot][pivot][one or no item greater than pivot], we know it's all been sorted

'''
import random

def quicksort(nums):
    if len(nums) <= 1:
        return nums

    pivot = random.choice(nums)

    left = [n for n in nums if n < pivot]
    same = [n for n in nums if n == pivot]
    right = [n for n in nums if n > pivot]

    return quicksort(left) + same + quicksort(right)

print(quicksort([3,4,5,1]))

'''
In-place:

'''

def quicksort_inplace(nums, l = 0, r = None):
    if r = None:
        r = len(nums) - 1
    if l < r:
        pivot_index = partition(nums, l, r)
        quicksort_inplace(nums, l, pivot_index - 1) # sort the section below pivot
        quicksort_inplace(nums, pivot_index + 1, r) # sort the seciton above pivot

def partition(nums, l, r):
    i = l - 1 # begins below the left index
    pivot = nums[high]
    for j in range(l, r):
        # i is the end of the lesser portion
        if nums[j] <= pivot:
            i += 1 # length of the lesser section increases by 1
            nums[i], nums[j] = nums[j], nums[i] # nums[j], which has been determined to be in the lesser section, is added 
    # swap pivot with one of the greater-than elements
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1 # return beginning of the high value

