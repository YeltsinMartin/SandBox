#include"ProblemHeaders.h"

void symmetricDifference(list<int> arr1, list<int> arr2)
{
    /*Find the Symmetric Difference
The mathematical term symmetric difference (△ or ⊕) of two sets is the set of elements which are in either of the two sets but not in both. For example, for sets A = {1, 2, 3} and B = {2, 3, 4}, A △ B = {1, 4}.

Symmetric difference is a binary operation, which means it operates on only two elements. So to evaluate an expression involving symmetric differences among three elements (A △ B △ C), you must complete one operation at a time. Thus, for sets A and B above, and C = {2, 3}, A △ B △ C = (A △ B) △ C = {1, 4} △ {2, 3} = {1, 2, 3, 4}.
*/
    cout << "Symmetric Difference: ";
    for (auto i : arr1)
    {
        bool found = false;
        for (auto j : arr2)
        {
            if (i == j) {
                arr2.remove(i);
                found = true;
                break;
            }
        }
        if (!found) cout << i;
    }
    for (auto i : arr2) cout << i;
    cout << endl;
}

void inventoryUpdate(vector<inventory> cur, vector<inventory> update) {
    /*
    Inventory Update
Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. 
Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array.
The returned inventory array should be in alphabetical order by item.
    */
    cout << "\n\nInventory Update : \n";
    for (inventory& i : update) 
    {
        bool found = false;
        for (inventory& j : cur) 
        {
            if (j.name == i.name) {
                j.number += i.number;
                found = true;
                break;
            }
        }
        if (!found) 
        {
            cur.push_back(i);
        }
    }
    for (auto i : cur) {
        cout << i.name << "\t" << i.number << "\n";
    }
}

vector<vector<char>> ans;
void permute(vector<char>& a, int idx) {
    
    if (idx == a.size()) {
        ans.push_back(a);
        return;
    }
    for (int i = idx; i < a.size(); i++) {
        swap(a[i], a[idx]);
        permute(a, idx + 1);
        swap(a[i], a[idx]);
    }
    return;
}

void permAlone(string input) {
    /*
    No Repeats Please
    Return the number of total permutations of the provided string that don't have repeated consecutive letters. 
    Assume that all characters in the provided string are each unique.
    For example, aab should return 2 because it has 6 total permutations (abc, bac, acb, bca, cab, cba), 
    but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.
    */
    vector <char> inputList;

    for (auto i : input) {
        inputList.push_back(i);
    }

    permute(inputList, 0);
    for (auto i : ans) {
        for (auto j : i) {
            cout << j;
        }
        cout << "\n";
    }
}


void slidingWindowCompare(vector<int> list, int windowSize) {
    for (int i = 0; i <=(list.size()-windowSize); i++) {
        int max = list.at(i);
        for (int j = i+1; j < i+ windowSize; j++) {
            if (max < list.at(j)) max = list.at(j);
        }
        cout << max;
    }
}

// Dynamic Programming

unsigned long long fibonacci(int num, map<int, unsigned long long>& prevFib) {
    if (num <= 0) return 0;
    else if (num <= 2) return 1;
    else if (prevFib.find(num) == prevFib.end())
        //prevFib.insert({ num, fibonacci(num - 1, prevFib) + fibonacci(num - 2, prevFib) });
        prevFib[num] = fibonacci(num - 1, prevFib) + fibonacci(num - 2, prevFib);
    return prevFib.at(num);
}

int _binarySearch(vector<int>& data, int val, int start, int end) {
    if (start > end) return -1;
    int mid = (start + end) / 2;
    if (data.at(mid) == val) return data.at(mid);
    else if (data.at(mid) > val) return _binarySearch(data, val, start, mid - 1);
    else if (data.at(mid) < val) return _binarySearch(data, val, mid + 1, end);
}

bool binarySearch(vector<int>& data, int val) {
    if (val == _binarySearch(data, val, 0, data.size()))
    {
        cout << val << " Found \n";
        return true;
    }
    else {
        cout << val << " Not Found \n";
        return false;
    }
    return false;
}

