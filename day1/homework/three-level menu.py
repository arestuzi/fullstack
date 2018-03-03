#!/usr/bin/env python3.6
# Author: Binglin Ji
'''
多级菜单
    三级菜单
    可依次选择进入各子菜单
    所需新知识点
'''
data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}
current_layer = data
#parent_layer = data
parent_layers = []

while True:
    for key in current_layer:
        print(key)

    choice = input("选择有效地区或输入'b'返回上一级菜单: ").strip()
    if len(choice) == 0: continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        current_layer = parent_layers.pop()
    else:
        print("no enter")




