import random
import learning_modules
import platform
import datetime
import re
import camelcase

#
# print("hello world")
#
# x = 8
# y = 4
# if y > x:
#     print("death")
# else:
#     print("life!")
#
# # My first Comment!
#
# """
# My second comment... Not as impressive..
# """
#
# a = 20
# b = "i can build a neural network!"
#
# print(a)
# print(b)
#
# while x > y:
#     print(b)
#     x -= 2
#
# b = 5
#
# while b <= a:
#     print(b)
#     b += 5
#
# best_string = '\nwhichever quotation marks work for you are best :)'
# print(best_string)
#
# a, b, c = "hello", "world", "cruel"
# print(a + ' ' + c + ' ' + b)
# a = b = c
# print(a + ' ' + c + ' ' + b)
#
#
# def grade_a_function():
#     print("() () ouch" + " " + a)
#
#
# grade_a_function()
#
# w = 10
#
#
# def reference():
#     q = "9"
#     print("i got the reference from " + q)
#
#
# reference()
#
#
# # print(w) - w is a local variable inside of syphilis(). that is it's SCOPE
#
#
# def reference2():
#     global w
#     w = "42"
#     print("i got the reference from " + w)
#
#
# reference2()
# print(w)
#
# a, b, c = 10, 2.255, "hello"
# print(type(a))
# print(type(b))
# print(type(c))
#
# d = 2e64
# print(d)
#
# print(random.randrange(1, 10))
#
# a = "hello world"
# print(a[random.randrange(1, 10)])
# print(a[random.randrange(1, 3):random.randrange(7, 10)])
# print(a[-1 * random.randrange(7, 10):-1 * random.randrange(1, 3)])
# print(len(a))
# print(a.strip())
# print(a.upper())
# print(a.replace("l", "c"))
# print(a.split(" "))
# print(type(a.split(" ")))
#
# print('\n')
#
# print(2 == 2)
# print(9 + 10 == 21)
#
# print(bool("tf does this do"))
# print(bool(15))
# # Evaluates to false if: all whitespace string, 0, or empty list, tuple, set or dictionary
#
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})
#
# x = 5
# y = 2
#
# print(x ** y)
# print(x // y)
# print(x < 10 and y > 1)
# print(x > 10 or y < 1)
#
# a = ['movie', 'book', 'game']
# b = 'book'
# print(b in a)
# print(b not in a)  # getting weird with double negatives
#
# print("you're not so good at bits so let's practice!")
# x = False
# y = True
# print(x | y)
# print(x & y)
# print(x ^ y)
# x = True
# print(x ^ y)  # Doesn't work now! Only 1 bit can be 1, not both...
#
# favorite_list = ['desk', 'chair', 'computer', 'phone', 'pen', 'ear-buds']
# print(favorite_list)
# print(favorite_list[1])
# print(favorite_list[-1])
# print(favorite_list[1:5])
# print(favorite_list[:5])
# print(favorite_list[2:])
# favorite_list[3] = "mouse"
# print(favorite_list)
# for i in favorite_list:
#     print(i)
#
# if 'mouse' in favorite_list:
#     print("mickey mouse is pretty cool")
#
# print(len(favorite_list))
# favorite_list.append('television')
# favorite_list.insert(2, 'laptop')
# favorite_list.remove('ear-buds')
# favorite_list.pop()
# del favorite_list[0]
# print(favorite_list)
#
# worst_list = favorite_list.copy()
# favorite_list.clear()
# print(favorite_list)
# del favorite_list
# # print(favorite_list) - What's favorite_list???
# okay_list = list(worst_list)
# okay_list.remove('pen')
# okay_list.remove('chair')
# worst_list.extend(okay_list)
# worst_list.sort()
# worst_list.reverse()
# print(okay_list)
# print(worst_list)
#
# comp_specs = {
#     "processor": "AMD Ryzen 5",
#     "graphics card": "GeForce GTX 1050 Ti",
#     "memory": "2x8gb",
#     "cooler": "Stock Corsair Fan",
#     "power supply": 24
# }
#
# print(comp_specs)
# x = comp_specs['memory']
# print(x)
# comp_specs["processor"] = "Intel 5i"
# for x in comp_specs:
#     print(x)
# for i in comp_specs.values():
#     print(i)
#
# print(len(comp_specs))
# comp_specs["hard drive"] = "WD Blue 1TB"
# for x, y in comp_specs.items():
#     print(x, y)
#
# better_specs = comp_specs.copy()
# better_specs["processor"] = "Intel i9 9900k"
# better_specs["graphics card"] = "GeForce GTX 2080"
# for i, j in better_specs.items():
#     print(i, j)
#
# all_specs = {
#     "model1": comp_specs,
#     "model2": better_specs
# }
#
# print(all_specs)
#
# for i in "telepathy":
#     print(i)
#
# for i in range(5, 101, 19):
#     print(i)
# else:
#     print("done :)")
#
#
# def my_family(first_name):
#     print(first_name + " Ross")
#
#
# my_family("Mike")
# my_family("Kari")
# my_family("Justin")
# my_family("Renee")
#
#
# def my_family_v2(*first_name):
#     place = 0
#     while place < len(first_name):
#         print(first_name[place] + " Ross")
#         place += 1
#
#
# my_family_v2("Mike", "Kari", "Justin", "Renee", "Ashley")
#
#
# def multiply_five(k):
#     return 5 * k
#
#
# print(multiply_five(3))
# print(multiply_five(5))
# print(multiply_five(9))
#
#
# def empty_function():
#     pass
#
#
# def tri_recursion(k):  # what this do? find out
#     if k > 0:
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)
#
#
# def lambda_test(n):  # Don't know if this is actually worth using or not...
#     return lambda h: h * n
#
#
# my_doubler = lambda_test(2)
# print(my_doubler(32))
#
#
# tech_giants = ['Microsoft', 'Google', 'Facebook', 'IBM', 'Samsung', 'HP', 'Micron', 'Ten-cent']
# for z in tech_giants:
#     print(z)
#
# tech_giants.append('Apple')
# print(tech_giants[len(tech_giants)-1])
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduction(self):
#         print("Hello my name is " + self.name)
#
#
# p1 = Person('Tyrone', 20)
# p1.age = 21
# print(p1.name + " " + str(p1.age))
# p1.introduction()
# del p1
#
#
# class People:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_name(self):
#         print(self.first_name, self.last_name)
#
#
# p1 = People("Tyrone", "Tyson")
# p1.print_name()
#
#
# class Employee:
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#
#     def print_name2(self):
#         print(self.first_name, self.last_name, self.salary)
#
#     def fire(self):
#         print("I'm sorry, " + self.first_name + ", you're fired.")
#
#
# s1 = Employee("Rochelle", "Clark", 67000)
# s1.print_name2()
# s1.fire()
#
# okay_list_it = iter(okay_list)
#
# print(next(okay_list_it))
# print(next(okay_list_it))
# print(next(okay_list_it))
#
# num_array = [52, 7, 10, 4, 39, 15, 64, 28]
# largest_num = 0
# for e in num_array:
#     if e > largest_num:
#         largest_num = e
#
#
# print(largest_num)
#
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         v = self.a
#         self.a += 1
#         return v
#
#
# my_class = MyNumbers()
# my_iter = iter(my_class)
#
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
#
#
# class MyNumbers2:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             h = self.a
#             self.a += 1
#             return h
#         else:
#             raise StopIteration
#
#
# my_class2 = MyNumbers2()
# my_iter = iter(my_class2)
#
# for x in my_iter:
#     print(x)
#
# learning_modules.greeting("Johnny Test")
# mod_people1_country = learning_modules.people1["country"]
# print(mod_people1_country)  # Cool! B)
# # You can also import modules with a nickname - makes it easier - don't forget!
# # You can also choose what to import - from [module] import [function/object]
# y = dir(platform)
# print(y)
#
# current_time = datetime.datetime.now()
# print(current_time.year)
# print(current_time.strftime("%A"))
#
# favorite_date = datetime.datetime(2040, 3, 6)
# print(favorite_date)
# print(favorite_date.strftime("%B"))
# print(favorite_date.strftime("%H"))
#
# """
#  -- -- Datetime Reference Table -- --
# Directive 	Description 	Example
# %a 	Weekday, short version 	Wed
# %A 	Weekday, full version 	Wednesday
# %w 	Weekday as a number 0-6, 0 is Sunday 	3
# %d 	Day of month 01-31 	31
# %b 	Month name, short version 	Dec
# %B 	Month name, full version 	December
# %m 	Month as a number 01-12 	12
# %y 	Year, short version, without century 	18
# %Y 	Year, full version 	2018
# %H 	Hour 00-23 	17
# %I 	Hour 00-12 	05
# %p 	AM/PM 	PM
# %M 	Minute 00-59 	41
# %S 	Second 00-59 	08
# %f 	Microsecond 000000-999999 	548513
# %z 	UTC offset 	+0100
# %Z 	Timezone 	CST
# %j 	Day number of year 001-366 	365
# %U 	Week number of year, Sunday as the first day of week, 00-53 	52
# %W 	Week number of year, Monday as the first day of week, 00-53 	52
# %c 	Local version of date and time 	Mon Dec 31 17:41:00 2018
# %x 	Local version of date 	12/31/18
# %X 	Local version of time 	17:41:00
# %% 	A % character 	%
# """
#
# txt = "The rain in Spain"
# aa = re.search("^The.*Spain$", txt)
# print(aa)
#
# ab = re.findall("ai", txt)
# print(ab)
#
# fun_str = "banana"
# ac = re.search("ana", fun_str)
# print(ac)
#
# ad = re.split("n", fun_str)
# print(ad)
#
# ae = re.split("n", fun_str, 1)
# print(ae)
#
# af = re.sub("a", "i", fun_str)
# print(af)
#
# ag = re.sub("a", "i", fun_str, 1)
# print(ag)
#
# ah = re.search("ana", fun_str)
# print(ah.span())
#
# """
# Character 	Description 	Example 	Try it
# [] 	A set of characters 	"[a-m]"
# . 	Any character (except newline character) 	"he..o"
# ^ 	Starts with 	"^hello"
# $ 	Ends with 	"world$"
# * 	Zero or more occurrences 	"aix*"
# + 	One or more occurrences 	"aix+"
# {} 	Exactly the specified number of occurrences 	"al{2}"
# | 	Either or 	"falls|stays"
# () 	Capture and group
#
# Any escape commands can be found on w3schools.com/python/python_regex.asp
#
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
# Set 	Description 	Try it
# [arn] 	Returns a match where one of the specified characters (a, r, or n) are present
# [a-n] 	Returns a match for any lower case character, alphabetically between a and n
# [^arn] 	Returns a match for any character EXCEPT a, r, and n
# [0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9] 	Returns a match for any digit between 0 and 9
# [0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# """
#
# cc = camelcase.CamelCase()
# txt2 = "hello cruel world"
# print(cc.hump(txt2))
#
# try:
#     print("9" + 10)
# except TypeError:
#     print("Error occurred")
# else:
#     print("Some other error")
#
# try:
#     x = 20
#     y = "telepathy"
#     print(x + y)
# except NameError:
#     print("something went wrong")
# except TypeError:
#     print("type error")
# else:
#     print("Some other error")
#
# try:
#     fa = open("demo_file.txt")
#     fa.write("Test Words")
#     print("written")
# except:
#     print("Something went wrong when writing to the file")
# finally:
#     fa.close()
#
# ai = 1  # Change to -1 to test
# if ai < 0:
#     raise Exception("Sorry, no negative numbers")
# else:
#     print("success")
#
# aj = 20  # Change to string to test
#
# if not type(aj) is int:
#     raise TypeError("Only integers allowed")
#
# name = input("Enter name: ")
# print("Your name is: " + name)
#
# age = input("Enter age: ")
# age = int(age) * 7
# if age > 100:
#     print("Wow! You're an old dog! Your age in dog years is: " + str(age))
# else:
#     print("Your age in dog years is: " + str(age))
#
# ego_boost = "You're cool, {}. You're {:.0f} years old."
# age /= 7
# print(ego_boost.format(name, age))

# Moved to learning_files.py

print(str())

test = ["one", "two", "three"]
test[2] = "four"
print(test)
