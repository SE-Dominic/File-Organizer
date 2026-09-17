from fileData import FileInfo
import os
class FolderRepository:
    def __init__(self, userEnteredPath):
        self.path = userEnteredPath
        self.files: list[FileInfo] = []
    def populateRepo(self):
        for filename in os.listdir(self.path):
            fileObject = FileInfo()
            if os.path.isdir(filename):
                continue
            
            filePath = os.path.join(self.path, filename) #get path
            file_extension = os.path.splitext(filename)[1].lower().strip('.') #get file extension
            file_size = os.path.getsize(filePath) #get file size in bytes
            
            fileObject.fileData["name"] = filename
            fileObject.fileData["path"] = filePath
            fileObject.fileData["extension"] = file_extension
            fileObject.fileData["size"] = file_size
            self.files.append(fileObject)
    def printFileNames(self):
        for obj in self.files:
            print(obj.fileData["name"])
    def findFile(self, key) -> int:
        for idx in range(self.files):
            if (self.files[idx]["name"] == key):
                return idx
            else:
                print("Not found.")
                return -1