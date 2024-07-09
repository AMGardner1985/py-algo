import heapq

def top_k_elements(arr, k):
    heap = []
    for num in arr:
        # do some logic to push onto heap according 
        # to problems criteria (e.g divisible by 3)
        
        heapq.heappush(heap,(CRITERIA, num))
        if len(heap) > k:
            heapq. (heap)
            
    return[num for num in heap]