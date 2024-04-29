# 1. Write a Python program to create an array of 3 integers and display the array items. Access individual elements through indexes.
import array

arr = array.array('i', [1, 3, 5])

print(arr)
print(arr[0])
print(arr[1]) 
print(arr[2], "\n")

# 2. Write a Python program to append a new item to the end of the array.
import array
arr = array.array('i', [1, 3, 5, 7, 9])

print("Original array:", arr)

arr.append(11)

print("New array:", arr, "\n")

# 3. Write a Python program to reverse the order of the items in the array.
import array

arr = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print("Original array:", arr)

arr.reverse()

print("Reversed array:", arr, "\n")

# 4. Write a Python program to find out if a given array of integers contains any duplicate elements. Return true if any value appears at least twice in the array, and return false if every element is distinct.
import array

def has_duplicates(arr):
  seen = set()

  for x in arr:
    
    if x in seen:
      return True
    
    else:
      seen.add(x)
  
  return False
  
arr1 = array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('i', [1, 2, 3, 4, 4])
arr3 = array.array('i', [1, 1, 2, 3, 4])

print(has_duplicates(arr1)) 
print(has_duplicates(arr2)) 
print(has_duplicates(arr3), "\n") 

# 5. Write a Python program to find the first duplicate element in a given array of integers. Return -1 if there are no such elements.
import array

def first_duplicate(arr):
  seen = set()

  for x in arr:
    
    if x in seen:
      return x
      
    else:
      seen.add(x)
  
  return -1
  
arr1 = array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('i', [1, 2, 3, 4, 4])
arr3 = array.array('i', [1, 1, 2, 3, 4])

print(first_duplicate(arr1)) 
print(first_duplicate(arr2)) 
print(first_duplicate(arr3)) 
