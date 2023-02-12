def remove_dublicates(nums):
    first_pointer, second_pointer = 0, 0 

    while second_pointer < len(nums):
        while second_pointer < len(nums) - 1 and nums[second_pointer] == nums[second_pointer + 1]:
            second_pointer += 1
            nums[first_pointer] = nums[second_pointer]
            first_pointer += 1
            second_pointer += 1
    return nums[::first_pointer]
print(remove_dublicates([0,0,0,1,2,2,2,3,4,4,4,5]))
