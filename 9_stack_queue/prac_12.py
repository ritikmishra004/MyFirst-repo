# nextGreaterElement

def nextGreaterElement(nums1, nums2):
        stack = []
        nge_map = {}  #  Map to store next greater for each number in nums2

        # Traverse nums2 from right to left
        for num in reversed(nums2):
            # Remove all smaller elements from stack
            while stack and stack[-1] <= num:
                stack.pop()
            
            #  If stack not empty, top is next greater
            nge_map[num] = stack[-1] if stack else -1

            # Push current element
            stack.append(num)
        
        # Get result for each element in nums1 from the map
        return [nge_map[num] for num in nums1]

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))
