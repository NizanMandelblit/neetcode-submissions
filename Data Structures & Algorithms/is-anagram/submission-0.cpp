class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;

        unordered_map<char, int> hashMap{};
        for (int i = 0; i < s.size(); i++)
            hashMap[s[i]]++;

        for (int i = 0; i < t.size(); i++)
            hashMap[t[i]]--;

        for (int i = 0; i < s.size(); i++)
            if (hashMap[s[i]])
                return false;
        return true;
    }
};
