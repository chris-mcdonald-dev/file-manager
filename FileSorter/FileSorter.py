import os, shutil

#checks if directory exists. creates directory if doesn't exist
new_dir_root = os.chdir('D:\\Documents')
checklist = os.listdir(new_dir_root)
dircheck = checklist.count('PyTest2')
if dircheck == 0:
    os.system('mkdir PyTest2')

#allocates new and old directories
new = r'D:\\Documents\\PyTest2'
orig = r'D:\\Downloads\\Test'

#organizes contents of folder into a list
ofiles = os.listdir(orig)
nfiles = os.listdir(new)

#creates a list of files already existing in new directory
existingfiles = []

no_files_moved = True

for file in ofiles:
    os.chdir(orig)
    if os.path.isfile(file):
        filecheck = nfiles.count(file)
        if filecheck == 0:
            shutil.move(file, new)
            no_files_moved = False
        else:
            existingfiles.append(file)

if len(existingfiles) > 0:
    print("These files already exist in the new directory.")
    print(*existingfiles, sep='\n')

if no_files_moved == True:
    print("\nAll of your files already existed in the new directory.")
else:
    print("All your files have been moved successfully.")