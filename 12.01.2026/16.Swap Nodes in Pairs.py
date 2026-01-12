class Solution(object):
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        
        temp=head.next 
        head.next=self.swapPairs(temp.next)
        temp.next=head

        return temp
