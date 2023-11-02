def removeDuplicates(nums):
    replacement_pointer = 1
    max_value = nums[-1]

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[replacement_pointer] = nums[i]
            replacement_pointer += 1
        if nums[i] == max_value:
            break
    return replacement_pointer


nums = [1,2]

print(removeDuplicates(nums))

print(nums)
