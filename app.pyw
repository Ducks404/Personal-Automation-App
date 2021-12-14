#!/usr/bin/env python3

import Unzipfiles
import downloadtoschool
import sortschool
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import os
from win10toast import ToastNotifier

# Unzips zipfiles in Downloads folder that start with _
class UnzipHandler(FileSystemEventHandler):    
    def on_modified(self, event):
        time.sleep(1)
        Unzipfiles.main()

# Sorts files in School folder
class SortSchoolHandler(FileSystemEventHandler):
    def on_modified(self, event):
        sortschool.main()

# Moves files starting with Dean Agha to School folder
class DownloadToSchoolHandler(FileSystemEventHandler):
    def on_modified(self, event):
        downloadtoschool.main()

# Toast notifier
toast = ToastNotifier()
toast.show_toast("Automation App", "The app has been started", duration=30)

# Changing current directory
os.chdir('C:/Users/Hp/Documents/dewa_stuff/dewa_scripts/Automation tasks/')

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
downloadtoschool_handler = DownloadToSchoolHandler()

# initializing the observer
observer = Observer()

# scheduling all handlers
watch_downloads = observer.schedule(unzip_handler, downloads, recursive=False)
observer.add_handler_for_watch(downloadtoschool_handler, watch_downloads)

watch_school = observer.schedule(school_handler, school, recursive=False)

# starting the observer
observer.start()
#print('Started')
logging.info('Started')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()