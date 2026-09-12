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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode temp = new ListNode(-1);
        ListNode temp2 = temp;

        ListNode traverseList1 = list1;
        ListNode traverseList2 = list2;

        while(traverseList1!=null && traverseList2!=null){
            if(traverseList1.val <= traverseList2.val){
                temp2.next = traverseList1;
                traverseList1 = traverseList1.next;
            }
            else if(traverseList1.val > traverseList2.val){
                temp2.next = traverseList2;
                traverseList2 = traverseList2.next;
            }
            temp2 = temp2.next;
        }

        if(traverseList1!=null){
            temp2.next = traverseList1;
        }
        else{
            temp2.next = traverseList2;
        }

        return temp.next;
    }
}