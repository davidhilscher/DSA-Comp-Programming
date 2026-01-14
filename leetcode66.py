"""LC 66 - Arrays"""


def plusOne(digits):
    num_str = ''.join(map(str, digits))
    num = int(num_str)
    sol = num + 1
    return [int(x) for x in str(sol)]



print(plusOne([1,2,4]))