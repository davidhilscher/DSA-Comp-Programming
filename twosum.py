"twosum."


def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
            


if __name__ == '__main__':
    print(twoSum([4, 5, 6, 3], 7))