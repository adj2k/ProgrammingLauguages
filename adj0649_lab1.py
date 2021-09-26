import os
value = input("Enter the directory you want to find the size of: (IE. /home/pi/Docmuents)\n")
directory = value
total_size = 0
for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        file_path = os.path.join(dirpath, file)

        if not os.path.islink(file_path):
            total_size += os.path.getsize(file_path)

print("Size of", directory, "is", total_size, "B")
print("Size of", directory, "is", total_size/1024, "KB") 
print("Size of", directory, "is", total_size/(1024*1024), "MB")

