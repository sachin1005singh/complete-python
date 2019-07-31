import sys
from cx_Freeze import setup , Executable
setup(name = "my_fil",
    wersion = "0.1",
    description = "you can draw image",
    executables = [Executable(r"E:\python program\turtle\1.py")]
    )
