def shuffle(nums, n):
    pointer = 1

    for i in range(n, len(nums)):
        element = nums.pop(i)
        nums.insert(pointer,element)
        pointer += 2
    return nums


nums = [1,2,3,4,4,3,2,1]

n = 4


print(shuffle(nums, n))
