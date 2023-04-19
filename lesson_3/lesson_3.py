"""This module providing Function to find substring in a file with one word per line."""
import os
from pympler import asizeof

## Works but eats a lot of memory
# def find_in_file(file_name: str, pattern: str) -> list[str]:
#     results: list[any] = []
#     with open(file_name, "r") as file:
#         while word := file.readline():
#             if pattern in word.lower():
#                 results.append(word)
#     return results

def find_in_file(file_name: str, pattern: str):
    """This function return line if find pattern."""
    with open(file_name, encoding="utf-8") as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if pattern in line:
                yield line

pattern: str = input("Enter a pattern to search: ")
FILE_NAME = "./rockyou.txt"
RESULTS_FILE = "./results.txt"

data = find_in_file(FILE_NAME, pattern)
results = list(data)

print(f'\nPattern {pattern} was found {len(results)} in words\n')
print(f'\nThe first words are: {results[:10]}\n')

with open(RESULTS_FILE, "w", encoding="utf-8") as file:
    file.writelines(results)

print(f'The size of results is: {asizeof.asizeof(results, stats = 0)}\n')

print(os.stat(RESULTS_FILE))
