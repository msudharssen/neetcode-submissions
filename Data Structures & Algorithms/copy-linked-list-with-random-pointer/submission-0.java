/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node copy = head;
        Node secondCopy = head;
        HashMap<Node, Node> mapOfOriginalNodes = new HashMap();

        while(copy!=null){
            Node nextNode = new Node(copy.val);
            mapOfOriginalNodes.put(copy, nextNode);
            copy = copy.next; 
        }

        while(secondCopy!=null){
            Node nodeToAddNext = mapOfOriginalNodes.get(secondCopy.next);
            Node randomNode = mapOfOriginalNodes.get(secondCopy.random);
            Node toAdd = mapOfOriginalNodes.get(secondCopy);
            toAdd.next = nodeToAddNext;
            toAdd.random = randomNode;
            secondCopy = secondCopy.next;
        }

        return mapOfOriginalNodes.get(head);
        
    }
}
