import os
import shutil

def main(exclude = []):
    path = "C:/Users/Hp/Documents/dewa_stuff/School/"

    os.chdir(path)

    files = os.listdir("./")

    pdf = ['pdf']
    images = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'tiff']
    videos = ['mp4', 'avi', 'webm']
    audios = ['mp3', 'wav']

    for file in files:
        if os.path.isfile(file) and file not in exclude:
            print('found a school pdf')
            shutil.move(f'{path}{file}', f'{path}{file}')

if __name__ == '__main__':
    main()
    print('Done!')