def removeElement(nums, val):
    while nums.count(val) != 0:
            nums.remove(val)
    return len(nums)




nums = [0,1,2,2,3,0,4,2]

val = 2

print(removeElement(nums, val))

print(nums)
