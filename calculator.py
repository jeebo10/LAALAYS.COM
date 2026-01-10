def calculator(num1, num2, operator):

    if operator  == '+':
        result = num1 + num2 
    elif operator == '-':
        result = num1 - num2 
    elif operator == '*':
        result = num1 * num2
    else:
        result = num1 / num2 
        
    return result

# natiijo=calculator(13,34, '*')
# print(natiijo)

natiijo=calculator(100,25, '/')
print(natiijo)
natiijo=calculator(100,25, '+')
print(natiijo)
natiijo=calculator(100,25, '-')
print(natiijo)









