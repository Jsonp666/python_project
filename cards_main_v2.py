#!  /usr/local/bin/python3

import cards_tools_v2

while True:
    cards_tools_v2.show_menu()
    action_str = input("请填写你的操作选项 ：")
    print("您的选项是【%s】" % action_str)

    # 123 是对名片的操作
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools_v2.new_card()
        elif action_str == "2":
            cards_tools_v2.show_all()
        else:
            cards_tools_v2.search_card()
    # 0 退出名片编辑
    # pass 是占位符的意思， 如果暂时不想写逻辑可以先添加pass  来保证程序的结构的顺利运行
    elif action_str == "0":

        break

    # 输入其他提示错误提示
    else:
        print("你的选项不正确请重新选择")

