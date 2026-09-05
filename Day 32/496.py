class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        lookup the value in the nums2 and then seacrh for the next greeater element
        """
        stack = [] 
        mp = {} 
        for num in nums2: 
            while stack and num>stack[-1]: 
                mp[stack.pop()] = num 
            stack.append(num) 
        res = [] 
        for num in nums1: 
            res.append(mp.get(num,-1)) 
        
        return res




        
