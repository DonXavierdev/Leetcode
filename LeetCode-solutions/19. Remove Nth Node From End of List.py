'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        temp = 0
        
        while curr:
            temp += 1
            curr = curr.next
        curr = head
        temp -= n
        prev = head
        if temp == 0 :
            head = head.next
            return head
        while temp:
            prev = head
            head = head.next
            temp-=1
        next_node = head.next
        head = prev
        head.next = next_node
        return curr