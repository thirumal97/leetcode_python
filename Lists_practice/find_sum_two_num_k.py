def find_sum(nums, k):
    
    # Replace this placeholder return statement with your code
    for i in range(len(nums)-1):
        # for every number in the range(0, 7)
        # 1, 2, 3, 4, 5, 6, 7, 
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return [nums[i], nums[j]]
    return []
    
# we can also solve this using the two pointer technique


def find_sum_two_sol(nums, k):
    nums.sort()
    left =0
    right = len(nums)-1

    while left < right:
        if(nums[left] + nums[right] < k):
            left += 1
        elif (nums[left] + nums[right] > k):
            right -=1
        else:
            return [nums[left], nums[right]]
        
    return []