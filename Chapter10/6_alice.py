# ======================================
#SUMMARY FROM claude.ai

# Creates a Path object - Uses pathlib.Path to represent the file 'alice.txt'

# Try block - Attempts to read the file's contents:
# Uses read_text() with UTF-8 encoding to read the entire file as a string

# Exception handling - If the file doesn't exist:
# Catches the FileNotFoundError exception
# Prints a friendly error message instead of crashing

# Else block - If the file was successfully read:
# Splits the text into words using split() (splits on whitespace)
# Counts the number of words using len()
# Prints the word count

# Key concepts:
# try-except-else: Error handling structure that prevents program crashes
# pathlib.Path: Modern way to work with file paths in Python
# FileNotFoundError: Specific exception raised when a file can't be found
# else clause: Only runs if no exception occurred in the try block
# The word count is approximate because split() separates on any whitespace, 
# which might not perfectly match actual word boundaries in all cases

# This is great for making programs more robust and user-friendly when working with files!

#=========================================

from pathlib import Path
path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry. The file {path} does not exist! ")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")