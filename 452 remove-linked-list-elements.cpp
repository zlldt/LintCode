/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


class Solution {
public:
    /*
     * @param head: a ListNode
     * @param val: An integer
     * @return: a ListNode
     */
    ListNode * removeElements(ListNode * head, int val) {
        ListNode dummy;
        dummy.next=head;
        head=&dummy;
        
        while(head->next!=NULL){
            if(head->next->val == val){
                head->next=head->next->next;
            }
            else{
                head=head->next;
            }
        }
     
    return dummy.next;
        // write your code here
    }
};
