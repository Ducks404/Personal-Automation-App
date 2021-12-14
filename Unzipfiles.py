#!/usr/bin/env python3

from zipfile import ZipFile
import os
import re
import logging

def make_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        return folder
    else:
        # regex meaning "(any number)"
        count = re.findall("\([0-9]+\)$", folder)
        count = int(count[0][1:-1]) if count else False
        if count:
            count += 1
            folder = folder[:-3]
            folder = f'{folder}({count})'
        else:
            folder = f'{folder}(2)'
        return make_folder(folder)

def unzip(file_name):
    # making a folder
    folder = file_name[1:-4]

    # make a folder
    folder = make_folder(folder)

    # opening the zip file in READ mode
    with ZipFile(file_name, 'r') as zip:  
        # extracting all the files
        zip.extractall(folder)

    # deleting the zip file
    os.remove(file_name)

def main(exclude=[]):
    # specifying the path to Downloads folder
    path = "C:/Users/Hp/Downloads"
    os.chdir(path)

    # list all files in Downloads folder
    files = os.listdir('./')
    print('main called')
    #print(files)
    
    zips = ['zip', '7z', 'tar', 'gz']

    for file in files:
        if os.path.isfile(file) and file.startswith('_') and file not in exclude:
            print(f'{file} is file and startswith _')
            ext = (file.split(".")[-1]).lower()

            # checking if file is a zip
            if ext in zips:
                #print(f'{file} is a zip file')
                unzip(file)
                logging.info(f"Extracted {file}")

    print('loop finished')

if __name__ == '__main__':
    main()