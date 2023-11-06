"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

'''
课堂练习：
1. 99乘法表输出
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
....
1x9=9 ..... 9x9=81
2. 对数字列表中数字的求和，求平均值，求最大值，求最小值
3. 输入任意数字求和，求平均值，求最大值，求最小值
4. 冒泡排序实现
'''

# 定义一个用来显示菜单的函数
def menu():
    print("*" * 20)
    print("1. 实战练习一")
    print("2. 实战练习二")
    print("3. 实战练习三")
    print("4. 实战练习四")
    print("5. 退出")
    print("*" * 20)

# 实战练习一
def case_1():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"{j}x{i}={i*j}", end=" ")
        print()
# 实战练习二: 对数字列表中数字的求和，求平均值，求最大值，求最小值
def case_2():
    nums = [12,34,3,6,56,33434,6,3,23,23,23,57,78,11,1,8,9]
    sum = 0
    avg = None
    max_num = nums[0]
    min_num = nums[0]

    for n in nums:
        sum += n
        if n > max_num:
            max_num = n

        if n < min_num:
            min_num = n

    print("SUM:", sum)
    avg = sum / len(nums)
    print("AVG:", avg)
    print("MAX:", max_num)
    print("MIN:", min_num)


# 实战练习三:输入任意数字求和，求平均值，求最大值，求最小值,直到输入bye结束
def case_3():
    sum = 0
    avg = None
    num = 0
    max_num = None
    min_num = None

    while True:
        flag = False
        n = input("请输入数字：")
        print(type(n))
        if n == "bye":
            break
        else:
            if n.startswith("-"): # -123123
                n = n[1:] # 123123
                flag = True

            if n.isdigit():
                n = int(n)
                if flag == True:
                    n *= -1
                num += 1
                sum += n

                if max_num == None:
                    max_num = n
                elif max_num < n:
                    max_num = n

                if min_num == None:
                    min_num = n
                elif max_num > n:
                    min_num = n

            elif n.find(".") != -1: # 3.13a  .1  1.  1231231231231.12312312312
                nums = n.split(".")   # ["3", "13"]
                if len(nums) == 2:
                    if nums[0].isdigit() and nums[1].isdigit():
                        n1 = int(nums[0])
                        n2 = float("0."+nums[1])
                        n = n1 + n2

                n = float(n)



    print("SUM:", sum)
    print("NUM:", num)
    avg = sum / num
    print("AVG:", avg)
    print("MAX:", max_num)
    print("MIN:", min_num)


# 实战练习四: 冒泡排序实现
def case_4():
    nums = [9,8,7,6,5,5,4,3,2,5,1,0]
    n = len(nums)

    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] >= nums[j+1]:
                # tmp = nums[j]
                # nums[j] = nums[j+1]
                # nums[j+1] = tmp
                nums[j], nums[j+1] = nums[j+1], nums[j]
                """
                a = 1
                b = 2
                a,b = b,a
                
                t = (b,a）
                a,b = t
                """

    print(nums)

# 定义一个启动函数，用来管理今天所有的实战练习代码
# 每一个练习都会使用一个函数来完成，通过start()函数进行管理
def start():
    while True:
        menu()
        op = input("请输入一个数字选择对应的功能：")
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
            print("输入数字不在正确范围内，请重新选择输入！")

if __name__ == '__main__':
    start()

