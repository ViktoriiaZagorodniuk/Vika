# В переменной month лежит какое-то число из интервала от 1 до 12./
# Определите в какую пору года попадает этот месяц (зима, лето, весна, осень).

month = int(input("Enter month: "))
if month >=3 and month <6:
    print("Spring")
elif month >= 6 and month < 9:
    print("summer")
elif month >=9  and month <12:
    print("autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("no such month")
