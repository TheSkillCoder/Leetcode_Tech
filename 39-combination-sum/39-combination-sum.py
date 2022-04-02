import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        
        def recursion(ind, target, lst):
            if target<0 or ind>=len(candidates):
                return
            if target==0:
                ans.append(lst)
                return
            l=copy.deepcopy(lst)
            l.append(candidates[ind])
            recursion(ind, target-candidates[ind], l)
            recursion(ind+1, target, lst)
            
        recursion(0, target, [])
        return ans