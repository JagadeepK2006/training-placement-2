class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        current=head
        result=''
        while current.next:
            result+=str(current.val)
            current=current.next
        result+=str(current.val)
        m=0
        snc,result=0,result[::-1]
        print(result)
        for i in result:
            snc+=int(i)*2**m
            m+=1
        
        return snc
