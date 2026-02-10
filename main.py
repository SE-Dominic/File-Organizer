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
    for file in os.listdir(folder_name):
        if file == file_to_be_found:
            newName = str(input("File was found! Rename to: ")) #ex. onee.txt
            fileRename = f"{folder_name}/{newName}"
            os.rename(file, fileRename)
        else:
            continue
    


if __name__ == "__main__":
    downloads_file = "/workspaces/File-Organizer/dummy_folder"
    if not os.path.isdir(downloads_file):
        print("Invalid folder path. Try again.")
    else:
        rename_file(downloads_file)
        #organize_folder(downloads_file)