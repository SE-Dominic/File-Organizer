import os, shutil
def organize_folder(folder_name):
    #loop through files in directory
    for filename in os.listdir(folder_name):
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
if __name__ == "__main__":
    downloads_file = "--file/path/here--"
    if not os.path.isdir(downloads_file):
        print("Invalid folder path. Try again.")
    else:
        organize_folder(downloads_file)