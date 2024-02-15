import random

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [1, 2, 3, 5, 8, 15, 21, 34, 55, 89, 300,45,30]
c= []



def ooo():
    for i in range (len(a)):
        num = random.choice(a)
        a.remove(num)
        print(a)
        c.append(num)
        print(c)
        print('-----------------------')




print(ooo())


# def out_15(list):
#     result = []
#     for i in list:
#         if i % 15 != 0:
#             result.append(i)
#     return result


# print(out_15(a))

# num = 1
# result = num / 15
# odp = isinstance(result,(float))
# if odp == True:
#     a.pop(a.index(num))
#     print(a)



# c = []
# for i in a:
#     if i not in a :
#             c.append(i)


# print(c)