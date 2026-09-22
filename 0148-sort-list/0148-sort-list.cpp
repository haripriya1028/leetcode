/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        ListNode* temp=head;
        vector<int>v;
        while(temp!=nullptr){
            v.push_back(temp->val);
            temp=temp->next;
        }
        sort(v.begin(), v.end());
        if(v.empty()) return nullptr;
        
        ListNode* head2= new ListNode(v[0]);
        ListNode* curr=head2;

        for(size_t i=1; i<v.size(); i++){
            curr->next=new ListNode(v[i]);
            curr=curr->next;
        }
        return head2;
    }
};