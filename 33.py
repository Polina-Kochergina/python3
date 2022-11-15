import os.path
 
path1 = os.getcwd()
path2 = ('D:\\vs_code\python\python1')

def Ls_size(path):
    files_list = os.listdir(path)
    print(len(files_list))
    size_of_file = []
    for f in files_list:
        size_of_file.append(os.stat(os.path.join(path, f)).st_size)

    print(len(size_of_file))

    directory = dict(zip(files_list, size_of_file))
    print("dir = ", directory)


    sorted_directory = dict(sorted(directory.items(), key = lambda x: x[1], reverse=True))
    print("sorted = ", sorted_directory)


    for key, value in sorted_directory.items():
        # print(key, value, 'k and v')
        if os.path.isdir(key):
            continue
        else:
            print(f"{key} ':' {value} B")

    print("path", path)

Ls_size(path2)
# Ls_size(path1)