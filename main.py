import os, shutil

def organize_folder(folder_name):
    #loop through files in directory
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename) #/dummy_folder/filename    
        #if file path is a directory skip over it
        if os.path.isdir(file_path):
            continue
        #get file extention without dot
        file_extension = os.path.splitext(filename)[1].lower().strip('.')
        '''
        splitext(filename) splits path into root and extension i.e ("photo", ".png")
        [1] grabs the second item returned from the splitext i.e ".png"
        .lower puts all characters into lowercase 
        .strip() removes any . characters from the start and end of a string
        '''
        #create subfolder for extenstion if it doesn't exist
        if not file_extension:
            file_extension = "other"
        
        #combine folder path with the file extension
        new_folder = os.path.join(folder_name, file_extension)
        
        os.makedirs(new_folder, exist_ok=True) #make the new folder a directory
        shutil.move(file_path, os.path.join(new_folder, filename)) #move file
        
        print(f"Moved: {filename} --> {new_folder}")

def rename_file(folder_name):
    file_to_be_found = str(input("Enter file name to be found: "))
    was_found = False
    for file in os.listdir(folder_name):
        #if os.path.isdir(file): #skip over folders inside of folder path (we only want files)
         #   print(f"{file} is a directory. ")
          #  continue
        if file == file_to_be_found:
            newName = str(input("File found! Enter new file name: "))
            
            old_path = os.path.join(folder_name, file) #source
            new_path = os.path.join(folder_name, newName) #destination
            os.rename(old_path, new_path)
            was_found = True #lets us know we have completed the task and we can print success message
            break
        else:
            continue
    if was_found == True:
        print("Name was successfully changed!")
    else:
        print("File not found in folder.")
    

class Dashboard:
    def __init__(self):
        self.folder_path: str

    def options(self):
        print("1. Organize Folder")
        print("2. Rename File")
        print("3. EXIT PROGRAM")

    def dashboard_loop(self):
        userinp = str(input("Enter folder path: "))
        if not os.path.isdir(userinp):
            print("Invalid folder path.")
            return
        self.folder_path = userinp
        self.options()
        choice = int(input("Enter choice: "))
        while choice != 3:
            if choice == 1:
                organize_folder(self.folder_path)
                choice = int(input(f"\n{self.options()}\n Enter choice: "))
            elif choice == 2:
                rename_file(self.folder_path)
                choice = int(input(f"\n{self.options()}\n Enter choice: "))
            else:
                print("Invalid choice. Try again.")
                choice = int(input(f"\n{self.options()}\n Enter choice: "))
        print("Program is terminated.")

if __name__ == "__main__":
    '''
    DUMMY FOLDER PATH -> /workspaces/File-Organizer/dummy_folder
    '''
    dashboard:Dashboard = Dashboard() 
    dashboard.dashboard_loop()
