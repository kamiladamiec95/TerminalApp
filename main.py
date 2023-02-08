import os
import pathlib
import shutil

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

        elif user_input_splitted[0] == "touch" and len(user_input_splitted) > 1:
            pathlib.Path(os.getcwd() + "/" + user_input_splitted[1]).touch()

        elif user_input_splitted[0] == "mv" and len(user_input_splitted) > 1:
            pathlib.Path(os.getcwd() + "/" + user_input_splitted[1]).rename(os.getcwd() + "/" + user_input_splitted[2] + "/" + user_input_splitted[1])

        elif user_input_splitted[0] == "pwd":
            print(os.getcwd())

        elif user_input_splitted[0] == "rm" and len(user_input_splitted) > 1:
            file_name = user_input_splitted[1]
            os.remove(file_name)

        elif user_input_splitted[0] == "rmdir" and len(user_input_splitted) > 1:
            folder_name = user_input_splitted[1]
            if user_input_splitted[2] == "-r":
                shutil.rmtree(folder_name)           
            else:
                os.rmdir(folder_name)

        elif user_input_splitted[0] == "zip" and len(user_input_splitted) > 1:
                file_to_zip = user_input_splitted[1]
                shutil.make_archive(file_to_zip, "zip")

        elif not user_input_splitted[0] == "quit":
            print("Error")    


if __name__ == "__main__":
    TerminalRun()