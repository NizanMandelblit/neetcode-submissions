class Solution {
public:
    bool hasDuplicate(vector<int> &nums) {
        unordered_map<int, int> hashMap{}; // value to index
        for (int i = 0; i < nums.size(); i++) {
            if (hashMap[nums[i]])
                return true;
            hashMap[nums[i]] = 1;
        }
        return false;
    }
};
