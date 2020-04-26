# ----การ Import ทั้งหมดทุกฟังชั่นใน Module-----
# import number
# from number import *

# ----การ Import บางฟังชั่นใน Module------
# from number import factorial, fibonacci

# -----การ Import และเปลี่ยนชื่อฟังชั่น------
from number import factorial as fa, fibonacci as fi

# เรียกใช้งาน

# ใช้งานแบบทั้งหมด
# print(number.factorial(5))
# print(number.fibonacci(100))

# ใช้งานบางฟังชั่น
# print(factorial(5))
# print(fibonacci(100))
print(fa(5))
print(fi(100))
