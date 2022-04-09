#pragma once

#include<list>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>  
#include<queue>
#include<stack>

#include<Windows.h>

using namespace std;

void symmetricDifference(std::list<int> arr1, std::list<int> arr2);


struct inventory {
    int number;
    string name;
};

void inventoryUpdate( vector<inventory> cur, vector<inventory> update);

void permAlone(string input);

void slidingWindowCompare(vector<int> list , int windowSize);

unsigned long long fibonacci(int num, map<int, unsigned long long>& prevFib);

bool binarySearch(vector<int>& data, int val);

template <class _Ty>
struct grt {
    bool operator()(const _Ty& _Left, const _Ty& _Right) const {
        return _Left < _Right;
    }
};

template <typename _Tx>
struct Node {
    _Tx value;
    Node<_Tx>* next;

    Node(_Tx pass):value(pass), next(nullptr) {
    }
};

template <typename _Tx>
class LinkedList {

    Node<_Tx>* head, *tail;

    int length;
public:

    LinkedList(_Tx val) {
        head = new Node(val);
        tail = head;
        length = 1;
    }

    LinkedList(std::initializer_list<_Tx> item) :head(nullptr), tail(nullptr), length(0){
        for (auto i : item) {
            this->append(i);
            length++;
        }
    }

    void append(_Tx val) {
        if (head == nullptr) {
            head = new Node<_Tx>(val);
            tail = head;
            return;
        }
        Node<_Tx>* ptr = head;
        while (ptr->next != nullptr) ptr = ptr->next;
        tail = new Node<_Tx>(val);
        ptr->next = tail;
    }

    Node<_Tx>* findNode(_Tx val) {
        Node<_Tx>* ptr = head;
        while (ptr != nullptr && ptr->value != val) ptr = ptr->next;
        return ptr;
    }

    void printList() 
    {
        Node<_Tx>* ptr = head;
        while (ptr != nullptr) {
            cout << ptr->value << "\t";
            ptr = ptr->next;
        }
        cout << "\n";
    }

    void reversePrint() {
        _reversePrint(this->head);
        cout << "\n";
    }

    int getLength() { return length; }

    _Tx* at(int pos) {
        if (pos > length || pos < 0) return nullptr;
        int curPos = 0;
        Node<_Tx>* ptr = head;
        while (ptr->next != nullptr && (pos - 1 != curPos)) {
            ptr = ptr->next;
            curPos++;
        }
        return &ptr->value;
    }

    void deleteNode(_Tx value) {
        Node<_Tx>* del;
        if (head->value == value) {
            del = head;
            head = head->next;
            delete del;
            return;
        }
        Node<_Tx>* ptr = head;
        bool found = false;
        while (ptr->next != nullptr ) {
            if (value == ptr->next->value) {
                found = true;
                break;
            }
            ptr = ptr->next;
        }
        if (found) {
            ptr->next = ptr->next->next;
            delete del;
        }
    }

    void partition(int val) {
        Node<_Tx>* next;
        Node<_Tx>* node = head;
        tail = head;
        while (node != nullptr) {
            next = node->next;
            if (node->value < val) {
                node->next = head;
                head = node;
            }
            else {
                tail->next = node;
                tail = node;
            }
            node = next;
        }
        tail->next = nullptr;
    }

    void findKthfromEndRecursive(int k) {
        _findKthNode(this->head, k);
    }

    void findKthfromEndRunner(int k) {
        Node<_Tx>* lead, * kthptr;
        lead = head;
        kthptr = head;
        for (int i = 0; i < k; i++) {
            if (lead != nullptr) lead = lead->next;
            else return; // list not long enough;
        }
        while (lead->next != nullptr) {
            lead = lead->next;
            kthptr = kthptr->next;
        }
        cout << "value: " << kthptr->value <<"\n";
    }

    void reverseList() {
        Node<_Tx>* prev = nullptr, * curr = head, * next = nullptr;
        tail = head;
        while (curr != nullptr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
    }

    Node<_Tx>* getHead() {
        return head;
    }
private:

    int _findKthNode(Node<_Tx>* ptr, int k) {
        int index = 0;
        if (ptr == nullptr) return 0;
        if (ptr->next != nullptr) index =  _findKthNode(ptr->next, k) +1;
        if (index == k) cout << "value " << ptr->value << "\n";
        return index;
    }

    void _reversePrint(Node<_Tx>* ptr)
    {
        if (ptr->next != nullptr) _reversePrint(ptr->next);
        cout << ptr->value << "\t";
    }

};

int twoCitySchedCost(vector<vector<int>> costs);

vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter);

int maxSumTwoNoOverlap(vector<int> nums, int firstLen, int secondLen);

Node<int>* addLists(Node<int>* list1, Node<int>* list2, int carry = 0, Node<int>* res = nullptr);

int eraseOverlapIntervals(vector<vector<int>> intervals); //Leet code 435

int numRescueBoats(vector<int> people, int limit); // Leet Code 881

void splitOddEvenSort(vector<int> data);

vector<string> findRepeatedDnaSequences(string s); //leet code 187

void rotateArray(vector<int> nums, int k); // leet code 189

uint32_t reverseBits(uint32_t n); //leet 190

int hammingWeight(uint32_t n); //leet 191

double findMedianSortedArrays(vector<int> nums1, vector<int> nums2);  //leet 4

Node<int>* getIntersectionNode(Node<int>* headA, Node<int>* headB); //leet160

int climbStairs(int n); //leet 70

bool isAnagram(string s, string t); //leet 242

bool isHappy(int n); // leet 202

int lastStoneWeight(vector<int> stones); //leet 1046

class MyStack {
    queue<int> myQ;

public:
    MyStack() {

    }

    void push(int x) {
        myQ.push(x);
    }


    int pop() {
        int len = myQ.size(), counter = 0;
        if (len > 0) {
            while (counter < len - 1) {
                int val = myQ.front();
                myQ.pop();
                counter++;
                myQ.push(val);
            }
            counter = myQ.front();
            myQ.pop();
        }
        return counter;
    }

    int top() {
        return myQ.back();
    }

    bool empty() {
        return myQ.size() == 0 ? true : false;
    }
}; //leet 225

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
    
};

TreeNode* invertTree(TreeNode* root);

void reverseString(vector<char> s); //leet 344

vector<int> firstandLast(vector<int> data, int val);


int canCompleteCircuit(vector<int> gas, vector<int> cost); //leet 134

void gameOfLife(vector<vector<int>> board); // leet M 289
