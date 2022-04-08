#CalStatisticsV1.py
def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出): ")
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出): ")
    return nums
def mean(nums):
    s = 0.0
    for num in nums:
        s += num
    return s / len(nums)
def dev(nums, mean):
    sdev = 0.0
    for num in nums:
        sdev += (num - mean) ** 2
    return pow(sdev / len(nums), 0.5)
def median(nums):
    nums = sorted(nums)
    size = len(nums)
    if size % 2 ==0:
        med = (nums[size // 2 - 1] + nums[size // 2]) / 2
    else:
        med = nums[size // 2]
    return med
n = getNum()
m = mean(n)
print("平均值:{},方差:{},中位数:{}.".format(m, dev(n, m), median(n)))