# # Задание 1
# class Point3D:
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def info(self):
#         print(f'x = {self.x}, y = {self.y}, z = {self.z}')
#
#     def distance(self, a, b):
#         return b - a
#
#     def distance2(self):
#         return f'Расстояние от x до y: {self.distance(self.x, self.y)}.\nРасстояние между y и z: {self.distance(self.y, self.z)}. '
#
# first = Point3D(2,5,8)
# second = Point3D(5,8,7)
# third = Point3D(8,7,3)
# first.info()
# print(first.distance2())
#
# # Задание 2
# class Square:
#
#      def __init__(self, side_leng):
#          self.side_leng = side_leng
#
#      def calculate_meaning(self):
#          return self.side_leng ** 2
#
#      def calculate_perimeter(self):
#          return 4 * self.side_leng
#
# side_leng = 5
# square = Square(side_leng)
# meaning = square.calculate_meaning()
# perimeter = square.calculate_perimeter()
#
# print(f"Площадь квадрата: {meaning}")
# print(f"Периметр квадрата: {perimeter}")
#
# # Задание 3
# class Triangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return 0.5 * self.a * self.b
#
#     def perimeter(self):
#         return self.a + self.b + (self.a ** 2 + self.b ** 2) ** 0.5
#
#
# triangle = Triangle(3, 5)
#
#
# print("Площадь треугольника:", triangle.area())
# print("Периметр треугольника:", triangle.perimeter())
#
# # Задание 7
# class Reader:
#
#         def __init__(self, full_name, ticket_number, faculty, birthdate, phone):
#             self.full_name = full_name
#             self.ticket_number = ticket_number
#             self.faculty = faculty
#             self.birthdate = birthdate
#             self.phone = phone
#
#        def takeBook(self, book_count):
#            print(f"{self.full_name} взял {book_count} книги")
#
#        def returnBook(self, book_count):
#            print(f"{self.full_name} вернул {book_count} книги")
#
# reader1 = Reader("Петров В. В.", "16", "География", "13.04.2000", "89644673443")
# reader1.takeBook(3)
# reader1.returnBook(2)




