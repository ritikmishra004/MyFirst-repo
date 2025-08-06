# nextGreaterElement

def nextGreaterElement(nums1, nums2):
    res = []
    for num in nums1:
        found = False
        next_greater = -1
        for i in range(len(nums2)):
            if nums2[i] == num:
                found = True
            if found and nums2[i] > num:
                next_greater = nums2[i]
                break
        res.append(next_greater)
    return res

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))
