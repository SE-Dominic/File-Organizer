import os, shutil
import folderRepository, strategy
#prepopulate
class FileService:
    def __init__(self, userEnteredPath):
        self.path = userEnteredPath
        self.repo = folderRepository.FolderRepository(self.path)
        self.strat = strategy.SortingContext()
        self.repo.populateRepo()
    def menu():
        print("1. Set new file path")
        print("Organization tools: ")
        print("2. By Extension")
        print("3. By File size")
        print("4. EXIT")
    def rename_file(self, fileName):
        was_found = False
        for file in os.listdir(self.path):
            if file == fileName:
                newName = str(input("File found! Enter new file name: "))
                old_path = os.path.join(fileName, file) #source
                new_path = os.path.join(fileName, newName) #destination
                os.rename(old_path, new_path)
                was_found = True #lets us know we have completed the task and we can print success message
                break
            else:
                continue
        if was_found == True:
            print("Name was successfully changed!")
        else:
            print("File not found in folder.") 
    
    def organizeByExtension(self):
        self.strat.setSortStrat(strategy.SortByExtension())
        self.strat.performSort(self.repo)
    def organizeBySize(self):
        self.strat = strategy.SortingContext.setSortStrat(strategy.SortBySize)
        self.strat.performSort(self.repo)