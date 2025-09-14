# Academy Tester (Python)

This package contains functions to streamline testing tasks in the [Jetbrains Academy](https://www.jetbrains.com/academy/) plugin available in PyCharm.

Examples of how to use the functions are available.

# Installation

```
pip install academy-tester
```

# Documentation

This module provides two helper classes, `OutputTester` and `ContentTester`, designed to be used with Python's `unittest` framework. `OutputTester` focuses on running scripts and testing their output, while `ContentTester` analyzes the source code itself using Abstract Syntax Trees (AST).

---

# Basic test template
```py
import unittest
from academy_tester import OutputTester, ContentTester


class TestPrintStatements(unittest.TestCase):
    def setUp(self):
        self.OTester = OutputTester(self)
        self.CTester = ContentTester(self)
```

### `OutputTester`

A utility class that wraps a `unittest.TestCase` to simplify testing the standard output of a Python script. It runs a target script as a subprocess, captures its output and error streams, and provides methods to assert conditions on the results.

#### **`__init__(self, testcase, filename="task.py")`**

Initialises the `OutputTester` with a `unittest.TestCase` instance and the name of the file to be tested.

* **Args** :
* `testcase` ( *unittest.TestCase* ): The test case instance (e.g., `self`) from which this class is being used. This is used to call assertion methods like `fail()`.
* `filename` ( *str, optional* ): The name of the Python script to be tested. Defaults to `"task.py"`.

---

#### **`test_output(self, output_requirements, input=[], message_addition="")`**

Runs the target script with specified inputs and asserts that one or more required strings are present in the script's standard output.

* **Args** :
* `output_requirements` ( *Union[str, list[str]]* ): A single string or a list of strings that must be found in the script's output.
* `input` ( *Iterable[str], optional* ): A sequence of strings to be passed to the script's standard input. Defaults to an empty list.
* `message_addition` ( *str, optional* ): An additional message to append to the failure message if an assertion fails.
* **Raises** :
* `AssertionError`: If the script produces an error or if any of the `output_requirements` are not found in the script's output.

---

#### **`test_count(self, expected_output, required_count, input=[])`**

Runs the script and asserts that a specific string appears a minimum number of times in the output, counting at most one occurrence per line.

* **Args** :
* `expected_output` ( *str* ): The string to search for in each line of the output.
* `required_count` ( *int* ): The minimum number of lines that must contain the `expected_output`.
* `input` ( *Iterable[str], optional* ): A sequence of strings to be passed to the script's standard input. Defaults to an empty list.
* **Raises** :
* `AssertionError`: If the actual count of lines containing the `expected_output` is less than `required_count`.

---

#### **`test_line_count(self, input=[])`**

Runs the script and returns the total number of lines in its standard output.

* **Args** :
* `input` ( *Iterable[str], optional* ): A sequence of strings to be passed to the script's standard input. Defaults to an empty list.
* **Returns** :
* *int* : The number of lines produced by the script.

---

### Class `ContentTester`

A utility class that uses Python's `ast` (Abstract Syntax Tree) module to statically analyze the source code of a script. This allows for testing code structure, variable assignments, and the use of specific language features without actually executing the script.

#### **`__init__(self, testcase, filename="task.py")`**

Initialises the `ContentTester` by parsing the target file into an AST.

* **Args** :
* `testcase` ( *unittest.TestCase* ): The test case instance from which this class is being used.
* `filename` ( *str, optional* ): The name of the Python script to be analyzed. Defaults to `"task.py"`.

---

#### **`check_tokens(self, token)`**

Counts the occurrences of a specific AST token type within the source code. This is useful for checking for operators, boolean logic, etc.

* **Args** :
* `token` ( *Type[ast.AST]* ): The AST node type to count. For example, `ast.Add` for the `+` operator or `ast.For` for a for-loop.
* **Returns** :
* *int* : The total number of instances of the specified token found in the code.
* **Example** :
  **Python**

```
  # Check how many times the addition operator (+) is used
  add_count = content_tester.check_tokens(ast.Add)
```

---

#### **`get_variables`**

A property that inspects the AST and returns a dictionary of all variables assigned at the top level of the script.

* **Returns** :
* *dict[str, object]* : A dictionary where keys are variable names (str) and values are their corresponding `ast` value nodes.

---

#### **`get_lists`**

A property that filters the script's variables and returns only the lists, with their constant values extracted.

* **Returns** :
* *dict[str, list]* : A dictionary where keys are the names of list variables and values are Python lists containing the constant elements from the source code.

---

#### **`get_function_count(self, function_id)`**

Counts how many times a function with a specific name is called within the script.

* **Args** :
* `function_id` ( *str* ): The name of the function to search for (e.g., `"print"`).
* **Returns** :
* *int* : The number of times the specified function is called.

---

#### **`get_attribute_count(self, attribute_id)`**

Counts how many times a specific attribute is accessed on an object (e.g., the `.append` in `my_list.append`).

* **Args** :
* `attribute_id` ( *str* ): The name of the attribute to search for (e.g., `"append"`).
* **Returns** :
* *int* : The number of times the specified attribute is accessed.
