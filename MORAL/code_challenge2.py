a = int(input("Enter the amount to deposit: "))
print("Here is the breakdown of the deposited amount")
b = a
c1 = b // 1000
b = b % 1000
c2 = b // 500
b = b % 500
c3 = b // 200
b = b % 200
c4 = b // 100
b = b % 100
c5 = b // 50
b = b % 50
c6 = b // 20
b = b % 20
c7 = b // 10
b = b % 10
c8 = b // 5
b = b % 5
c9 = b // 1
b = b % 1
print("1000 - ",c1)
print("500 - ",c2)
print("200 - ",c3)
print("100 - ",c4)
print("50 - ",c5)
print("20 - ",c6)
print("10 - ",c7)
print("5 - ",c8)
print("1 - ",c9)