int twoCitySchedCost(vector<vector<int>> costs) {
    vector<vector<int>> results;
    for (auto& i : costs) {
        int diff = i.at(1) - i.at(0);
        results.push_back({ diff, i.at(0), i.at(1) });
    }
    sort(results.begin(), results.end());
    int finalSum = 0;
    for (int i = 0; i < results.size(); i++)
    {
        if (i < results.size() / 2) finalSum += results.at(i).at(2);
        else finalSum += results.at(i).at(1);
    }
    return finalSum;
}


vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
    vector<vector<int>> result;

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            result.push_back({ abs(rCenter - row), abs(cCenter - col) });
        }
    }
    cout << "[";
    for (auto& i : result) {
        cout << "[";
        for (auto& j : i) {
            cout << j;
        }
        cout << "]";
    }
    cout << "]\n";
    return result;
}

int maxSumTwoNoOverlap(vector<int> nums, int firstLen, int secondLen) {

    int firstMax = 0;
    int secondMax = 0;
    vector<vector<int>> vectPos = { {}, {} };
    for (int outerloop = 0; outerloop <= nums.size() - firstLen; outerloop++) {
        int max = nums.at(outerloop);
        for (int innerLoop = outerloop+1; innerLoop < outerloop + firstLen; innerLoop++) {
            max += nums.at(innerLoop);
        }
        if (firstMax < max) { 
            firstMax = max;
            vector<int> tmp;
            for (int pos = outerloop; pos < outerloop + firstLen; pos++) tmp.push_back(pos);
            vectPos.at(0) = tmp;
        }
    }
    cout << "[";
    for (auto& i : vectPos.at(0)) cout << nums.at(i);
    cout << "]\n";

    vector<int> newList;
    for (int i = 0; i < nums.size(); i++) {
        bool found = false;
        for (auto& j : vectPos.at(0) ){
            if (j == i) { found = true; break; }
        }
        if (!found) newList.push_back(nums.at(i));
    }

    for (int outerloop = 0; outerloop <= newList.size() - secondLen; outerloop++) {
        int max = newList.at(outerloop);
        for (int innerLoop = outerloop + 1; innerLoop < outerloop + secondLen; innerLoop++) {
            max += newList.at(innerLoop);
        }
        if (secondMax < max) {
            secondMax = max;
            vector<int> tmp;
            for (int pos = outerloop; pos < outerloop + secondLen; pos++) tmp.push_back(pos);
            vectPos.at(1) = tmp;
        }
    }
    cout << "[";
    for (auto& i : vectPos.at(1)) cout << newList.at(i);
    cout << "]\n";
    return secondMax + firstMax;

}



Node<int>* addLists(Node<int>* list1, Node<int>* list2, int carry, Node<int>* res) {
    if (list1 == nullptr && list2 == nullptr) return res;

    int val1 = list1 != nullptr ? list1->value : 0;
    int val2 = list2 != nullptr ? list2->value : 0;

    int sum = val1 + val2 + carry;
    carry = sum > 10 ? 1 : 0;
    sum = sum % 10;

    Node<int>* ptr = res;
    if (ptr == nullptr) {
        res = new Node(sum);
    }
    else
    {
        while (ptr->next != nullptr) {
            ptr = ptr->next;
        }
        ptr->next = new Node(sum);
    }
    addLists(list1->next != nullptr ? list1->next : nullptr, list2->next != nullptr ? list2->next : nullptr, carry, res);

}


int eraseOverlapIntervals(vector<vector<int>> intervals) {

    less<vector <int>> ls;
    sort(intervals.begin(), intervals.end(), ls);

    int prev = intervals[0][1];
    int refcount = 0;
    for (int i = 1; i < intervals.size(); i++) {
        int start = intervals[i][0], end = intervals[i][1];
        if (start < prev) {
            refcount++;
            prev = min(end, prev);
        }
        else {
            prev = end;
        }
    }
    return refcount;
}

