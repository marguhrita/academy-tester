import unittest
import subprocess
import os, platform

# Path to the script you want to test
SCRIPT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "task.py")

class Tests(unittest.TestCase):

    def test(self):
        plat = platform.system().lower()
        python_version = "python" if plat == "windows" else "python3"

        # Execute the script using subprocess.Popen and capture the output
        process = subprocess.Popen(
            [python_version, SCRIPT_PATH],  # Command to run the script
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture standard error (optional)
            text=True,  # Ensure output is returned as a string
            encoding="utf-8",      # Ensure UTF-8 encoding
            errors="replace"   # Handle any bad characters gracefully  
        )


        #File Content
        with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
            out = f.read()



        # File Output Testing
        try:
            # Wait for the process to complete and capture the output
            stdout, stderr = process.communicate(timeout = 5)
            # Split the output into lines
            output = stdout.splitlines()


        except subprocess.TimeoutExpired:
            # Handle the case where the script hangs due to insufficient input
            process.kill()  # Terminate the hanging process
            self.fail("The script timed out")


print("Loaded test_utils")