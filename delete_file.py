import os
import shutil
import tqdm

def del_file(path):
    ls = os.listdir(path)
    for i in tqdm.tqdm(ls):
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

def del_dir(path):
    folder_paths = os.listdir(path)
    for folder in tqdm.tqdm(folder_paths):
        folder_path = os.path.join(path,folder)
        shutil.rmtree(folder_path)


if __name__ == '__main__':
    path = input('path:')
    del_file(path)
    del_dir(path)