with open("file1.txt") as file:
  new_file = file.readlines()
  print(new_file)

with open("file2.txt") as file2:
  new_file2 = file2.readlines()
  print(new_file2)

result = [int(num) for num in new_file and new_file2 if num in new_file and new_file2]
# Write your code above 👆

print(result)


