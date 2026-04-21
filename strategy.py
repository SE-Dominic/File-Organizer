from abc import ABC, abstractmethod
from fileData import FileInfo
#interface
class Strategy(ABC):
    @abstractmethod
    def sort(self, arr: list[FileInfo]):
        pass

#context
class SortingContext:
    def __init__(self):
        self.sortingStrategy = None
    def setSortStrat(self, strat: Strategy):
        self.sortingStrategy = strat
    def performSort(self, ar):
        self.sortingStrategy.sort(ar)


#concrete strategies
class SortByExtension(Strategy):
    def sort(self, arr: list[FileInfo]):
        """Sort FileInfo objects by extension using quickSort"""
        if arr is None or len(arr) == 0:
            return
        self._quickSort(arr, 0, len(arr) - 1)
    
    def _quickSort(self, arr: list[FileInfo], low: int, high: int):
        """Recursive quickSort helper"""
        if low < high:
            partition_index = self._partition(arr, low, high)
            self._quickSort(arr, low, partition_index - 1)
            self._quickSort(arr, partition_index + 1, high)
    
    def _partition(self, arr: list[FileInfo], low: int, high: int) -> int:
        """Partition array around pivot (extension at high index)"""
        pivot_extension = arr[high].getFileExtension().lower()
        i = low - 1
        
        for j in range(low, high):
            current_extension = arr[j].getFileExtension().lower()
            # Compare extensions; files with no extension come first
            if self._compare_extensions(current_extension, pivot_extension) <= 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    def _compare_extensions(self, ext1: str, ext2: str) -> int:
        """
        Compare two extensions.
        Returns: negative if ext1 < ext2, 0 if equal, positive if ext1 > ext2
        Files with no extension (empty string) sort first.
        """
        if ext1 == "" and ext2 == "":
            return 0
        if ext1 == "":
            return -1
        if ext2 == "":
            return 1
        return -1 if ext1 < ext2 else (0 if ext1 == ext2 else 1)
class SortBySize(Strategy):
    def sort(self, arr: list[FileInfo]):
        """Sort FileInfo objects by file size using quickSort"""
        if arr is None or len(arr) == 0:
            return
        self._quickSort(arr, 0, len(arr) - 1)
    
    def _quickSort(self, arr: list[FileInfo], low: int, high: int):
        """Recursive quickSort helper"""
        if low < high:
            partition_index = self._partition(arr, low, high)
            self._quickSort(arr, low, partition_index - 1)
            self._quickSort(arr, partition_index + 1, high)
    
    def _partition(self, arr: list[FileInfo], low: int, high: int) -> int:
        """Partition array around pivot (size at high index)"""
        pivot_size = arr[high].getFileSize()
        i = low - 1
        
        for j in range(low, high):
            if arr[j].getFileSize() <= pivot_size:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
 
 
class SortByModificationTime(Strategy):
    def sort(self, arr: list[FileInfo]):
        """Sort FileInfo objects by modification time using quickSort"""
        if arr is None or len(arr) == 0:
            return
        self._quickSort(arr, 0, len(arr) - 1)
    
    def _quickSort(self, arr: list[FileInfo], low: int, high: int):
        """Recursive quickSort helper"""
        if low < high:
            partition_index = self._partition(arr, low, high)
            self._quickSort(arr, low, partition_index - 1)
            self._quickSort(arr, partition_index + 1, high)
    
    def _partition(self, arr: list[FileInfo], low: int, high: int) -> int:
        """Partition array around pivot (mod_time at high index)"""
        pivot_time = arr[high].getModificationTime()
        i = low - 1
        
        for j in range(low, high):
            if arr[j].getModificationTime() <= pivot_time:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
 
 
 