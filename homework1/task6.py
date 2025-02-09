def count_words(filename):
    with open(filename, "r") as file:
        return len(file.read().split())

# Ensure the file exists before running
if __name__ == "__main__":
    print(count_words("task6_read_me.txt"))