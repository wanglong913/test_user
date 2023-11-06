"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os

'''
作业：
实现学生管理系统：

学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息 

1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。

    print("****************************************")
    print("*				学生管理系统			 *")
    print("*  	    1. 添加新学生信息              *")
    print("* 	    2. 通过学号修改学生信息		 *")
    print("*		3. 通过学号删除学生信息		 *")
    print("*		4. 通过姓名删除学生信息		 *")
    print("* 	    5. 通过学号查询学生信息          *")
    print("*		6. 通过姓名查询学生信息          *")
    print("*		7. 显示所有学生信息             *")
    print("*		8. 退出系统			  		 *")
    print("****************************************")
    select_op = input("输入编号选择操作：")

2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
9. 实现函数，输出所有学生信息
'''

import json
import os


def add_file(user):
    file = open("user.txt", "w", encoding="UTF-8")
    file.write(user)
    file.close()


def read_file():
    file_path = "user.txt"
    if not os.path.exists(file_path):
        file = open(file_path, "w", encoding="UTF-8")
        file.close()
    file = open("user.txt", "r", encoding="UTF-8")
    content = file.read()
    file.close()
    # print(f"content={content}")
    return content


def assignments():
    print("*" * 40)
    print("*               学生管理系统              *")
    print("*           1. 添加新学生信息             *")
    print("*           2. 通过学号修改学生信息        *")
    print("*           3. 通过学号删除学生信息        *")
    print("*           4. 通过姓名删除学生信息        *")
    print("*           5. 通过学号查询学生信息        *")
    print("*           6. 通过姓名查询学生信息        *")
    print("*           7. 显示所有学生信息           *")
    print("*           8. 退出系统                 *")
    print("*" * 40)
    print()


student = read_file()
if student != "":
    student = json.loads(student)
else:
    student = []


def case_1():
    global sta
    sid = input("请输入要添加的学生编号")
    name = input("请输入要添加的学生姓名")
    age = input("请输入要添加的学生年龄")
    gender = input("请输入要添加的学生性别")
    if student != []:
        for i in range(len(student)):
            if sid == student[i]["sid"]:
                sta = True
                break
            else:
                sta = False
    else:
        sta = None
    if sta:
        print("学员编号已存在，请重新输入")
    elif sta == False or sta is None:
        ss = {"sid": sid, "name": name, "age": age, "gender": gender}
        student.append(ss)
        add_file(json.dumps(student))
        print("学员添加成功")
        print(f"添加的学员信息是： 编号：{sid}，姓名：{name}，年龄：{age}，性别：{gender}")


# 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
def case_2():
    sid = input("请输入要修改的学员编号")
    global state
    if student:
        for i in range(len(student)):
            if sid == student[i]["sid"]:
                bb = student[i]
                state = True
                break
            else:
                state = False
    else:
        state = None
    if state:
        name = input("请输入新的学生姓名")
        age = input("请输入新的学生年龄")
        gender = input("请输入新的学生性别")
        ss = {"sid": sid, "name": name, "age": age, "gender": gender}
        a = student.index(bb)
        student[a] = ss
        add_file(json.dumps(student))
        print("学员更新成功")
        print(f"更新后的学员信息是： 编号：{sid}，姓名：{name}，年龄：{age}，性别：{gender}")
    else:
        print(f"学员编号 {sid} 不存在，请重新输入")


# 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
# 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
def case_3(select_op):
    global state
    global statess
    global statesser
    aaa = []
    if select_op == '3':
        sid = input("请输入要删除的学生编号")
        if student:
            for i in range(len(student)):
                if sid == student[i]["sid"]:
                    student.pop(i)
                    add_file(json.dumps(student))
                    state = True
                    break
                else:
                    state = False
        else:
            state = None
        if state:
            print("学员删除成功")
        else:
            print("学员编号不存在，请重新输入")
    elif select_op == '4':
        name = input("请输入要删除的学生姓名")
        if student:
            for i in range(len(student)):
                if name == student[i]["name"]:
                    aaa.append(i)
                    statess = True
                    statesser = True
                else:
                    statess = False
        else:
            statess = None
        aaa.sort(reverse=True)
        if statess == True and statesser == True:
            for i in range(len(aaa)):
                student.remove(student[int(aaa[i])])
                add_file(json.dumps(student))
            print("学员删除成功")
        else:
            print("学员姓名不存在，请重新输入")


# 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
# 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
def case_5(select_op):
    global state
    global statesser
    if select_op == '5':
        sid = input('请输入要查询的学生编号')
        if student:
            for i in range(len(student)):
                if sid == student[i]["sid"]:
                    ss = student[i]
                    print("该编号的学生信息如下：")
                    print(f"学生编号“{ss['sid']}，姓名：{ss['name']}，年龄：{ss['age']}，性别：{ss['gender']}")
                    state = True
                    break
                else:
                    state = False
        else:
            state = None
        if state is None or state == False:
            print(f"查询失败,学生编号：{sid}不存在")
    elif select_op == '6':
        name = input("请输入要查询的学生姓名")
        if student:
            for i in range(len(student)):
                if name == student[i]["name"]:
                    ss = student[i]
                    print(f"学生编号：{ss['sid']}，姓名：{ss['name']}，年龄：{ss['age']}，性别：{ss['gender']}")
                    statesser = True
                else:
                    statesser = False
        else:
            statesser = None
        if statesser is None or statesser == False:
            print(f"查询失败,学生姓名：{name}不存在")


# 实现函数，输出所有学生信息
def case_7():
    if student:
        for i in range(len(student)):
            ss = student[i]
            print(f"学生编号:{ss['sid']}，姓名：{ss['name']}，年龄：{ss['age']}，性别：{ss['gender']}")
    else:
        print("学生列表为空")


def start():
    while True:
        assignments()
        select_op = input("输入编号选择操作：")
        if select_op == "1":
            case_1()
        elif select_op == "2":
            case_2()
        elif select_op == "3":
            case_3(select_op)
        elif select_op == "4":
            case_3(select_op)
        elif select_op == "5":
            case_5(select_op)
        elif select_op == "6":
            case_5(select_op)
        elif select_op == "7":
            case_7()
        elif select_op == "8":
            break
        else:
            print("输入数字错误，请重新输入!")


if __name__ == "__main__":
    start()
