#include <vector>
#include <stdio.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int p=0;
        for (int i = 0; i < nums.size(); i++) if(nums[i]!=0) nums[p++] = nums[i];
        for(; p <nums.size();p++) nums[p] = 0;
    }
};

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    vector<int> n{0,1,0,3,12};
    s.moveZeroes(n);
    for(int e:n){
        printf("%d ", e);
    }
    return 0;
}
