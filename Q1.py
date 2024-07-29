# Question 1:
my_string = input("Please enter your full name and city:")

# a:
print(f"the string length is: {len(my_string)}")

# b:
print(f"The string with big letters is: {my_string.upper()}")

# c:
print(f"The string with small letters is: {my_string.lower()}")

# d:
words = my_string.split()  # I'm splitting the string for the case of big or small letters:
first_name = words[0].upper()
if first_name.startswith("DAVID"):
    print("The string indeed starts with my first name! ")
else:
    print(f"The string does not start with my first name.")

# e:
city_name = ' '.join(word.upper() for word in words[2:])  # Cities names can be more than 1 word.
if city_name == "RAMAT GAN":
    print("The string indeed has my city name!")
else:
    print("The string doesn't end with my city name")

# f:
words = my_string.split()
first_name = words[0]
last_name = words[1]
city_name = words[2:]
# another method:
first_name = my_string.split()[0]
last_name = my_string.split()[1]
city_name = ' '.join(word for word in words[2:])
print(f"First name: {first_name}\nLast name: {last_name}\nCity: {city_name}")

# g:
modified_string = my_string.replace(' ', '*')
print(f"{modified_string}")

words = modified_string.split('*')
first_name = modified_string.split('*')[0]
last_name = modified_string.split('*')[1]
city_name = ' '.join(word for word in words[2:])
print(f"First name: {first_name}\nLast name: {last_name}\nCity: {city_name}")

# h:
print(f"{my_string.center(50, '=')}")

# i:
print(f"{my_string[3:]}")

# j:
print(f"{my_string[:4]}")

# k:
print(f"{my_string[1::2]}")

# l:
print(f"{my_string.title()}")
