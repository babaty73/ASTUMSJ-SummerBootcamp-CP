# leetcode problem 83 remove duplicates from sorted list
class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next 
            else:
                current = current.next

        return head