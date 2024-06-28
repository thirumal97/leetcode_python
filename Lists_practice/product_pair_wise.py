def find_product(nums):
    
    # Replace this placeholder return statement with your code
    result = [1] * len(nums)
    lp = 1
    for i in range(len(nums)):
        result[i] = lp
        lp *= nums[i]
        print(result)
    
    rp = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= rp
        rp *= nums[i]


    return result

# O(n) time complexity
