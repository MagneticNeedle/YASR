#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+k);
        reverse(nums.begin()+k, nums.end());
    }
};

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    vector<int>nums{1,2,3,4,5,6,7};
    s.rotate(nums, 3);
    for(int elm:nums){
        printf("%d, ", elm);
    }    
    return 0;
}
