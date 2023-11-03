import os
put_file = os.getcwd()
while True:
    try:
        meneg = input("Выберите команду:\n"
                      "pwd - просмотр текущей папки\n"
                      "cd (папка) - переход на другую папку\n"
                      "touch (файл) - создание пустого файла\n"
                      "cat (файл) - вывод содержимого файла\n"
                      "ls - вывод списка файлов в папке\n"
                      "rm (файл) - удаление файла\n").split()

        if meneg[0] == "pwd":
            print(put_file)
        elif meneg[0] == "cd":
            put_file = os.path.join(put_file, meneg[1])
            print(put_file)
        elif meneg[0] == "touch":
            ad_file = os.path.join(put_file, meneg[1])
            new1file = open(ad_file, "w")
            new1file.close()
        elif meneg[0] == "cat":
            ad_file = os.path.join(put_file, meneg[1])
            new2file = open(ad_file, "r")
            print(new2file.read())
            new2file.close()
        elif meneg[0] == "ls":
            a1 = ""
            for i in os.listdir(put_file):
                if "." in i:
                    a1 += i + " "
                else:
                    a1 += i + "/"
            print(a1)
        elif meneg[0] == "rm":
            ad_file = os.path.join(put_file, meneg[1])
            os.remove(ad_file)
        else:
            print("Такой команды нет!")
    except FileNotFoundError:
        print("Нет такого файла!")
    except PermissionError:
        print("Неверное значение!")
    except IndexError:
        print("Неверное значение!")