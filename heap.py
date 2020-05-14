def findKthLargest(self, nums):
    '''
    O(N log k), since need to insert into heap of length k, N number of times
    '''
    heap = []
    
    for n in nums:
        if len(heap) < k:
            heap.append(n)
        elif len(heap) == k and n > min(heap):
            # if n is greater, replace with heap
            heap[heap.index(min(heap))] = n
    return min(heap)