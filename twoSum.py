class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # overall complexity is O(n) 
        # loop over n times in nums
        # space complexity is O(n) store n elements in dictionary
        new_dict = dict()
        for i in range(len(nums)):
            second_num = target - nums[i]
            if nums[i]  in new_dict:
                return [new_dict[nums[i]], i]
            new_dict[second_num] = i
            print(new_dict)

class BruteSolution():
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # time complexity O(n^2)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 5, 7, 11, 13]
    nums_1 = [3, 3, 3, 6]
    target = 9
    print(solution.twoSum(nums_1, target))
    bruteSolution = BruteSolution()
    brute_nums = [3,3, 3, 6]
    brute_target = 9
    print(bruteSolution.twoSum(brute_nums, brute_target))


