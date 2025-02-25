# 1.
# "Texnika" parent klass.Konstruktorida esa(brand, model, type) parametrlari bor. info() - (brand, model, type) ni
# print qilib beradi.
#
# "Notebooks" child klassi bor.Unda konstruktirida qo'shimcha (video_card, ram, display).
# more_info() - (brand, model, type, video_card, ram, display) ni print qilib beradi.
#
# "Televisions" child klassi bor.Unda konstruktirida(size, display) parametrlari bor.
# more_info() - (brand, model, type, size, display) ni print qilib beradi.
#
# "Smartphones" child klassi bor.Unda konstruktirida(size, sim_count) parametrlari bor.
# more_info() - (brand, model, type, size, sim_count) ni print qilib beradi.
#
# 2.
# "Transport" parent klass.Konstruktorida esa(brand, model, type) parametrlari bor.
# info() - (brand, model, type) ni print qilib beradi.
#
# "ElentroCars" - child klassi bor.Unda konstruktirida qo'shimcha (battery_life, chargin_time).
# more_info() - (brand, model, type, battery_life, chargin_time) ni print qilib beradi.
#
# "SportCars" - child klassi bor.Unda konstruktirida qo'shimcha (motor, color).
# more_info() - (brand, model, type, motor, color) ni print qilib beradi.
#
# "Truck" - childbklassi bor.Unda konstruktirida qo'shimcha (motor, height, long, wieght).
# more_info() - (brand, model, type, height, long, wieght) ni print qilib beradi.
#
# 3.1
# "University" - parent klass.Konstruktorida esa(university) parametrlari bor.
# info() - (university) ni print qilib beradi.
#
# "Staff" - child klass.Unda konstruktirida qo'shimcha (first_name, last_name, age) parametrlari bor.
# staff_info() - (university, first_name, last_name, age) ni print qilib beradi.
#
# "Student" - child klass.U "Staff" dan vorislik oladi.Unda konstruktirida qo'shimcha (group) parametrlari bor.
# more_info() - (university, first_name, last_name, age, group) ni print qilib beradi.
#
# "Teacher" - child klass.U "Staff" dan vorislik oladi.Unda konstruktirida qo'shimcha (position, subject) parametrlari bor.
# more_info() - (university, first_name, last_name, position, subject) ni print qilib beradi.
#
# "OtherStaff" - childklass.U "Staff" dan vorislik oladi.Unda konstruktirida qo 'shimcha (position) parametrlari bor.
# more_info() - (university, first_name, last_name, position,) ni print qilib beradi.
#
# 3.2
# "Object" - child klass.U "University" dan vorislik oladi.Unda konstruktirida qo'shimcha (name) parametrlari bor.
# object_info() - (university, name) ni print qilib beradi.
#
# "Computer" - child klass.U "Object" dan vorislik oladi.Unda konstruktirida qo'shimcha (soni, tizimi, holati) parametrlari bor.
# object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.
#
# "Mebel" - childklass.U "Object" dan vorislik oladi.Unda konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
# object_more_info() - (university, name, soni, turi, holati) ni print qilib beradi.

# 1
# class Texnika:
#     def __init__(self,brand,model,type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}")
#
# class Notebooks(Texnika):
#     def __init__(self,brand,model,type,video_card,ram,display):
#         super().__init__(brand,model,type)
#         self.video_card = video_card
#         self.ram = ram
#         self.display = display
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Video Card: {self.video_card}, RAM: {self.ram}, Display: {self.display}")
#
# class Televisions(Texnika):
#     def __init__(self,brand,model,type,size,display):
#         super().__init__(brand,model,type)
#         self.size = size
#         self.display = display
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Size: {self.size}, Display: {self.display}")
#
# class Smartphones(Texnika):
#     def __init__(self, brand, model, type, size, sim_count):
#         super().__init__(brand,model,type)
#         self.size = size
#         self.sim_count = sim_count
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Size: {self.size}, Sim Count: {self.sim_count}")
#
# laptop = Notebooks("Dell", "XPS 13", "Laptop", "Intel Iris Xe", 16, 13.3)
# tv = Televisions("Samsung", "QLED Q60A", "TV", 55, "4K UHD")
# phone = Smartphones("Apple", "iPhone 14", "Smartphone", 6.1, 2)
#
# laptop.more_info()
# tv.more_info()
# phone.more_info()


