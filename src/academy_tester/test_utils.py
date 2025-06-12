import subprocess
import os
import platform
from typing import Optional



def run_file(filename : str = "task.py", input : list[str] = [], timeout : int = 5) -> Optional[str]:
    """
    Runs a python file and performs any requested inputs
    Essentially a wrapper around subprocess.run

    Args: 
        filename (str): The name of the file to test. Defaults to "task.py"
        input (list of str): Text inputs for the file. Empty by default
        timeout (int): time allocated for the script to run before it terminates

    Returns:
        Optional[str]: The output from running the file, or None if Exception
    """

    # Get the python version for the platform
    plat = platform.system().lower()
    python_version = "python" if plat == "windows" else "python3"

    # get directory of the requested file
    directory = os.path.join(os.getcwd(), filename)

    process = subprocess.Popen(
            [python_version, directory],  # Command to run the script
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture standard error (optional)
            text=True,  # Ensure output is returned as a string
            encoding="utf-8",      # Ensure UTF-8 encoding
            errors="replace"   # Handle any bad characters gracefully  
        )
    

    # Run file with requested inputs and test output
    try:
        # Wait for the process to complete and capture the output
        stdout, stderr = process.communicate(input = "\n".join(input), timeout = 5)

        result = None if stderr else stdout
        return result


    except subprocess.TimeoutExpired:
        # Handle the case where the script hangs due to insufficient input
        process.kill()  # Terminate the hanging process
        return None

