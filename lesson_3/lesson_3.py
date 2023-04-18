
def find_in_file(file_name: str, pattern: str) -> list[str]:
    results: list[any] = []
    with open(file_name, "r") as file:
        while word := file.readline():
            if pattern in word.lower():
                results.append(word)
    return results
    

pattern: str = input("Enter word: ")
file_name = "./rockyou.txt"
results: list[str] = find_in_file(file_name, pattern)
print(len(results))

with open("./results.txt", "w") as file:
    file.writelines(results)
