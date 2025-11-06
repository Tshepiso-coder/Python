
from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
# path = Path('alice.txt')

# count_words(path)


# path = Path("./text_files/little_women.txt")
# count_words(path)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
 'little_women.txt']
for filename in filenames:
    path = Path("./text_files/" + filename)
    count_words(path)
    
