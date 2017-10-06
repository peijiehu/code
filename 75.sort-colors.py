class Solution(object):
    def sortColors(self, nums):
        # dutch partitioning problem - https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        # O(1) space
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

    def sortColorsNSpace(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # [2,0,1,0] => [0,0,1,2]
        count = [0] * 3
        for n in nums:
            count[n] += 1
        nums[:count[0]] = [0] * count[0]
        nums[count[0]:count[0]+count[1]] = [1] * count[1]
        nums[count[0]+count[1]:count[0]+count[1]+count[2]] = [2] * count[2]
