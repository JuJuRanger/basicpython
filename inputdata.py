# input จะ convert เป็น String ทั้งหมด ถ้าต้องการคำนวนต้องมีการแปลง

# fullname = input("Enter your name:")
# age = int(input("Enter your age:"))

# print(fullname)
# print(age+5)

user = input("Enter Username:")
pwd = input("Enter password:")

if user == "admin" and pwd == "1234":
    print("ok")
else:
    print("fail")
