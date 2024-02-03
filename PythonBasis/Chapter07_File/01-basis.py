"""
Created by Ignorant on 2024/1/28
Description: File Basis
"""

'''
open(file: int | str | bytes | PathLike[str] | PathLike[bytes],
        mode: Literal["r+", "+r", "rt+", "r+t", "+rt", "tr+", "t+r", "+tr", "w+", "+w", "wt+", "w+t", "+wt", "tw+",
                    "t+w", "+tw", "a+", "+a", "at+", "a+t", "+at", "ta+", "t+a", "+ta", "x+", "+x", "xt+", "x+t", "+xt",
                    "tx+", "t+x", "+tx", "w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx", "r", "rt", "tr", "U", "rU",
                    "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"] = "r",
        buffering: int = -1,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
        closefd: bool = True,
        opener: (str, int) -> int | None = None) -> TextIOWrapper
    Open file and return a stream. Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path if the file isn't in the current
    working directory) of the file to be opened or an integer file descriptor of the file to be wrapped.
    (If a file descriptor is given, it is closed when the returned I/O object is closed unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file is opened.
    It defaults to 'r' which means open for reading in text mode. Other common values are 'w' for writing
    (truncating the file if it already exists), 'x' for creating and writing to a new file,
    and 'a' for appending (which on some Unix systems, means that all writes append to the end of the file
    regardless of the current seek position). In text mode, if encoding is not specified the encoding used
    is platform dependent: locale.getpreferredencoding(False) is called to get the current locale encoding.
    (For reading and writing raw bytes use binary mode and leave encoding unspecified.) The available modes are:
    
Character Meaning
    >'r': open for reading (default)
    >'w': open for writing, truncating the file first
    >'x': create a new file and open it for writing
    >'a': open for writing, appending to the end of the file if it exists
    >'b': binary mode
    >'t': text mode (default)
    >'+': open a disk file for updating (reading and writing)
    >'U': universal newline mode (deprecated)
The default mode is 'rt' (open for reading text). For binary random access,
the mode 'w+b' opens and truncates the file to 0 bytes, while 'r+b' opens the file without truncation.
The 'x' mode implies 'w' and raises an FileExistsError if the file already exists.
'''

'''
'r' / 'w': plain text file
'rb' / 'wb': plain text file / image / music / video
'''

'''
read operation
    1.read(self, __n: int = -1) -> AnyStr
        Return all contents of the file
    2.readable(self) -> bool
        Return True if the file is readable
    3.readline(self, __limit: int = -1) -> AnyStr
        Return the next line of the file
    4.readlines(self, __hint: int = -1) -> list[AnyStr]
        Return a list of all lines of the file
'''
fis = open("data/a.txt", 'r')
# print(fis.read())
print(fis.readable())
# while True:
#     line = fis.readline()
#     print(line, end='')
#     if not line:
#         break
print(fis.readlines())
fis.close()

fbs = open("data/img1.png", 'rb')
print(fbs.read())
fbs.close()

'''
write operation
    1.write(self, __s: AnyStr) -> int
        Write AnyStr to the file and return the number of bytes written
    2.writelines(self, __lines: Iterable[AnyStr]) -> None
        Write AnyStr in Iterable to the file(with no '\n')
'''
fos = open("data/b.txt", 'w')
string = '''
Dear Admin:
    Hello! Welcome to Python Basis!
                                    Yours, Carl
'''
print(fos.write(string))
fos.writelines(["Hi!\n", "Glad to see you!\n"])
fos.close()

fos = open("data/b.txt", 'a')
fos.write("                Yours, Admin")
fos.close()
