class Solution(object):
    def jump(self, nums):
        #T(C(N)==O(N)) and S(C(N)==O(1)) as it requires non memory space allocation iteratively
        maxjumpdist= 0;currentmax = 0;jump= 0;#initializing the variables
        for i in range(len(nums)-1):#iterating throgh nums's length
            maxjumpdist= max(maxjumpdist, i + nums[i]);#maximizing the jump distance from current pos consecuitively
            if jump>= len(nums) - 1:jump+=1;break#incrementing minimum jump val 
            if i ==  currentmax:jump+=1;currentmax = maxjumpdist#updating the jump value's
        return jump#printing jump 
