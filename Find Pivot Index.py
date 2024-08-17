class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = [0]
        post_sum = [0]
        k = len(nums) -1
        for i in range(len(nums)):
            pre_sum.append(pre_sum[i] + nums[i])
            post_sum.insert(0,post_sum[0] + nums[k])
            k -= 1
        pre_sum = pre_sum[1:]
        post_sum = post_sum[:-1]
        for a in range(len(post_sum)):
            if post_sum[a] == pre_sum[a]: return a
        return -1
