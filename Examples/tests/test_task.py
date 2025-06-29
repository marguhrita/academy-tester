import unittest
import subprocess
import ast
from platform import system
from academy_tester import OutputTester, ContentTester


class TestPrintStatements(unittest.TestCase):
    def setUp(self):
        self.OTester = OutputTester(self)
        self.CTester = ContentTester(self, "task2.py")

    def test_output(self):


        self.OTester.test_output("womp\nwomp", input = ["womp"])

    def test_line_count(self):
        self.OTester.test_count("print", 1)

    def test_lists(self):
        p = self.CTester.get_lists()
        for l in p.items():
            print(l)
            


if __name__ == '__main__':
    unittest.main()