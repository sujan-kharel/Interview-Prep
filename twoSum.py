# Link: https://leetcode.com/problems/two-sum/

"""
    Time complexity: O(N)
    Space Complexity: O(N)

"""


def twoSum(lis, target):
    lisDict = {}

    for i, num in enumerate(lis):
        if num in lisDict:
            return [lisDict[num], i]

        lisDict[target-num] = i

    return []


lis = [2, 7, 11, 15]
target = 9
print(twoSum(lis, target))
