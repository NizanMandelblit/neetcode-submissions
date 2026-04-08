class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> hashMap;
        for(int num: nums){
            if(hashMap[num])
                return true;
            hashMap[num]++;
        }
                return false;


    }
};