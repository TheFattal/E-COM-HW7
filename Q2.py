# Question 2:
# a:
my_string = ' fun-day '
trimmed_string = my_string.strip()
print(f"Trimmed string:{trimmed_string}")

# b:
my_string = 'hello'
if my_string.isalpha():
    print("hello is alphabetic!")
else:
    print("hello isn't alphabetic!")

# c:
my_string = '777'
if my_string.isdigit():
    print("777 is numeric!")
else:
    print("777 isn't numeric!")

# d:
my_string = '   '
if my_string.isspace():
    print("the ___ string is only spaces!")
else:
    print("The string has characters other than space!")

# e:
new_list = ['N', 'I', 'N', 'J', 'A']
print(f"{''.join(letter for letter in new_list)}")

# f:
print(f"{'*'.join(letter for letter in new_list)}")

# g:
str1 = "hELLo"
str2 = str1.lower()
if 'e' in str2:
    print("Yes e is inside the string hELLo.")
else:
    print("No, e isn't inside the string hELLo.")

# h:
user_input = input("Enter a word or string: ")
result = [char.upper() for char in user_input if char.isalpha()]
print(result)
