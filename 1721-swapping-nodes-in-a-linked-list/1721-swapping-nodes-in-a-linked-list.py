# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        for i in range(k-1):
            temp=temp.next
            
        temporary=temp
        l=k
        while(temporary.next!=None):
            l+=1
            temporary=temporary.next
        temporary=head
        for i in range(l-k):
            temporary=temporary.next
        
        temp.val, temporary.val = temporary.val, temp.val
        return head