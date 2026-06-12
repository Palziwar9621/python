# ============================================================
# FILE I/O IN PYTHON
# ============================================================
# File I/O allows reading from and writing to files
# Python provides built-in functions and methods for file operations

# Opening a file: open('filename', 'mode')
# Modes:
# 'r'  - read (default)
# 'w'  - write (overwrites existing content)
# 'a'  - append (adds to end without overwriting)
# 'r+' - read and write
# 'rb' - read binary (for images, audio - works with bytes not strings)
# 'wb' - write binary
# 'rt' - read text (default, handles encoding automatically)
# 'wt' - write text

# binary mode: works with bytes, no encoding/decoding
# text mode:   works with strings, Python handles encoding (e.g. UTF-8)
# use binary for non-text files (images, audio)
# use text for text files

# ============================================================
# WRITING TO A FILE
# ============================================================
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# writelines() - write a list of strings at once
# include \n in each string for separate lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)

# append mode - adds to end without overwriting
with open('example.txt', 'a') as file:
    file.write('This is an additional line.\n')
# each run of this code adds another line, preserving previous content

# ============================================================
# READING FROM A FILE
# ============================================================
# read()      - reads entire file as one string
# readline()  - reads one line at a time
# readlines() - reads all lines, returns list of strings

# read() - entire file at once
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# readline() - line by line (good for large files)
f = open('example.txt', 'r')
while True:
    line = f.readline()
    if not line:  # empty string means end of file
        break
    print(line.strip())  # strip removes leading/trailing whitespace
f.close()  # important to close file to free system resources

# using with statement - automatically closes file even if error occurs
# 'r' is default mode so we can omit it
with open('example.txt') as file:
    content = file.read()
    print(content)

# handling FileNotFoundError
# writing to non-existent file creates it
# reading from non-existent file raises FileNotFoundError
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist. Please check the filename.")

# ============================================================
# SEEK AND TELL
# ============================================================
# seek(offset, whence) - move file pointer to specific position
# offset: number of bytes to move
# whence: 0 = from beginning (default), 1 = from current, 2 = from end

# tell() - returns current position of file pointer (bytes from start)
# useful for tracking where you are in the file

with open('example.txt', 'r') as file:
    print(type(file))    # <class '_io.TextIOWrapper'>
    file.seek(0)         # move pointer to beginning
    print(file.tell())   # 0 - at beginning
    data = file.read(5)  # read first 5 characters
    print(data)
    print(file.tell())   # now at position 5

# ============================================================
# TRUNCATE
# ============================================================
# truncate(size) - resize file to specified size in bytes
# if no size given, truncates at current pointer position
# data beyond specified size is REMOVED
# use with caution - can cause data loss

with open('example.txt', 'r+') as file:
    file.seek(0)
    file.truncate()  # clears all content from current position

# ============================================================
# BEST PRACTICE - USE WITH STATEMENT
# ============================================================
# with open(...) as file:
#     ...
# automatically closes the file even if an error occurs
# prevents resource leaks and data corruption