int numRescueBoats(vector<int> people, int limit) {

    less<int> ls;
    sort(people.begin(), people.end(), ls);
    int l = 0, r = people.size() -1 ;
    int numOfBoats = 0;
    while(r >= l) 
    {
        int capacityLeft = limit  - people.at(r);
        numOfBoats++;
        r--;
       if (l != r && capacityLeft < people[l]) {
           l++;
        }
    }
    return numOfBoats;

}

void splitOddEvenSort(vector<int> data) {

    set<int, less<int>> odd, even;

    for (auto& val : data) {
        if (val & 0x1) odd.insert(val);
        else even.insert(val); 
    }
}

vector<string> findRepeatedDnaSequences(string s) {
    set<string> data, result;
    for (int i = 0; i <= s.length() - 10; i++) {
        string substr = s.substr(i, 10);
        if (data.find(substr)!= data.end()) {
            result.insert(substr);
        }
        else {
            data.insert(substr);
        }
    }
    vector<string> res;
    for (auto& str : result) res.push_back(str);
    return res;
}

void rotateArray(vector<int> nums, int k) {
    list<int> data(nums.begin(), nums.end());
    for (int i = 0; i < k; i++) {
        data.push_front(data.back());
        data.pop_back();
    }
    cout << "["; for (auto& i : data) cout << i; cout << "]\n";
}

uint32_t reverseBits(uint32_t n) {
    uint32_t rev = 0;
    bool val = false;
    for (short i = 0; i < 32; i++) {
        val = n & (0x1 << i); //get bit
        rev = (rev << 1) + val; //append bit
    }
    return rev;
}

int hammingWeight(uint32_t n) {
    int count = 0;
    for (int i = 0; i < 32; i++) {
        n& (0x1 << i) ? count++ : count;
    }
    return count;

}

double findMedianSortedArrays(vector<int> nums1, vector<int> nums2) {
    int len = nums1.size() + nums2.size();
    vector<int> merged;
    int counter = 0;
    for(int lpos= 0 , rpos = 0; counter <= len /2 ; counter++ )
    {
        if (lpos >= nums1.size()) {
            merged.push_back(nums2.at(rpos));
            rpos++;
        }
        else if (rpos >= nums2.size()) {
            merged.push_back(nums1.at(lpos));
            lpos++;
        }
        else if (nums1.at(lpos) < nums2.at(rpos)) {
            merged.push_back(nums1.at(lpos));
            lpos++;
        }
        else {
            merged.push_back(nums2.at(rpos));
            rpos++;
        }
    }
    if (len & 0x1) return merged.at(counter-1);
    else return (merged.at(counter-1) + merged.at(counter - 2)) / 2.0;
}

Node<int>* getIntersectionNode(Node<int>* headA, Node<int>* headB) {

    Node<int> *a = headA, *b = headB;
    while (a != b) {
        a = a ? a->next : headB;
        b = b ? b->next : headA;
    }
    return a;
}

int rob(vector<int>& nums) {
    int rob1 = 0, rob2 = 0;
    for (auto& rob : nums) {
        int temp = max(rob + rob1, rob2);
        rob1 = rob2;
        rob2 = temp;
    }
    return rob2;
}


int _climb(int n, vector<int>& data) {
    if (data.at(n-1) != 0) return data.at(n);
    if (n == 1) return 1;
    if (n == 2) return 2;
    else if (n > 2) data.at(n) =  _climb(n - 1, data) + _climb(n - 2, data);
    return data.at(n);
}

int climbStairs(int n) {
    static vector<int> data;
    data.resize(50);
    for (auto& i : data) i = 0;
    return _climb(n, data);
}

bool isAnagram(string s, string t) {
    less<char> ls;
    sort(s.begin(),s.end(), ls);
    sort(t.begin(),t.end(), ls);
    return s.compare(t) == 0 ? true : false;
}

int sumOfSquares(int a) {
    if (a > 9)
    {
        int val = a % 10;
        a /= 10;
        return (val * val) + sumOfSquares(a);
    }
    else return a * a;
}
bool isHappy(int n) {
    set<int> a;
    while (a.find(n) == a.end()) {
        a.insert(n);
        n = sumOfSquares(n);
    }
    return (n == 1) ? true : false;
}

