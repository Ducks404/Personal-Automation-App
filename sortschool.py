import os

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
            ext = (file.split(".")[-1]).lower()
            if ext in pdf:
                os.rename(f'{path}{file}', f'{path}PDF/{file}')
            elif ext in images:
                os.rename(f'{path}{file}', f'{path}Images/{file}')
            elif ext in videos:
                os.rename(f'{path}{file}', f'{path}Videos/{file}')
            elif ext in audios:
                os.rename(f'{path}{file}', f'{path}Audios/{file}')
            else:
                os.rename(f'{path}{file}', f'{path}Others/{file}')

if __name__ == '__main__':
    main()