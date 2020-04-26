number = (1, 2, 3, 4, 5)
mix = (10, 20, [5, 4, 3, 2], True, 'JuJu..Ranger')

print(number[2])
print(mix[1])
print(mix[2])
print(mix[2][1])

# ลองเปลี่ยนค่าสมาชิก
# นิยามของ tuple หาเปลี่ยนแปลงค่า ทำให้เห็น error
number[2] = 10
print(number)
