
def yanghuiTriangle(n):
    i=1
    if n < 1 :
        return "请输入大于0的有效参数！"
    li = [1]
    while i <= n :
        yield li
        li = [li[x]+li[x+1] for x in range(len(li)-1)]
        li.insert(0, 1)
        li.append(1)
        i += 1
    return "执行完毕。"

g = yanghuiTriangle(10)
while True:
    try:
        x = next(g)
        print("g: ",x)
    except StopIteration as ex :
        print("generatoe return value: ",ex.value)
        break

# 方法2:
# def triangles():
#     li = [1]
#     while True:
#         yield li
#         li = [li[x]+li[x+1] for x in range(len(li)-1)]
#         li.insert(0, 1)
#         li.append(1)
#
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break








