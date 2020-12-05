import os

# Задаю константы
# Хорошим тоном является задавать константы "капсом". Таким образом вы показываете, 
# что эти переменные не стоит менять
ITEM_LINE = '├── '
SKIP_LINE = '│   '
LAST_LINE = '└── '
FULL_SKIP = '    '
DIR_SUFFIX = ' (d)'

string_to_merge = "alala"
# Функция вывода директории
def print_dir(path='.', prefix=''):
    # path - путь до директории     
    # prefix - строка, которая должна выводиться до вывода директории
    str_to_return = ""
    ldir = os.listdir(path)
    dirs = []
    files = []
    # Нужно определить список директорий (их надо отобразить первыми)    
    for item in ldir:
        if os.path.isdir(os.path.join(path, item)):
            dirs.append(item)
        else:
            files.append(item)
    
    # Цикл перебора директории
    #   Следующие две строки могут быть заменены на 
    #   for i, item in enumerate(dirs):
    for i in range(len(dirs)):
        item = dirs[i]
        
        # Собираю строку для печати элемента        
        str_to_print = prefix
        
        # Определяю какую линию стоит рисовать        
        # А также новый префикс        
        line = ITEM_LINE
        new_prefix = prefix+SKIP_LINE
        # ldir потому что таким образом мы проверяем момент состоит ли директория только из директорий
        if i == len(ldir)-1:
            line = LAST_LINE
            new_prefix = prefix+FULL_SKIP
        
        # Дособираем строку             
        str_to_print += line + item + DIR_SUFFIX + '\n'
        
        # Выводим и вызываем функцию еще раз для этой директории
        str_to_return += str_to_print + print_dir(os.path.join(path, item), new_prefix)
    # Аналогично выводим список файлов    
    for i in range(len(files)):
        item = files[i]
        
        str_to_print = prefix
        
        line = ITEM_LINE
        if i == len(files)-1:
            line = LAST_LINE
            
        str_to_print += line + item + '\n'
        str_to_return += str_to_print
    # Возвращаю ответ в виде строки    
    return str_to_return

<<<<<<< HEAD
res = print_dir(input())
string_to_merge = "alala"
print(res)
=======
if __name__=="__main__":
    res = print_dir(input())
    print(res)
>>>>>>> dev
