import os
import logging
import var

def main(exclude = []):
    path = var.school

    os.chdir(path)

    files = os.listdir("./")

    pdf = ['pdf']
    images = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'tiff']
    videos = ['mp4', 'avi', 'webm']
    audios = ['mp3', 'wav']

    for file in files:
        if os.path.isfile(file) and file not in exclude:
            ext = (file.split(".")[-1]).lower()
            if ext in pdf:
                os.rename(f'{path}{file}', f'{path}PDF/{file}')
                logging.info(f'Moved {file} to PDF folder')
            elif ext in images:
                os.rename(f'{path}{file}', f'{path}Images/{file}')
                logging.info(f'Moved {file} to Images folder')
            elif ext in videos:
                os.rename(f'{path}{file}', f'{path}Videos/{file}')
                logging.info(f'Moved {file} to Videos folder')
            elif ext in audios:
                os.rename(f'{path}{file}', f'{path}Audios/{file}')
                logging.info(f'Moved {file} to Audios folder')
            else:
                os.rename(f'{path}{file}', f'{path}Others/{file}')
                logging.info(f'Moved {file} to Others folder')

if __name__ == '__main__':
    main()