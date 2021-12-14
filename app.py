#!/usr/bin/env python3

import Unzipfiles
import sortschool
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

class UnzipHandler(FileSystemEventHandler):    
    def on_created(self, event):
        #print(event.src_path)
        time.sleep(1)
        Unzipfiles.main()

class SortSchoolHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(event.src_path)
        sortschool.main()

# configuring the log
logging.basicConfig(filename='C:/Users/Hp/Documents/dewa_stuff/dewa_scripts/Automation tasks/app.log', 
                    level=logging.INFO, 
                    format='<%(asctime)s> %(levelname)s : %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')

# defining the folders to observe
downloads = "C:/Users/Hp/Downloads"
school = "C:/Users/Hp/Documents/dewa_stuff/School/"

# initializing all handlers
unzip_handler = UnzipHandler()
school_handler = SortSchoolHandler()

# initializing the observer
observer = Observer()

# scheduling all handlers
watch_downloads = observer.schedule(unzip_handler, downloads, recursive=False)
watch_school = observer.schedule(school_handler, school, recursive=False)

# starting the observer
observer.start()
print('Started')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()