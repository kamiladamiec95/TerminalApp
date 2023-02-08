import os
import pathlib

def TerminalRun():

    user_input_splitted = [""]

    while (not user_input_splitted[0] == "quit"):
        user_input = input(">>")
        user_input_splitted = user_input.split()

        if user_input_splitted[0] == "ls":
            os.system("clear")
            print("\n".join(os.listdir(".")))

        elif user_input_splitted[0] == "cd":
            os.system("clear")
            if len(user_input_splitted) > 1:
                directory = user_input_splitted[1]
                if directory == ".":
                    os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
                os.chdir(directory)

        elif user_input_splitted[0] == "mkdir":
            folder_name = ""
            for name in user_input_splitted[1:]:
                folder_name = folder_name + name
            os.mkdir(os.getcwd() + "/" + folder_name)    


if __name__ == "__main__":
    TerminalRun()