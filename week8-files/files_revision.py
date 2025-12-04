import os 

if os.path.isfile("test.txt"):
    file = open("test.txt")
    print("File Open")
else:
    print("File not found and will be created")
    file = open("test.txt", "w")
    file.close()
    file = open("test.txt")
    print("File Open")
