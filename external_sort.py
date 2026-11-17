#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile
import sys
import time


class HeapNode:
    def __init__(self, item, file_handler):
        self.item = item
        self.file_handler = file_handler


class ExternalMergeSort:
    def __init__(self):
        self.sorted_temp_handlers = []
        self.cwd = os.getcwd()
        self.temp_dir = os.path.join(self.cwd, 'temp')

    def heapify(self, arr, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and arr[left].item < arr[smallest].item:
            smallest = left

        if right < n and arr[right].item < arr[smallest].item:
            smallest = right

        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, smallest, n)

    def construct_heap(self, arr):
        n = len(arr)
        for mid in range(n // 2 - 1, -1, -1):
            self.heapify(arr, mid, n)  # Corrección: pasar n completo, no n - 1

    def _save_run(self, buffer):
        buffer.sort()  # Ordena enteros directamente en RAM
        temp_file = tempfile.NamedTemporaryFile(
            mode='w+', dir=self.temp_dir, delete=False, encoding='utf-8'
        )
        temp_file.writelines(f"{num}\n" for num in buffer)
        temp_file.seek(0)
        self.sorted_temp_handlers.append(temp_file)

    def split_files(self, large_file_name, chunk_size):
        os.makedirs(self.temp_dir, exist_ok=True)
        if not os.path.exists(large_file_name):
            raise FileNotFoundError(f"No se encontró el archivo: {large_file_name}")

        with open(large_file_name, 'r', encoding='utf-8') as large_file:
            temp_buffer = []
            for line in large_file:
                clean_line = line.strip()
                if not clean_line:  # Ignora líneas vacías
                    continue
                temp_buffer.append(int(clean_line))

                if len(temp_buffer) == chunk_size:
                    self._save_run(temp_buffer)
                    temp_buffer = []

            # Corrección: guardar el bloque residual si N no es múltiplo de chunk_size
            if temp_buffer:
                self._save_run(temp_buffer)

    def merge_sorted_temp_files(self, output_file_name):
        heap_list = []

        for handler in self.sorted_temp_handlers:
            line = handler.readline().strip()
            if line:
                heap_list.append(HeapNode(int(line), handler))

        # Corrección: manejo de archivo vacío
        if not heap_list:
            open(output_file_name, 'w', encoding='utf-8').close()
            return 0

        self.construct_heap(heap_list)
        total_written = 0

        # Escribe directo a disco en lugar de acumular en RAM
        with open(output_file_name, 'w', encoding='utf-8') as out_file:
            while True:
                min_node = heap_list[0]
                if min_node.item == sys.maxsize:
                    break

                out_file.write(f"{min_node.item}\n")
                total_written += 1

                handler = min_node.file_handler
                next_line = handler.readline().strip()

                next_item = int(next_line) if next_line else sys.maxsize
                heap_list[0] = HeapNode(next_item, handler)
                self.heapify(heap_list, 0, len(heap_list))

        self._cleanup()
        return total_written

    def _cleanup(self):
        for handler in self.sorted_temp_handlers:
            name = handler.name
            handler.close()
            if os.path.exists(name):
                os.remove(name)
        self.sorted_temp_handlers.clear()


if __name__ == '__main__':
    large_file = 'largefile'
    output_file = 'sorted_output.txt'
    chunk_size = 10  # Puedes variar esto (ej. 10, 100, 1000) para comparar tiempos

    inicio = time.perf_counter()
    sorter = ExternalMergeSort()
    sorter.split_files(large_file, chunk_size)
    num_runs = len(sorter.sorted_temp_handlers)
    total = sorter.merge_sorted_temp_files(output_file)
    fin = time.perf_counter()

    print(f"Elementos ordenados: {total}")
    print(f"Runs generados (k): {num_runs}")
    print(f"Tiempo total: {fin - inicio:.6f} segundos")
    print(f"Resultado guardado en: {output_file}")