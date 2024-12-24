## File Handling in Python

**Last Updated**: 20 Dec, 2024

File handling refers to the process of performing operations on a file such as creating, opening, reading, writing, and closing it, through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

### File Modes in Python

When opening a file, we must specify the mode we want to use, which specifies what we want to do with the file. Here’s a table of the different modes available:

| Mode  | Description                                                                                  |
|-------|----------------------------------------------------------------------------------------------|
| `r`   | **Read mode**. Opens a file for reading. The file must exist.                                |
| `w`   | **Write mode**. Opens a file for writing. Creates a new file if it doesn’t exist or truncates the file if it exists. |
| `a`   | **Append mode**. Opens a file for appending. Creates a new file if it doesn’t exist.        |
| `b`   | **Binary mode**. Opens a file in binary mode.                                                |
| `t`   | **Text mode**. Opens a file in text mode. (This is the default mode.)                       |
| `x`   | **Exclusive creation mode**. Creates a new file and fails if it already exists.             |
| `r+`  | **Read and write mode**. Opens a file for both reading and writing. The file must exist.    |
| `w+`  | **Write and read mode**. Opens a file for both writing and reading. Creates a new file if it doesn’t exist or truncates the file if it exists. |
| `a+`  | **Append and read mode**. Opens a file for appending and reading. Creates a new file if it doesn’t exist. |
