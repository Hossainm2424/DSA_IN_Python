# Hash Table - is a data structure  that provides a very effective way to store and retrieve 
# value based on key.

# How Hash table work ? 
# Hash Table store data inkey-value pair, the key is unique and it is hashed using hash function to computute 
# index where the value is stored.

# What is a hash function ? 
# A hash function take an input(key) and returns an integer (hash code)

#Dictionary - Insertion /deletion / Look up by key  is O(1) on average 


# Basic of hash table in python 

# hash_Table ={}
# hash_Table['name']= 'Mohammed'
# hash_Table['age'] = 100
# hash_Table['city'] ='Philadelphia'

# # Accessing Elements 
# print(hash_Table['name'])

# # Modifying elements 
# hash_Table['age'] = 200

# # Deleting Elements 
# del hash_Table['city']

# #Checking if a key exist 
# if 'name' in hash_Table:
#     print('Name exist')

# print(hash_Table)


# Practice 
#Problem 1: Check for Duplicates Write a function that checks if a list contains 
# any duplicates using a hash table.

# nums = [1, 2, 3, 4, 5]

# def check_for_duplicate(nums):
#     seen ={}
#     for num in nums:
#         if num in seen:
#             return True
#         seen[num] =True

# print (check_for_duplicate(nums))


#Problem 2: Two Sum Problem Given an array of integers and a target sum, find two numbers in 
# the array that add up to the target. Return their indices.

# nums = [2, 7, 11, 15]
# target = 9

# def two_Sum(nums, target):
#     hashMap ={}
#     for i, num in enumerate(nums):
#         complement = target -num
#         if complement in hashMap:
#             return [hashMap[complement], i]
#         hashMap[num] =i

# print(two_Sum(nums, target))


#Problem 3: Find First Non-Repeating Character Given a string, find the first character
# that does not repeat, and return its index.

# s = "leetcodel"
# def first_non_repeting(s):
#     count ={}
#     for char in s:
#         count[char] =count.get(char, 0)+1
    
#     for i, char in enumerate(s):
#         if count[char] ==1:
#             return i
#     return -1

# print(first_non_repeting(s))


    

          






