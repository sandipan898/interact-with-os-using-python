"""
5.
Question 5
The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function
"""

import os


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    rel_path = str(os.getcwd())
    print(rel_path)
    os.chdir("../")
    relative_parent = os.getcwd()

    # Return the absolute path of the parent directory
    return relative_parent


print(parent_directory())
