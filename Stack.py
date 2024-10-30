# what is stack ? 
# Data structure know as last in first out (LIFO)
# Push and pop element is O(1)
# Searching an element by value is O(N)

# stack = []; 
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)

# print("top of stack",stack[-1])

# if stack:
#     pop_element =stack.pop()
#     print("Pop Element",pop_element)

# isEmpty = len(stack) ==0
# print("Is stack empty ", isEmpty)

# stack_size = len(stack)
# print("Stack Size", stack_size)

# print(stack)

# Exercise One
# stack_example =[]
# # 1.Add Element to stack
# stack_example.append(100)
# stack_example.append(200)
# stack_example.append(300)
# # 2.Peek at the top of the stack
# check_peek =stack_example[-1]
# print("check Peek", check_peek)
# # 3. Pop Element from the top 
# pop_element =stack_example.pop()
# print("Pop Element",pop_element)
# # 4.Print the stack
# print(stack_example)


#Exercise Two - Checking Balanced Parentheses
def isBalance(parenthese):
    stack =[]
    for char in parenthese:
        if char == '(':
            stack.append(char)
        elif char ==')':
            if not stack:
                return False
            stack.pop()
    return len(stack) ==0

print(isBalance('()'))









