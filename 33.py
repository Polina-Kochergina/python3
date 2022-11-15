import os
 
path1 = os.getcwd()

def Ls_size(path):
    files_list = os.listdir(path)
    print(len(files_list))
    size_of_file = []
    for f in files_list:
        size_of_file.append(os.stat(os.path.join(path, f)).st_size)

    print(len(size_of_file))

    for idx in range(len(files_list)-1):
        if os.path.isfile(files_list[idx]) == False:
            files_list.pop(idx)
            size_of_file.pop(idx)

    directory= dict(zip(files_list, size_of_file))
    print("dir = ", directory)


    sorted_directory = dict(sorted(directory.items(), reverse=True))
    print("sorted =", sorted_directory)

Ls_size("D:\\vs_code\python\python2")