"""This module is to find substring in a file with one word per line."""
import os

from pympler import asizeof


def find_in_file(file_name: str, pattern: str):
    """This function return line if find pattern."""
    with open(file_name, encoding="utf-8") as ifile:
        while True:
            line: str = ifile.readline()
            if not line:
                break
            if pattern in line:
                yield line


my_pattern: str = input("Enter a pattern to search: ")
FILE_NAME = "./rockyou.txt"
RESULTS_FILE = "./results.txt"

data = find_in_file(FILE_NAME, my_pattern)
results = list(data)

print(f"\nPattern {my_pattern} was found {len(results)} in words\n")
print(f"\nThe first words are: {results[:10]}\n")

with open(RESULTS_FILE, "w", encoding="utf-8") as rfile:
    rfile.writelines(results)

print(f"The size of results is: {asizeof.asizeof(results, stats = 0)}\n")

print(os.stat(RESULTS_FILE))
