import os
def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L.append(os.path.join(root, file))
    print(L)
    return

path=os.path.abspath(os.path.join(os.getcwd(),"..\.."))
file_name(path)