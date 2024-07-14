"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseListrecursive(self, head):
        if not head:
            return None
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return new_head


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    print(Solution().reverseListrecursive(head))
