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
    with open(file_name) as file:
        while True:
            line: str = file.readline()
            if not line:
                break
            if pattern in line:
                yield line

pattern: str = input("Enter a pattern to search: ")
file_name = "./rockyou.txt"
results_file = "./results.txt"

data = find_in_file(file_name, pattern)
results = list(data)

print(f'\nPattern {pattern} was found {len(results)} in words\n')
print(f't\The first words are: {results[:10]}\n')

with open(results_file, "w") as file:
    file.writelines(results)

print(f'The size of results is: {asizeof.asizeof(results, stats = 0)}\n')

print(os.stat(results_file))

