

# 定义奖品的变量
import random

#           0         1        2
prize = ["20元券", "谢谢惠顾", "笔记本"]

# 定义被抽到的奖品

result = ""
money = 0


# 打乱奖品数组

def reward(choose, result, money):
    if (choose == "20元券"):
        money = money + 20
        result = result + "20元券"

    if (choose == "谢谢惠顾"):
        result = result + "谢谢惠顾"
    if (choose == "笔记本"):
        result == result + "笔记本"

    return result, money


random.shuffle(prize)
# print(prize)       作弊代码行
# 强制转换类型
a = int(input("请输入1-3的数字，每位数字对应一个奖品\n"))
choose = prize[a - 1]
result, money = reward(choose, result, money)
print("您抽中的是 %s,您现在还有%d 元钱"%(result,money))
