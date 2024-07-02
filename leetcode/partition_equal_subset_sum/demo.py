from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        dp = set([0])
        target = sum(nums) // 2

        for num in nums:
            for t in dp.copy():
                if t + num == target:
                    return True
                dp.add(t + num)

        return False


res = Solution().canPartition([1, 5, 11, 5, 4])
print(res)
