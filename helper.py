import os, shutil

def del_every_2() -> None:
    files: list = os.listdir(folder)
    for i in range(0, len(files), 2):
        os.remove(f"{folder}\\{files[i]}")

def create_folders_and_sort() -> None:
    global files
    files = os.listdir(folder) #обновляем список
    os.mkdir("C:\\Users\\UserName\\Desktop\\global")
    counter_one: int = 1 #счетчик папок в общей директории
    glob_counter: int = 0 #счетчик файлов
    counter_three: int = -1
    how_photo: list = [8, 9, 8, 9, 9, 11, 11, 9, 10]
    for x in range(0, len(files), len(how_photo)):
        path = f"C:\\Users\\UserName\\Desktop\\global\\{str(counter_one)}"
        counter_one += 1
        os.mkdir(path)
        counter_three += 1
        for y in range(how_photo[counter_three]):
            if glob_counter >= len(files):
                break
            shutil.move(f"{folder}\\{files[glob_counter]}", path)
            glob_counter += 1

def only_create_folders() -> None:
    os.mkdir("C:\\Users\\UserName\\Desktop\\result")
    counter: int = 0
    for x in range(0, len(files), count_in_path):
        path: str = f"C:\\Users\\UserName\\Desktop\\result\\{str(counter + 1)}"
        counter += 1
        os.mkdir(path)

if __name__ == "__main__":
    name: str = input() #имя папки на рабочем столе
    count_in_path: int = 9
    folder: str = f"C:\\Users\\UserName\\Desktop\\{name}"
    only_create_folders()