# 2
# class Transport:
#     def __init__(self,brand,model,type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}")
#
# class Electro_Cars(Transport):
#     def __init__(self,brand,model,type,battery_life,chargin_time):
#         super().__init__(brand,model,type)
#         self.battery_life = battery_life
#         self.chargin_time = chargin_time
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Battery Life: {self.battery_life}, Charging Time: {self.chargin_time}")
#
# class Sport_Cars(Transport):
#     def __init__(self,brand,model,type,motor,color):
#         super().__init__(brand,model,type)
#         self.motor = motor
#         self.color = color
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Motor: {self.motor}, Color: {self.color}")
#
# class Truck(Transport):
#     def __init__(self,brand,model,type,height,long,wieght):
#         super().__init__(brand,model,type)
#         self.height = height
#         self.long = long
#         self.wieght = wieght
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Height: {self.height}, Long : {self.long}, Weight: {self.wieght}")
#
# electro_car = Electro_Cars("Tesla", "Model S", "Electric", "500km", "1h")
# sport_car = Sport_Cars("Ferrari", "488 GTB", "Sport", "V8", "Red")
# truck = Truck("Volvo", "FH16", "Truck", "D16K", "4m", "7m")
#
# electro_car.more_info()
# sport_car.more_info()
# truck.more_info()


# 3
# class University:
#     def __init__(self, university):
#         self.university = university
#
#     def info(self):
#         print(self.university)
#
#
# class Staff(University):
#     def __init__(self, university, first_name, last_name, age):
#         super().__init__(university)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def staff_info(self):
#         print(self.university, self.first_name, self.last_name, self.age)
#
#
# class Student(Staff):
#     def __init__(self, university, first_name, last_name, age, group):
#         super().__init__(university, first_name, last_name, age)
#         self.group = group
#
#     def more_info(self):
#         print(self.university, self.first_name, self.last_name, self.age, self.group)
#
#
# class Teacher(Staff):
#     def __init__(self, university, first_name, last_name, age, position, subject):
#         super().__init__(university, first_name, last_name, age)
#         self.position = position
#         self.subject = subject
#
#     def more_info(self):
#         print(self.university, self.first_name, self.last_name, self.position, self.subject)
#
#
# class OtherStaff(Staff):
#     def __init__(self, university, first_name, last_name, age, position):
#         super().__init__(university, first_name, last_name, age)
#         self.position = position
#
#     def more_info(self):
#         print(self.university, self.first_name, self.last_name, self.position)
#
# class Object(University):
#     def __init__(self, university, name):
#         super().__init__(university)
#         self.name = name
#
#     def object_info(self):
#         print(self.university, self.name)
#
#
# class Computer(Object):
#     def __init__(self, university, name, soni, tizimi, holati):
#         super().__init__(university, name)
#         self.soni = soni
#         self.tizimi = tizimi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(self.university, self.name, self.soni, self.tizimi, self.holati)
#
#
# class Mebel(Object):
#     def __init__(self, university, name, soni, turi, holati):
#         super().__init__(university, name)
#         self.soni = soni
#         self.turi = turi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(self.university, self.name, self.soni, self.turi, self.holati)
#
# student = Student("Tashkent University", "Ali", "Karimov", 20, "CS-101")
# teacher = Teacher("Tashkent University", "Dilshod", "Islomov", 40, "Professor", "Mathematics")
# other_staff = OtherStaff("Tashkent University", "Sardor", "Rahimov", 35, "Librarian")
# computer = Computer("Tashkent University", "Laboratory PC", 20, "Windows 10", "Yangi")
# mebel = Mebel("Tashkent University", "Stul", 50, "Yog'och", "Yaxshi")
#
# student.more_info()
# teacher.more_info()
# other_staff.more_info()
# computer.object_more_info()
# mebel.object_more_info()