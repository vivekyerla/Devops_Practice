'''
in python , everything is a function
in java, everything is object

python supports immutabality ... suitable for big data processing


string is immutable
list is mutable .. tuple is immutable

list = []
dictionary = {}
tuple = ()
set = {}
'''

# Append 123 to every element of list
# Your security team said every username contains 1 digit
# for example above user list is not valid we have to loop through the list and digit for the same

num = "123"

# traditional way to append 123 to every element of list
users = ["user1", "user2", "user3", "user4"]
for i in range(0, len(users)):
    users[i] = users[i] + num
print(users)

# list comprehension reduces four Lines of Code to one line
users = ["user1", "user2", "user3", "user4"]
users = [u + num for u in users]
print(users)



###########################################

# String defined
message = "Hello World"

# Strings in python considered as list of characters
for s in message:
    print(s)

# Using list comprehension
message = [s + " " for s in message]
print (message)
print(''.join(message)) #(this joins list of characters using empty string)
print('*'.join(message)) #(this joins list of characters using *)





