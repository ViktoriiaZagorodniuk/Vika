# year = 2020
# if year % 400 == 0:
#     print("%d високосный" %year)
# elif year % 100 == 0:
#     print("%d не високосный" %year)
# elif year % 4 == 0:
#     print("%d високосный" %year)
# else:
#     print("%d не високосный" %year)



years = int (input ("Пожалуйста, введите год запроса:"))
if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
         print (years, "високосный год")
else:
         print (years, "не високосный год")