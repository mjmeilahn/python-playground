
"""
    MULTI-LINE COMMENT!
    Yeeeeeeeaaaaaaaaaa!
"""

# 1. VARIABLES WITHIN A STRING
# age = 30
# name = "Matt"
# sentence = "Hi my name is {} and I am {} years old".format(name, age)
# print(sentence)
# print(f'My name is {name} and I am {age} yeards old.')



# 2. FUNCTIONS - REMEMBER YOU CAN ASSIGN DEFAULT VALUES
# def hello (str):
#     print(str)

# hello("Hello World!")

# def triple_print (str):
#     return print(str * 3)

# triple_print("hello")



# 3. LISTS
# numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

# for num in numbers:
#     if num > 90:
#         print(num)



# 4. DICTIONARIES
# dogs = {"Shepfield": 3, "Rosie": 5, "Callie": 6}
# print(dogs["Callie"])

# translations = {}
# words = ["PoGo","Spange","Lie-Fi"]
# definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

# for i in range(0, len(words)):
#     translations[words[i]] = definitions[i]

# print(translations)



# 5. CLASSES
class Dog:

    # ALWAYS PASS SELF IN METHODS

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def bark (self):
        print("My name is {} and I am {} years old!".format(self.name, self.age))

callie = Dog("Callie", 7)
callie.bark()