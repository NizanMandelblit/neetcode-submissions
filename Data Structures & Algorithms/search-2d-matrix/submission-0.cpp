/*
 * @lc app=leetcode id=74 lang=cpp
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
#include <vector>
using namespace std;
class Solution {
  public:
    bool searchMatrix(vector<vector<int>> &matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        int topRow = 0;           // like left pointer in binary search
        int bottomRow = rows - 1; // like right pointer in binary search

        while (topRow <= bottomRow) {
            int middleRow = (topRow + bottomRow) / 2;
            if (target > matrix[middleRow][cols - 1])
                topRow = middleRow + 1;

            else if (target < matrix[middleRow][0])
                bottomRow = middleRow - 1;

            else
                break;
        }

        if (topRow > bottomRow)
            return false; // no row where target exist

        // binary search on row
        int row = (topRow + bottomRow) / 2;
        int left = 0;
        int right = cols - 1;

        while (left <= right) {
            int middle = (left + right) / 2;
            if (target > matrix[row][middle])
                left = middle + 1;
            else if (target < matrix[row][middle])
                right = middle - 1;
            else
                return true;
        }

        return false;
    }
};
// @lc code=end
