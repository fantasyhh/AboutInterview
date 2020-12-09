"""
用Python编写一个函数：给定一个整型数组，从数组中找出重复次数最多的数
例如输入数组[1,6,7,3,2,5,8,1,3]，其中１和３都分别出现了两次，次数最多，输出[1,3]
要求不使用库函数；用最小的时间空间复杂度
"""

def getMaxNum(arry):
    temparry = {}  # 保存处理后的数据
    times = 0  # 保存最高的那个次数
    for i in arry:
        if not temparry.get(i, None):  # 若值为空
            # temparry追加一个元素
            temparry[i] = 1
        else:
            temparry[i] += 1  # 键对应的值+1
    for k, v in temparry.items():
        if v > times:
            times = v
    return [k for k, v in temparry.items() if v == times]


a1 = [1, 4, 4, 5, 5, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
a2 = [1, 6, 7, 3, 2, 5, 8, 1, 3]
print("The max duplicate-times number is : {}".format(getMaxNum(a1)))
print("The max duplicate-times number is : {}".format(getMaxNum(a2)))
