def menu():
    print("=" * 20)
    print("1, 实战练习1")
    print("2, 实战练习2")
    print("3, 实战练习3")
    print("4, 实战练习4")
    print("5, 退出")
    print("=" * 20)


# 99乘法表
def case_1():
    print('case_1')
    for i in range(1, 10):
        for g in range(1, i + 1):
            print(f"{g}*{i}={i * g}", end=" ")  # 用来打印
        print()  # 用来换行


# 求数列的和与均值、最大值最小值
def case_2():
    print('case_2')
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 321]
    sum = 0
    avg = None
    if nums[0] == None:
        print("数列为空")
    else:
        max_num = nums[0]
        min_num = nums[0]
    for i in nums:
        sum += i
        if i >= max_num:
            max_num = i
        if i <= min_num:
            min_num = i
    print("SUM：", sum)
    avg = sum / len(nums)
    print("AVG：", avg)
    print("MAX：", max_num)
    print("MIN：", min_num)


# 输入任意数字求和，均值，最大值，最小值
def case_3():
    print('case_3')
    nun = 0
    sum = 0
    avg = None
    max_num = None
    min_num = None
    flag = False
    while True:
        n = input("请输入数字，注：输入的不是数字不算：")
        if n == "bye":
            break
        else:
            if n.startswith("-"):  # 若是负数，则进行切片，
                n = n[1:]
                flag = -1
            if n.isdigit():  # 排除非数字输入，仅适合正整数
                n = int(n)
                if flag == True:
                    n *= -1
                sum += n
                nun += 1
                if max_num == None:
                    max_num = n
                elif max_num <= n:
                    max_num = n
                if min_num == None:
                    min_num = n
                elif min_num >= n:
                    min_num = n
            elif n.find(".") != -1:  # 在 n 中找小数点
                if n.startswith("-"):  # 若是负数，则进行切片，
                    n = n[1:]
                    flag = -1
                    sss = n.split(".")
                    if len(sss) == 2:
                        if sss[0].isdigit() and sss[1].isdigit():
                            n1 = int(sss[0])
                            n2 = float("0."+sss[1])
                            n = n1+n2
                            if flag == True:
                                n *= -1
                            um += n
                            nun += 1
                            if max_num == None:
                                max_num = n
                            elif max_num <= n:
                                max_num = n
                            if min_num == None:
                                min_num = n
                            elif min_num >= n:
                                min_num = n

    print("SUM：", sum)
    print("输入数字总数=：", nun)
    avg = sum / nun
    print("AVG：", avg)
    print("MAX：", max_num)
    print("MIN：", min_num)


# 冒泡排序
def case_4():
    print('case_4')
    nums = [9, 58, 34, 156, 22, 1.0, 558, 1125, 0, 6122, 1, 5, 33, 62, 1.00]
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):  # 必须 -1，否则下标越界报错， 减 i 是本次比较终止位置
            if nums[j] >= nums[j + 1]:
                """
                a=1,b=2
                t = (b,a)  组包
                a,b = t  解包
                """
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # 组包与解包
                # ss = nums[j]
                # nums[j] = nums[j + 1]
                # nums[j + 1] = ss
    print(nums)


def start():
    while True:
        menu()
        op = input("请输入一个数字选择对应功能：")
        if op == "1":
            case_1()
        elif op == "2":
            case_2()
        elif op == "3":
            case_3()
        elif op == "4":
            case_4()
        elif op == "5":
            break
        else:
            print("输入数字错误，请重新输入!")


# 此为 入口函数
if __name__ == '__main__':
    start()
