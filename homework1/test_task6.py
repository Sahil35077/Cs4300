import pytest
import os
from task6 import count_words

# List of text files for testing
TEXT_FILES = ["task6_read_me.txt"]

# Metaprogramming: Dynamically create test functions based on file names
def generate_test_function(filename):
    def test_function():
        file_path = os.path.join(os.path.dirname(__file__), filename)
        assert os.path.exists(file_path), f"File {filename} does not exist!"
        assert count_words(filename) > 0, f"{filename} should contain words!"
    return test_function

# Generate a test function for each file
for filename in TEXT_FILES:
    test_name = f"test_word_count_{filename.replace('.', '_')}"
    globals()[test_name] = generate_test_function(filename)