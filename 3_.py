import os

# вывести текущую директорию
print("Текущая деректория:", os.getcwd())

for files in os.walk("."):  
    for filename in files:
        print(filename)

