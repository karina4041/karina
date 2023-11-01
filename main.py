import os
put = os.getcwd()
put_newfile = os.path.join(put, "newfile")
print(put_newfile)
try:
    os.mkdir(put_newfile)
except FileExistsError:
    pass
file_path = os.path.join(put_newfile, "file")
#записывать и читать
with open("file_path", "w+") as file:
    file.write("344")
    print(file.read())
#os.remove("1.txt") удаление файла
print(os.path.exists("1.txt"))