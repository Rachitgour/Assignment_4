file_handler = open("output.txt", 'wt')
a = input("Enter text to write to the file: ")
file_handler.write(a)
file_handler.close()
file_name = "output.txt"
print(f"Data successfully written to {file_name} \n")

with open("output.txt", 'at') as file_handler:
    b = input("Enter additional text to append: ")
    file_handler.write(b)
    print("Data successfully appended\n")

print(f"Final content of {file_name}")
print("Line 1: ", a)
print("Line 2: ", b)
