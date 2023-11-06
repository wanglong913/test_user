# 1. LV1 作业，但是用面向对象
# 2. 读取并存储文件
import json
import os


class FileWork:
    def __init__(self, user):
        self.user = user

    def add_file(self):
        file = open("user.txt", "w", encoding="UTF-8")
        file.write(self.user)
        file.close()
        return True

    def read_file():
        file_path = "user.txt"
        if not os.path.exists(file_path):
            file = open(file_path, "w", encoding="UTF-8")
            file.close()
            print('文件新创建成功')
        file = open("user.txt", "r", encoding="UTF-8")
        content = file.read()
        file.close()
        if content != "":
            content = json.loads(content)
        elif content == "" or content is None:
            content = []
        return content


class Student:
    def __init__(self, select_op=None, sid=None, name=None, age=None, gender=None):
        self.select_op = select_op
        self.gender = gender
        self.age = age
        self.name = name
        self.sid = sid

    def menu():
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

    def file_work():
        file = FileWork.read_file()
        return file

    def add_stu(self):
        global sta
        file_list = Student.file_work()
        if file_list:
            for i in range(len(file_list)):
                if self.sid == file_list[i]["sid"]:
                    sta = True
                    break
                else:
                    sta = False
        else:
            sta = None
        if sta:
            print("学员编号已存在，请重新输入")
        elif sta == False or sta is None:
            ss = {"sid": self.sid, "name": self.name, "age": self.age, "gender": self.gender}
            file_list.append(ss)
            files = FileWork(json.dumps(file_list))
            files.add_file()
            print("学员添加成功")
            print(f"添加的学员信息是： 编号：{self.sid}，姓名：{self.name}，年龄：{self.age}，性别：{self.gender}")
        return True

    def upd_stu(self):
        global state, bb
        file_list = Student.file_work()
        if file_list:
            for i in range(len(file_list)):
                if self.sid == file_list[i]["sid"]:
                    bb = file_list[i]
                    state = True
                    break
                else:
                    state = False
        else:
            state = None
        if state:
            name = Input_stu.enter_name()
            age = Input_stu.enter_age()
            gender = Input_stu.enter_gender()
            ss = {"sid": self.sid, "name": name, "age": age, "gender": gender}
            a = file_list.index(bb)
            file_list[a] = ss
            files = FileWork(json.dumps(file_list))
            files.add_file()
            print("学员更新成功")
            print(f"更新后的学员信息是： 编号：{self.sid}，姓名：{name}，年龄：{age}，性别：{gender}")
        else:
            print(f"学员编号 {self.sid} 不存在，请重新输入")
        return True

    def del_stu(self):
        global state
        global statess
        global statesser
        file_list = Student.file_work()
        aaa = []
        if self.select_op == '3':
            sid = Input_stu.enter_sid_del()
            if file_list:
                for i in range(len(file_list)):
                    if sid == file_list[i]["sid"]:
                        file_list.pop(i)
                        files = FileWork(json.dumps(file_list))
                        files.add_file()
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
        elif self.select_op == '4':
            name = Input_stu.enter_name_del()
            if file_list:
                for i in range(len(file_list)):
                    if name == file_list[i]["name"]:
                        aaa.append(i)
            else:
                statess = None
            aaa.sort(reverse=True)
            if aaa != []:
                for i in range(len(aaa)):
                    file_list.remove(file_list[int(aaa[i])])
                    files = FileWork(json.dumps(file_list))
                    files.add_file()
                print("学员删除成功")
            elif aaa == []:
                print("学员姓名不存在，请重新输入")

    def sel_stu(self):
        global state
        statesser = False
        file_list = Student.file_work()
        ccc = []
        if self.select_op == '5':
            sid = input('请输入要查询的学生编号')
            if file_list:
                for i in range(len(file_list)):
                    if sid == file_list[i]["sid"]:
                        ss = file_list[i]
                        print("该编号的学生信息如下：")
                        print(f"学生编号:{ss['sid']}，姓名：{ss['name']}，年龄：{ss['age']}，性别：{ss['gender']}")
                        state = True
                        break
                    else:
                        state = False
            else:
                state = None
            if state is None or state == False:
                print(f"查询失败,学生编号：{sid} ,不存在")
        elif self.select_op == '6':
            name = input("请输入要查询的学生姓名")
            if file_list:
                for i in range(len(file_list)):
                    if name == file_list[i]["name"]:
                        ss = file_list[i]
                        print(f"学生编号：{ss['sid']}，姓名：{ss['name']}，年龄：{ss['age']}，性别：{ss['gender']}")
                        ccc.append(i)
            else:
                statesser = None
            if statesser is None or ccc == []:
                print(f"查询失败,学生姓名：{name} ,不存在")
        elif self.select_op == '7':
            if file_list:
                for i in range(len(file_list)):
                    ss = file_list[i]
                    print(f"学生编号:{ss['sid']}，姓名：{ss['name']}，年龄：{ss['age']}，性别：{ss['gender']}")
            else:
                print("学生列表为空")


class Input_stu:
    def enter_sid():
        sid = input("请输入要添加的学生编号")
        return sid

    def enter_sid_upd():
        sid = input("请输入要修改的学生编号")
        return sid

    def enter_sid_del():
        sid = input("请输入要删除的学生编号")
        return sid

    def enter_name():
        name = input("请输入要添加的学生姓名")
        return name

    def enter_name_del():
        name = input("请输入要删除的学生姓名")
        return name

    def enter_age():
        age = input("请输入要添加的学生年龄")
        return age

    def enter_gender():
        gender = input("请输入要添加的学生性别")
        return gender


class Start:
    def start(self):
        while True:
            Student.menu()
            select_op = input("输入编号选择操作：")
            if select_op == "1":
                sid = Input_stu.enter_sid()
                name = Input_stu.enter_name()
                age = Input_stu.enter_age()
                gender = Input_stu.enter_gender()
                stud = Student(sid=sid, name=name, age=age, gender=gender)
                stud.add_stu()

            elif select_op == "2":
                sid = Input_stu.enter_sid_upd()
                stud = Student(sid=sid)
                stud.upd_stu()

            elif select_op == "3":
                stud = Student(select_op=select_op)
                stud.del_stu()

            elif select_op == "4":
                stud = Student(select_op=select_op)
                stud.del_stu()

            elif select_op == "5":
                stud = Student(select_op=select_op)
                stud.sel_stu()

            elif select_op == "6":
                stud = Student(select_op=select_op)
                stud.sel_stu()

            elif select_op == "7":
                stud = Student(select_op=select_op)
                stud.sel_stu()

            elif select_op == "8":
                print('系统退出成功')
                break

            else:
                print("输入错误，请重新输入!")


stt = Start()
stt.start()
