import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "testpython"
class FileSystemEventHandler(FileSystemEventHandler):
    def on_created(self, event):
         print(f"Olá,{event.src_path}foi criado!")
         
    def on_deleted(self,event):
         print(f"Opa! Alguém excluiu{event.src_path}!")
         
         
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    Observer.stop()
     
     
     
     
    