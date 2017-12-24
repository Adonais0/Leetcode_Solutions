def twoSum(nums, target):# Exceed time limit
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_list = list(range(len(nums)))
    while index_list:
        base = [index_list.pop(0)] #base = [0], base = [1], base = [2] ...
        print(base)
        base2 = list(set(index_list)-set(base)) #base2 = [1,2,3]
        print("base2")
        print(base2)
        while base2:
            sub = base + [base2.pop(0)] # [0,1] base2 = [2,3]
            print("sub")
            print(sub)
            print(nums[sub[0]]+nums[sub[1]])
            if nums[sub[0]]+nums[sub[1]] == target:
                return sub
print(twoSum([3,2,3],5))

def twoSum1(nums, target):# O(N) = 1
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_list = list(range(len(nums)))
    d = {}
    for i in index_list:
        if target-nums[i] in d:
            return [i,d[target-nums[i]]]
        else:
            d[nums[i]] = i
print(twoSum1([3,2,3],5))
