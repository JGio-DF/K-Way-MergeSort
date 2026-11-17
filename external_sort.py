#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile
import sys


# Nodo del min-heap.
class heapnode:
    
    def __init__(self, item, fileHandler):
        self.item = item
        self.fileHandler = fileHandler


class externamMergeSort:

    def __init__(self):
        self.sortedTempFileHandlerList = []
        self.getCurrentDir()

    def getCurrentDir(self):
        self.cwd = os.getcwd()

    def heapify(self, arr, i, n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left].item < arr[i].item:
            smallest = left
        else:
            smallest = i

        if right < n and arr[right].item < arr[smallest].item:
            smallest = right

        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, smallest, n)

    def construct_heap(self, arr):
        l = len(arr) - 1
        mid = l // 2
        while mid >= 0:
            self.heapify(arr, mid, l)
            mid -= 1

    def mergeSortedtempFiles_low_level(self):
        heap_list = []
        sorted_output = []

        for tempFileHandler in self.sortedTempFileHandlerList:
            item = int(tempFileHandler.readline().strip())
            heap_list.append(heapnode(item, tempFileHandler))

        self.construct_heap(heap_list)

        while True:
            min_node = heap_list[0]
            if min_node.item == sys.maxsize:
                break

            sorted_output.append(min_node.item)
            fileHandler = min_node.fileHandler
            item = fileHandler.readline().strip()

            if not item:
                item = sys.maxsize
            else:
                item = int(item)

            heap_list[0] = heapnode(item, fileHandler)
            self.heapify(heap_list, 0, len(heap_list))

        return sorted_output

    def splitFiles(self, largeFileName, smallFileSize):
        temp_dir = os.path.join(self.cwd, 'temp')
        os.makedirs(temp_dir, exist_ok=True)

        with open(largeFileName, 'r', encoding='utf-8') as largeFileHandler:
            tempBuffer = []
            size = 0
            while True:
                number = largeFileHandler.readline()
                if not number:
                    break
                tempBuffer.append(number)
                size += 1

                if size % smallFileSize == 0:
                    tempBuffer = sorted(tempBuffer, key=lambda no: int(no.strip()))
                    tempFile = tempfile.NamedTemporaryFile(
                        mode='w+', dir=temp_dir, delete=False, encoding='utf-8'
                    )
                    tempFile.writelines(tempBuffer)
                    tempFile.seek(0)
                    self.sortedTempFileHandlerList.append(tempFile)
                    tempBuffer = []


if __name__ == '__main__':
    largeFileName = 'largefile'
    smallFileSize = 10
    obj = externamMergeSort()
    obj.splitFiles(largeFileName, smallFileSize)
    print("Resultado ordenado:")
    print(obj.mergeSortedtempFiles_low_level())
