
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode tempA=headA;
        ListNode tempB=headB;
        if (headA == null || headB == null) return null;

        while(tempA!=tempB)
        {
            tempA=(tempA==null)?headB:tempA.next;
            tempB=(tempB==null)?headA:tempB.next;
        }
        return tempA;
    }
}
