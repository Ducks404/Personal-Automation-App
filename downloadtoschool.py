import os
import shutil

def main(exclude = []):
    target = 'C:/Users/Hp/Documents/dewa_stuff/School/'
    home = "C:/Users/Hp/Downloads/"

    os.chdir(home)

    files = os.listdir("./")

    for file in files:
        if file.startswith('Dean Agha') and os.path.isfie(file) and file not in exclude:
            print('found a school file')
            shutil.move(f'{home}{file}', f'{target}{file}')

if __name__ == '__main__':
    main()
    print('Done!')