# 字符串相关操作
# str_h = "hello word"
#
# # 字符串长度
# print(len(str_h))
#
# # 字母在字符串中出现的次数
# print(str_h.count('l'))
#
# # 某个字母出现的位置
# print(str_h.index('e'))

# 切片demo
num_str = "01234567"
num_jie = num_str[2:5:3]
print(num_jie)
num_jie_dao = num_str[:]
print(num_jie_dao)

num_jie_bu = num_str[::2]
print(num_jie_bu)

