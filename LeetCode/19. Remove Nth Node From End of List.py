class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=ListNode(0,head)
        right=head
        left=temp
        for i in range(n):
            right=right.next

        while right:
            right=right.next
            left=left.next

        left.next=left.next.next
        return temp.next
