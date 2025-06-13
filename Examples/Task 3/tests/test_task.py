import unittest
import subprocess
import os
from platform import system
from academy_tester import Tester


class TestPrintStatements(unittest.TestCase):
    def test(self):

        t = Tester(self)

        #t.test_output(["print", "Hello there"])

        t.test_count("print", 1)

        t.test_output("womp", input = ["womp"])


if __name__ == '__main__':
    unittest.main()