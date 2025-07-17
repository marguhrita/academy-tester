import unittest
import subprocess
import ast
from platform import system
from academy_tester import OutputTester, ContentTester


class TestPrintStatements(unittest.TestCase):
    def setUp(self):
        self.OTester = OutputTester(self, "task2.py")
        self.CTester = ContentTester(self, "task2.py")

    def test_output(self):
        #self.OTester.test_output("womp\nwomp", input = ["womp"])
        pass

    def test_line_count(self):
        self.OTester.test_count("print", 1)

    def test_lists(self):
        p = self.CTester.get_lists
        

    def test_functions(self):
        count = self.CTester.get_function_count("print")

        print(count)

    def test_ops(self):
        count = self.CTester.check_tokens(ast.Add)

    def test_variables(self):
        for n, v in self.CTester.get_variables.items():
            if not f"print({n})" in self.CTester.get_file_contents:
                self.fail(f"Make sure you have printed the variable {n}")
                
            

    


if __name__ == '__main__':
    unittest.main()