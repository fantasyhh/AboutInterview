"""
手动实现一个函数，检查ip是否合法，不能使用自带库函数
IPv4的ip地址格式：（1~255）.（0~255）.（0~255）.（0~255）
"""


class Solution:
    def check_ip(self, ipstr):
        dot_position = []
        index = 0
        dot_count = 0
        for s in ipstr:
            if s == ".":
                dot_position.append(index)
                dot_count += 1
            index += 1
        if dot_count != 3:
            return False
        p1 = ipstr[0:dot_position[0]]
        p2 = ipstr[dot_position[0]+1:dot_position[1]]
        p3 = ipstr[dot_position[1]+1:dot_position[2]]
        p4 = ipstr[dot_position[2]+1:]
        for p in (p1, p2, p3, p4):
            for n in p:
                if n not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                    return False

        if dot_position[0] >= 3:
            if p1 > '255' or dot_position[0] > 3:
                return False
        if dot_position[1]-dot_position[0]-1 >= 3:
            if p2 > '255' or dot_position[1]-dot_position[0]-1 > 3:
                return False
        if dot_position[2]-dot_position[1]-1 >= 3:
            if p3 > '255' or dot_position[2]-dot_position[1]-1 > 3:
                return False
        if index-dot_position[2]-1 >= 3:
            if p4 > '255' or index-dot_position[2]-1 > 3:
                return False
        return True


print(check_ip('192.168.122.2'))
print(check_ip('192.168.122.s'))
print(check_ip('192.168.122'))
print(check_ip('192.168.01.2'))
print(check_ip('192.168.1234.2'))
print(check_ip('3.3.3.2'))
