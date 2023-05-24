# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
    total=0
    for num in range(1, n+1):
        total+= num
    # print(total)
    return total
sum_to(6)

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
    largest_num= list[0]
    for num in list:
        if num> largest_num:
            largest_num= num
    # print(largest_num)
    return largest_num
largest([10, 4, 2, 231, 91, 54])

# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(str1, str2):
    # print(str1.count(str2))
    return str1.count(str2)
occurrences('fleep floop', 'ee')
# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
    total= 1
    for arg in args:
        total*= arg
    # print(total)
    return total
product(4, 0.5, 5)