import unittest
import subprocess
from dataclasses import dataclass
from typing import Optional, Union, Iterable
import os, platform
import ast


@dataclass
class RunResult:
    output: str
    error: Optional[str] = None

class OutputTester():
    def __init__(self, testcase : unittest.TestCase, filename : str = "task.py"):
        self.cwd = os.getcwd()
        self.filename : str = filename
        self.testcase = testcase

    def test_output(self, output_requirements : Union[str, list[str]], input : Iterable[str] = [], message_addition : str = "") -> None:
        """
            Runs a python file with a set of inputs, and checks if the output has all the required strings. 
        """

        # retrieve output using formatted input
        result = self._run_file(self.filename, input)

        output_requirements = [output_requirements] if isinstance(output_requirements, str) else output_requirements

        if result.error:
            self.testcase.fail(result.output)
        else:
            for req in output_requirements:
                if not req in result.output:
                    print(f"output:{result.output}")
                    self.testcase.fail(f"{req} was not found in output!")


    def test_count(self, expected_output : str, required_count : int, input : Iterable[str] = []) -> None:
        """
            Counts occurrences of an expected output with a specific input. 
            Only counts one occurence for each line
            Args:
                input (Iterable[str]): User input for the script
                expected_output (str): what to check for in output
        """

        result = self._run_file(self.filename, input)
        
        if not result.error:
            count = 0
            for line in result.output.splitlines():
                if expected_output in line:
                    count += 1

            if count < required_count:
                self.testcase.fail(f"Expected {required_count} instances of {expected_output} in output, got {count}")
            
    
    def test_line_count(self, input : Iterable[str] = []) -> int:
        """
        """
        result : RunResult = self._run_file(self.filename, input)

        return len(result.output.splitlines())

    def _run_file(self, filename : str, input : Iterable[str], timeout : float = 5) -> RunResult:
        """
        Runs a python file and performs any requested inputs
        Essentially a wrapper around subprocess.run

        Args: 
            filename (str): The name of the file to test. Defaults to "task.py"
            input (str): Text inputs for the file. Empty by default
            timeout (float): time allocated for the script to run before it terminates

        Returns:
            Optional[str]: The output from running the file, or None if Exception
        """

        # Get the python version for the platform
        plat = platform.system().lower()
        python_version = "python" if plat == "windows" else "python3"

        # get directory of the requested file
        directory = os.path.join(self.cwd, filename)
        print(directory)

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
            stdout, stderr = process.communicate(input = "\n".join(input), timeout = timeout)

        except subprocess.TimeoutExpired:
            # Handle the case where the script hangs due to insufficient input
            process.kill()  # Terminate the hanging process
            return RunResult(output = "", error="Script Timed Out")
        

        return RunResult(output = stdout, error = stderr)
    

class ContentTester():
    def __init__(self, testcase : unittest.TestCase, filename : str = "task.py"):
        self.testcase = testcase
        self.filename = filename

    def get_lists(self) -> dict[str, list]:
        tree : ast.Module = self._parse()

        l = {}

        for node in ast.walk(tree):
            match node:
                case ast.Assign(
                    targets=[ast.Name(id=name)],
                    value=ast.List(elts=elts)
                ):
                    l[name] = [
                        item.value if isinstance(item, ast.Constant) else None
                        for item in elts
                    ]

        return l
    
    def _parse(self) -> ast.Module:

        script = self._get_file_contents()

        tree = ast.parse(script)

        return tree


    def _get_file_contents(self) -> str:
        directory = os.path.join(os.getcwd(), self.filename)


        with open(directory, 'r', encoding='utf-8') as f:
            return f.read()