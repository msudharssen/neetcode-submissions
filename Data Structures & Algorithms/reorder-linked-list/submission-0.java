/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {

        ArrayList<ListNode> arr = new ArrayList();

        ListNode curr = head;

        while (curr!=null){
            arr.add(curr);
            curr = curr.next;
        }

       
        int a = 0;
        int b = arr.size()-1;

        while (a < b){
            arr.get(a).next = arr.get(b);
            a++;
            if(a==b){
                break;
            }
            arr.get(b).next = arr.get(a);
            b--;
        }

        arr.get(a).next = null;

        
    }
}
