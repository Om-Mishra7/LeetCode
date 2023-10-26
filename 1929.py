def getConcatenation(nums):
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums


nums = [1,3,2,1]

print(getConcatenation(nums))