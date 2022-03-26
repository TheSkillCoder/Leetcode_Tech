class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for ind, val in enumerate(nums):
            if val not in dic.keys():
                dic[val]=[ind]
            else:
                dic[val].append(ind)

        for i in nums:
            if target-i == i and len(dic[target-i])>1:
                return[dic[i][0], dic[target-i][1]]
            elif target-i == i and len(dic[target-i])==1:
                continue
            if target-i in dic:
                return[dic[i][0], dic[target-i][0]]