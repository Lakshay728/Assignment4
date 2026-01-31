#Task 1
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print("File not found.")

#Task 2
with open ("newset.txt" , "w") as file:
    data = file.write(input())
    print("Data successfully written")

with open ("newset.txt" , "a") as file:
    data = file.write(input())  
    print("Data appended successfully")
    
with open ("newset.txt" , "r")  as file:
     data = file.read()
     print(data)