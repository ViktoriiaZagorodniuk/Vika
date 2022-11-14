# Пользователь вводит трехзначное число. Найдите сумму его цифр.
# (используйте %)

# number = int(input("Please enter number : "))
# a = int(n[0])
# b = int(n[1])
# c = int(n[2])
#     print("sum:", a + b + c)


n = int(input("Please enter number : "))
c = n % 10
n = n // 10
b = n % 10
a = n // 10
    print("sum:", a + b + c)



# n = int(input('number'))
# sum = 0
# while n > 0:
# d = n % 10
# n = n // 10
# sum += d
#     print('sum is ', sum)