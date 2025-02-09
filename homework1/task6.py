import os

def count_words(filename):
    """ Reads a file and returns the number of words in it. """
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, "r") as file:
        return len(file.read().split())

# Ensure the function runs when executing task6.py
if __name__ == "__main__":
    print(f"Word count in task6_read_me.txt: {count_words('task6_read_me.txt')}")