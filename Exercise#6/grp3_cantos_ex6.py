# 1. Finding the Maximum of Three Numbers: 
def find_max(a, b, c):
    return max(a, b, c)

# Example usage:
print(find_max(23, 34, 29))
print(find_max(45, 33, 47))  
print(find_max(12, 12, 11), "\n")

# 2. Summing All Numbers in a List
def sum_list(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

# Example usage:
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list), "\n") 

# 3. Reversing a String
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# 4. Example usage:
original_str = "Hello, World!"
print(reverse_string(original_str), "\n") 

#Counting Upper and Lower Case Letters
def count_case_letters(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Example usage:
sample_string = "Hello I'm John Rick, Nice to meet you. How's it goin?"
upper, lower = count_case_letters(sample_string)
print(f"No. of Upper case characters: {upper}")
print(f"No. of Lower case characters: {lower}")

# 4. Counting Upper and Lower Case Letters
def count_case_letters(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Example usage:
sample_string = "Hello Mr. Rogers, how are you this fine Tuesday?"
upper, lower = count_case_letters(sample_string)
print(f"No. of Upper case characters: {upper}")
print(f"No. of Lower case characters: {lower}", "\n")

# 5. Creating a New List with Distinct Elements
def unique_list(numbers):
    return list(set(numbers))

# Example usage:
original_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(unique_list(original_list))  # Output: [1, 2, 3, 4, 5]
