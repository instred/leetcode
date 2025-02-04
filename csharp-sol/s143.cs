namespace csharp_sol 
{

    public static class S143 
    {
        public static void ReorderList(ListNode head) 
        {
            
            if (head.next == null)
            {
                return;
            }
            ListNode slow = head;
            ListNode fast = head.next;

            while (fast != null && fast.next != null)
            {
                slow = slow.next;
                fast = fast.next.next;
            }
            
            ListNode l2 = slow.next;
            slow.next = null;

            ListNode prev = null;
            ListNode tmp;

            while (l2 != null)
            {
                tmp = l2.next;
                l2.next = prev;
                prev = l2;
                l2 = tmp;
            }
            ListNode tmp2;
            ListNode l1 = head;
            while (prev != null)
            {
                tmp = l1.next;
                tmp2 = prev.next;
                l1.next = prev;
                prev.next = tmp;
                l1 = tmp;
                prev = tmp2;
            }
            
        }
    }
}
