from cx_Freeze import setup, Executable

setup(
    name ="AniBeat",
    version = "Demo",
    description ="Enjoy the game",
    executables = [Executable("main.py")]

)
