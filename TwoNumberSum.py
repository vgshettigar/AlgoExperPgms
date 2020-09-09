def twoNumSum(nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [target - nums[i],nums[i]]
            else:
                required[nums[i]]=i
            if i== len(nums)-1:
                return []

array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
targetSum = 164
myresult = twoNumSum(array, targetSum)
print(myresult)

