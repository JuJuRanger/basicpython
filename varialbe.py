a = 3
b = 4.92
c = "JuJu..Ranger"

print(a)
print(b)
print(c)
print(a, b, c)


x = y = z = 10
j, k = 5, 15
print(x, y, z)
print(j, k)

status = True
msg = False

print(status, msg)

# concat
# วิธีที่ 1
print("ราคาขายต่อชิ้น", b, "บาท มีจำนวน", a, "ชิ้น")

# วิธีที่ 2
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่ 3
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
