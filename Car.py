class Car(object):
    # Propertires
    color = ""  # self.color
    brand = ""  # self.brand
    number_of_wheels = 3  # self.number_of_wheels
    number_of_seats = 4  # self.number_of_seats
    maxspeed = 0  # self.maxspeed

    # Constructor
    def __init__(self, color, brand, number_of_wheels, number_of_seats, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_wheels = number_of_wheels
        self.number_of_seats = number_of_seats
        self.maxspeed = maxspeed

    # Create method set color
    def setcolor(self, x):
        self.color = x

    def setcolor(self, x):
        self.brand = x

    def setcolor(self, x):
        self.maxspeed = x

    def printdata(self):
        print("Color of this car is ", self.color)
        print("Brand of this car is ", self.brand)
        print("Maxspeed of this car is ", self.maxspeed)

    # Deconstructor
    def __del__(self):
        print()
