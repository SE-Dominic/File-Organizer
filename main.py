from folderRepository import FolderRepository
import strategy, fileOrganizerService
if __name__ == "__main__":
    '''
    DUMMY FOLDER PATH -> /workspaces/File-Organizer/dummy_folder
    '''
    dummyPath = "/workspaces/File-Organizer/dummy_folder"
    fileService = fileOrganizerService.FileService(dummyPath)
    fileService.organizeByExtension()
    fileService.repo.printFileNames()