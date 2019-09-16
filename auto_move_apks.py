# 1. pip install watchdog
# 2. Change <USERNAME> below

from watchdog.observers import Observer  
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MoveFilesHandler(FileSystemEventHandler):
    def process(self, event):
        if not os.path.isdir(folder_destination):
            os.mkdir(folder_destination, 0o755)

        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destionation = folder_destination + "/" + filename
            os.rename(src, new_destionation)

    def on_modified(self, event):
        self.process(event)

folder_to_track = "/Users/<USERNAME>/Downloads"
folder_destination = "/Users/<USERNAME>/Desktop/APKs"

event_handler = MoveFilesHandler()

observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

