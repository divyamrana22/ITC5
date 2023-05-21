def count_numbers(number_list):
    counts = {}
    
    for number in number_list:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
    return counts
 
# Input 10 integers
numbers = []
for i in range(10):
    number = int(input(f"Enter integer {i+1}: "))
    numbers.append(number)



positive = []
negative = []
odd = []
even = []

print("Number of occurrences:")
x = count_numbers(numbers)
for num in x :
    print(f'{num} : {x[num]}')



# Positive numbers and negative numbers
for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)

# Even numbers and odd numbers
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Even numbers:", even)
print("Odd numbers:", odd)