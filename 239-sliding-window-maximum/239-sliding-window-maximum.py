class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        temp = collections.deque()
        ans=[]
        left = right = 0
        
        while(right<len(nums)):

            while(len(temp)!=0 and nums[temp[-1]]<nums[right]):
                temp.pop()
            temp.append(right)
            
            if left>temp[0]:
                temp.popleft()
            
            if right+1>=k:
                ans.append(nums[temp[0]])
                left+=1
                
            right+=1
            
        return ans