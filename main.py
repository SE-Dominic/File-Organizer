import os, shutil
#/workspaces/File-Organizer/dummy_folder/one.txt
def organize_folder(folder_name):
    #loop through files in directory
    for filename in os.listdir(folder_name):
        print(f"printing filename: {filename}")
        file_path = os.path.join(folder_name, filename) #/dummy_folder/image.png    
        #if its a directory skip it
        if os.path.isdir(file_path):
            continue
        #get file extention without dot
        file_extension = os.path.splitext(filename)[1].lower().strip('.')
        if not file_extension:
            file_extension = "other"
        #create subfolder for extenstion if it doesn't exist
        #combine folder path with the file extension
        new_folder = os.path.join(folder_name, file_extension)
        #make the new folder a directory
        os.makedirs(new_folder, exist_ok=True)
        #move file
        shutil.move(file_path, os.path.join(new_folder, filename))
        print(f"Moved: {filename} --> {new_folder}")

def rename_file(folder_name):
    file_to_be_found = str(input("Enter file name to be found: "))
    was_found = False
    for file in os.listdir(folder_name):
        if os.path.isdir(file): #skip over folders inside of folder path (we only want files)
            continue
        if file == file_to_be_found:
            newName = str(input("File found! Enter new file name: "))
            old_path = os.path.join(folder_name, file) #source
            new_path = os.path.join(folder_name, newName) #destination
            os.rename(old_path, new_path)
            was_found = True
            break
        else:
            continue
    if was_found == True:
        print("Name as successfully changed!")
    else:
        print("File not found in folder.")
    

if __name__ == "__main__":
    chosen_folder = "/workspaces/File-Organizer/dummy_folder"
    if not os.path.isdir(chosen_folder):
        print("Invalid folder path. Try again.")
    else:
        #organize_folder(chosen_folder)
        rename_file(chosen_folder)