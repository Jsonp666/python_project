# 字典相关代码
user_info = {
      "name": "asdaa111",
      "age": 18,
      "weight": 150
             }
#
# print(user_info)
#
# # 取值
# print(user_info["name"])
# # 新增/修改
# user_info["aaa"] = 180
# print(user_info)
# user_info['aaa'] = 170
# print(user_info)
# # 删除
# user_info.pop('aaa')
# print(user_info)
#
# # 统计键值对数量
# print(len(user_info))
# # 合并字典 如果被合并的字典中存在相同键值对，会覆盖原有的键值对
# temp_test = {
#     "work": "IT",
#     "age": 20
# }
# user_info.update(temp_test)
# print(user_info)
# # 清空字典
# user_info.clear()
# print(user_info)
# 遍历字典
# for k in user_info:
#     print("%s : %s" % (k, user_info[k]))
# 列表和字典配合使用
card_list = [
    {"name": "xiaoming",
     "age": 18
     },
    {"name": "xiaowang",
     "age": 18
     }
]
for card in card_list:
    print(card)
