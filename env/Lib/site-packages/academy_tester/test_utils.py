import subprocess
import os
import platform
import unittest


def run_file(directory : str = "task.py", input : list[str] = []) -> str:
    """
    Runs a python file and performs any requested inputs
    Essentially a wrapper around subprocess.run

    Args: 
        directory (str): The directory of the file to test. Defaults to "task.py"
        input (list of str): Text inputs for the file. Empty by default

    Returns:
        str: The output from running the file
    """

    # Get the python version for the platform
    plat = platform.system().lower()
    python_version = "python" if plat == "windows" else "python3"


    print(f"cwd:{os.getcwd()}")
    process = subprocess.Popen(
            [python_version, directory],  # Command to run the script
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture standard error (optional)
            text=True,  # Ensure output is returned as a string
            encoding="utf-8",      # Ensure UTF-8 encoding
            errors="replace"   # Handle any bad characters gracefully  
        )
    
    return ""


if __name__ == "__main__":
    run_file()