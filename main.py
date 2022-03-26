# Squared Numbers using List Comprehension
numbers = [1,1,2,3,5,8,13,21,34,55]
#new_list = [new_item for item in list]
squared_list = [num ** 2 for num in numbers]
print(squared_list)

# Print only if even number is present in List
numbers = [1,1,2,3,5,8,13,21,34,55]
#new_list = [new_item for item in list if test]
result = [num for num in numbers if num % 2 == 0]
print(result)