int lastStoneWeight(vector<int> stones) {
    greater<int> gt;
    make_heap(stones.begin(), stones.end());
    
    while (stones.size() > 1) {
        int first = stones.front();
        pop_heap(stones.begin(), stones.end()); stones.pop_back();
        int sec = stones.front();
        pop_heap(stones.begin(), stones.end()); stones.pop_back();
        stones.push_back(abs(first - sec));
    }
    return stones.size() == 1 ? stones.front() : 0;
}

TreeNode* invertTree(TreeNode* root) {
    stack< TreeNode*> st;
    if (root != nullptr) st.push(root);
    while (!st.empty()) {
        TreeNode* ptr = st.top();
        st.pop();
        if (ptr->right) st.push(ptr->right);
        if (ptr->left)  st.push(ptr->left);
        TreeNode* temp = ptr->left;
        ptr->left = ptr->right;
        ptr->right = temp;

    }
    return root;
}

void reverseString(vector<char> s) {
    for (int i = 0, j = s.size()-1; i < s.size()/2; i++, j--) {
        char temp = s.at(i);
        s.at(i) = s.at(j);
        s.at(j) = temp;
    }
}

vector<int> firstandLast(vector<int> data, int val) {
    int left = 0, right = data.size(), mid = 0;
    int start = -1 , end = -1;
    while (left < right) {
        mid = (left + right)/ 2;
        if (data.at(mid) == val && data.at(mid - 1) < val) {
            start = mid;
            break;
        }
        else if (data.at(mid) >= val) right = mid - 1; 
        else  left = mid + 1;
    }
    end = start ;
    while (data.at(end+1) <= val  && end < data.size() && start != -1) {
        end += 1;
    }
    vector<int> out = { start, end };
    return out;
}

int canCompleteCircuit(vector<int> gas, vector<int> cost) {
    bool canComplete = false;
    int start = 0, maxJ = 0;
    while (!canComplete){
        int remain = 0;
        bool started = false;
        for (int j = start; ; j < gas.size() -1 ? j++ : j = 0) {
            if (start == j && started) {
                canComplete = true;
                break;
            }
            started = true;
            
            remain += gas.at(j) - cost.at(j);
            if (remain < 0) {
                maxJ = j;
                break;
            }
            
        }
        if (canComplete) return start;
        start = maxJ + 1;
    }
    return  -1;
}

int findNeighhours(vector<vector<int>>& board, int x, int y) {
    int row, cols, neigh = 0;
    row = board.size();
    cols = board.at(0).size();
    for (int i = x-1; i <= x+1; i++) {
        for (int j = y-1; j <= y+1; j++) {
            if ( (i < 0 | i > row - 1) || (j < 0 | j > cols - 1)  || ((i ==x) & (j ==y)) ){
                continue;
            }
            else {
                if(board.at(i).at(j) == 1 ) neigh++;
            }
        }
    }
    return neigh;
}

void gameOfLife(vector<vector<int>> board) {
    int row, cols;
    row = board.size();
    cols = board.at(0).size();
    while (1) {
        vector<vector<int>> temp;
        for (int i = 0; i < row; i++) {
            vector<int> rowVal;
            for (int j = 0; j < cols; j++) {
                int neighbours = findNeighhours(board, i, j);
                if (neighbours < 2) {
                    rowVal.push_back(0);
                }
                else if (board[i][j] & (neighbours == 2 || neighbours == 3)) {
                    rowVal.push_back(1);
                }
                else if (neighbours == 3) {
                    rowVal.push_back(1);
                }
                else if (neighbours > 3) {
                    rowVal.push_back(0);
                }
                else rowVal.push_back(0);
            }
            temp.push_back(rowVal);
        }
        string out;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < cols; j++) {
                string s = temp[i][j] ? "X\t" : "O\t";
                out.append(s);
                board[i][j] = temp[i][j];
            }
            out.append("\n");
        }
        system("cls");
        system("color 0A");
        cout << out;
        Sleep(500);
    }
    
}