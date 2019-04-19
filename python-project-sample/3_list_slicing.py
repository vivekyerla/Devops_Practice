users = ["user1", "user2", "user3", "user4"]

# Slicing of list is done using ... list[1: 3: 2] = list [start: end: step]
# first element (1) is starting index which is always inclusive ... means include 1st index
# second element (3) is ending index which is always exclusive ... means exclude 3rd index
# third element (2) is called step

print (users[1:3])
print(users[1:]) #starting from second to last
print (users[1:-1])
print (users[:3]) #print the first 3rd items
print (users[::-1])#reversing a list

