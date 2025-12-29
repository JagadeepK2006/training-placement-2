public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head==null || head.next==null)
        {
            return null;
        }
        ListNode fast = head;
        ListNode slow = head;
        while(fast!=null && fast.next!=null)
        {
            slow = slow.next;
            fast=fast.next.next;
            if(slow==fast)
            {
                //LL is cyclic
                //Make the slow pointer to point head and iterate single movement of slow and fast.
                //Collision point is start of cycle
                slow=head;
                while(slow!=fast)
                {
                    slow=slow.next;
                    fast=fast.next;
                }
                return slow;
               
            }
        }
        return null;
    }
}
