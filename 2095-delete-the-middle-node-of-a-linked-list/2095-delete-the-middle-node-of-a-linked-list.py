# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        temp = None
        while fast != None and fast.next!= None:
            print("slow", slow.val, "fast", fast.val)
            temp = slow
            slow = slow.next
            fast = fast.next.next
        if temp == None:
            return temp
        temp.next = slow.next
        del slow
        return head
        