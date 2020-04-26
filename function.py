# การสร้างฟันชั่นแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")


# สร้าง function แบบมี return value
def area(width, height):
    total = width * height
    return total


# function ที่มีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Language: {lang}")


# เรียกใช้ function
hello('name')
print(area(5, 8))
show_info()
show_info('JuJu..Ranger', 15000, 'PHP')
