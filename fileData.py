class FileInfo:
    def __init__(self):
        self.fileData = {
            "name": str,
            "path": str,
            "size": int,
            "mod_time": float,
            "extension": str,
        }
    def getFileName(self):
        return self.fileData["name"]
    def getFilePath(self):
        return self.fileData["path"]
    def getFileSize(self):
        return self.fileData["size"]
    def getModificationTime(self):
        return self.fileData["mod_time"]
    def getFileExtension(self):
        return self.fileData["extension"]