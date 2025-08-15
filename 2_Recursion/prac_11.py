def subsequences(arr):
    def helper(index, current):
        if index == len(arr):        # Base case
            print(current)
            return
        
        # Include
        helper(index + 1, current + [arr[index]])
        
        # Exclude
        helper(index + 1, current)
    
    helper(0, [])
    
subsequences([1, 2, 3])
