"""
手动实现一个函数，检查ip是否合法，不能使用自带库函数，包括int 、split等函数
IPv4 地址由十进制数和点来表示，每个地址包含 4 个十进制数，其范围为 0 - 255， 用(".")分割。比如，172.16.254.1；
同时，IPv4 地址内的数不会以 0 开头。比如，地址 172.16.254.01 是不合法的。

"""


class Solution:
    def check_ip(self, ipstr):
        # .分割的位置
        dot_position = []
        index = 0
        dot_count = 0
        for s in ipstr:
            if s == ".":
                dot_position.append(index)
                dot_count += 1
            index += 1
        #　如果'.'的个数不为３
        if dot_count != 3:
            return False
        dot1, dot2, dot3 = dot_position
        # 取出四个部分的字符串
        p1, p1_len = ipstr[0:dot1], dot1
        p2, p2_len = ipstr[dot1+1:dot2], dot2-dot1-1
        p3, p3_len = ipstr[dot2+1:dot3], dot3-dot2-1
        p4, p4_len = ipstr[dot3+1:], index-dot3-1

        #　如果两位数第一个字符为0，也不符合
        if p1_len >1:
            if p1[0] == '0':
                return False 
        if p2_len >1:
            if p2[0] == '0':
                return False 
        if p3_len >1:
            if p3[0] == '0':
                return False 
        if p4_len >1:
            if p4[0] == '0':
                return False 

        # 检测这四个部分是否有非数字部分
        for p in (p1, p2, p3, p4):
            # 如果有空的部分，直接pass
            if not p:
                return False
            for n in p:
                if n not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    return False

        if p1_len >= 3:
            if p1 > '255' or p1_len > 3:
                return False
        if p2_len >= 3:
            if p2 > '255' or p2_len > 3:
                return False
        if p3_len >= 3:
            if p3 > '255' or p3_len > 3:
                return False
        if p4_len >= 3:
            if p4 > '255' or p4_len > 3:
                return False
        return True

s = Solution()

assert(s.check_ip('1.2.3.4')) == True
assert(s.check_ip('0.0.0.0')) == True
assert(s.check_ip('255.255.255.255')) == True
assert(s.check_ip('::')) == False
assert(s.check_ip('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff')) == False
assert(s.check_ip('2001::f:1234')) == False

assert(s.check_ip('')) == False
assert(s.check_ip(':')) == False
assert(s.check_ip('foo')) == False
assert(s.check_ip('01.02.03.04')) == False
assert(s.check_ip('256.256.256.256')) == False
assert(s.check_ip('1.2.3')) == False
assert(s.check_ip('1.2.3.4.5')) == False
assert(s.check_ip('-1.2.3.4')) == False
assert(s.check_ip('2001:g::')) == False

assert(s.check_ip('192.0.0.0')) == True
assert(s.check_ip('@.3.4.5')) == False
assert(s.check_ip('0.012.3.3')) == False
assert(s.check_ip('6.6.6.6')) == True

