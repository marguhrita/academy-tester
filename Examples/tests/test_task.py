import unittest
from academy_tester import OutputTester, ContentTester
import ast


class TestPrintStatements(unittest.TestCase):
    def setUp(self):
        self.OTester = OutputTester(self)
        self.CTester = ContentTester(self)

    def testForLoop(self):
        for_count = self.CTester.check_tokens(ast.For)

        if for_count < 1:
            self.fail(f"You should have at least one \"for\" loop. Current number: {for_count}")



if __name__ == '__main__':
    unittest.main()
