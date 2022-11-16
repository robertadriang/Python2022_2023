# 1)	Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul dat ca parametru.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
import os
from os.path import isfile, join, splitext, isdir


def get_extensions_from_directory(dir):
    files = [f for f in os.listdir(dir) if isfile(join(dir, f))]
    files_extensions = set()
    for f in files:
        files_extensions.add(splitext(join(dir, f))[1][1:])
    return sorted(list(files_extensions))


print("1:", get_extensions_from_directory('.'))


# 2)	Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie,
# calea absolută a fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
def write_path_from(dir, file):
    try:
        f = open(file, 'w+')
        for (root, directories, files) in os.walk(dir):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                if fileName.startswith('A') or fileName.startswith('a'):
                    print(full_fileName, file=f)
        f.close()
        return f'Finished writing to file {file}'
    except:
        return f'Unable to open/write to file {file}'


print("2:", write_path_from('.', ".\paths.txt"))


# 3)	Să se scrie o funcție ce primește ca parametru un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
# sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie.
# Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
def file_or_directory(path):
    if isfile(path):
        try:
            f = open(path, 'rb')
            f_size = f.seek(0, 2)  # end of file
            f.seek(f_size - 20, 0)  # set to last 20 characters
            return ''.join([chr(e) for e in f.read(20)])
        except:
            f'Unable to open/read from file {path}'
    else:
        file_extension_counter = {}
        for (root, directories, files) in os.walk(path):
            for fileName in files:
                key = fileName.split('.')[-1]
                if key in file_extension_counter:
                    file_extension_counter[key] += 1
                else:
                    file_extension_counter[key] = 1
        return sorted(list(file_extension_counter.items()), reverse=True, key=lambda e: e[1])


print("3:", file_or_directory('.\paths.txt'))
print("3:", file_or_directory('.\RSA_Source.cpp'))
print("3:", file_or_directory('.'))

# 4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală.
print("4:", get_extensions_from_directory('.'))


# 5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search șireturneaza o listă de fișiere care conțin to_search.
# Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv
# iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
# Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
def search_in_file(file, to_search):
    try:
        with open(file) as f:
            if f.seek(0, 2) < 4000000:  # we load small files (<4mb directly into memory)
                f.seek(0, 0)
                if to_search in f.read():
                    return True
                return False
            else:  # we read line by line bigger files (MIGHT not get the expected search term
                for line in f:
                    if to_search in line:
                        return True
                return False
    except:
        print(f'Unable to open/read from file {file}')


def search_function(target, to_search):
    try:
        if isfile(target):
            if search_in_file(target, to_search):
                return [target]
            return []
        elif isdir(target):
            result = []
            for (root, directories, files) in os.walk(target):
                for fileName in files:
                    full_fileName = os.path.join(root, fileName)
                    if search_in_file(full_fileName, to_search):
                        result.append(full_fileName)
            return result
        else:
            raise ValueError(target, to_search)
    except Exception as e:
        params = e.args
        print(f'[EXCEPTION]:{params[0]} is neither file nor directory!')
        return []


print("5:", search_function('a', 'b'))
print("5:", search_function('D:\DONALD', 'elemente'))
print("5:", search_function('D:\DONALD\message.txt', 'elemente'))


# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru în plus:
# o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor,
#  se va apela funcția respectivă cu instanța excepției ca parametru
def callback(e, file=None):
    params = e.args
    if isinstance(e, FileNotFoundError):
        print(str(FileNotFoundError), f'[EXCEPTION]:{params[0]} is neither file nor directory!')
    else:
        print(type(e), e, f'in file {file.name}')
    return []


def search_in_file_with_callback(file, to_search, callback_function):
    try:
        with open(file) as f:
            if f.seek(0, 2) < 4000000:  # we load small files (<4mb directly into memory)
                f.seek(0, 0)
                if to_search in f.read():
                    return True
                return False
            else:  # we read line by line bigger files (MIGHT not get the expected search term
                for line in f:
                    if to_search in line:
                        return True
                    return False
    except Exception as e:
        return callback_function(e, f)


def search_function_with_callback(target, to_search, callback_function):
    try:
        if isfile(target):
            if search_in_file_with_callback(target, to_search, callback_function):
                return [target]
            return []
        elif isdir(target):
            result = []
            for (root, directories, files) in os.walk(target):
                for fileName in files:
                    full_fileName = os.path.join(root, fileName)
                    if search_in_file_with_callback(full_fileName, to_search, callback_function):
                        result.append(full_fileName)
            return result
        else:
            raise FileNotFoundError(target, to_search)
    except Exception as e:
        return callback_function(e)


print("6:", search_function_with_callback('a', 'b', callback))
print("6:", search_function_with_callback('D:\DONALD', 'elemente', callback))
print("6:", search_function_with_callback('D:\DONALD\message.txt', 'elemente', callback))


# 7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar cu următoarele cămpuri:
# full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False daca se poate citi din/scrie in fisier.
def f_stats(path):
    stats = dict()
    stats['full_path'] = os.path.abspath(path)
    if os.path.isfile(path):
        stats['file_size'] = os.path.getsize(path)
    else:  # if it is a directory we calculate the summ of all files in the directory
        size = 0
        for (root, directories, files) in os.walk(path):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                size += os.path.getsize(full_fileName)
        stats['file_size'] = size
    stats['file_extension'] = splitext(path)[1][1:]
    stats['can_read'] = os.access(path, os.R_OK)
    stats['can_write'] = os.access(path, os.W_OK)
    return stats


print("7:", f_stats('D:\DONALD\message.txt'))
print("7:", f_stats('.'))


# Să se scrie o funcție ce primește un parametru cu numele dir_path.
# Acest parametru reprezintă calea către un director aflat pe disc.
# Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
# Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]
# Calea "C:\\director" are pe disc următoarea structură:
# C:\\director\\fisier1.txt <- fișier
# C:\\director\\fisier2.txt <- fișier
# C:\\director\\director1 <- director
# C:\\director\\director2 <- director
def absolute_from_root(path):
    return [os.path.join(path, f) for f in os.listdir(path) if isfile(join(path, f))]


print("8:", absolute_from_root('C:\\Users\Robert\OneDrive\Desktop'))
