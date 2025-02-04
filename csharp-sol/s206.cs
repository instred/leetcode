namespace csharp_sol 
{
    public class ListNode 
    {
        public int val;
        public ListNode next;
        public ListNode(int val = 0, ListNode next = null) 
        {
            this.val = val;
            this.next = next;
        }
    }

    public static class S206 
    {
        public static ListNode ReverseList(ListNode head) 
        {
            
            ListNode tmp;
            ListNode prev = null;

            while (head != null)
            {
                tmp = head.next;
                head.next = prev;
                prev = head;
                head = tmp;
            }
            
            return prev;
        }
    }
}