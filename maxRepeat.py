"""
用Python编写一个函数：给定一个整型数组，从数组中找出重复次数最多的数
例如输入数组[1,6,7,3,2,5,8,1,3]，其中１和３都分别出现了两次，次数最多，输出[1,3]
类似的还有出现一次；找出多数元素，多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素
"""
from typing import List


class Solution:
    def maxElement(self, arry: List[int]):
        temparry = {}  # 保存处理后的数据
        times = 0  # 保存最高的那个次数
        for i in arry:
            if i not in temparry:  # 若值为空
                # temparry追加一个元素
                temparry[i] = 1
            else:
                temparry[i] += 1  # 键对应的值+1
        for k, v in temparry.items():
            if v > times:
                times = v
        return [k for k, v in temparry.items() if v == times]

    def majorityElement(self, arry: List[int]):
        # 排序法
        arry = sorted(arry)
        return arry[len(arry)//2]

    def majorityElement2(self, arry: List[int]):
        # Boyer-Moore 投票算法
        count, candi = 0, 0
        for i in arry:
            if i == candi:
                count += 1
            else:
                if count == 0:
                    candi, count = i, 1
                else:
                    count -= 1
        return candi


s = Solution()
a1 = [1, 4, 4, 5, 5, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
a2 = [2, 2, 1, 1, 1, 2, 2]
print("The max duplicate-times number is : {}".format(s.maxElement(a1)))
print("The majority element is : {}".format(s.majorityElement(a2)))
print("The majority element is : {}".format(s.majorityElement2(a2)))
