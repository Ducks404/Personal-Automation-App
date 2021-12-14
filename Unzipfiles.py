#!/usr/bin/env python3

import zipfile
import tarfile
import py7zr
import os
import re
import logging
import var

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

def unzip(file_name, folder):
    # opening the zip file in READ mode
    with zipfile.ZipFile(file_name, 'r') as zip:  
        # extracting all the files
        zip.extractall(folder)

def untar(file_name, folder):
    # opening the tar file in READ mode
    with tarfile.open(file_name) as tar:  
        # extracting all the files
        tar.extractall(folder)

def unzip7(file_name, folder):
    # opening the 7zip file in READ mode
    with py7zr.SevenZipFile(file_name) as zip7:
        # extracting all the files
        zip7.extractall(folder)


def main(exclude=[]):
    # specifying the path to Downloads folder
    path = var.downloads
    os.chdir(path)

    # list all files in Downloads folder
    files = os.listdir('./')
    #print('main called')
    #print(files)
    
    zips = ['zip']
    tar = ['tar', 'gz']
    zip7 = ['7z']

    for file in files:
        if os.path.isfile(file) and file.startswith('_') and file not in exclude:
            #print(f'{file} is file and startswith _')
            ext = (file.split(".")[-1]).lower()

            # checking if file is a compressed file
            if ext in zips + tar + zip7:
                print('compressed file found')
                # making a folder
                folder = file[1:-4]

                # make a folder
                folder = make_folder(folder)

                if ext in zips:
                    #print(f'{file} is a zip file')
                    unzip(file, folder)
                    logging.info(f"Zip extracted {file}")
                elif ext in tar:
                    untar(file, folder)
                    logging.info(f"Tar extracted {file}")
                elif ext in zip7:
                    unzip7(file, folder)
                    logging.info(f"7zip extracted {file}")
                
                # deleting the compressed file
                os.remove(file)

    #print('loop finished')

if __name__ == '__main__':
    main()