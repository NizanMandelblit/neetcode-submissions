/*
 * @lc app=leetcode id=146 lang=cpp
 *
 * [146] LRU Cache
 */
using namespace std;
#include <list>
#include <unordered_map>
// @lc code=start
class LRUCache {
  private:
    struct Node {
        int m_key;
        int m_value;
        Node(int key, int value) {
            this->m_key = key;
            m_value = value;
        }
    };

    int m_capacity = 0;
    unordered_map<int, list<Node *>::iterator> hashMap; // Maps keys to list iterators
    list<Node *> lru; // List to track LRU order (most recent at front, least recent at back)

  public:
    LRUCache(int capacity) {
        m_capacity = capacity;
    }

    int get(int key) {
        if (hashMap.count(key) == 0)
            return -1;
        const auto it_node = hashMap[key];
        lru.splice(
            lru.begin(), lru, it_node); // moves the location of the node to be at the front()
        return (*it_node)->m_value;
    }

    void put(int key, int value) {
        if (hashMap.count(key)) {
            (*hashMap[key])->m_value = value;
            lru.splice(lru.begin(),
                       lru,
                       hashMap[key]); // moves the location of the node to be at the front()
            return;
        }

        // new node
        // If the cache is at capacity, remove the least recently used item
        if (hashMap.size() == m_capacity) {
            Node *lru_node = lru.back();
            hashMap.erase(lru_node->m_key);
            lru.pop_back();
            delete lru_node;
        }

        // Insert the new node at the front of the list
        Node *node = new Node(key, value);
        lru.push_front(node);
        hashMap[node->m_key] = lru.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end
