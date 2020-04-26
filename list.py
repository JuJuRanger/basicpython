# การสร้างข้อมูลแบบ list
number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Jany', 'Wasan']
mixed = [10, 25.75, True, 'JuJu..Ranger']

# การเข้าถึงสมาชิกใน list
print(number[1])
print(name[3])
print(mixed[2], mixed[3])
print(number)

# การนับจำนวนสมาชิกใน List
print("สมาชิกทั้งหมดของ number=", len(number))

# การสร้าง list แบบว่าง (empty list)
data = []

# การเพิ่มสมาชิกเข้าไปใน list ว่าง
data.append(10)
data.append(100)
data.append(1000)
print(data)

# การอัพเดทสมาชิกใน list
data[1] = 200
print(data)

# function loop อ่านสมาชิกทั้งหมด
for n in number:
    print(n)

# Loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num
print(sum)
