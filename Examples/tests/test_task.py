import unittest
from academy_tester import OutputTester, ContentTester
import ast

class TestPrintStatements(unittest.TestCase):
    def setUp(self):
        self.OTester = OutputTester(self)
        self.CTester = ContentTester(self)

    def testFunctionExists(self):
        print(self.CTester.get_user_defined_functions())


if __name__ == '__main__':
    unittest.main()
