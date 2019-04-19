#!/usr/local/bin/python3.7
# The above shebang line is needed in Linux ... not in Windows

#Accessing elements of List 
users = ["user1", "user2", "user3"]     # list defined

# Accessing first element in list
print(users[0])
print(users[len(users) - len(users)])

# Accessing last element in list
print(users[-1])
print(users[len(users) - 1])

# Accessing second last element in list
print(users[-2])
print(users[len(users) - 2])

##########################################

#List Manipulation
#Add or move elements in the list
users =[]       # Empty list defined
users.append("ahmad")
users.append("john")
users.append("linda")
print (users)
users.insert(1,"mary")       #insert add an item at specific index
users.append("john")
print (users)

#Sorting of List
print (sorted(users))   #This will only print sorted list .. will not sort the list
print (users)
sorted_users = sorted(users)    #create new list with sorted users
print(sorted_users)

#Sorting the actual list
users.sort() #This will sort a list
print(users)

