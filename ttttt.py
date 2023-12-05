# import csv
#
# # with open('test.csv' , 'r') as f:
# #     read = csv.DictReader(f)
# #
# #     for i in read:
#         # print(i)
#
# data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
# with open('test2.csv','w') as file :
#     write = csv.writer(file)
#
#     write.writerow(data)
#
#
# import csv
#
# data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
#
# with open('example.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['name', 'age'])
#     writer.writeheader()
#     writer.writerows(data)

# Initialize an empty list
# data = []
#
# # Get input from the user
# name = input('Name: ')
# age = int(input('Age: '))  # Convert age to an integer
#
# # Create a dictionary and add it to the list
# data.append({'name': name, 'age': age})
#
# # Print the list of dictionaries
# print(data)

dict = {}
llist = []

name = input('name: ')
age = input('age: ')

dict[name] = age
print(dict)

llist.append({'name': name , 'age': age})
print(llist)

