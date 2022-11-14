# num = int(input("Введите число: "))
# count = 0
# while num > 1:
#     count += not num % 2
#     num -= 1
# print("четных чисел", count)



n = int(input())
count = 0
for i in range(1, n):
    count += i & 1
print(count)
