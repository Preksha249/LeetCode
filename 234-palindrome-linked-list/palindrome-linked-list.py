# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        list = []
        list2 = []
        while head:
            list.append(head.val)
            head = head.next
        r= len(list)-1
        while r>=0:
            list2.append(list[r])
            r-=1
        print(list,list2)
        return list == list2

       