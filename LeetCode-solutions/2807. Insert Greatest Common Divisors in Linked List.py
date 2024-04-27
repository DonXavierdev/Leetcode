# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            nextnode = curr.next
            comdiv = gcd(curr.val,nextnode.val)
            curr.next = ListNode(comdiv)
            curr.next.next = nextnode
            curr = nextnode
        return head
    
        
