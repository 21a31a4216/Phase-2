def findPivotIndexAndMove(nums, left, right):
    pivot = nums[right]
    position = left 
    for index in range(left, right):
        if nums[index] <= pivot:
            temp = nums[index]
            nums[index] = nums[position]
            nums[position] = temp
            position += 1 
    nums[position], nums[right] = nums[right], nums[position]
    return position
def findPivotAndSort(nums, left, right):
    if left >= right:
        return
    pivotIndex = findPivotIndexAndMove(nums, left, right)
    findPivotAndSort(nums, left, pivotIndex - 1)
    findPivotAndSort(nums, pivotIndex + 1, right)
def performQuickSort(nums):
    n = len(nums)
    findPivotAndSort(nums, 0, n - 1)
nums = [9, 8, 7, 6, 5, 4, 3, 2, 100]
print("Before sorting:", nums)
performQuickSort(nums)
print("After sorting:", nums)



# output
# Before sorting: [9, 8, 7, 6, 5, 4, 3, 2, 100]
# After sorting: [2, 3, 4, 5, 6, 7, 8, 9, 100]