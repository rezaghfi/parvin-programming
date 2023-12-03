# 145 = 14 * 10 + 2 * 2 + 1 * 1

money = int(input("enter your money: "))

ten = money // 10

print(ten)

money = money - (10 * (money//10))

two = money // 2

money = money - (2 * (money//2))

one = money

print("ten coin: ", ten, "two coin: ", two, "one coin: ", one)