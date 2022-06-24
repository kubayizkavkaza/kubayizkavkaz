x = int(input())
a = x//1000
b = x // 100 % 10
c = x // 10 % 10
d = x % 10
sum = a + d
razn = b - c
if sum == razn:
    print("ДА")
else:
    print("НЕТ")
