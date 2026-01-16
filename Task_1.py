
file_handler = open('sample.txt', 'rt')
file_name ="sample.txt"
line1 = file_handler.readline()
line2 = file_handler.readline()
if file_name == "sample.txt":
        print("Reading file content:")
        print(f"Line 1: {line1}")
        print(f"Line 2: {line2}")
        file_handler.close()
else:
    print(f"The file {file_name} does not exist")

