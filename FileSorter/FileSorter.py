import os, shutil, time
from watchdog.observers import Observer
from watchdog.events import (FileSystemEventHandler)


#allocates old directory
orig = r'D:\Downloads'


#creates a list of files already existing in new directory
existingfiles = []

files_moved = 0

sorted_path_dict = {
    'audio' : r'D:\Music\Sorted Audio',
    'video' : r'D:\Videos\Sorted Videos',
    'image' : r'D:\Pictures\Sorted Images',
    'compressed' : r'D:\Documents\FileSorter\Compressed Files',
    'torrent' : r'D:\Documents\FileSorter\Torrent Files',
    'executable' : r'D:\Documents\FileSorter\Executable Files',
    'document' : r'D:\Documents\FileSorter\Document Files',
}

#extension variables
audio_f = ['.mp3', '.wav']
video_f = ['.mp4', '.avi', '.mkv']
image_f = ['.jpg', '.png', '.gif', '.bmp']
compressed_f = ['.zip', '.rar', '.7z']
torrent_f = ['.tor', '.torrent']
executable_f = ['.exe', '.msi']
document_f = ['.txt', '.doc', '.docx', '.rtf', '.pdf']

file_type_dict = {
    'audio' : audio_f,
    'video' : video_f,
    'image' : image_f,
    'compressed' : compressed_f,
    'torrent' : torrent_f,
    'executable' : executable_f,
    'document' : document_f,
}

#checks if directory exists. creates directory if doesn't exist
for x, foldercheck in sorted_path_dict.items():
    if os.path.exists(foldercheck):
        pass
    else:
        os.mkdir(foldercheck)

#uses watchdog to organize files
class Watcher(FileSystemEventHandler):
    def sort(self):
        global files_moved
        for filename in os.listdir(orig):
            os.chdir(orig)
            copycount = 0
            if os.path.isfile(filename):
                for file_type_var, extensions_var in file_type_dict.items():
                    file_ext = os.path.splitext(filename)[1].lower()
                    for i in extensions_var:
                        if i == file_ext:
                            print(filename, "is a", file_type_var, "file")
                            for spd_ftype_var, spd_path_var in sorted_path_dict.items():
                                if file_type_var == spd_ftype_var:
                                    new = spd_path_var
                                    time.sleep(.4)
                                    if filename not in os.listdir(new):
                                        os.rename(filename, new + "\\" + filename)
                                        print(filename, "has been moved to ", new)
                                        files_moved += 1
                                    else: 
                                        print("This file already exists in the new directory. We'll rename it for you.")
                                        existingfiles.append(filename)
                                        copycount += 1
                                        new_name = new + '\\' + os.path.splitext(filename)[0] + " " + str(copycount) + os.path.splitext(filename)[1]
                                        os.rename(filename, new_name)
                                        print(filename, " has been renamed to ", new_name)
                                        files_moved += 1

            
    #tells watchdog when to schedule handler
    def on_any_event(self, event):
        self.sort()
                    

event_handler = Watcher()

#run on start
event_handler.sort()


observer = Observer()

#schedules observer and allocates path
observer.schedule(event_handler, orig, recursive=True)

#starts observer
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

if len(existingfiles) > 0:
    print("These files already existed in the new directory and have been renamed.")
    print(*existingfiles, sep='\n')

print("In total, we moved", files_moved, "files for you.\nHope that was helpful!")
print("All of your files have been organized successfully.")

input()