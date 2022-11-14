# Пользователь вводит трехзначное число. Найдите сумму его цифр.
# (используйте %)

n = int(input("Please enter number : "))
a = int(n[0])
b = int(n[1])
c = int(n[2])
    print(a + b + c)


# n = int(input("Please enter number : "))
# c = n % 10
# n = n // 10
# b = n % 10
# a = n // 10
#     result = sun(int(input n)) for i in range(n))
#     print(result)



# n = int(input('number'))
# sum = 0
# while n > 0:
# d = n % 10
# n = n // 10
# sum += d
#     print('sum is ', sum)


# str1=str(input())
# print(str1)
# k=0
# for elem in str1:
#     if elem.isdigit():
#         k += int(elem)
#         print(elem)
# print("k=" ,k)


# найти сумму четных чисел в строке
s = input()
sum = 0
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        sum += int(s[i])
    print(sum)

