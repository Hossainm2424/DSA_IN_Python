# What is dictionary in Python? 
# A dictionary in python is an unordered  collection of key-value pairs. 

# Creating a Dictionary 
my_dict = {1:"Apple", 2:'Banana', 3:'Orange'}

# Accessing values using key 
print(my_dict[1])

# Updating the value 
my_dict[1] ='Cherry'

# adding Key-value pairs 
my_dict[4] ="Coconut"

# deleting key-value pairs 
del my_dict[4]

#checking if the key exists 
if 2 in my_dict:
    print("2  Key Exists")


#Returns the value for the specified key
print(my_dict.get(1))

#Return view object that display all the keys in the dictionary 
keys = my_dict.keys()
print(list(keys))

#Returns a view object containing all the values in the dictionary.
values = my_dict.values()
print('Values in dictionary : ', list(values))


# Returns a view object that displays a list of key-value pairs
items = my_dict.items()
print('items in dictionary : ', list(items))

print(my_dict)



