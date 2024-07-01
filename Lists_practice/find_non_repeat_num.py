def find_first_unique(nums):
    
    # Replace this placeholder return statement with your code
    # [1, 2, 3, 1]
    # output is 2 what can we do here is make a count
    # if count is 1 and that too, we need to attach with the index
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]] += 1
        else:
            dict[nums[i]] = 1
    print(dict)
    for num in nums:
        if dict[num] == 1:
            return num

    return 0