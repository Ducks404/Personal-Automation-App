import os
import logging

def main(exclude = []):
    # Specifying source and target
    source = "C:/Users/Hp/Downloads/"
    target = 'C:/Users/Hp/Documents/dewa_stuff/School/'

    os.chdir(source)

    files = os.listdir("./")

    for file in files:
        # Moving files that start with Dean Agha
        if file.startswith('Dean Agha') and os.path.isfile(file) and file not in exclude:
            #print('found a school file')
            os.rename(f'{source}{file}', f'{target}{file}')
            logging.info(f'Moved {file} to School folder')

if __name__ == '__main__':
    main()
    #print('Done!')