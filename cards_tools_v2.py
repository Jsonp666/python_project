card_list = []

def show_menu():
    # 显示菜单
    print("*" * 50)
    print("欢迎使用名片管理系统")
    print("")
    print("1、新增名片")
    print("2、显示全部")
    print("3、搜索名片")
    print("")
    print("0、退出系统")
    print("*" * 50)


def new_card():
    # 新增名片
    print("新增名片")
    name = input("请输入姓名 :")
    email = input("请输入邮箱 ：")
    card_dist = {"name": name,
                 "email": email
                 }
    # 把用户的字典信息追加到列表里面
    card_list.append(card_dist)
    print("新增成功")


def show_all():
    # 判断是否存在名片， 如果没有返回到menu
    if len(card_list) == 0:
        print("目前还没有名片， 请添加名片")
        return
    # 显示全部
    print(card_list)


def search_card():
    # 搜索名片

    find_name = input("请输入要搜索到姓名：")

    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("找到了")

            card_action(card_dict)

            break

    else:

        print("抱歉没有找到 %s" % find_name)


def card_action(card_dict):

    print(card_dict)

    card_act = input("请输入你要进行的操作 1 修改 2 删除 0 返回主菜单 ：")

    if card_act == "1":

        # card_dict['name'] = input("请输入修改的姓名：")
        #
        # card_dict['email'] = input("请输入修改的邮箱：")
        card_dict['name'] = input_card_info(card_dict['name'], input("请输入修改的姓名【回车不修改】："))

        card_dict['email'] = input_card_info(card_dict['email'], input("请输入修改的邮箱【回车不修改】："))

        print("修改名片")

    elif card_act == "2":

        card_list.remove(card_dict)

        print("删除名片")


def input_card_info(def_value, imp_value):

    if len(imp_value) > 0:

        return imp_value

    else:

        return def_value
