import os
import re
import shutil
from random import randint

def dothething(folder_path):
    # for root, dirs, files in os.walk(folder_path):
    #     for dir_name in dirs:
    #         print(os.path.join(root, dir_name))
    #         print(dir_name)

    images_path = []

    sub_folders_list = os.listdir(folder_path)

    for sub in [os.path.join(folder_path, x) for x in sub_folders_list]:
        items_list = os.listdir(sub)
        target_images = []
        for i in items_list:
            if re.search('original', i):
                target_images.append(i)
        if target_images != []:
            images_path.append(os.path.join(sub, target_images[0]))
        
    for v in images_path:
        shutil.copy2(v, 'dataset/'+"".join(chr(randint(97,121)) for i in range(6))+ os.path.splitext(v)[1])
        # print('/new/'+"".join(chr(randint(97,121)) for i in range(10)) + os.path.splitext(v)[1])


def rename_files(folder_path):
    file_list = os.listdir(folder_path)
    file_list.sort()  # Sort the file names alphabetically

    for i, filename in enumerate(file_list, start=1):
        extension = os.path.splitext(filename)[1]  # Get the file extension
        new_filename = str(i) + extension
        new_filepath = os.path.join(folder_path, new_filename)
        old_filepath = os.path.join(folder_path, filename)
        os.rename(old_filepath, new_filepath)
        print(f"Renamed {filename} to {new_filename}")

if __name__ == '__main__':
    # print(os.getcwd())
    # path = 'D:\Github\BuildMate\FloorPlans-CNN-Classifier\dataset\cubicasa5k\colorful'
    path = 'D:\Github\BuildMate\FloorPlans-CNN-Classifier\dataset'
    # dothething(path)
    rename_files(path)
    # print(os.listdir(path))